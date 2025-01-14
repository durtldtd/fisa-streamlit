import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from io import BytesIO
#test를 입력하는 검색창을 하나 만듭니다.
#ani_list에 있는 글자가 일부라도들어가면
#img_list에 있는 해당 그림이 출력되는 검색창을 하나 만들어 주세요

#첫화면
st.write("무슨 주식을 사야 부자가 되려나..")


# 사이드바 입력
st.sidebar.markdown("### 회사 이름과 기간을 입력하세요")
company = st.sidebar.text_input("회사 이름", value="삼성전자")
date_range = st.sidebar.date_input(
    "시작일 - 종료일",
    value=(datetime.date(2019, 1, 1), datetime.date(2024, 1, 15)),
)
fetch_button = st.sidebar.button("주가 데이터 확인")


if fetch_button:
    #임시 데이터
    dates = pd.date_range(start=date_range[0], end=date_range[1], freq="B")
    data = {
        "Date": dates,
        "Open": np.random.randint(30000, 40000, len(dates)),
        "High": np.random.randint(40000, 50000, len(dates)),
        "Low": np.random.randint(20000, 30000, len(dates)),
        "Close": np.random.randint(30000, 40000, len(dates)),
        "Volume": np.random.randint(1000000, 10000000, len(dates)),
        "Change": np.random.uniform(-0.05, 0.05, len(dates)),
    }
    df = pd.DataFrame(data)
    df["Change"] = df["Change"].round(4)


    # 결과 출력
    st.markdown(f"### [{company}] 주가 데이터")
    st.dataframe(df)


    # 그래프 그리기
    st.markdown(f"#### [{company}] 종가(Close) 차트")
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Close"])
    ax.set_xlabel("날짜")
    ax.set_ylabel("종가")
    ax.set_title(f"{company} 종가 추세")
    st.pyplot(fig)


    # 다운로드 버튼
    st.download_button(
        label="CSV 파일 다운로드",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=f"{company}_stock_data.csv",
        mime="text/csv",
    )
    
    def to_excel(df):
        # 엑셀 파일로 변환
        output = BytesIO()# 바이너리 데이터로 다루기
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Stock Data")
        return output.getvalue()

    excel_data = to_excel(df)
    
    st.download_button(
        label="엑셀 파일 다운로드",
        data=excel_data,    
        file_name=f"{company}_stock_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )