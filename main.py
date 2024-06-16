import streamlit as st
from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

st.title("聊天助手")

#memory = ConversationBufferMemory(return_messages = True)
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory()
    st.session_state["messages"] = [{"role" : "ai",
                                     "content":"你好，我是你的AI助手，有什么可以帮助你的吗？"}]
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("")
if prompt:
       st.session_state["messages"].append({"role" : "human" , "content" : prompt})
       st.chat_message("human").write(prompt)

       with st.spinner("AI正在思考中，请稍等..."):
           response = get_chat_response(prompt, st.session_state["memory"])
       msg = {"role" : "ai", "content" : response}
       st.session_state["messages"].append(msg)
       st.chat_message("ai").write(response)

