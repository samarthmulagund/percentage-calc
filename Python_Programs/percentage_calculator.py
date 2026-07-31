import streamlit as st
import base64
import os
def get_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()
st.set_page_config(
    page_title="Percentage Calc",
    page_icon="📊"
)

img = get_base64("Python_Programs/images/calc-backdrop.jpeg")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
language = st.selectbox("Choose preferred language",
                        ["English", "ಕನ್ನಡ", "हिंदी"])
if language == "English":
    st.title("Percentage Calc")
    marks_obtained = st.number_input("Give your marks obtained.(If you want to calculate marks obtained visit my website Quick Calc)", step= 1)
    total_marks = st.number_input("Give your total marks obtained.(If you want to calculate total marks visit my website Quick Calc)", step= 1)
    if st.button("% Calculate Percentage") :
        st.write(f"You Percentage is {marks_obtained / total_marks * 100}")

elif language == "ಕನ್ನಡ":
    st.title("ಶೇಕಡಾವಾರು ಕ್ಯಾಲ್ಕುಲೇಟರ್")
    marks_obtained = st.number_input("ನೀವು ಪಡೆದ ಅಂಕಗಳನ್ನು ನೀಡಿ.(ನೀವು ಪಡೆದ ಅಂಕಗಳನ್ನು ಲೆಕ್ಕ ಹಾಕಲು ಬಯಸಿದರೆ ನನ್ನ ವೆಬ್‌ಸೈಟ್ ಕ್ವಿಕ್ ಕ್ಯಾಲ್ಕ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.)", step=1)
    total_marks = st.number_input("ನೀವು ಪಡೆದ ಒಟ್ಟು ಅಂಕಗಳನ್ನು ನೀಡಿ.(ನೀವು ಒಟ್ಟು ಅಂಕಗಳನ್ನು ಲೆಕ್ಕ ಹಾಕಲು ಬಯಸಿದರೆ ನನ್ನ ವೆಬ್‌ಸೈಟ್ ಕ್ವಿಕ್ ಕ್ಯಾಲ್ಕ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.)", step=1)
    if st.button("% ಲೆಕ್ಕಾಚಾರ ಮಾಡಿ"):
        st.write(f"ನಿಮ್ಮ ಶೇಕಡಾವಾರು {marks_obtained / total_marks * 100}")

elif language == "हिंदी":
    st.title("प्रतिशत कैलकुलेटर")
    marks_obtained = st.number_input("अपने प्राप्त अंक बताएं.(अगर आप अपने प्राप्त अंकों की गणना करना चाहते हैं, तो मेरी वेबसाइट 'Quick Calc' पर जाएँ।)", step=1)
    total_marks = st.number_input("अपने कुल प्राप्त अंक बताएं.(अगर आप कुल अंक कैलकुलेट करना चाहते हैं, तो मेरी वेबसाइट 'Quick Calc' पर जाएँ।)", step=1)
    if st.button("% गणना"):
        st.write(f"आपका प्रतिशत है {marks_obtained / total_marks * 100}")