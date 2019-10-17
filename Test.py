# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from lxml import etree
import warnings
import time

# 忽略警告
warnings.filterwarnings("ignore")
# 设置chromedriver的路径
driver_path = r"D:\Software_installation_program\chromedriver\chromedriver_win32\chromedriver.exe"
# 设置代理ip，谨防封掉自己的ip地址
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--proxy-server=http://125.123.120.109:9999")
# 启用chromedriver
driver = webdriver.Chrome(executable_path=driver_path)
# 使用代理
# driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
# 代理测试
# driver.get("http://httpbin.org/ip")
# 用户名Emile
# userName ='wh910512@163.com'
# 密码
# passWord ='wh910512'

driver.get('https://www.baidu.com/')
# driver.get('https://www.douban.com/')
# driver.get('https://analytics.zhihuiya.com/')
# driver.get('https://www.lagou.com/jobs/5348568.html?show=be57519d92034344beceeb194890329e')
driver.set_window_size(1500, 1000)
# 打开多个Tab、切换页面
# driver.execute_script("window.open('https://www.taobao.com/')")
# print(driver.current_url)
# driver.switch_to.window(driver.window_handles[1])
# print(driver.current_url)

# 页面缓冲时间（隐式等待）
# driver.implicitly_wait(3)
# 页面缓冲时间(显示等待-->智能)
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'kwssss'))
    )
    print(element)
except TimeoutException as ex:
    print(ex)
# else:
#     pass
# finally:
#     driver.close()


# html = etree.HTML(driver.page_source)
# html.xpath("")

# 百度测试
# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_name('wd')
# inputTag = driver.find_element_by_class_name('s_ipt')
inputTag = driver.find_element(By.ID, 'kw')
# inputTag.send_keys('python')
time.sleep(3)
inputTag.clear()
# submitBtn = driver.find_element(By.ID, 'su')
# submitBtn =driver.find_element_by_xpath("//*[@id='su']")
# submitBtn.click()
# 百度测试

# selenium行为链测试
# inputTag = driver.find_element_by_id('kw')
# submitBtn = driver.find_element(By.ID, 'su')
# actions = ActionChains(driver)
# actions.move_to_element(inputTag)
# actions.send_keys_to_element(inputTag, 'Python')
# actions.move_to_element(submitBtn)
# actions.click(submitBtn)
# actions.perform()

# 豆瓣测试 chexbox
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()
# 豆瓣测试 chexbox

# inputTag.clear()
# print(driver.page_source)
# 拉勾网测试


# 智慧芽
# 智慧芽取消rememberMe记忆功能
# rememberBtn = driver.find_element_by_name('rememberMe')
# rememberBtn.click()
# 智慧芽取消rememberMe记忆功能
# inputTag = driver.find_element_by_name('username')
# print(inputTag)
# inputTag.send_keys("ssss")
# 智慧芽
# driver.close()
# 智慧芽自动登录
# userNameInput = driver.find_element_by_name('username')
# passWordInput = driver.find_element_by_id('password')
# submitBtn = driver.find_element_by_id('log-button')
# loginActions = ActionChains(driver)
# loginActions.move_to_element(userNameInput)
# loginActions.send_keys_to_element(userNameInput, userName)
# loginActions.move_to_element(passWordInput)
# loginActions.send_keys_to_element(passWordInput, passWord)
# loginActions.move_to_element(submitBtn)
# loginActions.click()
# loginActions.perform()
# 智慧芽自动登录


'''
1、如果只是想要解析网页中的数据，那么推荐将网页源代码扔给lxml来解析，
因为lxml底层使用的是C语言，所以解析效率会更高。
2、如果是想要对元素进行一些操作，比如给一个文本 框输入值，或者是点击某个按钮，
那么必须使用selenium给我们提供的查找元素的方法。
常见的表单元素：input type = 'text/password/email/number'
button、input[type = 'submit']
chexbox：input = 'chexbox'
select；下拉列表
'''
