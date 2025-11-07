import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("🌍 국가별 MBTI 분포 시각화 대시보드")

# CSV 파일 로드
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 국가 선택
countries = df['Country'].unique()
selected_country = st.selectbox("국가를 선택하세요:", countries)

# 선택한 국가의 데이터 필터링
country_data = df[df['Country'] == selected_country].drop(columns=['Country'])

# MBTI 타입별 비율 정렬
country_data = country_data.melt(var_name='MBTI', value_name='Percentage')
country_data = country_data.sort_values('Percentage', ascending=False)

# 색상 설정 (1등 빨강 + 나머지 그라데이션)
colors = ['#FF0000'] + px.colors.sequential.Blues[len(country_data)-1:]

# 그래프 생성
fig = px.bar(
    country_data,
    x='MBTI',
    y='Percentage',
    title=f"{selected_country}의 MBTI 유형 비율",
    text='Percentage',
    color=country_data['MBTI'],
    color_discrete_sequence=colors
)

# 그래프 꾸미기
fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig.update_layout(
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (%)",
    showlegend=False,
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
