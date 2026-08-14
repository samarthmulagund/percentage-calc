import streamlit as st
import base64
import os
def get_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

def colored_text(text, color):
    st.markdown(
        f"<p style='color:{color};'>{text}</p>",
            unsafe_allow_html=True
        )
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

    def colored_text(text, color):
        st.markdown(
            f"<p style='color:{color};'>{text}</p>",
            unsafe_allow_html=True
        )


    colored_text("Percentage Calc", "#FFD700")
    colored_text(
        "Give your marks obtained.(If you want to calculate marks obtained visit my website Quick Calc)"
        "#FFD700"
    )
    marks_obtained = st.number_input(
        "",
        step=0.5,
        label_visibility = "collapsed"
    )
    colored_text(
        "Give your total marks .(If you want to calculate total marks visit my website Quick Calc)"
        "#FFD700"
    )
    total_marks = st.number_input(
        "",
        step=0.5,
        label_visibility = "collapsed"
    )
    if st.button("% Calculate Percentage") :
        if total_marks > 0:
            percentage = marks_obtained / total_marks * 100
            if percentage <= 100 :
                colored_text(f"You Percentage is {percentage}%", "#FFD700")
            else:
                colored_text("Invalid Input", "#FFD700")
        else:
            print("Total Marks should be more than 0")

elif language == "ಕನ್ನಡ":
    colored_text("ಶೇಕಡಾವಾರು ಕ್ಯಾಲ್ಕುಲೇಟರ್", "#FFD700")
    marks_obtained = st.selectbox(colored_text("ನೀವು ಪಡೆದ ಅಂಕಗಳನ್ನು ನೀಡಿ.(ನೀವು ಪಡೆದ ಅಂಕಗಳನ್ನು ಲೆಕ್ಕ ಹಾಕಲು ಬಯಸಿದರೆ ನನ್ನ ವೆಬ್‌ಸೈಟ್ ಕ್ವಿಕ್ ಕ್ಯಾಲ್ಕ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.)", "#FFD700", step=0.5))
    total_marks = st.selectbox(colored_text("ನಿಮ್ಮ ಒಟ್ಟು ಅಂಕಗಳನ್ನು ನೀಡಿ.(ನೀವು ಒಟ್ಟು ಅಂಕಗಳನ್ನು ಲೆಕ್ಕ ಹಾಕಲು ಬಯಸಿದರೆ ನನ್ನ ವೆಬ್‌ಸೈಟ್ ಕ್ವಿಕ್ ಕ್ಯಾಲ್ಕ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.)", "#FFD700", step=0.5))

    if st.button("% ಲೆಕ್ಕಾಚಾರ ಮಾಡಿ"):
        percentage = marks_obtained / total_marks * 100
        if percentage < 100 :
            colored_text(f"ನಿಮ್ಮ ಶೇಕಡಾವಾರು {percentage}%", "#FFD700")
        else:
            colored_text("ಅಮಾನ್ಯ ಇನ್‌ಪುಟ್","#FFD700")
elif language == "हिंदी":
    colored_text("प्रतिशत कैलकुलेटर", "#FFD700")
    marks_obtained = st.selectbox(colored_text("अपने प्राप्त अंक बताएं.(अगर आप अपने प्राप्त अंकों की गणना करना चाहते हैं, तो मेरी वेबसाइट 'Quick Calc' पर जाएँ।)","#FFD700", step=0.5))
    total_marks = st.selectbox(colored_text("अपने कुल अंक बताएं।.(अगर आप कुल अंक कैलकुलेट करना चाहते हैं, तो मेरी वेबसाइट 'Quick Calc' पर जाएँ।)","#FFD700", step=0.5))

    if st.button("% गणना"):
        percentage = marks_obtained / total_marks * 100
        if percentage < 100 :
            colored_text(f"आपका प्रतिशत है {percentage}%","#FFD700")
        else:
            colored_text("अमान्य निवेश","#FFD700")