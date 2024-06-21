import google.generativeai as genai 
import streamlit as st
genai.configure(api_key="AIzaSyDZpZbLl9D4so-_RH-vIQ4dgea9GCYJLbc")
model = genai.GenerativeModel('gemini-pro')
#5개 이상 구현 , 멀티턴 사용, 광명고등학교 주제, 마크다운 문법활용

st.set_page_config('GM_Info',page_icon='✨')
st.title('🔆 :blue[GM] Info')

agree= st.checkbox(':green[광명고등학교 학생]입니까?') #1

if agree : 
        pw = st.text_input( #2
        '교장선생님의 존함은?',
        type = 'password'
    )
        if pw != '' :
            if pw == '강석형':
                st.write("어서오세요! :blue[환영합니다]😉")
                
                grade =  st.selectbox ( #눌러서 해당하는 값 넣는 박스 (생년월일 적을 때 처럼) #3
                        "🌸 몇 학년인가요?",
                        ('1학년', '2학년','3학년'),
                        index=None 
                        )
                
                if grade == '3학년':
                            C1 = st.radio(  #4
                            "🍀몇 반인가요?",
                            ('1반','2반','3반','4반','5반','6반','7반','8반','9반','10반','11반'),
                            index=None 
                            )
                            if C1 == '2반':
                                st.image('수행정리표.jpeg') #5
                                st.write("📌 :green[6월 일정은 다음과 같습니다!] 화이팅! (^^ゞ ")
                            if C1 == '1반' or C1 == '3반' or C1 == '4반' or C1 == '5반' or C1 == '6반' or C1 == '7반' or C1 == '8반' or C1 == '9반' or C1 == '10반' or C1 == '11반':
                                  st.write('아직 제공하지 않는 서비스 단계입니다. 추후에 업데이트 될 예정입니다. 😥')
                                  
                                  
                
                if grade == '2학년'or grade == '1학년' : 
                    st.write('아직 제공하지 않는 서비스 단계입니다. 추후에 업데이트 될 예정입니다. 😥')
                else :
                      st. write(" ")
                if 'history' not in st.session_state:
                    st.session_state.history = []
                for i in st.session_state.history:
                    if type(i) == dict :
                        with st.chat_message('user'):
                            st.write(i['parts'])
                    else :
                        with st.chat_message('ai') :
                            st.write(i.parts[0].text)


                #채팅창 만들기
                tx = st.chat_input('📚 스터디 헬퍼! 공부 팁등을 알려드릴게요😎! ')

                #user창
                #with 실행종료가 되면 자원(메모리)
                if tx : 
                    with st.chat_message('user'):
                        st.write(tx)
                        st.session_state.history.append({
                            'role':'user',
                            'parts':tx

                        })


                    with st.chat_message('ai'):
                        with st.spinner('잠시만 기다려주세요...💭') :
                            response = model.generate_content(tx) #tx기준으로 답변 생성
                            st.session_state.history.append(response.candidates[0].content)
                            st.write(response.text)
                    
                

            else :
                st.write('옳지 않습니다. 다시 시도하세요.')
            
    
            