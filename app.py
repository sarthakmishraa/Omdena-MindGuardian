import streamlit as st
import time
from streamlit_option_menu import option_menu
import google.generativeai as genai

API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home", "Problem Statement", "Goals and Outcomes", "Collaborators"],
        icons = ["house", "file-earmark", "list-check", "person-circle"],
        menu_icon = "cast"
    )

if selected == "Problem Statement":
    st.title("Problem Statement - MindGuardian")

    st.header("A Chatbot Companion for Gen Z Well-Being")

    st.subheader("Background")
    st.write("The rise of digital technology has revolutionised the way people interact,\
             work, and entertain themselves. Among the most affected demographic groups \
             are Generation Z (Gen Z), typically defined as individuals born between the \
             mid-1990s and early 2010s. This generation has grown up surrounded by \
             digital devices, such as smartphones, tablets, and computers, which have \
             become integral to their daily lives. According to a report by Amin et al. \
             (2020), Bangladesh has experienced a rapid increase in internet penetration, \
             with a significant portion of the population accessing the internet via \
             smartphones. This widespread availability of digital devices has led to \
             extensive use among young people, including Gen Z. In recent years, the \
             pervasive use of digital devices among Generation Z (Gen Z) has raised \
             concerns globally. Bangladesh, like many other countries, has witnessed \
             a surge in digital device addiction (DDA) among its young population. \
             This addiction has multifaceted repercussions, ranging from diminished \
             academic performance to compromised mental well-being. Understanding the \
             scope and consequences of DDA among Gen Z in Bangladesh is crucial for \
             devising effective intervention strategies.")
    st.divider()
    st.subheader("Problem")
    st.write("The COVID-19 pandemic has heightened levels of social isolation and \
             reliance on digital technologies for communication and entertainment.")
    st.write("Generation Z individuals in Bangladesh face significant challenges \
             related to depression and overwhelming digital device use. \
             Traditional mental health interventions may be inaccessible or \
             stigmatised, exacerbating the problem. Mihelič et el. (2023) explores \
             various factors contributing to cyberloafing behaviour among Generation Z \
             (Gen Z) students and suggests several solutions to address this issue. \
             There is a pressing need for innovative, accessible, and culturally sensitive \
             solutions to support the mental well-being of Gen Z in Bangladesh.")
    st.divider()

if selected == "Goals and Outcomes":
    st.title("Goals and Outcomes")
    st.header("Project Goals")
    st.markdown("- Develop comprehensive survey questionnaires to assess the perceptions, \
                experiences, and preferences of Gen Z individuals regarding depression, \
                digital device usage, and potential intervention strategies.")
    st.markdown("- Collect and analyse survey data to identify common themes, challenges, \
                and preferences related to mental health and digital device management among \
                Gen Z in Bangladesh.")
    st.markdown("- Utilise survey findings to inform the design and development of an \
                AI-powered chatbot tailored to address the specific needs and preferences \
                of Gen Z individuals in combating depression and device addiction.")
    st.markdown("- Implement and evaluate the effectiveness of the chatbot in providing \
                personalised support, guidance, and resources to Gen Z users, with a focus \
                on improving mental well-being and promoting healthier digital habits.")
    st.divider()
    st.header("Learning Outcomes")
    st.markdown("- Comprehensive survey questionnaires provide valuable insights into the \
                perceptions, experiences, and preferences of Gen Z individuals regarding \
                depression and device addiction in Bangladesh.")
    st.markdown("- Development and implementation of an AI-powered chatbot tailored to \
                address the specific needs and preferences of Gen Z users, with the \
                potential to provide accessible and personalized support for combating \
                depression and device addiction.")
    st.markdown("- Improved awareness, engagement, and utilisation of mental health \
                resources and support mechanisms among Gen Z individuals in Bangladesh,     \
                leading to enhanced mental well-being and healthier digital habits.")
    st.divider()

if selected == "Collaborators":
    st.title("Collaborators")

    st.markdown(
        "<div\
            style='text-align:center'\
        >\
            <h3>Data Collection Team</h3>\
            <div style='display:flex; justify-content: space-around'>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Paul Turyahabwa</h4>\
                    <h5>Co-lead</h5>\
                </div>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Kevin Medri</h4>\
                    <h5>Lead</h5>\
                </div>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Mahmudul Hasan</h4>\
                    <h5>Co-lead</h5>\
                </div>\
            </div>\
            <hr>\
            <h3>Data Preprocessing Team</h3>\
            <div style='display:flex; justify-content: space-around'>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Paul Turyahabwa</h4>\
                    <h5>Lead</h5>\
                </div>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Sanghamirta Basu</h4>\
                    <h5>Co-lead</h5>\
                </div>\
            </div>\
            <hr>\
            <h3>Exploratory Data Analysis Team</h3>\
            <div style='display:flex; justify-content: space-around''>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Paul Turyahabwa</h4>\
                    <h5>Co-lead</h5>\
                </div>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Liyana M Bava</h4>\
                    <h5>Lead</h5>\
                </div>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Andrew Asher</h4>\
                    <h5>Co-lead</h5>\
                </div>\
            </div>\
            <hr>\
            <h3>Model Development Team</h3>\
            <div style='display:flex; justify-content: space-around''>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Omkar Bhatkande</h4>\
                    <h5>Co-lead</h5>\
                    <h5><a href='https://www.linkedin.com/in/omkar-bhatkande/'>LinkedIn</a></h5>\
                </div>\
                <div>\
                    <img src='./assets/sarthak.jpg' alt='profile' />\
                    <h4>Hemanth Sai</h4>\
                    <h5>Co-lead</h5>\
                </div>\
            </div>\
            <hr>\
            <h3>Model Deployment Team</h3>\
            <div style='display:flex; justify-content: space-around''>\
                <div>\
                    <img src='assets/sarthak.jpg' alt='profile' />\
                    <h4>Sarthak Mishra</h4>\
                    <h5>Co-lead</h5>\
                    <h5><a href='https://www.linkedin.com/in/sarthakmishraa/'>LinkedIn</a></h5>\
                </div>\
            </div>\
            <hr>\
        </div>", unsafe_allow_html=True)

if selected == "Home":
    st.image("assets/omdenaLogo.png",
             caption="Creating Impact through AI",
             width=240)
    
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
            A gen Z kid is going to ask you a question, do not give a very long response.
            And do not answer the question if you do not know the answer, just say you do
            not have the answer.
            Question: 
            ''' + question
            response = model.generate_content(prompt)

            for word in response.text.split():
                yield word + " "
                time.sleep(0.10)

        with st.chat_message("ai"):
            response = st.write_stream(response_generator(question))
        st.session_state.messages.append({"role": "ai", "content": response})