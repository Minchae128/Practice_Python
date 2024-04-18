# pip install playwright
# playwright install
# pip install pandas
# pip install lxml
# pip install html5lib

# 1. 네이버에 RPA를 검색
# 2.뉴스 탭 이동
# 3. 뉴스의 제목, 내용, 주소를 엑셀 파일로 만들어서 저장
# 힌트 : query_selector_all를 사용해보세요 / gpt랑 해보세용

# Playwright 라이브러리에서 sync_playwright 함수를 가져옵니다.
from playwright.sync_api import sync_playwright
import pandas as pd  # pandas 라이브러리를 가져옵니다.

# Playwright 라이브러리에서 sync_playwright 함수를 가져옵니다.
from playwright.sync_api import sync_playwright
import pandas as pd  # pandas 라이브러리를 가져옵니다.

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

    # 검색창에 RPA를 입력하기 위해 검색창을 클릭합니다.
    page.click('//*[@id="query"]')
    
    # 검색창에 'RPA'를 입력합니다.
    page.fill('//*[@id="query"]', 'RPA')
    
    # 검색 버튼을 클릭하여 검색을 수행합니다.
    page.click('//*[@id="sform"]/fieldset/button')
    
    # 네이버 뉴스 탭으로 이동하기 위해 뉴스 탭을 클릭합니다.
    page.click('//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a')
    
    # 뉴스 제목, 내용, 링크를 저장할 리스트를 초기화합니다.
    news_titles = []  # 뉴스 제목을 저장할 리스트
    news_contents = []  # 뉴스 내용을 저장할 리스트
    news_links = []  # 뉴스 링크를 저장할 리스트

    # 뉴스 제목을 추출합니다.
    news_title_elements = page.query_selector_all('.news_tit')

    # 뉴스 제목을 리스트에 저장합니다.
    for title_element in news_title_elements:
        news_titles.append(title_element.inner_text())

    # 뉴스 내용을 추출합니다.
    news_content_elements = page.query_selector_all('.dsc_txt_wrap')

    # 뉴스 내용을 리스트에 저장합니다.
    for content_element in news_content_elements:
        news_contents.append(content_element.inner_text())

    # 뉴스 링크를 추출합니다.
    news_link_elements = page.query_selector_all('.news_tit')

    # 뉴스 링크를 리스트에 저장합니다.
    for link_element in news_link_elements:
        news_links.append(link_element.get_attribute('href'))

    # 뉴스 정보를 데이터프레임으로 변환합니다.
    news_df = pd.DataFrame({'제목': news_titles, '내용': news_contents, '링크': news_links})

    # 뉴스 정보를 엑셀 파일로 저장합니다.
    news_df.to_excel('뉴스_정보.xlsx', index=False)

    # 사용자 입력을 대기합니다.
    input('작업 완료! 엔터 키를 누르면 종료됩니다.')
    
   # 브라우저를 닫습니다.
    browser.close()