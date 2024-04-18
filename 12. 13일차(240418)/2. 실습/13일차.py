# Playwright 라이브러리에서 sync_playwright 함수를 가져옵니다.
from playwright.sync_api import sync_playwright

# Playwright를 사용하여 브라우저 조작을 시작합니다.
with sync_playwright() as p:
    
    # Chromium 브라우저를 띄우고, 최대화된 상태로 시작합니다.
    # headless=False로 설정하여 브라우저를 헤드리스 모드가 아닌 일반 모드로 실행합니다.
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])

    # 새로운 페이지를 생성합니다.
    # 뷰포트를 사용하지 않도록 설정합니다.
    page = browser.new_page(no_viewport=True)

    # 생성한 페이지를 지정된 URL로 이동시킵니다.
    page.goto('https://www.naver.com')

    # 페이지의 타이틀을 출력합니다.
    print(page.title())

    link_url = page.get_attribute('//*[@id="shortcutArea"]/ul/li[6]/a', 'href')

    print(link_url)
    
    page.goto(link_url)

    # 사용자 입력을 기다립니다. (프로그램을 종료하지 않기 위함)
    input('대기중>>>>>')

    # 브라우저를 닫습니다.
    browser.close()
