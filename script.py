from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta, date
import undetected_chromedriver as uc
import time

def clickButton(identifier, name):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, identifier))
        )

        button.click()
        print(f"Clicked {name} button.")

    except Exception as e:
        print(f"{name} button not found:", e)
    
    time.sleep(3)

def findDay(offset=0):
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

def fillForm():
    phone_number = '3432040702'
    email = 'coktamyssovthingis@gmail.com'
    name = 'Chingis Toktamyssov'

    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "PhoneNumber"))  # example locator
    )
    phone_input.send_keys(phone_number)
    print("Filled phone number.")

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Email"))  # example locator
    )    
    email_input.send_keys(email)
    print("Filled email.")

    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "field3198"))  # example locator
    )
    name_input.send_keys(name)
    print("Filled name.")

    time.sleep(3)

options = uc.ChromeOptions()
options.binary_location = "/usr/bin/brave"
driver = uc.Chrome(options=options, headless=False)

link = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata"
driver.get(link)
time.sleep(3)

clickButton("//div[contains(text(), 'Volleyball - adult')]", 'Volleyball - adult')
clickButton("//button[contains(., 'Confirm')]", 'Confirm')

day, weekday = findDay(1)
print("Looking for day:", day)
clickButton(f"//span[contains(text(), '{day}')]", day)

goalTime = findTime(weekday)
goalTime = "8:45 PM"
clickButton(f"//a[contains(., '{goalTime}')]", goalTime)

fillForm()
clickButton("//button[contains(., 'Confirm')]", 'Confirm')

driver.quit()

# try:
#     goal_time = '7:45 PM'
#     if future_dt.weekday() == 3:
#         goal_time = '5:30 PM'
#     button = driver.find_element(By.XPATH, "//span[contains(text(), goal_time)]")
#     button.click()
#     print("Clicked time button:", goal_time)
# except Exception as e:
#     print("time button not found", e)


# # Optional: Print the page title
# Close the browser
driver.quit()