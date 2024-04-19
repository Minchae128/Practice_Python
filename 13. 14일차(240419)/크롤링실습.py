from playwright.sync_api import sync_playwright
import pandas as pd 


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)

    page.goto('https://acme-test.uipath.com/login')

    print(page.title())


    page.click('//*[@id="email"]')
    page.fill('//*[@id="email"]', 'wltnrhk@naver.com')

    page.click('//*[@id="password"]')
    page.fill('//*[@id="password"]', 'Q6.VztxHd$Mk6PM')

    page.click('//html/body/div/div[2]/div/div/div/form/button')

    page.click('//*[@id="dashmenu"]/div[2]/a/button')

    wild_list = []
    desxription_list = []
    type_list = []
    status = []
    date_list = []

    wild_list_elements = page.query_selector_all()

        # 뉴스 제목을 추출합니다.
    news_title_elements = page.query_selector_all('.news_tit')

    # 뉴스 제목을 리스트에 저장합니다.
    for title_element in news_title_elements:
        news_titles.append(title_element.inner_text())

page_num = 1
while True:
    page_num += 1
    next_page = page.query_selector(f'xpath=//a[@class="page-numbers" and text() = "{page_num}"]')

    if next_page:
        with page.expect_navigation():
            next_page.click()
    else:
        break

    


