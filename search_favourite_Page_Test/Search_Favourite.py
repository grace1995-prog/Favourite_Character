from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://d28dp6fycxce58.cloudfront.net/")
# User searches for favorite character (initial search)
search_field = driver.find_element(By.XPATH, "//html/body/div[1]/div/div[1]/div/input")
search_field.send_keys("Morty Smith")
time.sleep(2)
# Clear the search field
search_field.clear()
time.sleep(2)
# Close the browser
driver.quit()



