from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta, date
import undetected_chromedriver as uc
import time

def clickButton(identifier, name, driver):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, identifier))
        )

        button.click()
        print(f"Clicked {name} button.")

    except Exception as e:
        print(f"{name} button not found:", e)
    
    time.sleep(3)

def findDay(offset):
    date_str = str(date.today())
    dt = datetime.strptime(date_str, "%Y-%m-%d")

    future_dt = dt + timedelta(days=offset)

    formatted_date = f"{future_dt.strftime('%A %B')} {future_dt.day}, {future_dt.year}"
    weekday = future_dt.strftime('%A')

    return formatted_date, weekday

def findTime(weekday):
    goal_time = '7:45 PM'
    if weekday == 'Saturday':
        goal_time = '5:30 PM'

    return goal_time

def fillForm(driver):
    phone_number = '3432040702'
    email = 'coktamyssovthingis@gmail.com'
    name = 'Chingis Toktamyssov'

    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "PhoneNumber"))
    )
    phone_input.send_keys(phone_number)
    print("Filled phone number.")

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Email"))
    )    
    email_input.send_keys(email)
    print("Filled email.")

    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "field3198"))
    )
    name_input.send_keys(name)
    print("Filled name.")

    time.sleep(3)

def fillCode(code, driver):
    code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "code"))
    )
    code_input.send_keys(code)
    print("Filled verification code.")

    time.sleep(3)