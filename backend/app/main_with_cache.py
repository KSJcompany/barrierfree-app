from fastapi import FastAPI, Query
from typing import List
import shelve
import os

from app.utils.naver_api import search_naver_blog
from app.crawler.blog_crawler import get_naver_blog_content
from app.services.keyword_analysis import calculate_score
from app.services.summarizer import make_chatbot_summary

app = FastAPI()

# ✅ 캐시 경로 설정
CACHE_PATH = "app/cache/accessibility_cache.db"
os.makedirs("app/cache", exist_ok=True)

@app.get("/get_accessibility_score")
def get_accessibility_score(place: str = Query(..., description="장소명")):
    # 1. 캐시 확인
    with shelve.open(CACHE_PATH) as cache:
        if place in cache:
            result = dict(cache[place])
            result["from_cache"] = True
            return result

    # 2. 블로그 검색
    blog_urls = search_naver_blog(place)
    if not blog_urls:
        return {
            "error": "❌ 장소에 대한 리뷰를 찾을 수 없습니다.",
            "place": place
        }

    # 3. 본문 크롤링
    blog_contents = []
    for url in blog_urls:
        content = get_naver_blog_content(url)
        if content:
            blog_contents.append(content)

    if not blog_contents:
        return {
            "error": "❌ 블로그 본문 수집에 실패했습니다.",
            "place": place
        }

    # 4. 점수 계산
    combined_text = " ".join(blog_contents)
    score, pos_keywords, neg_keywords = calculate_score(combined_text)

    # 5. 요약 생성
    summary = make_chatbot_summary(place, pos_keywords, neg_keywords, blog_contents)

    # 6. 결과 구성
    result = {
        "place": place,
        "score": score,
        "positive_keywords": pos_keywords,
        "negative_keywords": neg_keywords,
        "review_samples": blog_contents,
        "chat_style_summary": summary,
        "from_cache": False
    }

    # 7. 캐시 저장
    with shelve.open(CACHE_PATH) as cache:
        cache[place] = result

    return result
