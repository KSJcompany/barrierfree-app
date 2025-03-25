import streamlit as st
import requests

st.set_page_config(page_title="배리어프리 분석 챗봇", page_icon="🧠")
st.title("🧠 장소 배리어프리 접근성 분석기")

# 🔹 장소명 입력
place = st.text_input("장소명을 입력하세요 (예: 서울숲, 여의도공원 등)")

if st.button("분석하기") and place:
    with st.spinner("리뷰 분석 중..."):
        try:
            # FastAPI 서버로 요청
            response = requests.get(
                "http://localhost:8000/get_accessibility_score",
                params={"place": place}
            )

            if response.status_code == 200:
                data = response.json()

                if "error" in data:
                    st.error(data["error"])
                else:
                    st.success(f"📍 '{place}'에 대한 분석 결과입니다!")

                    # 캐시 여부 안내
                    if data.get("from_cache"):
                        st.info("📦 캐시된 결과입니다 (분석된 장소입니다).")
                    else:
                        st.success("✅ 새로 분석된 결과입니다.")

                    # 점수 표시
                    st.metric(label="접근성 점수", value=f"{data['score']}점")

                    # 키워드 시각화
                    st.subheader("✅ 긍정 키워드")
                    st.write(", ".join(data["positive_keywords"]) or "없음")

                    st.subheader("❌ 부정 키워드")
                    st.write(", ".join(data["negative_keywords"]) or "없음")

                    # 챗봇 스타일 요약
                    st.subheader("🤖 챗봇 요약")
                    st.write(data["chat_style_summary"])

                    # 리뷰 본문
                    st.subheader("📄 리뷰 샘플")
                    for i, review in enumerate(data["review_samples"], start=1):
                        st.markdown(f"**리뷰 {i}**")
                        st.text_area(f"리뷰 본문 {i}", review, height=150)

            else:
                st.error(f"서버 오류: {response.status_code}")

        except Exception as e:
            st.error(f"요청 중 오류가 발생했습니다: {e}")
