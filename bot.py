# sebelum digunakan sebaiknya mempunyai selenium di perangkat anda
# pip install selenium

from selenium import webdriver
import time

# Isi nomornya bisa pake array
nomornya = "Nomornya"
isinya = "Halo gan ini ulangan ke "


browser = webdriver.Chrome('E:\instalanP2\chromedriver.exe')


for x in range(6):
    browser.get(
        'https://web.whatsapp.com/send?phone=' + nomornya + '&text='+isinya+str(x))
    time.sleep(7)
    button = browser.find_element_by_xpath("//button[@class='_35EW6']")
    button.click()
    time.sleep(1)

browser.close()
