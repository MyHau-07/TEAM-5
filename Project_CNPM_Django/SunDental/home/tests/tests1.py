from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Cấu hình trang web và thông tin tài khoản thử nghiệm
URL = "http://127.0.0.1:8000/"  # Thay bằng URL thật
REGISTER_URL = "http://127.0.0.1:8000/register"  # URL trang đăng ký


VALID_USERNAME4 = "DatBug"
VALID_PASSWORD4 = "Thanhbug123"
VALID_PASSWORD4_Confirm = ""        #Không password_confirm


VALID_USERNAME6 = ""                #Không username
VALID_PASSWORD6 = "Thanhbug123"
VALID_PASSWORD6_Confirm = "Thanhbug123"

VALID_USERNAME7 = ""          #Không điền gì cả
VALID_PASSWORD7 = ""
VALID_PASSWORD7_Confirm = ""

INVALID_USERNAME8 = "user@!#"   #SaiUserName
VALID_PASSWORD8 = "Thanhbug123"
VALID_PASSWORD8_Confirm = "Thanhbug123"


VALID_USERNAME = "user1"           #Đúng 
VALID_PASSWORD = "Thanhbug123"      
VALID_PASSWORD_Confirm = "Thanhbug123"

VALID_USERNAME2 = "dentist1"           #Đúng 
VALID_PASSWORD2 = "Thanhbug12"      
VALID_PASSWORD2_Confirm = "Thanhbug12"

VALID_USERNAME3 = "ClinicOwner"           #Đúng 
VALID_PASSWORD3 = "Thanhbug1"      
VALID_PASSWORD3_Confirm = "Thanhbug1"


# Danh sách các trường hợp thử nghiệm
test_cases = [
    {"username": VALID_USERNAME4, "password": VALID_PASSWORD4, "password": VALID_PASSWORD4_Confirm, "expected": "fail"},
 
    {"username": VALID_USERNAME6, "password": VALID_PASSWORD6, "password": VALID_PASSWORD6_Confirm, "expected": "fail"},
    {"username": VALID_USERNAME7, "password": VALID_PASSWORD7, "password": VALID_PASSWORD7_Confirm, "expected": "fail"},
    {"username": INVALID_USERNAME8, "password": VALID_PASSWORD8, "password": VALID_PASSWORD8_Confirm,"expected": "fail"},
    {"username": VALID_USERNAME, "password": VALID_PASSWORD, "password": VALID_PASSWORD_Confirm,"expected": "success"},
    {"username": VALID_USERNAME2, "password": VALID_PASSWORD2, "password": VALID_PASSWORD2_Confirm,"expected": "success"},
    {"username": VALID_USERNAME3, "password": VALID_PASSWORD3, "password": VALID_PASSWORD2_Confirm,"expected": "success"},
]

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

def register_test(username, password, password_confirm):
    """Hàm thực hiện đăng ký với thông tin được cung cấp."""
    driver.get(URL)  # Vào trang chủ
    time.sleep(2)
    
    try:
        # Tìm và nhấp vào nút đăng ký
        register_button = driver.find_element(By.LINK_TEXT, "Đăng ký")
        register_button.click()
        time.sleep(2)
        
        # Tìm và nhập username
        username_field = driver.find_element(By.NAME, "username")
        username_field.clear()
        username_field.send_keys(username)
        time.sleep(1)

        # Tìm và nhập email (tạo email ngẫu nhiên nếu cần)
        email_field = driver.find_element(By.NAME, "email")
        email_field.clear()
        email_field.send_keys(f"{username}@example.com")
        time.sleep(1)
        
        # Tìm và nhập password
        password_field = driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(1)

        # Tìm và nhập password confirm
        password_confirm_field = driver.find_element(By.NAME, "password_confirm")
        password_confirm_field.clear()
        password_confirm_field.send_keys(password_confirm)
        time.sleep(1)
        
        # Tìm và nhấn nút đăng ký
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(3)
        
        # Kiểm tra đăng ký thành công
        if driver.current_url == "http://127.0.0.1:8000/login_view/":  # Thay bằng URL sau đăng ký thành công
            return "success"
        else:
            return "fail"
    except Exception as e:
        print(f"Lỗi trong quá trình đăng ký: {e}")
        return "fail"

# Chạy thử nghiệm cho từng trường hợp
for case in test_cases:
    result = register_test(case["username"], case["password"], case["password"])
    print(f"🔹 Test với username='{case['username']}', password='{case['password'][:3]}***': {result} (mong đợi: {case['expected']})")

# Đóng trình duyệt sau khi kiểm tra xong
driver.quit()
