import time
from selenium import webdriver


driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
driver.get("https://phptravels.com/")
time.sleep(10)
driver.find_element_by_xpath("//span[text()='Login']").click()

C_W=driver.current_window_handle
W_H=driver.window_handles

for i in W_H:
    if i!=C_W:
        driver.switch_to_window(i)


driver.find_element_by_name("username").send_keys("Puneeth")
driver.close()
driver.quit()



