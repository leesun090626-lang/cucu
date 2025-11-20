import streamlit as st

# MBTI -> (dessert, tea, emoji, one-line reason, pairing sentence)
PAIRS = {
    "ISTJ": ("Victoria sponge (UK)", "Earl Grey", "📚🍰", "클래식하고 믿음직한 맛의 조합이에요.", "버터리한 스펀지와 베르가못 향의 얼그레이가 안정감 있게 어우러져요."),
    "ISFJ": ("Apple pie (USA)", "Chamomile", "🏡🥧", "따뜻하고 포근한 느낌을 주는 조합이에요.", "달큼한 사과와 부드러운 카모마일이 편안하게 마음을 녹여줘요."),
    "INFJ": ("Yokan (일본의 단팥젤리)", "Genmaicha (현미녹차)", "🌙🍵", "섬세하고 사려깊은 감성을 잘 살려줘요.", "부드러운 단맛과 고소한 현미녹차가 은은하게 어울려요."),
    "INTJ": ("Dark chocolate fondant", "Pu-erh", "🧠🍫", "깊고 복합적인 풍미를 즐기는 타입에게 좋아요.", "진한 초콜릿과 발효된 푸얼의 흙향이 강렬하게 조화돼요."),
    "ISTP": ("Basque burnt cheesecake", "Tieguanyin Oolong", "🔧🧀", "텍스처와 향의 대조를 즐기기 좋아요.", "겉은 탄, 속은 부드러운 치즈케이크와 고소한 청향 우롱이 잘 맞아요."),
    "ISFP": ("Crème brûlée", "Jasmine tea", "🎨✨", "감각적인 풍미를 좋아하는 사람에게 추천해요.", "카라멜화된 설탕과 은은한 자스민 향이 부드럽게 연결돼요."),
    "INFP": ("Strawberry mochi", "Matcha", "🌸🍡", "몽환적이고 서정적인 맛의 조합이에요.", "쫄깃한 모찌의 달콤함과 말차의 흙내음이 동화처럼 어울려요."),
    "INTP": ("Lemon tart", "Sencha", "🔎🍋", "상쾌하고 논리적인 대조를 좋아한다면 좋아요.", "상큼한 레몬의 산미와 녹차의 깔끔함이 머리를 맑게 해줘요."),
    "ESTP": ("Baklava", "Moroccan mint tea", "⚡️🍯", "에너지 넘치고 즉각적인 만족을 주는 조합이에요.", "진한 꿀과 견과의 달콤함을 상쾌한 민트가 깔끔하게 정리해줘요."),
    "ESFP": ("Chocolate éclair", "Assam", "🎉🍫", "화려하고 즉흥적인 즐거움을 좋아하는 타입이에요.", "진한 초콜릿 필링과 풀바디 홍차의 힘이 무대 같아요."),
    "ENFP": ("Assorted macarons", "Rooibos (vanilla)", "🌈🍥", "호기심 많고 다채로운 맛을 즐기기 좋아요.", "사르르 녹는 마카롱과 부드러운 루이보스 바닐라가 편하고 즐거워요."),
    "ENTP": ("Tiramisu", "Lapsang Souchong", "💡☕️", "도발적이고 실험적인 대비를 즐겨요.", "커피향 마스카르포네와 스모키한 차의 대조가 놀랍도록 잘 어울려요."),
    "ESTJ": ("Black Forest cake", "Darjeeling", "🏛️🍒", "전통적이고 품격 있는 선택이에요.", "체리와 초콜릿의 조합을 다즐링의 꽃향이 정교하게 받쳐줘요."),
    "ESFJ": ("New York cheesecake", "English Breakfast", "🤝🧁", "사교적이고 모두에게 사랑받는 조합이에요.", "리치한 치즈케이크와 클래식한 잉글리시 브렉퍼스트가 편안하게 어울려요."),
    "ENFJ": ("Pavlova", "Darjeeling (2nd flush 추천)", "🌟🥥", "우아하고 사람을 돋보이게 하는 선택이에요.", "가벼운 머랭과 상큼한 과일이 다즐링의 섬세함과 잘 어우러져요."),
    "ENTJ": ("Opera cake", "Keemun black tea", "🚀🎂", "야망 있고 구조적인 맛을 선호하는 분께 좋아요.", "여러 층의 커피-초코와 금방 느껴지는 키문 차의 균형이 탁월해요.")
}

st.set_page_config(page_title="MBTI 디저트 & 티 추천 🫖🍰", page_icon="🧁")

st.title("MBTI로 고르는 디저트 & 티 추천! 🎯")
st.write("너의 MBTI를 고르면 잘 어울리는 디저트와 티를 추천해줄게 — 실제로 존재하는 메뉴만 골랐어. 😄")

mbti = st.selectbox("MBTI를 선택해줘:", list(PAIRS.keys()))

if mbti:
    dessert, tea, emoji, one_liner, pairing = PAIRS[mbti]

    st.markdown(f"### {mbti} 추천 조합 {emoji}")
    st.write(f"**디저트:** {dessert}")
    st.write(f"**티:** {tea}")

    st.markdown("---")
    st.write(f"**왜 이 조합을 추천하는지?** {one_liner}")
    st.write(f"**어떻게 잘 어울리는가?** {pairing}")

    # Fun serving suggestion
    st.info("서빙 팁: 디저트는 작은 조각으로, 차는 한 모금씩 천천히 마셔봐 — 맛의 층을 더 잘 느낄 수 있어! ☕️✨")

    st.markdown("---")
    st.write("**참고:** 추천한 디저트와 티는 전 세계에서 실제로 찾아볼 수 있는 종류들이에요. 스트릿푸드/카페에 따라 레시피가 조금씩 달라질 수 있어요.")

    st.balloons()

# Footer
st.write("앱을 스트림릿 클라우드에 올리려면 이 파일을 repo에 넣고 배포하면 돼요. 궁금하면 도와줄게! 💪")
