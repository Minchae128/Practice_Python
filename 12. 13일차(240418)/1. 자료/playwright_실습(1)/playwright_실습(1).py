from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    # 네이버 이동, wait_until로 네트워크 응답이 없을 때 까지 대기
    page.goto("https://www.naver.com/", wait_until='networkidle')
    # 코로나 검색
    page.fill('//*[@id="query"]', "RPA")
    page.press('//*[@id="query"]', "Enter")
    # 뉴스탭 클릭
    page.click('//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a')
    page.wait_for_timeout(1000)
    
    # 뉴스 기사 항목 선택
    page.wait_for_selector('//div[@class = "news_area"]')

    for _ in range(0, 3):
        page.keyboard.press('End')
        page.wait_for_timeout(500)

    elements = page.query_selector_all('xpath=//div[@class = "news_area"]')

    news_data = []

    for element in elements:
        title = element.query_selector('xpath=.//a[@class = "news_tit"]').text_content().strip()
        link = element.query_selector('xpath=.//a[@class = "news_tit"]').get_attribute('href').strip()
        content = element.query_selector('xpath=.//div[@class = "news_dsc"]').text_content().strip()
        news_data.append({'title': title, 'content': content, 'link': link})

    df = pd.DataFrame(news_data)

    df.to_excel('뉴스.xlsx', index=False)

    browser.close()