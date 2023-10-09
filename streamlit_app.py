from langchain.chat_models import ChatOpenAI
from langchain.schema import
import streamlit as st
from streamlit_chat import message

st.title("Customer simulator")

openai_api_key = st.secrets["openai"]


