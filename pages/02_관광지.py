# app.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def main():
    st.title("서울 주요 관광지 지도 보기")
    st.write("외국인 관광객에게 인기가 높은 서울의 주요 관광지 TOP 10을 지도에 표시합니다.")
    
    # 관광지 정보 리스트 (이름, 위도, 경도)
    places = [
        ("Gyeongbokgung Palace", 37.579617, 126.977041),
        ("Bukchon Hanok Village", 37.582604, 126.983400),
        ("N Seoul Tower", 37.551169, 126.988227),
        ("Insadong", 37.574107, 126.985059),
        ("Myeongdong", 37.560596, 126.985877),
        ("Dongdaemun Design Plaza (DDP)", 37.566794, 127.009368),
        ("Hongdae (Hongik Univ. area)", 37.557174, 126.924789),
        ("Changdeokgung Palace + Secret Garden", 37.579544, 126.991932),
        ("Cheonggyecheon Stream", 37.569180, 126.979200),
        ("Lotte World Tower & Mall", 37.514474, 127.100410),
    ]
    
    df = pd.DataFrame(places, columns=["Name", "Lat", "Lon"])
    st.subheader("관광지 리스트")
    st.dataframe(df)
    
    # 지도 생성
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["Lat"], row["Lon"]],
            popup=row["Name"],
            tooltip=row["Name"]
        ).add_to(m)
        
    st.subheader("지도에서 위치 보기")
    st_folium(m, width=700, height=500)

if __name__ == "__main__":
    main()

