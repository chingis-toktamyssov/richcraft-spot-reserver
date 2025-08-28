from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta, date
import undetected_chromedriver as uc
import time

from handleEmail import get_verification_code
from handleRichcraft import clickButton, findDay, findTime, fillForm, fillCode

options = uc.ChromeOptions()
options.binary_location = "/usr/bin/brave"
driver = uc.Chrome(options=options, headless=False)

link = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata"
driver.get(link)
time.sleep(3)

clickButton("//div[contains(text(), 'Volleyball - adult')]", 'Volleyball - adult', driver)
clickButton("//button[contains(., 'Confirm')]", 'Confirm', driver)

day, weekday = findDay(2)
print("Looking for day:", day)
clickButton(f"//span[contains(text(), '{day}')]", day, driver)

goalTime = findTime(weekday)
clickButton(f"//a[contains(., '{goalTime}')]", goalTime, driver)

fillForm(driver)
clickButton("//button[contains(., 'Confirm')]", 'Confirm', driver)

time.sleep(10)
code = get_verification_code()

fillCode(code, driver)
clickButton("//button[contains(., 'Confirm')]", 'Confirm', driver)

driver.quit()