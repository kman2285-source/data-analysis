import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="대학원 기말고사 마스터 시스템", page_icon="🎓", layout="wide")

# 스타일 지정
st.markdown("""
    <style>
    .question-box { background-color: #ffffff; padding: 25px; border-radius: 15px; border-left: 8px solid #4a90e2; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .tech-box { border-left: 8px solid #28a745 !important; }
    .concept-box { background-color: #f0f7f4; padding: 20px; border-radius: 10px; border-left: 5px solid #28a745; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# 1. 데이터셋 정의 (코드 상단에 배치하여 NameError 방지)
# ---------------------------------------------------------------------

# [고급데이터세미나 65문항 데이터]
questions_ba = [{"id": i, "chapter": "고급데이터세미나", "question": f"실전 대비 문항 {i}입니다.", 
                 "options": ["A", "B", "C", "D"], "answer": "A", "explanation": "해설준비중", "concept": "개념"} for i in range(1, 66)]

# [기술가치평가 30문항 데이터]
questions_tech = [
    {"id": 1, "chapter": "06강", "question": "비용접근법에서 과거 지출 비용에 현가계수를 곱하는 이유는 미래 가치를 반영하기 위해서이다. (O/X)", "options": ["O", "X"], "answer": "X", "explanation": "현재가치로 환산하기 위함입니다.", "concept": "현가계수 목적"},
    {"id": 2, "chapter": "06강", "question": "비용조정계수는 평점합이 음수일 경우 1보다 작아져 평가금액이 감액된다. (O/X)", "options": ["O", "X"], "answer": "O", "explanation": "음수이면 1 미만이 되어 감액됩니다.", "concept": "비용조정계수"},
    {"id": 3, "chapter": "07강", "question": "시장접근법은 거래사례가 존재해야만 적용 가능하다. (O/X)", "options": ["O", "X"], "answer": "O", "explanation": "거래사례 조사가 필수입니다.", "concept": "시장접근법"},
    {"id": 4, "chapter": "07강", "question": "시점 수정 시 사용하는 지표는 생산자물가지수이다. (O/X)", "options": ["O", "X"], "answer": "O", "explanation": "사례 보정에 생산자물가지수를 활용합니다.", "concept": "시점 수정"},
    {"id": 5, "chapter": "08강", "question": "매출액 추정 시 의뢰인의 희망 금액에 맞춰 역산하는 것이 원칙이다. (O/X)", "options": ["O", "X"], "answer": "X", "explanation": "객관성이 훼손되므로 금지됩니다.", "concept": "평가자 윤리"},
    {"id": 6, "chapter": "09강", "question": "데이터의 가격은 사용가치를 의미한다. (O/X)", "options": ["O", "X"], "answer": "X", "explanation": "가격은 교환가치, 가치는 사용가치입니다.", "concept": "가치와 가격"},
    {"id": 7, "chapter": "09강", "question": "데이터요소법에서 비중 100%는 전체 데이터 사용을 의미한다. (O/X)", "options": ["O", "X"], "answer": "O", "explanation": "전체 데이터 활용 시 비중은 100%입니다.", "concept": "데이터 비중"},
    {"id": 8, "chapter": "06강", "question": "기대이자율 결정 시 법인세율을 제외한다. (O/X)", "options": ["O", "X"], "answer": "X", "explanation": "법인세율과 가산이자율을 포함합니다.", "concept": "기대이자율"},
    {"id": 9, "chapter": "09강", "question": "데이터 가치평가 결과는 가액 형태로 도출된다. (O/X)", "options": ["O", "X"], "answer": "O", "explanation": "최종 가액 형태로 결과가 나옵니다.", "concept": "평가 결과물"},
    {"id": 10, "chapter": "07강", "question": "시장접근법은 미래 수익을 추정하여 할인하는 방법이다. (O/X)", "options": ["O", "X"], "answer": "X", "explanation": "수익추정은 수익접근법입니다.", "concept": "가치평가 방식"},
    {"id": 11, "chapter": "06강", "question": "비용접근법 산식에서 VE의 의미는? (기술가치평가[  ])", "options": ["금액", "자산", "비용", "수익"], "answer": "금액", "explanation": "VE는 기술가치평가금액입니다.", "concept": "VE 정의"},
    {"id": 12, "chapter": "07강", "question": "조정계수 산식 분모의 숫자는? (1+평점합/?)", "options": ["20", "30", "40", "50"], "answer": "40", "explanation": "공식의 분모는 40입니다.", "concept": "조정계수"},
    {"id": 13, "chapter": "08강", "question": "매출액 추정 전 과정에서 일맥상통해야 할 원칙은 [  ]적 일관성이다.", "options": ["수치", "논리", "시장", "환경"], "answer": "논리", "explanation": "논리적 일관성이 핵심입니다.", "concept": "추정 원칙"},
    {"id": 14, "chapter": "09강", "question": "데이터 가치평가에서 합의된 가격은 [  ]가치이다.", "options": ["교환", "사용", "미래", "현재"], "answer": "교환", "explanation": "가격은 교환가치입니다.", "concept": "가치 vs 가격"},
    {"id": 15, "chapter": "06강", "question": "비용접근법 공식 내 n은 무엇을 뜻하는가?", "options": ["개수", "횟수", "기간", "시기"], "answer": "기간", "explanation": "n은 비용발생기간입니다.", "concept": "공식 변수"},
    {"id": 16, "chapter": "07강", "question": "시장접근법은 기술거래시장이 [  ]해야 적용 가능하다.", "options": ["존재", "없어야", "폐쇄", "공개"], "answer": "존재", "explanation": "거래시장이 존재해야 합니다.", "concept": "전제 조건"},
    {"id": 17, "chapter": "08강", "question": "무형자산은 유형자산과 달리 [  ]가 없다.", "options": ["가치", "형체", "기능", "용도"], "answer": "형체", "explanation": "무형자산은 형체가 없는 재산권입니다.", "concept": "무형자산 특성"},
    {"id": 18, "chapter": "09강", "question": "데이터 가치 산정 시 작성하는 표는 데이터 [  ]표이다.", "options": ["구성", "통계", "가격", "판매"], "answer": "구성", "explanation": "데이터 구성표를 작성합니다.", "concept": "데이터요소법"},
    {"id": 19, "chapter": "06강", "question": "부실 보고 시 평가자가 처벌받는 법은 [  ]이다.", "options": ["상법", "민법", "형법", "특허법"], "answer": "상법", "explanation": "상법 벌칙 규정에 의거합니다.", "concept": "벌칙 규정"},
    {"id": 20, "chapter": "07강", "question": "시장접근법은 수요와 [  ]의 법칙을 바탕으로 한다.", "options": ["공급", "비용", "수익", "투자"], "answer": "공급", "explanation": "수요와 공급의 법칙입니다.", "concept": "시장 법칙"},
    {"id": 21, "chapter": "08강", "question": "성장률이 높지만 성장성 지표 점수가 [  ] 경우는 논리적 모순이다.", "options": ["낮은", "높은", "같은", "없는"], "answer": "낮은", "explanation": "성장률과 평점은 정비례해야 합니다.", "concept": "논리적 일관성"},
    {"id": 22, "chapter": "09강", "question": "데이터 가치는 [  ]에 따라 달라진다.", "options": ["목적", "용량", "장소", "색상"], "answer": "목적", "explanation": "평가 목적이나 소유자에 따라 달라집니다.", "concept": "가치 상대성"},
    {"id": 23, "chapter": "06강", "question": "기대이자율 구성요소는 사업화 [  ]이자율과 법인세율이다.", "options": ["가산", "기본", "누적", "할인"], "answer": "가산", "explanation": "사업화 가산이자율을 포함합니다.", "concept": "기대이자율"},
    {"id": 24, "chapter": "07강", "question": "거래사례 정보는 [  ]되어 있는 경우가 많다.", "options": ["비공개", "공개", "무료", "공식"], "answer": "비공개", "explanation": "비공개되는 경우가 많아 사례 확보가 어렵습니다.", "concept": "제약 사항"},
    {"id": 25, "chapter": "08강", "question": "매출액 추정은 기술가치평가에서 [  ] 중요한 단계이다.", "options": ["가장", "별로", "거의", "전혀"], "answer": "가장", "explanation": "전 과정 중 가장 중요한 단계입니다.", "concept": "추정 중요성"},
    {"id": 26, "chapter": "09강", "question": "데이터 가치평가 시 최종 [  ]이 도출된다.", "options": ["가액", "용량", "빈도", "수치"], "answer": "가액", "explanation": "가액 형태로 결과가 나옵니다.", "concept": "평가 결과물"},
    {"id": 27, "chapter": "06강", "question": "시점 보정 시 생산자 [  ] 지수를 활용한다.", "options": ["물가", "소비자", "금리", "환율"], "answer": "물가", "explanation": "생산자물가지수를 활용합니다.", "concept": "시점 보정"},
    {"id": 28, "chapter": "07강", "question": "기술 및 시장 [  ]을 반영하여 거래금액을 조정한다.", "options": ["특성", "비용", "매출", "위치"], "answer": "특성", "explanation": "기술 및 시장 특성을 반영합니다.", "concept": "특성 반영"},
    {"id": 29, "chapter": "08강", "question": "매출 추정 모형 중 하나는 [  ] 확산모형이다.", "options": ["BASS", "선형", "곡선", "기반"], "answer": "BASS", "explanation": "BASS 확산모형 등이 있습니다.", "concept": "확산모형"},
    {"id": 30, "chapter": "09강", "question": "데이터 요소법은 [  ]를 결정하기 위함이다.", "options": ["비중", "용량", "시간", "수량"], "answer": "비중", "explanation": "데이터 비중을 결정합니다.", "concept": "요소법"}
]

# ---------------------------------------------------------------------
# 3. 사이드바 및 메인 화면 로직
# ---------------------------------------------------------------------
st.sidebar.title("📚 과목 선택")
subject = st.sidebar.radio("학습할 과목:", ("고급데이터세미나", "기술가치평가"))

# 데이터 연결
data = questions_ba if subject == "고급데이터세미나" else questions_tech
total_q = len(data)

# 과목 변경 시 리셋
if 'current_sub' not in st.session_state or st.session_state.current_sub != subject:
    st.session_state.q_idx = 0
    st.session_state.current_sub = subject
    st.session_state.show_ans = False

# 문제 번호 슬라이더
selected_id = st.sidebar.slider("문제 번호 선택", 1, total_q, value=st.session_state.q_idx + 1)
st.session_state.q_idx = selected_id - 1

st.title(f"📝 {subject} 기말고사 문제은행")
st.progress((st.session_state.q_idx + 1) / total_q)

# 현재 문제 렌더링
q = data[st.session_state.q_idx]
theme = "tech-box" if subject == "기술가치평가" else ""

st.markdown(f"""
    <div class="question-box {theme}">
        <span style="color: #4a90e2; font-weight: bold;">[Q {q['id']}] {q['chapter']}</span>
        <p style='font-size:20px; font-weight: 500;'>{q['question']}</p>
    </div>
""", unsafe_allow_html=True)

user_choice = st.radio("정답 선택:", q['options'], key=f"ans_{subject}_{q['id']}")

if st.button("💡 정답 확인"):
    st.session_state.show_ans = True

if st.session_state.show_ans:
    if user_choice == q['answer']:
        st.success(f"🎯 정답입니다! (선택: {user_choice})")
    else:
        st.error(f"🧐 틀렸습니다. 정답은 {q['answer']} 입니다.")
    st.write(f"해설: {q['explanation']}")
    st.markdown(f'<div class="concept-box">💡 핵심 개념: {q["concept"]}</div>', unsafe_allow_html=True)

# 하단 빠른 이동
st.divider()
st.subheader("📍 빠른 이동")
cols = st.columns(10)
for i in range(total_q):
    with cols[i % 10]:
        if st.button(str(i+1), key=f"quick_{subject}_{i}"):
            st.session_state.q_idx = i
            st.session_state.show_ans = False
            st.rerun()
