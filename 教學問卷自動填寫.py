from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

    

path="C:\\Users\\josh9\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe"  #####改為webdriver在你電腦中的路徑
chrome_options = Options()
#chrome_options.add_argument("--headless")  # 無頭模式
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
# 設置 ChromeDriver 服務
service = Service(path)

# 初始化 WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)


def write(driver):
    driver.implicitly_wait(5)
    # 示例：選擇 "我每堂課後用於本課程之平均時數" 為 "2-3小時"
    driver.execute_script("document.getElementById('basic_4').click();")
    time.sleep(random.uniform(2, 5))
    # 示例：選擇 "我上本課程的預期分數為" 為 "80-89分以上"
    driver.execute_script("document.getElementById('basic_8').click();")
    time.sleep(random.uniform(2, 4))
    # 示例：選擇 "我上本課程的出席率是" 為 "75%以上"
    driver.execute_script("document.getElementById('basic_12').click();")
    driver.implicitly_wait(0.8)
    # 示例：選擇 "課程有教學助理" 為 "是"
    driver.execute_script("document.getElementById('basic_15').click();")
    driver.implicitly_wait(0.9)
    # 示例：選擇 "課程內容" 為 "同意"
    driver.execute_script("document.getElementById('q_1').click();")
    driver.implicitly_wait(1)
    driver.execute_script("document.getElementById('q_7').click();")
    driver.implicitly_wait(0.6)
    driver.execute_script("document.getElementById('q_13').click();")
    driver.implicitly_wait(2)
    driver.execute_script("document.getElementById('q_19').click();")
    driver.implicitly_wait(1)
    driver.execute_script("document.getElementById('q_25').click();")
    driver.implicitly_wait(0.48)
    driver.execute_script("document.getElementById('q_31').click();")
    driver.implicitly_wait(0.74)
    driver.execute_script("document.getElementById('q_37').click();")
    driver.implicitly_wait(1.5)
    driver.execute_script("document.getElementById('q_43').click();")
    driver.implicitly_wait(0.9)
    driver.execute_script("document.getElementById('q_49').click();")
    driver.implicitly_wait(0.8)
    driver.execute_script("document.getElementById('q_55').click();")
    driver.implicitly_wait(1.2)
    driver.execute_script("document.getElementById('q_61').click();")
    driver.implicitly_wait(0.4)
    driver.execute_script("document.getElementById('q_67').click();")
    driver.implicitly_wait(0.7)
    driver.execute_script("document.getElementById('q_73').click();")
    driver.implicitly_wait(0.3)
    driver.execute_script("document.getElementById('q_79').click();")
    driver.implicitly_wait(0.66)
    driver.execute_script("document.getElementById('q_85').click();")
    driver.implicitly_wait(0.44)
    driver.execute_script("document.getElementById('q_91').click();")
    driver.implicitly_wait(0.37)
    ##
    driver.execute_script("document.getElementById('check00').click();")
    driver.implicitly_wait(0.84)
    driver.execute_script("document.getElementById('sendOK').click();")
    # 隨機等待，模擬人類行為
    driver.implicitly_wait(3)
    time.sleep(random.uniform(5, 10))
    # 先等待彈出框出現
    confirm_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "remodal-confirm")))
    # 點擊 "送出" 按鈕
    driver.execute_script("arguments[0].click();", confirm_button)
    time.sleep(random.uniform(5, 10))
    
 







driver.get("https://www026190.ccu.edu.tw/evaluation/001.php")
driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/input[1]").click()
time.sleep(random.uniform(2, 5))

driver.find_element(By.ID,"btn1").click()

driver.implicitly_wait(4)

username_element = driver.find_element(By.ID, "username")
username_element.send_keys("")  ### 輸入你自己的學號
driver.implicitly_wait(5)
time.sleep(random.uniform(4,5))
password_element=driver.find_element(By.ID, "password")
password_element.send_keys("")   #####  輸入你自己的密碼
driver.implicitly_wait(3)
time.sleep(random.uniform(3, 4))
# 創建 ActionChains 對象
actions = ActionChains(driver)

# 移動滑鼠到指定位置
actions.move_by_offset(10, 100).perform()

wait = WebDriverWait(driver, 10)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
time.sleep(random.uniform(2, 5))
    # 切換回主要的 frame
driver.switch_to.default_content()
driver.implicitly_wait(3)


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mdc-button mdc-button--raised']"))).click()
driver.implicitly_wait(4)

buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'填寫')]")

for button in buttons:
    # 點擊按鈕
    time.sleep(random.uniform(3,5))
    button.click()
    # 填寫問卷
    write(driver)
    driver.implicitly_wait(5)
    
     # 等待警報框出現
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    
    # 選擇警報框
    alert = driver.switch_to.alert
    
    # 點擊警報框的確定按鈕
    alert.accept()
    
    # 切換回主要的 frame
    driver.switch_to.default_content()
