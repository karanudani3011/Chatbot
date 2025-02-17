import streamlit as st
import requests
from streamlit_extras.switch_page_button import switch_page 


# Set page config
st.set_page_config(page_icon="🤖", layout="centered")

API_KEY = "api key"
API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

def fetch_groq_response(prompt):
    """Fetch AI-generated response from API."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json().get("choices")[0].get("message", {}).get("content", "").strip()
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

# Logout button to redirect to login page
if st.button("Logout", key="logout_button", help="Log out and go to the login page", on_click=lambda: switch_page("login")):
    st.session_state.clear()  # Clear session state to log out the user
    switch_page("login")  # Redirect to login page

# Display Chatbot UI
st.markdown("<h1>🤖 AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h3>AI-powered assistant</h3>", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input for chatbot
user_input = st.text_input("You:", "")

# Send button action
if st.button("Send"):
    if user_input:
        # Get response from AI
        bot_response = fetch_groq_response(user_input)

        # Append to chat history
        st.session_state.chat_history.append({"user": user_input, "bot": bot_response})

        # Use session_state to manually trigger rerun
        st.session_state.chat_history_updated = True  # Adding a flag to trigger the rerun

# Display chat history if updated
if "chat_history_updated" in st.session_state and st.session_state.chat_history_updated:
    for chat in st.session_state.chat_history:
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**ChatBot:** {chat['bot']}")
        st.markdown("---")
    # Reset the flag after rendering the chat history
    st.session_state.chat_history_updated = False

# Footer message about privacy
st.markdown("<footer>🔒 We respect your privacy. Your data is not stored.</footer>", unsafe_allow_html=True)

