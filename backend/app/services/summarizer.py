from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ✅ EXAONE-T5 모델 로딩 (최초 1회 로드)
tokenizer = AutoTokenizer.from_pretrained("lg-ai/exaone-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("lg-ai/exaone-t5-base")

def make_chatbot_summary(place: str, pos_keywords: list, neg_keywords: list, reviews: list) -> str:
    """
    장소에 대한 리뷰와 키워드를 바탕으로 챗봇 스타일의 접근성 요약을 생성합니다.
    """

    # 입력 텍스트 생성
    review_text = " ".join(reviews[:2])[:1000]  # 길이 제한 대비 자름

    prompt = f"""
장소 접근성 요약 요청

장소명: {place}
긍정 키워드: {', '.join(pos_keywords) or '없음'}
부정 키워드: {', '.join(neg_keywords) or '없음'}
리뷰 요약: {review_text}

출력: 사용자에게 {place}의 휠체어 접근성을 설명해 주세요. 2~3문장으로 자연스럽고 친절하게 알려주세요.
""".strip()

    # 토큰화 및 모델 생성
    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=128,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
