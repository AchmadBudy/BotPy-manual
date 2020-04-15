# sebelum digunakan sebaiknya mempunyai selenium di perangkat anda
# pip install selenium

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

# Isi nomornya bisa pake array
nomornya = "nomornya" #nomornya contoh 62851324252
isinya = "Halo gan ini ulangan ke "


browser = webdriver.Chrome(ChromeDriverManager().install())


for x in range(6):
    browser.get(
        'https://web.whatsapp.com/send?phone=' + nomornya + '&text='+isinya+str(x))
    time.sleep(7)
    button = browser.find_element_by_xpath("//button[@class='_35EW6']")
    button.click()
    time.sleep(1)

browser.close()
