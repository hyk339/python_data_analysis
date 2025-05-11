from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.naver.com/'
driver.get(url)

# page_source 메서드를 통해 열려있는 창의 HTML 코드를 확인할 수도 있다.
# print(driver.page_source[1:1000])

#driver.find_element(By.LINK_TEXT, value='뉴스').click()
#driver.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[5]/a').click()

driver.find_element(By.CLASS_NAME, value = 'search_input').send_keys('퀀트 투자 포트폴리오 만들기')
driver.find_element(By.CLASS_NAME, value = 'btn_search').send_keys(Keys.ENTER)

time.sleep(2)

driver.find_element(By.CLASS_NAME, value='box_window').clear()
driver.find_element(By.CLASS_NAME, value='box_window').send_keys('네이버')
driver.find_element(By.CLASS_NAME, value='bt_search').click()

time.sleep(2)


# 스크롤 끝까지 내리기
#driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')


prev_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)

    curr_height = driver.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        break
    prev_height = curr_height


time.sleep(1)

print("=======test 1==========")


html = BeautifulSoup(driver.page_source, 'lxml')
txt = html.find_all(class_ = 'sds-comps-text sds-comps-text-ellipsis-1 sds-comps-text-type-headline1')
txt_list = [i.get_text() for i in txt]

print("=======test 2==========")

print(txt_list[0:10])


driver.quit()