import streamlit as st
import time
import google.generativeai as genai

st.title("OMDENA-MindGuardian")

API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input("Say something"):
    with st.chat_message("human"):
        st.markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})

    def response_generator(question):
        prompt = '''
        You are a seasoned mental health professional specializing in Gen Z.
        Provide empathetic, evidence-based guidance on anxiety, depression,
        social media impact, academic stress, and identity exploration.
        Offer coping strategies, resources, and encourage help-seeking behavior.
        A gen Z kid is going to ask you a question, answer that in no more than
        three paragraphs.
        Question: 
        ''' + question
        response = model.generate_content(prompt)

        for word in response.text.split():
            yield word + " "
            time.sleep(0.10)

    with st.chat_message("ai"):
        response = st.write_stream(response_generator(question))
    st.session_state.messages.append({"role": "ai", "content": response})