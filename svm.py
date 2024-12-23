from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading

def myfunc(): 
    service = Service(ChromeDriverManager().install())
    opt = webdriver.ChromeOptions()
    opt.add_argument("--log-level=1")

    driver = webdriver.Chrome(service=service, options=opt)
    website = "https://neal.fun/sun-vs-moon/"
    driver.get(website)
    time.sleep(2)
    sun_button = driver.find_element(By.TAG_NAME, "body").find_element(By.ID, "sun-btn")
    print(sun_button.text)
    while True:
        myChain = ActionChains(driver)
        myChain.w3c_actions.pointer_action._duration = 0   
        myChain.click(sun_button).perform()

t1 = threading.Thread(target=myfunc)
t2 = threading.Thread(target=myfunc)
t3 = threading.Thread(target=myfunc)
t4 = threading.Thread(target=myfunc)
t5 = threading.Thread(target=myfunc)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

