from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_naver_blog_content(blog_url: str) -> str:
    """
    네이버 블로그 본문 텍스트를 크롤링합니다.
    최신/구버전 에디터 모두 대응하며, iframe 안의 콘텐츠를 추출합니다.
    """
    try:
        options = Options()
        options.add_argument('--headless')            # 창 안 띄우고 백그라운드 실행
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--lang=ko_KR')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(blog_url)
        time.sleep(2)

        try:
            # 네이버 블로그는 본문이 iframe(mainFrame) 안에 있음
            driver.switch_to.frame("mainFrame")
            time.sleep(1)

            # 최신 에디터 (Smart Editor ONE)
            try:
                content = driver.find_element(By.CSS_SELECTOR, ".se-main-container").text
            except:
                # 구버전 에디터
                content = driver.find_element(By.ID, "postViewArea").text

        except Exception as inner_e:
            print(f"[본문 추출 실패] iframe 구조 인식 실패: {inner_e}")
            content = ""

        driver.quit()
        return content

    except Exception as e:
        print(f"[크롬 드라이버 오류] 블로그 본문 수집 실패: {e}")
        return ""
