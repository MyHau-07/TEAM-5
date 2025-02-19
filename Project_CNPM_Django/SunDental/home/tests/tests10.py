from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


URL = "http://127.0.0.1:8000/" 
URL1 = "http://127.0.0.1:8000/dentist_dashboard"
VALID_USERNAME = "dentist1"
VALID_PASSWORD = "Thanhbug12"


driver = webdriver.Chrome()


def login(username, password):
    driver.get(URL)
    time.sleep(2)
    
    login_button = driver.find_element(By.LINK_TEXT, "Đăng nhập")
    login_button.click()
    time.sleep(2)


    username_field = driver.find_element(By.NAME, "username")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(2)  

    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(2)


    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(3)  
    
def dangkilichnghi():
    driver.get(URL1)
    dkln_btn = driver.find_element(By.ID,"showRegisterForm") 
    dkln_btn.click()
    time.sleep(2)
    
    name_input = driver.find_element(By.ID,"inputPatientName") 
    name_input.clear()
    name_input.send_keys("Nguyễn Anh Huy")
    time.sleep(2)
    
    date_input = driver.find_element(By.ID,"inputDate") 
    date_input.clear()
    date_input.send_keys("02-21-2025")
    time.sleep(2)
    
    canghi_input = Select(driver.find_element(By.ID, "inputDoctorName")) 
    canghi_input.select_by_visible_text("Ca sáng")
    time.sleep(2)
    
    lido_input = Select(driver.find_element(By.ID, "inputDepartmentName")) 
    lido_input.select_by_visible_text("Lý do sức khỏe")
    time.sleep(2)
    
    mota_input = driver.find_element(By.ID,"inputSymptoms")
    mota_input.clear()
    mota_input.send_keys("Bị sốt nặng")
    time.sleep(2)
    
    dk_btn = driver.find_element(By.ID,"dkbtn")
    dk_btn.click()
    time.sleep(15)
    driver.quit()
    
login(VALID_USERNAME,VALID_PASSWORD)
dangkilichnghi()