from django.test import TestCase
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Cấu hình trang web và thông tin tài khoản thử nghiệm
URL = "http://127.0.0.1:8000/"  # Thay bằng URL thật
URL1 = "http://127.0.0.1:8000/booking"
VALID_USERNAME = "user1"
VALID_PASSWORD = "Thanhbug123"

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

        # Tìm và nhấn nút đăng nhập
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(3)  # Đợi phản hồi

        # Kiểm tra đăng nhập thành công
        if driver.current_url == "http://127.0.0.1:8000/patient_dashboard":  # Thay "dashboard" bằng URL thật sau đăng nhập
            return "success"
        else:
            return "fail"
    except Exception as e:
        print(f"Lỗi trong quá trình đăng nhập: {e}")
        return "fail"

def booking_test():
    """Hàm thực hiện đăng ký dịch vụ với thông tin được cung cấp."""
    driver.get(URL1)  # Điều hướng đến trang booking
    time.sleep(2)  # Đợi trang tải

    try:
        # Điền thông tin vào form
        fullname_field = driver.find_element(By.NAME, "fullname")
        fullname_field.clear()
        fullname_field.send_keys("Nguyen Thanh Bug")
        time.sleep(3)

        phone_field = driver.find_element(By.NAME, "phone")
        phone_field.clear()
        phone_field.send_keys("0901234567")
        time.sleep(3)

        email_field = driver.find_element(By.NAME, "email")
        email_field.clear()
        email_field.send_keys("thanhbug@example.com")
        time.sleep(3)

        # Chọn địa điểm
        location_select = Select(driver.find_element(By.NAME, "location"))
        location_select.select_by_visible_text("02 Võ Oanh, Phường 25, Bình Thạnh, Hồ Chí Minh")
        time.sleep(3)
        # Chọn dịch vụ
        service_select = Select(driver.find_element(By.NAME, "service"))
        service_select.select_by_visible_text("Nhổ răng")
        time.sleep(3)
        # Điền thông tin bệnh
        message_field = driver.find_element(By.NAME, "message")
        message_field.clear()
        message_field.send_keys("Cần nhổ răng hàm dưới.")
        time.sleep(3)
        # Tải ảnh nếu có (tùy chọn)

        # Chọn ngày và giờ hẹn
        date_field = driver.find_element(By.NAME, "appointment_date")
        date_field.send_keys("02-20-2025")
        time.sleep(3)

        time_select = Select(driver.find_element(By.NAME, "appointment_time"))
        time_select.select_by_visible_text("08:45 AM")
        time.sleep(3)

        # Nhấn nút "Hoàn tất"
        complete_button = driver.find_element(By.ID, "complete-btn")
        complete_button.click()
        time.sleep(3)

        # Kiểm tra kết quả đăng ký
        if "booking" in driver.current_url:
            return "success"
        else:
            return "fail"
    except Exception as e:
        print(f"Lỗi trong quá trình đăng ký: {e}")
        return "fail"

# Chạy thử nghiệm cho từng trường hợp
for case in test_cases:
    result = login_test(case["username"], case["password"])
    print(f"🔹 Test với username='{case['username']}', password='{case['password'][:3]}***': {result} (mong đợi: {case['expected']})")

    # Nếu đăng nhập thành công, kiểm tra booking
    if result == "success":
        booking_result = booking_test()
        print(f"🔸 Test đăng ký dịch vụ: {booking_result}")

# Đóng trình duyệt sau khi kiểm tra xong
driver.quit()
