from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta, date
import undetected_chromedriver as uc
import time

from handleEmail import get_verification_code
from handleRichcraft import clickButton, findDay, findTime, fillForm

options = uc.ChromeOptions()
options.binary_location = "/usr/bin/brave"
driver = uc.Chrome(options=options, headless=False)

link = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata"
driver.get(link)
time.sleep(3)

clickButton("//div[contains(text(), 'Volleyball - adult')]", 'Volleyball - adult')
clickButton("//button[contains(., 'Confirm')]", 'Confirm')

day, weekday = findDay(2)
print("Looking for day:", day)
clickButton(f"//span[contains(text(), '{day}')]", day)

goalTime = findTime(weekday)
clickButton(f"//a[contains(., '{goalTime}')]", goalTime)

fillForm()
clickButton("//button[contains(., 'Confirm')]", 'Confirm')

time.sleep(10)
code = get_verification_code()

###submit ciode

driver.quit()