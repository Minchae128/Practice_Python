from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--start-maximized"]) # 헤드리스 False, 창 최대화
    context = browser.new_context(no_viewport=True) # 최대화를 고정하려면 no_viewport=True 도 넣어줘야 함, args만 넣으면 다시 창이 줄어듬
    page = context.new_page()
    # 로그인
    page.goto("https://acme-test.uipath.com/login", wait_until='networkidle')
    page.fill('//input[@id = "email"]', "fortm2002@naver.com")
    page.fill('//input[@id = "password"]', "asdf1234")
    page.click('//button[@class = "btn btn-primary"]')
    # 대쉬보드
    page.click('//button[@class = "btn btn-default btn-lg"]') # work items 클릭
    # Work Items
    page_num = 1 # 시작페이지
    data = []

    while True:
        # page.wait_for_timeout(2000) # expect_navigation() 기능 사용으로 비활성화
        # 데이터 추출 로직
        rows = page.query_selector_all('xpath=//table[@class = "table"]//tr') # 모든 행
        for row in rows[1:]: # 첫 번째는 컬럼 데이터
            href = row.query_selector('xpath=./td[1]/a').get_attribute('href') # 링크 추출
            cells = row.query_selector_all('xpath=./td') # 행 안에 있는 모든 셀 데이터
            row_data = [cell.text_content() for cell in cells] # 리스트 컴프리헨션으로 모든 셀 데이터의 텍스트를 저장
            row_data[0] = href # 리스트 첫 번째 요소 변경
            data.append(row_data) # 행 데이터 저장
            # print(row_data)

        # 다음페이지 로직
        page_num += 1 
        next_page = page.query_selector(f'xpath=//a[@class = "page-numbers" and text() = "{page_num}"]')
        if next_page: # 다음 페이지 엘리먼트가 있는지 확인
            # next_page.click()이 호출되어 페이지 이동이 시작될 때 해당 이동이 완료될 때까지 대기
            with page.expect_navigation():
                next_page.click()
        else:
            break # 다음 페이지에 해당하는 엘리먼트가 없으면 반복문 종료

    browser.close() # 브라우저 종료
    df = pd.DataFrame(data, columns=['href', 'WIID', 'Description', 'Type', 'Status', 'Date'])
    df.to_excel('acme_items.xlsx', index=False) # 데이터 저장