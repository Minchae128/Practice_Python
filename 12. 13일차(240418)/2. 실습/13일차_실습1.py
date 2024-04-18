# pip install playwright
# playwright install
# pip install pandas
# pip install lxml
# pip install html5lib

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

    # 링크의 href 속성을 가져옵니다.
    link_url = page.get_attribute('//*[@id="shortcutArea"]/ul/li[6]/a', 'href')
    print(link_url)
    
    # 가져온 링크로 이동합니다.
    page.goto(link_url)

    # 클릭할 요소의 XPath를 제대로 지정합니다.
    page.click('//*[@id="menu"]/ul/li[4]/a')

    # 문서의 src 속성을 가져옵니다.
    doc_src = page.get_attribute('//*[@id="frame_ex1"]', 'src')
    #print(doc_src)


   # URL을 올바르게 조합하여 HTML 문서를 가져옵니다.
    response = page.goto(link_url + doc_src)
    html_content = response.text()


    # HTML 문서를 데이터프레임으로 변환합니다.
    doc_df = pd.read_html(html_content, encoding='CP949')[0]

    doc_df_reset = doc_df.reset_index(drop=True)

    doc_df_reset.columns = doc_df_reset.columns.droplevel()

    # 데이터프레임을 엑셀 파일로 저장합니다.
    doc_df_reset[['통화명', '매매기준율']].to_excel('환율정보.xlsx', sheet_name='컬럼두개저장실습', index=False)

    input('대기중>>>>')
    
   # 브라우저를 닫습니다.
    browser.close()