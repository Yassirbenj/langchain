from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

import streamlit as st
from streamlit_chat import message

st.title("Customer simulator")

openai_api_key = st.secrets["openai"]

chat=ChatOpenAI(temperature=0.5,openai_api_key=openai_api_key)

customer_persona="You are a customer responding to a call from a sales person"

with st.sidebar:
    with st.form("input form"):
        st.write("<h3>Enter the customer personae ✨</h3>", unsafe_allow_html=True)
        mode=st.selectbox('What mode do you want for customer?',('Receiving a call from a sales person', 'Doing a call to customer service'))
        industry=st.text_input("Enter customer industry:")
        position=st.text_input("Enter customer position:")
        company_char=st.text_input("Enter company characterstics:")
        pain_points=st.text_input("Enter pain points:")
        decision_making_factors=st.text_input("Enter some decision factors:")
        personnality=st.text_input("Enter some key personnality characteristics:")
        if st.form_submit_button("Initiate discussion"):
            customer_persona = f"You are a customer {mode}. you have the following characterstics."
            customer_persona += f"You are in the industry of {industry}, you have the position of {position}."
            customer_persona += f"The main characteristics of the company you are working for are {company_char}."
            customer_persona += f"The main pain points in your business are {pain_points} and your decision making factors are {decision_making_factors}." 
            customer_persona += f"your main personality trait are {personnality}."
            customer_persona += f"you respond briefly to the question. you are a customer not an assistant "

if "messages" not in st.session_state:
    st.session_state.messages=[
     SystemMessage(content=customer_persona)
    ]

if prompt := st.chat_input("Start your call with an introduction"):
  st.session_state.messages.append(HumanMessage(content=prompt))
  with st.spinner ("Thinking..."):
    response=chat(st.session_state.messages)
  st.session_state.messages.append(AIMessage(content=response.content))

messages=st.session_state.get('messages',[])
for i,msg in enumerate(messages[1:]): 
    if i % 2 == 0:
    #    st.write('yes')
        message(msg.content,is_user=True,key=str(i)+'_user')
    else:
        message(msg.content,is_user=False,key=str(i)+'_ai')


