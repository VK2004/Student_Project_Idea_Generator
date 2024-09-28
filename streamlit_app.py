import streamlit as st
from openai import OpenAI

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
# Title of the app
st.title("🎓 AI-Powered Project Idea Generator")

# Initial message from assistant asking for user's field of interest
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What is your field of interest?"}]

# Displaying previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Taking user input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    # Append user's input to session state
    st.session_state.messages.append({"role": "user", "content": f"Generate creative and relevant project ideas in the field of: {prompt}. Provide options with varying difficulty levels."})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    
