from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.naver.com/")
driver.maximize_window()

# 코로나 검색
search_box = driver.find_element(By.XPATH, '//*[@id="query"]')
search_box.send_keys("코로나")
search_box.send_keys(Keys.ENTER)

# 뉴스탭을 클릭하기 위해 요소가 있는지 확인
news_tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a'))
)
news_tab.click()

# 스크린샷을 저장합니다.
driver.save_screenshot("news_tab_selenium.png")

driver.quit()
