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

# CSS 스타일 정의
st.markdown("""
    <style>
    .button-3d {
        background-color: #ffffff; /* 버튼 배경색: 흰색 */
        border: 2px solid #000000; /* 테두리 검정색 */
        color: #000000; /* 글씨 검정색 */
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        box-shadow: 0 6px #999;
        border-radius: 8px;
        transition: all 0.3s ease;
    }

    .button-3d:hover {
        background-color: #f0f0f0; /* 호버 시 배경색 약간 회색 */
        box-shadow: 0 12px #666;
    }

    .button-3d:active {
        background-color: #e0e0e0; /* 클릭 시 배경 더 진한 회색 */
        box-shadow: 0 4px #666;
        transform: translateY(4px);
    }

    .center {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 텍스트 번역 (언어에 따라 다르게 설정)
text = {
    "KOR": {
        "title": "힌트 사이트",
        "description": "아래 힌트 버튼을 클릭하세요.",
        "password_prompt": "{}의 비밀번호를 입력하세요:",
        "success": "{}의 비밀번호가 맞았습니다! 이미지를 확인하세요.",
        "error": "비밀번호가 틀렸습니다.",
        "home_button": "홈으로 가기",
        "cctv_button": "CCTV로 연결하기",
        "hints": ["힌트 1", "힌트 2", "힌트 3", "힌트 4"],  # 힌트 4 추가
    },
    "ENG": {
        "title": "Hints",
        "description": "Click the hint buttons below.",
        "password_prompt": "Enter the password for {}:",
        "success": "The password for {} is correct! Check the image.",
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
    st.markdown('<div class="center">', unsafe_allow_html=True)  # 버튼 중앙 정렬
    for i, (hint, data) in enumerate(passwords.items()):
        button_html = f"""
        <form action="" method="get">
            <button type="submit" name="hint" value="{hint}" class="button-3d">
                {current_text["hints"][i]}
            </button>
        </form>
        """
        st.markdown(button_html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # 버튼 동작
    selected_hint = st.experimental_get_query_params().get("hint", [None])[0]
    if selected_hint and selected_hint in passwords:
        st.session_state["selected_hint"] = selected_hint

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
    home_html = """
    <form action="" method="get">
        <button type="submit" name="home" class="button-3d">홈으로 가기</button>
    </form>
    """
    st.markdown(home_html, unsafe_allow_html=True)
    if st.experimental_get_query_params().get("home"):
        reset_to_home()
