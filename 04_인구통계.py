import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(page_title="서울시 연령별 인구 분석", page_icon="🌆", layout="wide")

st.title("🌆 서울시 자치구별 연령 인구 분포 대시보드")
st.markdown("2025년 10월 기준 서울시 각 구의 **연령별 인구 분포**를 확인할 수 있습니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("popuiation.csv", encoding="cp949")
    # 숫자형 변환
    cols = [c for c in df.columns if "2025년10월_거주자_" in c and "세" in c]
    for c in cols:
        df[c] = df[c].astype(str).str.replace(",", "").astype(int)
    return df, cols

df, age_cols = load_data()

# 행정구역명 정리
df["행정구역"] = df["행정구역"].str.replace(r"\s*\(.*\)", "", regex=True)

# 서울시 전체 제거하고 구별만 선택
gu_list = df["행정구역"].tolist()[1:]

# 지역 선택
selected_gu = st.selectbox("📍 자치구를 선택하세요", gu_list)

# 선택된 구 데이터 필터링
gu_data = df[df["행정구역"] == selected_gu].iloc[0]

# 연령별 데이터 추출
age_numbers = [int(c.split("_")[-1].replace("세", "").replace("이상", "100")) for c in age_cols]
pop_values = [gu_data[c] for c in age_cols]

# 데이터프레임 구성
plot_df = pd.DataFrame({
    "연령": age_numbers,
    "인구수": pop_values
})

# Plotly 그래프
fig = px.line(
    plot_df,
    x="연령",
    y="인구수",
    markers=True,
    title=f"📊 {selected_gu} 연령별 인구 분포 (2025년 10월)",
    labels={"연령": "나이(세)", "인구수": "인구수(명)"},
)

fig.update_traces(line=dict(color="#3A86FF", width=3))
fig.update_layout(template="plotly_white", hovermode="x unified")

st.plotly_chart(fig, use_container_width=True)

# 추가 정보
st.markdown("---")
st.caption("데이터 출처: 서울특별시 통계포털 (2025년 10월 거주자 인구 기준)")
