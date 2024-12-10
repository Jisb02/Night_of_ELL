import streamlit as st

# 비밀번호와 연결된 힌트별 이미지 경로 설정
passwords = {
    "hint1": {"password": 1202, "image": "hint/hint001.JPG"},
    "hint2": {"password": 2444, "image": "hint/hint002.jpg"},
    "hint3": {"password": 3179, "image": "hint/hint003.jpg"},
    "hint4": {"password": 4609, "image": "hint/hint004.jpg"},  # 힌트 4 추가
}

# 초기 언어 설정
if "language" not in st.session_state:
    st.session_state["language"] = "KOR"  # 기본값: 한국어
if "selected_hint" not in st.session_state:
    st.session_state["selected_hint"] = None  # 초기값은 None

# 언어 전환 버튼
col1, col2 = st.columns([8, 1])  # 오른쪽 상단에 배치
with col2:
    if st.session_state["language"] == "KOR":
        if st.button("ENG", key="lang_eng"):
            st.session_state["language"] = "ENG"
            st.session_state["selected_hint"] = None  # 언어 전환 시 홈 화면으로 리셋
    elif st.session_state["language"] == "ENG":
        if st.button("KOR", key="lang_kor"):
            st.session_state["language"] = "KOR"
            st.session_state["selected_hint"] = None  # 언어 전환 시 홈 화면으로 리셋

# 텍스트 번역 (언어에 따라 다르게 설정)
text = {
    "KOR": {
        "title": "힌트 사이트",
        "description": "힌트 버튼을 더블 클릭하여 비밀번호를 입력 후 엔터. 힌트 이미지를 확인하세요.",
        "password_prompt": "{}의 비밀번호를 입력하세요:",
        "success": "{}의 비밀번호가 맞았습니다!",
        "error": "비밀번호가 틀렸습니다.",
        "home_button": "홈으로 가기",
        "cctv_button": "CCTV로 연결하기",
        "hints": ["힌트 1", "힌트 2", "힌트 3", "힌트 4"],  # 힌트 4 추가
    },
    "ENG": {
        "title": "Hints",
        "description": "Double-Click the hint button to enter the password and view the image.",
        "password_prompt": "Enter the password for {}:",
        "success": "The password for {} is correct!",
        "error": "The password is incorrect.",
        "home_button": "Go to Home",
        "cctv_button": "Go to CCTV",
        "hints": ["Hint 1", "Hint 2", "Hint 3", "Hint 4"],  # 힌트 4 추가
    },
}

# 선택된 언어에 따라 텍스트 로드
lang = st.session_state["language"]
current_text = text[lang]

def reset_to_home():
    st.session_state["selected_hint"] = None

# 홈 화면 처리
if st.session_state["selected_hint"] is None:
    # 홈 화면
    st.title(current_text["title"])
    st.write(current_text["description"])

    # 힌트 버튼 표시
    for i, (hint, data) in enumerate(passwords.items()):
        # 버튼 클릭 시 상태 변경 (고유 키 추가)
        if st.button(current_text["hints"][i], key=f"hint_button_{i}"):
            st.session_state["selected_hint"] = hint  # 선택된 힌트 상태 변경

    # CCTV로 연결하기 버튼 추가
    if st.button(current_text["cctv_button"], key="cctv_button"):
        st.markdown(
            '<a href="https://24ellcctv.streamlit.app/" target="_blank" style="text-decoration:none;"><button style="background-color:#007BFF; color:white; border:none; padding:10px 15px; font-size:16px; cursor:pointer;">🔗 CCTV로 연결하기</button></a>',
            unsafe_allow_html=True,
        )
else:
    # 선택된 힌트 화면
    selected_hint = st.session_state["selected_hint"]
    data = passwords[selected_hint]

    st.title(f"{selected_hint} {current_text['title']}")
    password_input = st.number_input(
        current_text["password_prompt"].format(selected_hint),
        min_value=0,
        step=1,
        format="%d",
        key=f"password_input_{selected_hint}",
    )

    # 비밀번호 확인
    if password_input == data["password"]:
        st.success(current_text["success"].format(selected_hint))
        st.image(data["image"], caption=f"{selected_hint} 이미지", use_container_width=True)
    elif password_input != 0:  # 숫자가 입력되었으나 틀렸을 경우
        st.error(current_text["error"])

    # 홈으로 가기 버튼
    if st.button(current_text["home_button"], key="home_button"):
        reset_to_home()