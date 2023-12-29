import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
import pandas as pd
import folium
from PIL import Image
import emoji
import os

# Page setting
st.set_page_config(layout="wide", page_title="공항 이상행동 탐지 솔루션")


# 사이드 바 꾸미기
with st.sidebar: 
#logo 삽입
    st.markdown("""
    <center style='margin-top: -75px; margin-bottom: 20px;'>
        <img src='https://github.com/Hyunah0127/Aivle/blob/main/%EB%B9%85%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C/logo6.png?raw=true' width=170>
    </center>
    """, unsafe_allow_html=True)

# OptionMenu 생성
    options = [
        emoji.emojize("실시간 CCTV"),
        emoji.emojize("EVENT"),
        emoji.emojize("구역별 혼잡도")
        ]
    selected = option_menu(menu_title="MENU",  # 메뉴 제목
    options=options, menu_icon="airplane")
        
# 실시간 CCTV 누를 때
# 실시간 CCTV 탭 선택 시 메인 화면에 탭 생성
if selected == emoji.emojize("실시간 CCTV"):
     # Markdown을 사용한 스타일링 타이틀
    st.markdown("""
        <style>
        .big-font {
            font-size:36px !important;
            font-weight: bold;
            color: #1B365C;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">실시간 CCTV</p>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["1층", "2층", "3층"])

    with tab1:
                    
        # 각 CCTV 위치에 해당하는 동영상 파일 경로 또는 URL
        video_file_paths = [
            os.path.abspath('C:/Users/user/aivle school/빅프로젝트/대시보드/fi001.mp4'),  # 첫 번째 CCTV 동영상 파일 경로
            os.path.abspath('C:/Users/user/aivle school/빅프로젝트/대시보드/fi001.mp4'),   # 두 번째 CCTV 동영상 파일 경로
            os.path.abspath('C:/Users/user/aivle school/빅프로젝트/대시보드/fi001.mp4'),
            os.path.abspath('C:/Users/user/aivle school/빅프로젝트/대시보드/fi001.mp4'),
            os.path.abspath('C:/Users/user/aivle school/빅프로젝트/대시보드/fi001.mp4'),
            os.path.abspath('C:/Users/user/aivle school/빅프로젝트/대시보드/fi001.mp4'),
            os.path.abspath('C:/Users/user/aivle school/빅프로젝트/대시보드/fi001.mp4'),
            os.path.abspath('C:/Users/user/aivle school/빅프로젝트/대시보드/fi001.mp4'),
            os.path.abspath('C:/Users/user/aivle school/빅프로젝트/대시보드/fi001.mp4'),
        ]

        # 3행 3열 그리드 생성 및 각 그리드에 동영상 삽입
        for i in range(3):  # 3행
            cols = st.columns(3)  # 각 행에 3열
            for j, col in enumerate(cols, start=1):
                with col:
                    # 현재 행과 열에 따라 CCTV 번호 계산
                    cctv_number = i * 3 + j
                    st.subheader(f"CCTV {cctv_number}")
                    # 각 CCTV 번호에 해당하는 동영상 재생
                    st.video(video_file_paths[cctv_number - 1],start_time=0)

    with tab2:
        st.write("2층")

    with tab3:
        st.write("3층")
        
        

# EVENT 누를 떄
if selected == emoji.emojize("EVENT"):
     # Markdown을 사용한 스타일링 타이틀
    st.markdown("""
        <style>
        .big-font {
            font-size:36px !important;
            font-weight: bold;
            color: #1B365C;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">사고발생 현황</p>', unsafe_allow_html=True)

   