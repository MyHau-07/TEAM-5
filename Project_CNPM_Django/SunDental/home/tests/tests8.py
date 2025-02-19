from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# Cấu hình trang web và thông tin tài khoản thử nghiệm
URL = "http://127.0.0.1:8000/"  # Thay bằng URL thật
URL1 = "http://127.0.0.1:8000/quanlidichvu"
VALID_USERNAME = "ClinicOwner"
VALID_PASSWORD = "Thanhbug1"


# Danh sách các trường hợp thử nghiệm
test_cases = [
    {"username": VALID_USERNAME, "password": VALID_PASSWORD, "expected": "success"},
]

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

def login_test(username, password):
    """Hàm thực hiện đăng nhập với thông tin được cung cấp."""
    driver.get(URL)
    time.sleep(2)  # Đợi trang tải
    
    try:
        # Tìm và nhấp vào nút đăng nhập
        login_button = driver.find_element(By.LINK_TEXT, "Đăng nhập")
        login_button.click()
        time.sleep(2)

        # Tìm và nhập username
        username_field = driver.find_element(By.NAME, "username")
        username_field.clear()
        username_field.send_keys(username)
        time.sleep(2)  # Đợi trang tải

        # Tìm và nhập password
        password_field = driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)  # Đợi trang tải

        # Tìm và nhấn nút đăng nhập (có thể dùng XPATH nếu không có NAME)
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(3)  # Đợi phản hồi

        # Kiểm tra đăng nhập thành công
        if driver.current_url == "http://127.0.0.1:8000/clinic_owner_dashboard":  # Thay "dashboard" bằng URL thật sau đăng nhập
            return "success"
        else:
            return "fail"
    except Exception as e:
        print(f"Lỗi trong quá trình đăng nhập: {e}")
        return "fail"

def access_test():
    """Kiểm tra quyền truy cập vào các trang quan trọng sau khi đăng nhập."""
    pages = {
        "phongkham": "http://127.0.0.1:8000/hosophongkham",
        "chinhanh": "http://127.0.0.1:8000/quanlichinhanh",
        "nhanvien": "http://127.0.0.1:8000/quanlinhanvien/",
        "dichvu": "http://127.0.0.1:8000/quanlidichvu"
    }

    for page_name, page_url in pages.items():
        try:
            driver.get(page_url)
            time.sleep(2)  # Đợi trang tải

            if driver.current_url == page_url:
                print(f"✅ Truy cập {page_name}: success")
            else:
                print(f"❌ Truy cập {page_name}: fail (bị chặn hoặc lỗi)")
        except Exception as e:
            print(f"⚠️ Lỗi khi truy cập {page_name}: {e}")

def register_test():
    """Hàm thực hiện thêm dịch vụ mới với thông tin được cung cấp."""
    driver.get(URL1)  # Điều hướng đến trang chính
    time.sleep(2)  # Đợi trang tải

    try:
        # Kiểm tra nút "Thêm Dịch Vụ Mới" và click vào nó
        add_service_button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='modal' and @data-bs-target='#addServiceModal']")
        add_service_button.click()
        time.sleep(3)  # Đợi modal xuất hiện

        # Tên dịch vụ
        service_name_input = driver.find_element(By.NAME, "name")
        service_name_input.clear()
        service_name_input.send_keys("Cấy ghép Implant")  # Nhập tên dịch vụ
        time.sleep(1)  # Đợi 1 giây

        # Giá dịch vụ
        service_price_input = driver.find_element(By.NAME, "price")
        service_price_input.clear()
        service_price_input.send_keys("5000000")  # Nhập giá dịch vụ
        time.sleep(1)  # Đợi 1 giây

        # Mô tả dịch vụ
        service_info_input = driver.find_element(By.NAME, "info")
        service_info_input.clear()
        service_info_input.send_keys("Cấy ghép implant chất lượng cao, bảo hành 10 năm.")  # Nhập mô tả
        time.sleep(1)  # Đợi 1 giây

        # Thời gian thực hiện
        service_time_input = driver.find_element(By.NAME, "time")
        service_time_input.clear()
        service_time_input.send_keys("60 phút")  # Nhập thời gian
        time.sleep(1)  # Đợi 1 giây

        # Tải hình ảnh (giả sử có sẵn một file hình ảnh)
        service_image_input = driver.find_element(By.NAME, "image")
        service_image_input.send_keys("C:/Users/Nguyen Ngoc Hieu/Downloads/dv1.jpg")  # Đường dẫn đến hình ảnh
        time.sleep(1)  # Đợi 1 giây

        # Nhấn nút "Lưu"
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(3)  # Đợi kết quả

        # Kiểm tra kết quả sau khi thêm dịch vụ
        if driver.current_url == "http://127.0.0.1:8000/quanlidichvu/":  # Thay URL này bằng URL thật của trang quản lý dịch vụ
            return "success"
        else:
            return "fail"
    except Exception as e:
        print(f"Lỗi trong quá trình thêm dịch vụ: {e}")
        return "fail"

# Chạy thử nghiệm cho từng trường hợp
for case in test_cases:
    result = login_test(case["username"], case["password"])
    print(f"🔹 Test với username='{case['username']}', password='{case['password'][:3]}***': {result} (mong đợi: {case['expected']})")

    # Nếu đăng nhập thành công, kiểm tra quyền truy cập vào các trang
    if result == "success":
        #access_test()
        register_test()

# Đóng trình duyệt sau khi kiểm tra xong
driver.quit()
