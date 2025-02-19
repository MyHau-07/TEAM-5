from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Cấu hình trang web và thông tin tài khoản thử nghiệm
URL = "http://127.0.0.1:8000/"  # Thay bằng URL thật
VALID_USERNAME = "ClinicOwner"
VALID_PASSWORD = "Thanhbug1"

VALID_USERNAME2 = "ClinicOwner"
VALID_PASSWORD2 = ""                #Không password

VALID_USERNAME3 = ""                #Không username
VALID_PASSWORD3 = "Thanhbug1"

VALID_USERNAME4 = ""          #Không điền gì cả
VALID_PASSWORD4 = ""

# Danh sách các trường hợp thử nghiệm
test_cases = [
    {"username": VALID_USERNAME4, "password": VALID_PASSWORD4, "expected": "fail"},
    {"username": VALID_USERNAME3, "password": VALID_PASSWORD3, "expected": "fail"},
    {"username": VALID_USERNAME2, "password": VALID_PASSWORD2, "expected": "fail"},
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
        "Ho so phong kham": "http://127.0.0.1:8000/hosophongkham",
        "Quan li chi nhanh": "http://127.0.0.1:8000/quanlichinhanh",
        "Quan li nhan vien": "http://127.0.0.1:8000/quanlinhanvien/",
        "Quan li dich vu": "http://127.0.0.1:8000/quanlidichvu"
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

# Chạy thử nghiệm cho từng trường hợp
for case in test_cases:
    result = login_test(case["username"], case["password"])
    print(f"🔹 Test với username='{case['username']}', password='{case['password'][:3]}***': {result} (mong đợi: {case['expected']})")

    # Nếu đăng nhập thành công, kiểm tra quyền truy cập vào các trang
    if result == "success":
        access_test()

# Đóng trình duyệt sau khi kiểm tra xong
driver.quit()
