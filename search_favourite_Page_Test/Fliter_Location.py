from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://d28dp6fycxce58.cloudfront.net/")
# User searches for favorite character (initial search)
Filter_location = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/select")
Filter_location.click()
time.sleep(2)

Select_location = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/select")
Select_location.send_keys("Abadango")
time.sleep(2)
# Close the browser
driver.quit()
