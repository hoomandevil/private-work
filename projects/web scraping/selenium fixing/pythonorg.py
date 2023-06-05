from selenium import webdriver
from selenium.webdriver.common.by import By      #by for finding elements

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_driver_path = "C:\Development\chromedriver_win32"
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n+1] = {
        "name": event_names[n].text,
        "time": event_times[n].text
    }

print(events)

driver.quit()