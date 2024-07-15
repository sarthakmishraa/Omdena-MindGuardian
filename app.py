import streamlit as st
import random
import time

st.title("OMDENA-MindGuardian")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something"):
    with st.chat_message("human"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

def response_generator():
    response = random.choice(
        [
            "I am not really a chatbot right now, I am in my building phase. \
                This is just a test app.",

            "Think of me as under construction! I'm still learning and \
                developing new abilities, so I might not be a fully functional \
                    chatbot just yet. This is a trial version to gather feedback and \
                        help me grow into something truly helpful.",

            "While I can't claim to be a complete chatbot at this stage, \
                I'm in the exciting early stages of development. This app is a \
                    stepping stone, allowing us to test my potential and see what \
                        amazing things I can learn to do.",

            "Imagine me as a chef perfecting a new recipe! This app is like a trial run, \
                giving us a chance to see how I respond to your questions and interactions. \
                    It's all part of the process of becoming a truly valuable language model.",

            "Right now, I'm like a complex machine being calibrated. \
                This test app helps us identify areas where I can improve \
                    and refine my responses. It's all leading to a more powerful and intelligent future.",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.10)

with st.chat_message("ai"):
    response = st.write_stream(response_generator())
st.session_state.messages.append({"role": "ai", "content": response})