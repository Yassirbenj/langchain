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

messages=[
 SystemMessage(content="you are a helpful assistant")
]

if prompt := st.chat_input("Start your call with an introduction"):
  message(prompt,is_user=True)
  messages.append(HumanMessage(content=prompt))
  st.write(messages)
  #response=chat(message)
  #message(response.content,is_user=False)


