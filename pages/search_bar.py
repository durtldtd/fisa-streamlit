import streamlit as st
import pandas as pd
import numpy as np
import datetime

#test를 입력하는 검색창을 하나 만듭니다.
#ani_list에 있는 글자가 일부라도들어가면
#img_list에 있는 해당 그림이 출력되는 검색창을 하나 만들어 주세요
st.write("무슨 주식을 사야 부자가 되려나..")
# 사이드바 입력
st.sidebar.markdown("### 회사 이름과 기간을 입력하세요")
company = st.sidebar.text_input("회사 이름", value="삼성전자")
date_range = st.sidebar.date_input(
    "시작일 - 종료일",
    value=(datetime.date(2019, 1, 1), datetime.date(2021, 12, 31)),
)
fetch_button = st.sidebar.button("주가 데이터 확인")
