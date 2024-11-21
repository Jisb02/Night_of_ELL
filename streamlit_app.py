import streamlit as st

# 비밀번호와 연결된 힌트별 이미지 경로 설정
passwords = {
    "hint1": {"password": 1202, "image": "hint/hint001.JPG"},
    "hint2": {"password": 2444, "image": "hint/hint002.JPG"},
    "hint3": {"password": 9160, "image": "hint/hint003.JPG"},
    "hint4": {"password": 509, "image": "hint/hint004.JPG"},  # 숫자형이므로 앞의 0 제거
}

# 상태 관리: 현재 선택된 버튼 저장
if "selected_hint" not in st.session_state:
    st.session_state["selected_hint"] = None  # 초기값은 None


def reset_to_home():
    """홈 화면으로 돌아가는 함수"""
    st.session_state["selected_hint"] = None


# 홈 화면 처리
if st.session_state["selected_hint"] is None:
    st.title("힌트 비밀번호 시스템")
    st.write("힌트 버튼을 눌러 비밀번호를 입력하고 이미지를 확인하세요.")

    # 힌트 버튼 표시
    for hint, data in passwords.items():
        # 버튼 클릭 시 상태 변경
        if st.button(f"힌트 {hint[-1]}", key=hint):
            st.session_state["selected_hint"] = hint
else:
    # 선택된 힌트 화면
    selected_hint = st.session_state["selected_hint"]
    data = passwords[selected_hint]

    st.title(f"{selected_hint} 비밀번호 입력")
    password_input = st.number_input(
        f"{selected_hint}의 비밀번호를 입력하세요:", min_value=0, step=1, format="%d", key=f"password_input_{selected_hint}"
    )

    # 비밀번호 확인
    if password_input == data["password"]:
        st.success(f"{selected_hint}의 비밀번호가 맞았습니다!")
        st.image(data["image"], caption=f"{selected_hint} 이미지", use_container_width=True)
    elif password_input != 0:  # 숫자가 입력되었으나 틀렸을 경우
        st.error("비밀번호가 틀렸습니다.")

    # 홈으로 가기 버튼
    if st.button("홈으로 가기", key="home_button"):
        reset_to_home()
