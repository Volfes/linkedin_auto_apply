from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# user info
user_email = "xxxx"
user_password = "xxxx"
chrome_path = "xxxx"
timeout = 11


# chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-data-dir=xxxx")
driver = webdriver.Chrome(service=Service('web_driver/chromedriver.exe'),
                        chrome_options=chrome_options)  


#Check if logged in
def log_in():
    logged_in = driver.find_element(By.CLASS_NAME, "global-nav__primary-link-text")
    if not logged_in:
        username = driver.find_element(By.NAME, "session_key")
        username.send_keys(user_email)
        password = driver.find_element(By.NAME, "session_password")
        password.send_keys(user_password)
        log_in = driver.find_element(By.CSS_SELECTOR, 
                                    "#main-content > section.section.min-h-\[560px\].flex-nowrap.pt-\[40px\].babybear\:flex-col.babybear\:min-h-\[0\].babybear\:px-mobile-container-padding.babybear\:pt-\[24px\] > div > div > form:nth-child(7) > div.flex.justify-between.sign-in-form__footer--full-width > button")
        log_in.click()
        time.sleep(2)

    else:
        print("Zalogowany") 


def main():
    driver.get('https://www.linkedin.com/')
    time.sleep(1)
    log_in()
    driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3599781855&distance=25&f_E=1%2C2&f_TPR=r86400&f_WT=1%2C2%2C3&geoId=103263110&keywords=data%20analyst&sortBy=R')
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[1]')))
    a = 0
    i = 0
    while True:
        # try:
            # i += a
        for i in range(25):
            print(i)
            job = driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i+1}]')
            job.click()
            time.sleep(1)
                # if i % 6 == 0:
                #     driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{10}]/div/div[1]/div[1]').click()
                #     driver.execute_ script("window.scrollTo(0, document.body.scrollHeight);")
                #     time.sleep(2)
        # except:
        #     a = i
        #     time.sleep(2)
        #     print("last i: ",i)
        #     print("fail")




main()

