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

if "messages" not in st.session_state:
    st.session_state.messages=[
     SystemMessage(content="you are a helpful assistant")
    ]

if prompt := st.chat_input("Start your call with an introduction"):
  st.session_state.messages.append(HumanMessage(content=prompt))
  with st.spinner ("Thinking..."):
    response=chat(st.session_state.messages)
  st.session_state.messages.append(AIMessage(content=response.content))

messages=st.session_state.get('messages',[])
for i,msg in messages:
    if i % 2 == 0:
        message(msg,is_user=True,key=str(i)+'_user')
    else:
        message(msg,is_user=False,key=str(i)+'_ai')


