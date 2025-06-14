import streamlit as st
import time
from langchain_core.messages import HumanMessage
from graph_bot import build_graph, init_state

# Configure the page
st.set_page_config(page_title="💬 Jaax's Chatbot", layout="centered")

# Add custom styles
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        .chat-box {
            max-height: 500px;
            overflow-y: auto;
            background: #f4f4f4;
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: inset 0 0 8px rgba(0,0,0,0.1);
        }
        .jaax-msg {
            background: linear-gradient(135deg, #d0f0c0, #b0e0e6);
            padding: 10px 16px;
            border-radius: 10px;
            text-align: right;
            margin: 10px 0;
            font-weight: bold;
        }
        .bot-msg {
            background: linear-gradient(135deg, #fff, #e6e6e6);
            padding: 10px 16px;
            border-radius: 10px;
            text-align: left;
            margin: 10px 0;
        }
        .typing-dots {
            display: inline-block;
            width: 1em;
            height: 1em;
            border-radius: 50%;
            background: #aaa;
            animation: blink 1.4s infinite;
            margin: 0 2px;
        }
        @keyframes blink {
            0%, 100% { opacity: 0.2; }
            50% { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Options")
    if st.button("🗑️ Reset Chat"):
        st.session_state.state = init_state()
        st.session_state.chat_history = []

# Initialize session state
if "state" not in st.session_state:
    st.session_state.graph = build_graph()
    st.session_state.state = init_state()
    st.session_state.chat_history = []

# Page Title with gradient text
st.markdown("""
    <h2 style='text-align: center; font-size: 36px; font-weight: bold; color: #1a1a1a;'>
        🤖 Welcome, Jaax!
    </h2>
""", unsafe_allow_html=True)


st.caption("💡 Powered by Me")

# Chat display
st.markdown('<div class="chat-box">', unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    if sender == "jaax":
        st.markdown(f'<div class="jaax-msg">Jaax: {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">Bot: {message}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.chat_history.append(("jaax", user_input))
    st.session_state.state["messages"].append(HumanMessage(content=user_input))

    # Bot is typing animation
    with st.chat_message("bot"):
        with st.spinner("Mapla is thinking..."):
            st.markdown(
                '<span class="typing-dots"></span><span class="typing-dots"></span><span class="typing-dots"></span>',
                unsafe_allow_html=True,
            )
            time.sleep(1.3)

    # Get AI response
    result = st.session_state.graph.invoke(st.session_state.state)
    ai_msg = result["messages"][-1]
    ai_content = ai_msg.content

    # Typing animation effect
    display = st.empty()
    typed = ""
    for char in ai_content:
        typed += char
        display.markdown(f'<div class="bot-msg">Bot: {typed}</div>', unsafe_allow_html=True)
        time.sleep(0.015)

    st.session_state.chat_history.append(("bot", ai_content))
    st.session_state.state = result
