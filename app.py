import streamlit as st

# 페이지 설정
st.set_page_config(page_title="BA 기말고사 90문항 마스터", page_icon="🎓", layout="wide")

# 스타일 설정
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .question-box { background-color: #ffffff; padding: 30px; border-radius: 15px; border-left: 8px solid #4a90e2; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .concept-box { background-color: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 5px solid #1976d2; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

# ----------------- 데이터베이스 (1~90번) -----------------
questions = [
    {
        "id": 1, "chapter": "6장 회귀분석", 
        "question": "교재 사례인 '칼리지 스코어카드'에서 Earnings = 25000 + 0.5*Cost + 3000*City 일 때, 도시 대학(City=1)의 평균비용이 20,000달러라면 예상 수입은?",
        "options": ["35,000", "38,000", "41,000", "30,000"], "answer": "38,000",
        "explanation": "25000 + (0.5 * 20000) + 3000 = 38000.", "concept": "더미변수와 수치변수의 결합 예측"
    },
    {
        "id": 2, "chapter": "6장 잔차 분석",
        "question": "잔차도(Residual Plot)에서 잔차가 '깔때기 모양(Cone Shape)'으로 퍼지는 현상이 발견되었다면 어떤 가정이 위반된 것인가?",
        "options": ["독립성", "정규성", "동분산성 (Homoskedasticity)", "선형성"], "answer": "동분산성 (Homoskedasticity)",
        "explanation": "잔차의 분산이 일정하지 않고 변하는 것을 이분산성(Heteroskedasticity)이라고 합니다.", "concept": "이분산성 진단"
    },
    {
        "id": 3, "chapter": "7장 대수 변환 모형",
        "question": "Log-Log 모형 ln(Y) = b0 + 0.75*ln(X) 에서 계수 0.75가 의미하는 바는?",
        "options": ["X가 1단위 증가할 때 Y가 0.75 단위 증가", "X가 1% 증가할 때 Y가 75% 증가", "X가 1% 증가할 때 Y가 0.75% 증가", "탄력성이 0이 아님"], "answer": "X가 1% 증가할 때 Y가 0.75% 증가",
        "explanation": "로그-로그 모형의 계수는 직접적으로 탄력성(Elasticity)을 나타냅니다.", "concept": "탄력성 해석"
    },
    {
        "id": 4, "chapter": "8장 성능 평가",
        "question": "실제 Positive인 사례들 중 모형이 Positive라고 정확히 찾아낸 비율을 뜻하는 지표는?",
        "options": ["정확도", "특이도", "민감도 (Sensitivity/Recall)", "정밀도"], "answer": "민감도 (Sensitivity/Recall)",
        "explanation": "TP / (TP + FN)으로 계산되는 재현율입니다.", "concept": "재현율과 민감도"
    },
    {
        "id": 5, "chapter": "8장 PCA",
        "question": "주성분 분석(PCA)에서 첫 번째 주성분(PC1)이 갖는 특징으로 옳은 것은?",
        "options": ["데이터의 변동성(분산)을 가장 적게 설명한다", "데이터의 변동성(분산)을 가장 많이 설명한다", "항상 종속변수와 상관관계가 1이다", "변수의 개수를 늘린다"], "answer": "데이터의 변동성(분산)을 가장 많이 설명한다",
        "explanation": "PC1은 전체 데이터 분산을 최대화하는 방향으로 설정됩니다.", "concept": "PC1의 정의"
    }
]

# 90번까지 문항 리스트를 채우는 자동화 (나머지 85문제 자동 생성)
if len(questions) < 90:
    for i in range(len(questions) + 1, 91):
        questions.append({
            "id": i, "chapter": f"기말고사 대비 실전 문제", 
            "question": f"교재 범위(6장~8장) 내 학습 확인을 위한 {i}번 문제입니다. 향후 이 부분의 텍스트를 수정하여 실제 문제를 입력하세요.",
            "options": ["보기 1", "보기 2", "보기 3", "보기 4"], "answer": "보기 1",
            "explanation": "여기에 문제에 대한 상세 해설을 입력할 수 있습니다.", "concept": "관련 핵심 개념"
        })

# ----------------- 사이드바 내비게이션 -----------------
st.sidebar.title("🎮 문제 내비게이터")
st.sidebar.markdown("원하는 문제 번호로 바로 이동하세요.")

# 스크롤 대용: 슬라이더
selected_id = st.sidebar.slider("문제 선택", 1, 90, st.session_state.get('q_idx', 0) + 1)
st.sidebar.divider()

# ----------------- 메인 로직 -----------------

# 세션 상태 관리
if 'q_idx' not in st.session_state or st.session_state.q_idx != selected_id - 1:
    st.session_state.q_idx = selected_id - 1
if 'show_ans' not in st.session_state:
    st.session_state.show_ans = False

# 현재 문제
q = questions[st.session_state.q_idx]

# 화면 렌더링
st.title(f"📝 기말고사 대비 문제은행 ({st.session_state.q_idx + 1}/90)")

with st.container():
    st.markdown(f"""<div class="question-box">
        <h3>[{q['chapter']}]</h3>
        <p style='font-size:22px;'>{q['question']}</p>
    </div>""", unsafe_allow_html=True)
    
    st.write("")
    user_choice = st.radio("정답 선택:", q['options'], key=f"q_{q['id']}")

st.divider()

# 버튼 레이아웃
col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("⬅️ 이전 문제"):
        if st.session_state.q_idx > 0:
            st.session_state.q_idx -= 1
            st.session_state.show_ans = False
            st.rerun()

with col2:
    if st.button("💡 정답 확인"):
        st.session_state.show_ans = True

with col3:
    if st.button("다음 문제 ➡️"):
        if st.session_state.q_idx < 89:
            st.session_state.q_idx += 1
            st.session_state.show_ans = False
            st.rerun()

# 정답 공개
if st.session_state.show_ans:
    if user_choice == q['answer']:
        st.success(f"🎯 정답입니다! : {q['answer']}")
    else:
        st.error(f"🧐 다시 생각해보세요! (정답: {q['answer']})")
    
    with st.expander("📖 상세 해설 및 핵심 개념 보기", expanded=True):
        st.write(q['explanation'])
        st.markdown(f"""<div class="concept-box">
            <strong>💡 핵심 개념:</strong><br>{q['concept']}
        </div>""", unsafe_allow_html=True)

# 하단 빠른 이동 숫자 버튼 (스크롤 보조)
st.divider()
st.subheader("📍 빠른 이동 (1~90번)")
cols = st.columns(10)
for i in range(90):
    with cols[i % 10]:
        if st.button(f"{i+1}", key=f"nav_{i}"):
            st.session_state.q_idx = i
            st.session_state.show_ans = False
            st.rerun()
