from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"]) # 헤드리스 False, 창 최대화
    context = browser.new_context(no_viewport=True) # 최대화를 고정하려면 no_viewport=True 도 넣어줘야 함, args만 넣으면 다시 창이 줄어듬
    page = context.new_page()

    page.goto("https://www.naver.com/", wait_until='networkidle')
    page.fill('//*[@id="query"]', "코로나")
    page.press('//*[@id="query"]', "Enter")
    page.click('//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a')
    page.screenshot(path="news_tab_playwright.png")
    browser.close()