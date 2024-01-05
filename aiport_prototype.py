import streamlit as st
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from PIL import Image
import emoji
import os
from urllib.parse import quote
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
import requests
import jsons
import datetime

# Page setting
st.set_page_config(layout="wide", page_title="공항 이상행동 탐지 솔루션")


# 사이드 바 꾸미기
with st.sidebar: 
#logo 삽입
    st.markdown("""
    <center style='margin-top: -75px; margin-bottom: 20px;'>
        <img src='https://github.com/jayjinnie/KT-AIVLE-SCHOOL-DX-4th/blob/cae9c2e2c4a1ba3eff2b31094d5502695b38937e/21_BigProject/image/logo.png?raw=true' width=170>
    </center>
    """, unsafe_allow_html=True)

# OptionMenu 생성
    options = [
        emoji.emojize("실시간 CCTV"),
        emoji.emojize("이상행동 발생 구역 모니터링"),
        emoji.emojize("구역별 혼잡도")
        ]
    selected = option_menu(menu_title="관제 서비스 선택",  # 메뉴 제목
    options=options, menu_icon="airplane")
        
# 실시간 CCTV 확인
# 실시간 CCTV 탭 선택 시 메인 화면에 탭 생성
if selected == emoji.emojize("실시간 CCTV"):
     # Markdown을 사용한 스타일링 타이틀
    st.markdown("""
        <style>
        .big-font {
            font-size:36px !important;
            font-weight: bold;
            color: #1B365C;
            margin-top: -70px;  # 텍스트 위의 여백 줄임
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<p class="big-font" style="color:white;">실시간 CCTV</p>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["1층", "2층", "3층", "4층"])

    with tab1:        
        # 각 CCTV 위치에 해당하는 동영상 파일 경로 또는 URL
        video_file_paths = [
            os.path.abspath('video/normal1.mp4'),  # CCTV 동영상 파일 경로
            os.path.abspath('video/normal2.mp4'),
            os.path.abspath('video/normal3.mp4'),
            os.path.abspath('video/normal4.mp4'),
            os.path.abspath('video/falldown_detection.mp4'),
            os.path.abspath('video/normal5.mp4')
        ]
        
        cctv_titles = [
            '1~3번 출입구',
            '4~6번 출입구',
            '7~9번 출입구',
            '10~12번 출입구',
            '13~14번 출입구',
            '택시 승강장'
        ]
        
        # 3행 3열 그리드 생성 및 각 그리드에 동영상 삽입
        for i in range(2):  # 3행
            cols = st.columns(3)  # 각 행에 3열
            for j, col in enumerate(cols, start=1):
                with col:
                    # 현재 행과 열에 따라 CCTV 번호 계산
                    cctv_number = i * 3 + j
                    st.subheader(cctv_titles[cctv_number - 1])
                    # 각 CCTV 번호에 해당하는 동영상 재생
                    st.video(video_file_paths[cctv_number - 1],start_time=0)



    with tab2:
        # 각 CCTV 위치에 해당하는 동영상 파일 경로 또는 URL
        video_file_paths = [
            os.path.abspath('video/normal5.mp4'),  # CCTV 동영상 파일 경로
            os.path.abspath('video/normal6.mp4'),
            os.path.abspath('video/normal7.mp4'),
            os.path.abspath('video/normal8.mp4'),
            os.path.abspath('video/normal9.mp4'),
            os.path.abspath('video/normal10.mp4')
        ]
        
        cctv_titles = [
            '입국심사 A게이트',
            '입국심사 B게이트',
            '입국심사 C게이트',
            '입국심사 D게이트',
            '입국심사 E게이트',
            '입국심사 F게이트'
        ]
        
        # 3행 3열 그리드 생성 및 각 그리드에 동영상 삽입
        for i in range(2):  # 3행
            cols = st.columns(3)  # 각 행에 3열
            for j, col in enumerate(cols, start=1):
                with col:
                    # 현재 행과 열에 따라 CCTV 번호 계산
                    cctv_number = i * 3 + j
                    st.subheader(cctv_titles[cctv_number - 1])
                    # 각 CCTV 번호에 해당하는 동영상 재생
                    st.video(video_file_paths[cctv_number - 1],start_time=0)

    with tab3:
        # 각 CCTV 위치에 해당하는 동영상 파일 경로 또는 URL
        video_file_paths = [
            os.path.abspath('video/normal8.mp4'),  # CCTV 동영상 파일 경로
            os.path.abspath('video/normal7.mp4'),
            os.path.abspath('video/normal6.mp4'),
            os.path.abspath('video/normal5.mp4'),
            os.path.abspath('video/normal4.mp4'),
            os.path.abspath('video/normal3.mp4')
        ]
        
        cctv_titles = [
            '체크인 카운터 A',
            '체크인 카운터 B',
            '1번 자동출국심사대',
            '2번 자동출국심사대',
            '3번 자동출국심사대',
            '4번 자동출국심사대'
        ]
            
        # 3행 3열 그리드 생성 및 각 그리드에 동영상 삽입
        for i in range(2):  # 3행
            cols = st.columns(3)  # 각 행에 3열
            for j, col in enumerate(cols, start=1):
                with col:
                    # 현재 행과 열에 따라 CCTV 번호 계산
                    cctv_number = i * 3 + j
                    st.subheader(cctv_titles[cctv_number - 1])
                    # 각 CCTV 번호에 해당하는 동영상 재생
                    st.video(video_file_paths[cctv_number - 1],start_time=0)
    
    with tab4:
        # 각 CCTV 위치에 해당하는 동영상 파일 경로 또는 URL
        video_file_paths = [
            os.path.abspath('video/normal7.mp4'),  # CCTV 동영상 파일 경로
            os.path.abspath('video/normal8.mp4'),
            os.path.abspath('video/normal9.mp4'),
            os.path.abspath('video/normal10.mp4'),
            os.path.abspath('video/normal1.mp4'),
            os.path.abspath('video/normal2.mp4')
        ]
        
        cctv_titles = [
            '면세점 A구역',
            '면세점 B구역',
            '탑승구역 1~8번',
            '탑승구역 16~21번',
            '탑승구역 34~39번',
            '탑승구역 47~50번'
        ]
            
        # 3행 3열 그리드 생성 및 각 그리드에 동영상 삽입
        for i in range(2):  # 3행
            cols = st.columns(3)  # 각 행에 3열
            for j, col in enumerate(cols, start=1):
                with col:
                    # 현재 행과 열에 따라 CCTV 번호 계산
                    cctv_number = i * 3 + j
                    st.subheader(cctv_titles[cctv_number - 1])
                    # 각 CCTV 번호에 해당하는 동영상 재생
                    st.video(video_file_paths[cctv_number - 1],start_time=0)
        

# 이상행동 EVENT 확인
if selected == emoji.emojize("이상행동 발생 구역 모니터링"):
    # Markdown을 사용한 스타일링 타이틀
    st.markdown("""
        <style>
        .big-font {
            font-size:36px !important;
            font-weight: bold;
            color: #1B365C;
            margin-top: -70px;  # 텍스트 위의 여백 줄임
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<p class="big-font" style="color:white;">이상행동 발생 구역 모니터링</p>', unsafe_allow_html=True)
        
    cols = st.columns((5,5))  # 페이지를 세로로 5:5 비율로 분할

    with cols[0]:  # 좌측 페이지
        st.error('이상행동 "실신" 감지되었습니다.')
        st.info("'실신' 탐지 확률: 99.3%")
        st.success("사건 관련 인원: 1명")
    
        # CCTV 영상 출력
        st.video("video/falldown_detection.mp4", start_time=0)

    with cols[1]:  # 우측 페이지
        st.markdown("""
    <center style='margin-top: 0px; margin-bottom: 0px;'>
        <img src='https://github.com/jayjinnie/KT-AIVLE-SCHOOL-DX-4th/blob/af25d8d95ff514f4303fbca8611fe64b977a2172/21_BigProject/image/1-2%EC%B8%B5%20%EC%A7%80%EB%8F%84.jpg?raw=true' width=500>
    </center>
    """, unsafe_allow_html=True)
        
        st.markdown("""
    <center style='margin-top: 0px; margin-bottom: 20px;'>
        <img src='https://github.com/jayjinnie/KT-AIVLE-SCHOOL-DX-4th/blob/af25d8d95ff514f4303fbca8611fe64b977a2172/21_BigProject/image/3-4%EC%B8%B5%20%EC%A7%80%EB%8F%84.jpg?raw=true' width=500>
    </center>
    """, unsafe_allow_html=True)

# 혼잡도 확인
if selected == emoji.emojize("구역별 혼잡도"):
    # 승객 혼잡도 API 로드        
    context=ssl.create_default_context()
    context.set_ciphers('DEFAULT')
    key = 'udvJG%2FCmvBCOdsMRK4RToVX2Xn90wTACwv6QfY2dYMzu1i5X2aTm9x2LbntK0RVaL2cfQ9GigHr1goleScrEUQ%3D%3D'
    url = 'http://apis.data.go.kr/B551177/PassengerNoticeKR/getfPassengerNoticeIKR?serviceKey='+key+'&selectdate=0&type=json'
    response = requests.get(url)
    result = response.content.decode("utf-8")
    json = jsons.loads(result)['response']['body']['items']
    data = pd.DataFrame(json)
    data.columns = ['일자', '시간대', 'T1 입국장 동편(A,B)', 'T1 입국장 서편(E,F)', 'T1 입국심사(C)', 'T1 입국심사(D)', 'T1 입국장 합계', 
                    'T1 출국장1,2', 'T1 출국장3', 'T1 출국장4', 'T1 출국장5,6', 'T1 출국장 합계', 
                    'T2 입국장 1', 'T2 입국장 2', 'T2 입국장 합계',
                    'T2 출국장 1', 'T2 출국장 2', 'T2 출국장 합계']
    
    # '합계'를 가지고 있는 행을 제거
    data = data[data['일자'] != '합계']
    
    # 데이터 형 변환
    data['일자'] = pd.to_datetime(data['일자'], format='%Y%m%d')

    # 나머지 컬럼들을 float으로 변환
    float_columns = ['T1 입국장 동편(A,B)', 'T1 입국장 서편(E,F)', 'T1 입국심사(C)', 'T1 입국심사(D)', 'T1 입국장 합계',
                     'T1 출국장1,2', 'T1 출국장3', 'T1 출국장4', 'T1 출국장5,6', 'T1 출국장 합계', 'T2 입국장 1', 'T2 입국장 2',
                     'T2 입국장 합계', 'T2 출국장 1', 'T2 출국장 2', 'T2 출국장 합계']
    data[float_columns] = data[float_columns].astype(float)

    st.markdown("""
        <style>
        .big-font {
            font-size:36px !important;
            font-weight: bold;
            color: #1B365C;
            margin-top: -70px;  # 텍스트 위의 여백 줄임
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<p class="big-font" style="color:white;">시간대별 공항 내 승객 혼잡도 현황</p>', unsafe_allow_html=True)

    # 필터 버튼 생성
    selected_column = st.selectbox("구역 선택", ['T1 입국장 합계', 'T1 출국장 합계', 'T2 입국장 합계', 'T2 출국장 합계'])

    # 데이터프레임으로부터 시간대별 합계 데이터 추출
    sumset_data = data.groupby('시간대').mean()[['T1 입국장 합계', 'T1 출국장 합계', 'T2 입국장 합계', 'T2 출국장 합계']].reset_index()

    # 시각화
    fig = px.bar(sumset_data, x='시간대', y=selected_column,
                 labels={'value': '승객 총합'},
                 title='시간대별 공항 내 승객 혼잡도 현황')
    # 결과 출력
    st.plotly_chart(fig)
    
    # 필터 버튼 생성 (T1, T2 선택)
    selected_terminal = st.selectbox("터미널을 선택하세요", ['T1 입국장', 'T1 출국장', 'T2 입국장', 'T2 출국장'])

    # 선택된 터미널에 따라 데이터 필터링
    filtered_data = data.filter(like=selected_terminal)
    
    # '시간대' 컬럼 추가
    if '시간대' in data.columns:
        time_column = data.pop('시간대')  # '시간대' 컬럼을 추출하고 원본 데이터프레임에서 제거
        filtered_data.insert(0, '시간대', time_column)  # '시간대' 컬럼을 맨 앞에 삽입
        
    # 테이블 차트 생성 및 시각화
    fig = ff.create_table(filtered_data) # colorscale 설정

    # 결과 출력
    st.plotly_chart(fig)