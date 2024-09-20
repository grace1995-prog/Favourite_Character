from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://d28dp6fycxce58.cloudfront.net/")
# User selects  favorite character (initial search)
list_Modal = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/button[1]")
list_Modal.click()
time.sleep(10)
select_character = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/button[1]/div[1]/img")
select_character.click()
time.sleep(2)
# navigate to favourite Modal
Navigate_to_fav_Tab = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/button[2]")
Navigate_to_fav_Tab.click()
time.sleep(2)
# Close the browser
driver.quit()
