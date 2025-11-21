from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.google.com")

# Find an element by its NAME and interact with it
search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Selenium Python tutorial")

search_box.submit()

title = driver.title

print (title)

if title == "Google Search" :
    print ("Test OK")

# Close the browser
driver.quit()