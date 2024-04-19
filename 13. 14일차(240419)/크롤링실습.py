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

