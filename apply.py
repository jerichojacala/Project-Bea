from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, NoSuchFrameException
import os
import time

driver = webdriver.Chrome()
driver.get(placeholderlink)

def find_element_recursively(driver, value):
    try:
        # Try to find the element in the current context
        return driver.find_element(By.XPATH, f'//*[contains(@id, "{value}") or contains(@name, "{value}") or contains(@placeholder, "{value}")]')
    except NoSuchElementException:
        # If not found, try to find the element in each frame
        frames = driver.find_elements(By.TAG_NAME, 'iframe')
        for frame in frames:
            driver.switch_to.frame(frame)
            try:
                # Recursively search in the current frame
                element = find_element_recursively(driver, value)
                if element:
                    return element
            except NoSuchElementException:
                pass
            driver.switch_to.default_content()
    return None

def fill(key, value):
    field = find_element_recursively(driver, value)
    if field:
        try:
            field.send_keys(key)
        except ElementNotInteractableException:
            print("Element is not interactable.")
    else:
        print("ELEMENT NOT FOUND")
    return

keys = [('fakeemail@gmail.com', 'email'),('John','first'),('Smith','last'),('1-800-123-4567','phone'),('Boston','city'),('MA','state')]
for key in keys:
    fill(*key)