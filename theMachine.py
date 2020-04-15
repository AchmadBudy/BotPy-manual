# required !!!
# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def loops(numberOfLoop, phone, msg):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    n = numberOfLoop
    t = 0
    phoneNumber = phone
    message = msg
    for x in range(n):
        for number in phoneNumber:
            browser.get('https://web.whatsapp.com/send?phone=' +
                        number + '&text='+message)
            time.sleep(3)
            element_present = EC.presence_of_element_located(
                (By.XPATH, "//button[@class='_35EW6']"))
            button = WebDriverWait(browser, 4).until(element_present)
            button.click()
            print("Send Message to number  "+str(number)+" success")
            time.sleep(2)
            element_presents = EC.presence_of_element_located(
                (By.XPATH, "//button[@class='_2SbJ1']"))
            WebDriverWait(browser, 4).until(element_presents)
            t += 1
    print("======================= End Loop ===========================")
    print("============ Success Loop for "+str(t)+" number ============")
    browser.close()
