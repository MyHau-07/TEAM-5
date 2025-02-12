# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

# Cài đặt các gói cần thiết để build các package Python như psycopg2 và mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Thiết lập thư mục làm việc
WORKDIR /app

# Tắt việc tạo các file .pyc và buffering của Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy file requirements và cài đặt các package Python
COPY requirements.txt .
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Expose port 9000
EXPOSE 9000

# Tạo user không root và gán quyền cho thư mục /app
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Khởi chạy ứng dụng Django
CMD ["python", "manage.py", "runserver", "localhost:9000"]
