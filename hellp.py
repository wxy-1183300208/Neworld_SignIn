from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 创建Chrome驱动程序，自动管理ChromeDriver版本
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# 从环境变量中读取数据，包含账号密码和登录页面测试
u = os.environ["USERNAME"]
p = os.environ["PASSWORD"]

print('u', u)
print('p', p)
driver.get("https://neworld.cloud/auth/login")

# 获取cookies
time.sleep(5)

# 账号密码登录
driver.find_element(By.ID, 'email').clear()
driver.find_element(By.ID, "email").send_keys(u)

driver.find_element(By.ID, 'passwd').clear()
driver.find_element(By.ID, "passwd").send_keys(p)

time.sleep(1)
driver.find_element(By.ID, "login").click()

# 刷新页面
driver.refresh()

# 再次刷新页面
driver.refresh()

# 点击签到按钮
driver.find_element(By.ID, "checkin").click()
