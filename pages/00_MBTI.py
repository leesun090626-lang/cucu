................................import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천 🌟", page_icon="🧭", layout="centered")

st.title("MBTI로 찾는 진로 추천 💡")
st.write("원하는 MBTI 유형을 골라봐! 그 유형에 잘 맞는 진로 2가지와, 각 진로에 어울리는 학과와 성격 특징까지 친절하게 알려줄게~ 😊")

MBTI_DATA = {
    "ISTJ": [
        {"career":"회계사 📊", "majors":"회계학, 경영학", "personality":"꼼꼼하고 책임감 강함, 규칙·절차를 잘 지켜요"},
        {"career":"공무원 🏛️", "majors":"행정학, 법학", "personality":"안정성과 조직 내 규범을 선호하는 타입"}
    ],
    "ISFJ": [
        {"career":"간호사 ❤️‍🩹", "majors":"간호학", "personality":"배려심 깊고 세심해서 돌봄 역할에 딱이에요"},
        {"career":"사회복지사 🤝", "majors":"사회복지학, 상담학", "personality":"다른 사람 도와주는 데 기쁨을 느껴요"}
    ],
    "INFJ": [
        {"career":"상담사 🗣️", "majors":"심리학, 상담학", "personality":"사람의 내면을 이해하려 하고 공감 능력 높음"},
        {"career":"작가/창작자 ✍️", "majors":"문예창작, 국문학, 미디어학", "personality":"심오한 아이디어와 가치를 표현하길 좋아해요"}
    ],
    "INTJ": [
        {"career":"연구원 🔬", "majors":"자연과학, 공학, 수학", "personality":"전략적이고 체계적으로 문제를 푸는 걸 좋아함"},
        {"career":"전략 컨설턴트 ♟️", "majors":"경영학, 경제학", "personality":"장기적 계획과 구조를 설계하는 데 강함"}
    ],
    "ISTP": [
        {"career":"기계/항공 엔지니어 🛠️", "majors":"기계공학, 항공우주공학", "personality":"실용적이고 손으로 만드는 걸 즐겨요"},
        {"career":"현장 기술자 ⚙️", "majors":"전기·전자, 산업공학", "personality":"문제 해결을 즉시 실행하는 스타일"}
    ],
    "ISFP": [
        {"career":"그래픽/패션 디자이너 🎨", "majors":"디자인학, 시각디자인", "personality":"미적 감각과 감정 표현이 뛰어나요"},
        {"career":"사진작가/아티스트 📸", "majors":"사진학, 예술학", "personality":"순간의 감성을 잘 포착하는 타입"}
    ],
    "INFP": [
        {"career":"문학/콘텐츠 작가 ✨", "majors":"문예창작, 미디어·커뮤니케이션", "personality":"가치 중심적이고 상상력이 풍부해요"},
        {"career":"심리상담사 💬", "majors":"심리학, 상담학", "personality":"타인의 이야기를 공감하며 듣는 데 강함"}
    ],
    "INTP": [
        {"career":"데이터 과학자 📈", "majors":"통계학, 컴퓨터공학, 산업공학", "personality":"논리적 분석과 호기심이 많음"},
        {"career":"연구 개발(R&D) 🧠", "majors":"물리·화학·공학계열", "personality":"이론과 개념을 깊게 파고드는 것을 좋아함"}
    ],
    "ESTP": [
        {"career":"영업/트레이더 💼", "majors":"경영학, 경제학", "personality":"순간 판단과 설득력이 뛰어나요"},
        {"career":"응급구조/현장 운영 🚑", "majors":"응급구조학, 산업안전학", "personality":"액션 지향적이며 스트레스 상황에서도 침착함"}
    ],
    "ESFP": [
        {"career":"공연예술가/MC 🎤", "majors":"연극영화, 방송·연예학", "personality":"사람들 앞에서 빛나는 걸 즐기고 에너지가 넘침"},
        {"career":"이벤트 플래너 🎉", "majors":"관광경영, 이벤트·엔터테인먼트학", "personality":"사교적이고 즉흥 상황을 잘 관리함"}
    ],
    "ENFP": [
        {"career":"마케팅/브랜드 기획 🚀", "majors":"광고홍보, 경영학", "personality":"아이디어가 많고 사람을 연결하는 능력 탁월"},
        {"career":"창업가/스타트업 🧩", "majors":"경영학, 컴퓨터공학(아이디어 기반)", "personality":"새로운 가능성을 실험하길 좋아함"}
    ],
    "ENTP": [
        {"career":"스타트업 창업가 💡", "majors":"경영학, 컴퓨터공학, 디자인", "personality":"논쟁적이고 창의적이며 기회를 포착함"},
        {"career":"제품 기획/전략가 🧭", "majors":"산업디자인, 경영학, 컴퓨터공학", "personality":"문제의 핵심을 빠르게 파악하고 해결책 제시"}
    ],
    "ESTJ": [
        {"career":"프로젝트 매니저 📌", "majors":"경영학, 산업공학", "personality":"조직적이고 실행력이 뛰어나 리드하기 좋아함"},
        {"career":"군무/조직 관리 🪖", "majors":"행정학, 경찰행정학", "personality":"규율과 책임을 중시하는 타입"}
    ],
    "ESFJ": [
        {"career":"교사/교육 코디네이터 🍎", "majors":"교육학, 유아교육", "personality":"사람을 돌보고 조직화하는 데 재능이 있음"},
        {"career":"의료/간호 관리 🏥", "majors":"보건행정, 간호학", "personality":"팀 돌봄과 대인관계 조율에 강함"}
    ],
    "ENFJ": [
        {"career":"HR/조직 개발자 🌱", "majors":"경영학(인사), 심리학", "personality":"사람을 이끌고 성장시키는 걸 좋아함"},
        {"career":"교육/코칭 전문가 🎯", "majors":"교육학, 상담학", "personality":"동기부여와 멘토링에 능숙"}
    ],
    "ENTJ": [
        {"career":"CEO/경영자 🏆", "majors":"경영학, 경제학", "personality":"결단력 있고 목표 지향적이며 리더십 강함"},
        {"career":"경영 전략 컨설턴트 📋", "majors":"경영학, 경제학, 통계학", "personality":"문제 구조화와 솔루션 제시에 능숙"}
    ]
}

mbti_list = list(MBTI_DATA.keys())
selected = st.selectbox("MBTI 유형을 선택해줘:", mbti_list)

if st.button("추천 받기 💫"):
    st.markdown(f"### {selected}에게 어울리는 진로 🌈")
    careers = MBTI_DATA.get(selected, [])
    for i, item in enumerate(careers, 1):
        st.subheader(f"{i}. {item['career']}")
        st.write(f"**추천 학과:** {item['majors']}")
        st.write(f"**어울리는 성격:** {item['personality']}")
        st.write("---")

st.caption("청소년에게 친근한 말투로 만들었어요 — 마음에 안 들면 바꿔줄게! ✨")



















































































































































































































































































































































































































