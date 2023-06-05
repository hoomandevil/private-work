from selenium import webdriver

options = webdriver.ChromeOptions()  # using this option method to preventing
options.add_experimental_option("detach", True)  # the chromedriver closing automatically

chrome_driver_path = "C:\Development\chromedriver_win32"
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

driver.get(
    "https://www.amazon.com/SAMSUNG-Internal-Gaming-MZ-V8P2T0B-AM/dp/B08RK2SR23/ref=sr"
    "_1_4?qid=1685772461&s=electronics&sr=1-4&th=1")
info = driver.find_element("id", "corePrice_feature_div")  # new element methode search
print(info.text)

driver.close()
