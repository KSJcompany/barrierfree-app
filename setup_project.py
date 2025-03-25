import os

folders = [
    "app",
    "app/crawler",
    "app/services",
    "app/utils",
    "app/cache"
]

files = {
    "app/main_with_cache.py": "# 🔧 FastAPI 진입점 (기본 구조, 나중에 채워넣기)\n\nfrom fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/')\ndef root():\n    return {'message': 'Hello Barrier-Free World!'}",
    "app/crawler/blog_crawler.py": "# 📄 블로그 본문 크롤링 함수 (Selenium)\ndef get_naver_blog_content(blog_url):\n    pass  # TODO: implement",
    "app/services/keyword_analysis.py": "# 📊 키워드 기반 점수 분석 함수\ndef calculate_score(text):\n    pass  # TODO: implement",
    "app/services/summarizer.py": "# 🤖 EXAONE 챗봇 스타일 요약 함수\ndef make_chatbot_summary(place, pos_keywords, neg_keywords, reviews):\n    pass  # TODO: implement",
    "app/utils/naver_api.py": "# 🌐 네이버 블로그 검색 API 호출 함수\ndef search_naver_blog(place):\n    pass  # TODO: implement",
    "requirements.txt": "fastapi\nuvicorn\nselenium\nwebdriver-manager\ntransformers\nsentencepiece\nrequests\nbeautifulsoup4\nstreamlit",
    "README.md": "# 🧠 Barrier-Free 챗봇 프로젝트\n\n장소명 기반으로 블로그 리뷰를 분석하여 휠체어 접근성(배리어프리 점수)을 예측합니다.",
    "streamlit_app.py": "# 📱 Streamlit 웹 UI (추후 작성)\n\nimport streamlit as st"
}

def setup_project():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"📁 생성됨: {folder}")
    for filepath, content in files.items():
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            print(f"📄 파일 생성됨: {filepath}")
    print("\n✅ 프로젝트 폴더가 성공적으로 생성되었습니다!")

if __name__ == "__main__":
    setup_project()
