# app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, date

st.set_page_config(page_title="지하철 Top10 시각화", layout="wide")

st.title("📊 2025년 10월 — 역별 승·하차 합계 Top10")
st.markdown(
    """
    날짜(2025년 10월 중 하루)와 호선을 선택하면 해당 조건에서
    **승차총승객수 + 하차총승객수** 합계가 가장 큰 **상위 10개 역**을 인터랙티브 막대그래프로 보여줍니다.
    """
)

@st.cache_data
def load_csv(uploaded_file):
    # 다중 인코딩 시도(cp949, euc-kr, utf-8, latin1)
    encodings = ['cp949', 'euc-kr', 'utf-8', 'latin1']
    last_err = None
    for enc in encodings:
        try:
            df = pd.read_csv(uploaded_file, encoding=enc)
            return df
        except Exception as e:
            last_err = e
    # 마지막으로 판다스 자동 파서 시도
    try:
        uploaded_file.seek(0)
        return pd.read_csv(uploaded_file)
    except Exception:
        raise ValueError(f"파일을 읽을 수 없습니다. 마지막 에러: {last_err}")

def preprocess(df):
    # 열명 있는지 안전 체크(한국어 컬럼명 가정)
    expected = ['사용일자','노선명','역명','승차총승객수','하차총승객수']
    missing = [c for c in expected if c not in df.columns]
    if missing:
        raise ValueError(f"데이터에 필요한 컬럼이 없습니다: {missing}")

    # 사용일자 -> datetime 변환 (예: 20251001 또는 '20251001')
    df['사용일자'] = df['사용일자'].astype(str)
    # 8자리 YYYYMMDD 여부 체크
    def parse_ymd(s):
        s = s.strip()
        if len(s) == 8 and s.isdigit():
            return datetime.strptime(s, "%Y%m%d").date()
        # 다른 형식이면 판다스에 맡김
        try:
            return pd.to_datetime(s).date()
        except:
            return pd.NaT
    df['사용일자_parsed'] = df['사용일자'].apply(parse_ymd)
    # 숫자형 칼럼 안전 처리
    df['승차총승객수'] = pd.to_numeric(df['승차총승객수'], errors='coerce').fillna(0).astype(int)
    df['하차총승객수'] = pd.to_numeric(df['하차총승객수'], errors='coerce').fillna(0).astype(int)
    df['합계'] = df['승차총승객수'] + df['하차총승객수']
    return df

# --- 사이드바: 파일 업로드 & 필터 ---
st.sidebar.header("데이터 업로드 및 필터")
uploaded = st.sidebar.file_uploader("CSV 파일 업로드", type=['csv'], accept_multiple_files=False)

# Date picker: 2025-10-01 ~ 2025-10-31
min_date = date(2025,10,1)
max_date = date(2025,10,31)
sel_date = st.sidebar.date_input("날짜 선택 (2025년 10월)", value=min_date, min_value=min_date, max_value=max_date)

# 파일이 업로드되었을 때만 처리
if uploaded is None:
    st.info("CSV 파일을 업로드해 주세요. (예: 사용일자, 노선명, 역명, 승차총승객수, 하차총승객수 컬럼 포함)")
    st.stop()

try:
    df_raw = load_csv(uploaded)
except Exception as e:
    st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
    st.stop()

# 전처리
try:
    df = preprocess(df_raw)
except Exception as e:
    st.error(f"전처리 오류: {e}")
    st.stop()

# 호선 선택 박스 (데이터에 있는 고유 노선 기준)
lines = sorted(df['노선명'].dropna().unique().tolist())
lines_display = ["(전체)"] + lines
sel_line = st.sidebar.selectbox("호선 선택", lines_display, index=0)

# 필터링: 날짜 & 호선
filtered = df[df['사용일자_parsed'] == sel_date]
if sel_line != "(전체)":
    filtered = filtered[filtered['노선명'] == sel_line]

if filtered.empty:
    st.warning("선택한 조건에 해당하는 데이터가 없습니다. 날짜 또는 호선을 확인해주세요.")
    st.stop()

# 역 기준 집계 (역명으로 그룹)
agg = (
    filtered.groupby(['노선명','역명'], as_index=False)
    .agg({'승차총승객수':'sum','하차총승객수':'sum','합계':'sum'})
)

# Top10 by 합계
top10 = agg.sort_values('합계', ascending=False).head(10).reset_index(drop=True)

# 색상 생성: 1등 빨간색, 나머지는 블루 그라데이션(짙은->연한)
def make_colors(n):
    colors = []
    if n <= 0:
        return colors
    # 1등 빨강
    colors.append('rgba(255,0,0,1)')
    if n == 1:
        return colors
    # 기본 블루 RGB (Plotly 기본 파랑 계열)
    base = (0, 116, 217)  # (r,g,b)
    # 나머지 개수
    m = n - 1
    # 알파(투명도)를 1.0 -> 0.25 로 선형 감소시켜 '연해지는' 효과
    for i in range(m):
        alpha = 0.95 - (i * (0.7 / max(1, m-1))) if m>1 else 0.6
        r,g,b = base
        colors.append(f'rgba({r},{g},{b},{alpha:.2f})')
    return colors

colors = make_colors(len(top10))

# Plotly 막대 그리기
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=top10['역명'],
        y=top10['합계'],
        text=top10['합계'],
        textposition='auto',
        marker=dict(color=colors, line=dict(width=0.5, color='rgba(0,0,0,0.15)')),
        hovertemplate=
            '<b>%{x}</b><br>' +
            '노선: %{customdata[0]}<br>' +
            '승차: %{customdata[1]:,}<br>' +
            '하차: %{customdata[2]:,}<br>' +
            '합계: %{y:,}<extra></extra>',
        customdata=top10[['노선명','승차총승객수','하차총승객수']].values
    )
)

fig.update_layout(
    title=f"{sel_date.strftime('%Y-%m-%d')} — {sel_line if sel_line!='(전체)' else '전체 호선'} 기준 Top 10 역",
    xaxis_title="역명",
    yaxis_title="승차 + 하차 합계",
    template='simple_white',
    bargap=0.2,
    xaxis_tickangle=-45,
    margin=dict(l=40, r=20, t=80, b=150),
    height=600
)

# 반응형으로 출력
st.plotly_chart(fig, use_container_width=True)

# 데이터 테이블 보기 옵션
with st.expander("Top10 원본 데이터 보기 (테이블)"):
    st.dataframe(top10)

# 결측치 및 간단 요약
st.markdown("### 🔎 데이터 체크")
na_info = df_raw.isna().sum()
st.write("원본 데이터 결측치 개수(컬럼별):")
st.write(na_info)

st.markdown("### ⚙️ 사용 방법")
st.markdown(
    """
    1. 좌측에서 CSV 파일 업로드  
    2. 날짜(2025년 10월)를 선택  
    3. 호선을 선택하면 조건에 맞는 Top10 막대그래프가 출력됩니다.
    """
)
