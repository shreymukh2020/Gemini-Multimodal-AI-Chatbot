import os
import json
from PIL import Image
import pytesseract  # OCR Library
import streamlit as st
from streamlit_option_menu import option_menu
import google.generativeai as genai

# Working directory path
working_dir = os.path.dirname(os.path.abspath(__file__))

# Path of config_data file
config_file_path = f"{working_dir}/config.json"
config_data = json.load(open(config_file_path))

# Loading the GOOGLE_API_KEY
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# Configuring google.generativeai with API key
genai.configure(api_key=GOOGLE_API_KEY)

# App Configuration
st.set_page_config(page_title="Gemini AI", page_icon="🌊", layout="wide")

# Custom CSS for Enhanced UI
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

        body {
            background-color: #f4f4f4;
            font-family: 'Poppins', sans-serif;
        }
        .stSidebar {
            background-color: #0077B6 !important; /* Ocean Blue */
            color: #FFFFFF !important;
        }
        .stTitle, .stMarkdown {
            color: #023E8A; /* Deep Blue */
        }
        .stButton > button {
            background-color: #0096C7; /* Light Ocean Blue */
            color: #FFFFFF;
            border-radius: 10px;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #005F73; /* Darker Shade */
        }
        .stTextArea textarea {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation with Ocean Blue Theme
with st.sidebar:
    st.markdown("## 🌊 Gemini AI Suite", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=[
            '🤖 AI ChatBot', 
            '📷 Image Captioning', 
            '📝 Text Generation', 
            '📚 Text Summarization', 
            '📄 OCR Text Extraction'
        ],
        icons=['robot', 'camera', 'pen', 'book', 'file-text'],
        default_index=0,
        styles={
            "container": {"padding": "10px", "background-color": "#0077B6"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "5px", "color": "white"},
            "nav-link-selected": {
                "background-color": "#0096C7", 
                "color": "white", 
                "border-radius": "10px",
                "font-weight": "bold"
            }
        }
    )

# Function to translate roles for chat history
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# AI Chatbot Page
if selected == '🤖 AI ChatBot':
    # Load Gemini-Pro model for Chat
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    st.title("🤖 AI ChatBot")
    st.markdown("Chat with Gemini-Pro AI and get instant responses.", unsafe_allow_html=True)

    # Add a button to clear chat history
    if st.button("Clear Chat History"):
        if "chat_session" in st.session_state:
            st.session_state.chat_session.history = []
            st.success("Chat history cleared!")
        else:
            st.warning("No chat history to clear.")

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = gemini_pro_model.start_chat(history=[])

    # Display existing chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input for user prompt
    user_prompt = st.chat_input("Ask Gemini-Pro...")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

# Image Captioning Page
elif selected == "📷 Image Captioning":
    st.title("📷 Snap Narrate")
    st.markdown("Upload an image and let AI generate a caption for you.", unsafe_allow_html=True)

    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image and st.button("Generate Caption"):
        image = Image.open(uploaded_image)
        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(image.resize((600, 400)), use_column_width=True)
        
        with col2:
            gemini_vision_model = genai.GenerativeModel("gemini-1.5-flash")
            caption_response = gemini_vision_model.generate_content(["Write a short caption for this image", image])
            caption = caption_response.text
            st.info(caption)

# Text Generation Page
elif selected == "📝 Text Generation":
    st.title("📝 Text Generation")
    st.markdown("Provide a prompt, and Gemini-Pro will generate text based on your input.", unsafe_allow_html=True)

    user_prompt = st.text_area("Enter a prompt for text generation")

    if st.button("Generate Text"):
        if user_prompt.strip():
            try:
                gemini_pro_model = genai.GenerativeModel("gemini-pro")
                generated_text_response = gemini_pro_model.generate_content(user_prompt)
                generated_text = generated_text_response.text
                st.success("Text Generated:")
                st.text_area("Generated Text", generated_text, height=200)
            except Exception as e:
                st.error(f"Error generating text: {e}")
        else:
            st.warning("Please enter a prompt to generate text.")

# Text Summarization Page
elif selected == "📚 Text Summarization":
    st.title("📚 Text Summarization")
    st.markdown("Provide a long piece of text, and Gemini-Pro will summarize it for you.", unsafe_allow_html=True)

    user_prompt = st.text_area("Enter text to summarize")

    if st.button("Generate Summary"):
        if user_prompt.strip():
            try:
                gemini_pro_model = genai.GenerativeModel("gemini-pro")
                summary_response = gemini_pro_model.generate_content(f"Summarize the following text: {user_prompt}")
                summary = summary_response.text
                st.success("Summary Generated:")
                st.text_area("Summarized Text", summary, height=200)
            except Exception as e:
                st.error(f"Error generating summary: {e}")
        else:
            st.warning("Please enter text to summarize.")

# OCR Text Extraction Page
elif selected == "📄 OCR Text Extraction":
    st.title("📄 OCR Text Extraction")
    st.markdown("Upload an image containing text, and the AI will extract and display the text for you.", unsafe_allow_html=True)

    uploaded_image = st.file_uploader("Upload an image with text...", type=["jpg", "jpeg", "png"])

    if uploaded_image and st.button("Extract Text"):
        image = Image.open(uploaded_image)
        extracted_text = pytesseract.image_to_string(image)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(image.resize((600, 400)), use_column_width=True)

        with col2:
            if extracted_text.strip():
                st.subheader("Extracted Text:")
                st.text_area("Recognized Text", extracted_text, height=200)
            else:
                st.warning("No text detected in the image. Try a different image.")
