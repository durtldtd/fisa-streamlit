import streamlit as st

#test를 입력하는 검색창을 하나 만듭니다.
#ani_list에 있는 글자가 일부라도들어가면
#img_list에 있는 해당 그림이 출력되는 검색창을 하나 만들어 주세요

st.text("회사 이름과 기간을 입력하세요")
ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

search=st.text_input("검색어를 입력하세요")


for ani in ani_list:
    if search in ani:
        img_idx=ani_list.index(ani)
if search !='':# 초기상태를 이미지없이 실행하도록
    st.image(img_list(img_idx))
st.date_input("시작일-종료일")
st.button("주가 데이터 확인")

