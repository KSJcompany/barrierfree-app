# 📊 키워드 기반 배리어프리 점수 계산

# 긍정/부정 키워드 정의 (상황에 따라 확장 가능)
positive_keywords = ["휠체어", "유모차", "경사로", "엘리베이터", "슬로프", "평지"]
negative_keywords = ["계단", "문턱", "턱 있음", "좁음", "높낮이", "미끄러움"]

def calculate_score(text: str):
    """
    블로그 텍스트에서 긍정/부정 키워드를 카운트하여 배리어프리 점수를 계산합니다.
    기본 점수는 50점이며, 키워드에 따라 ± 가중치를 적용합니다.
    """
    score = 50
    pos_found = []
    neg_found = []

    for word in positive_keywords:
        if word in text:
            pos_found.append(word)
            score += 10

    for word in negative_keywords:
        if word in text:
            neg_found.append(word)
            score -= 15

    # 점수 범위 보정
    score = max(0, min(100, score))

    return score, pos_found, neg_found
