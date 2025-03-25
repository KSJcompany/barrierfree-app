import requests
from app.config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET

def search_naver_blog(place: str, display=3) -> list:
    try:
        url = "https://openapi.naver.com/v1/search/blog"
        headers = {
            "X-Naver-Client-Id": NAVER_CLIENT_ID,
            "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
        }
        params = {
            "query": place + " 후기",
            "display": display,
            "sort": "date"
        }

        res = requests.get(url, headers=headers, params=params)
        if res.status_code != 200:
            print(f"[ERROR] Naver API 응답 오류: {res.status_code}")
            return []

        items = res.json().get("items", [])
        return [item["link"] for item in items]

    except Exception as e:
        print(f"[예외] 네이버 블로그 검색 실패: {e}")
        return []

