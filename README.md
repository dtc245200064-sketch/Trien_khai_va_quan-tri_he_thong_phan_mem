# Đề 40: Triển khai Hạ tầng Hệ thống Đặt Lịch Hẹn (Appointment Booking)

Hệ thống hạ tầng dịch vụ đặt lịch hẹn trực tuyến được triển khai hoàn chỉnh bằng Docker Compose, Nginx Reverse Proxy, CSDL PostgreSQL, pgAdmin và hệ thống Giám sát tập trung (Prometheus, Loki, Grafana).

## 🚀 Cấu trúc Hạ tầng
- **Web Frontend:** Giao diện đặt lịch hẹn trực tuyến (HTML/CSS/JS + Nginx).
- **Backend API:** FastAPI (Python) xử lý logic nghiệp vụ và trả về kết quả JSON.
- **Database:** PostgreSQL 15 quản trị dữ liệu lịch hẹn + pgAdmin 4 UI quản lý DB.
- **Reverse Proxy:** Nginx xử lý điều hướng tập trung qua Cổng 80.
- **Monitoring & Logging:** Prometheus (metrics), Loki (logs) & Grafana (dashboard).

## 🛠️ Hướng dẫn Khởi chạy Hệ thống

### 1. Yêu cầu hệ thống
- Môi trường Ubuntu Linux / Virtual Machine
- Đã cài đặt Docker & Docker Compose Plugin

### 2. Lệnh khởi chạy
```bash
git clone [https://github.com/dtc245200064-sketch/Trien_khai_va_quan_tri_he_thong_phan_mem.git](https://github.com/dtc245200064-sketch/Trien_khai_va_quan_tri_he_thong_phan_mem.git)
cd Trien_khai_va_quan_tri_he_thong_phan_mem
docker compose up -d --build

