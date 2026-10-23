from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(docs_url="/docs", openapi_url="/openapi.json")

def get_db():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres-db"),
        database=os.getenv("POSTGRES_DB", "appointment"),
        user=os.getenv("POSTGRES_USER", "appointment_app"),
        password=os.getenv("POSTGRES_PASSWORD", "secretpassword"),
        port=os.getenv("POSTGRES_PORT", "5432")
    )
    return conn

# Tự động khởi tạo bảng dữ liệu khi ứng dụng chạy
def init_db():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id SERIAL PRIMARY KEY,
                full_name VARCHAR(250) NOT NULL,
                phone VARCHAR(50) NOT NULL,
                service_id INT,
                slot_id INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("Error initializing DB:", e)

init_db()

class AppointmentCreate(BaseModel):
    full_name: str
    phone: str
    service_id: int
    slot_id: int

@app.get("/metrics")
def get_metrics():
    return {"status": "ok"}

@app.post("/api/appointments")
def create_appointment(data: AppointmentCreate):
    try:
        conn = get_db()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "INSERT INTO appointments (full_name, phone, service_id, slot_id) VALUES (%s, %s, %s, %s) RETURNING id;",
            (data.full_name, data.phone, data.service_id, data.slot_id)
        )
        new_id = cur.fetchone()['id']
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Đặt lịch thành công!", "id": new_id}
    except Exception as e:
        print("Backend Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
