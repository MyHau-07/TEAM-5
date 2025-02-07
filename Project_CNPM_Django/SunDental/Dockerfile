# Sử dụng Python slim để giảm dung lượng image
FROM python:3-slim

# Cập nhật package list và cài đặt các dependencies cần thiết
RUN apt-get update && apt-get install -y gcc libpq-dev

# Thiết lập biến môi trường
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Đặt thư mục làm việc
WORKDIR /app

# Copy trước requirements.txt để tận dụng caching của Docker
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# Sau đó mới copy toàn bộ source code
COPY . /app/

# Tạo user không phải root để chạy ứng dụng
RUN adduser --system --uid 5678 appuser && chown -R appuser /app
USER appuser

# Mở cổng 9000
EXPOSE 9000

# Khởi chạy ứng dụng bằng gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:9000", "SunDental.wsgi"]
