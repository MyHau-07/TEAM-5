from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# Cấu hình trang web và thông tin tài khoản thử nghiệm
URL = "http://127.0.0.1:8000/"  # Thay bằng URL thật
URL1 = "http://127.0.0.1:8000/quanlinhanvien/"
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
    """Hàm thực hiện đăng ký nhân viên mới với thông tin được cung cấp."""
    driver.get(URL1)  # Điều hướng đến trang chính
    time.sleep(2)  # Đợi trang tải

    try:
        # Kiểm tra lại nếu nút Thêm nhân viên mới là một phần tử trong modal hay không
        add_employee_button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='modal' and @data-bs-target='#addEmployeeModal']")
        add_employee_button.click()
        time.sleep(3)  # Đợi modal xuất hiện

        # Họ và tên
        full_name_input = driver.find_element(By.ID, "name1")
        full_name_input.clear()
        full_name_input.send_keys("Nguyễn Văn Đạt")  # Nhập tên
        time.sleep(2)  # Đợi 1 giây

        # Chọn chức vụ
        specialization_select = Select(driver.find_element(By.ID, "Spec1"))
        specialization_select.select_by_visible_text("Dược sĩ")  # Chọn chức vụ
        time.sleep(2)  # Đợi 1 giây

        # Nhập số giấy phép hành nghề nha khoa
        license_number_input = driver.find_element(By.ID, "Licensenumber1")
        license_number_input.clear()
        license_number_input.send_keys("2945300475")  # Nhập số giấy phép
        time.sleep(2)  # Đợi 1 giây

        # Chọn chi nhánh
        dental_branch_select = Select(driver.find_element(By.ID, "Dentalbranch1"))
        dental_branch_select.select_by_visible_text("Chi nhánh 3 - Quận 10")  # Chọn chi nhánh
        time.sleep(2)  # Đợi 1 giây

        # Nhập số điện thoại
        phone_number_input = driver.find_element(By.ID, "PhoneNumber1")
        phone_number_input.clear()
        phone_number_input.send_keys("02925300425")  # Nhập số điện thoại
        time.sleep(2)  # Đợi 1 giây

        # Nhập email
        email_input = driver.find_element(By.ID, "Email1")
        email_input.clear()
        email_input.send_keys("DatNguyen29email@example.com")  # Nhập email
        time.sleep(2)  # Đợi 1 giây

        # Nhập ngày sinh
        birthday_input = driver.find_element(By.ID, "Birthday1")
        birthday_input.clear()
        birthday_input.send_keys("04-30-1975")  # Nhập ngày sinh
        time.sleep(2)  # Đợi 1 giây

        # Chọn giới tính
        gender_select = Select(driver.find_element(By.NAME, "Gender123"))
        gender_select.select_by_visible_text("Nam")  # Chọn giới tính
        time.sleep(2)  # Đợi 1 giây

        # Nhấn nút "Lưu"
        submit_button = driver.find_element(By.XPATH, "//button[@id='Luu1']")
        submit_button.click()
        # Đợi 3 giây để kiểm tra kết quả
        time.sleep(3)
        # Kiểm tra đăng ký thành công
        if driver.current_url == "http://127.0.0.1:8000/quanlinhanvien/":  # Thay "dashboard" bằng URL thật sau đăng ký
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

    # Nếu đăng nhập thành công, kiểm tra quyền truy cập vào các trang
    if result == "success":
        #access_test()
        register_test()

# Đóng trình duyệt sau khi kiểm tra xong
driver.quit()
