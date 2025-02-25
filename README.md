
# Gemini AI Suite 🤖

The **Gemini AI Suite** is an Multimodal AI-powered application that integrates different features leveraging the **Gemini 1.5 Flash** model. This app allows users to interact with AI in several ways, such as chatting with a virtual assistant, generating text from prompts, summarizing content, extracting text from images, and more.

## Features

1. **AI ChatBot**: 🤖 Interact with a conversational AI chatbot powered by **Gemini 1.5 Flash**.
2. **Image Captioning**: 🖼️ Upload an image and get a caption generated using **Gemini 1.5 Flash**.
3. **Text Generation**: ✍️ Generate creative text based on a given prompt using **Gemini 1.5 Flash**.
4. **Text Summarization**: 📄➡️📃 Provide a long piece of text, and get a concise summary.
5. **OCR Text Extraction**: 📸➡️📝 Extract text from images containing textual content using **Gemini 1.5 Flash**.

## Features and Models

| Feature              | Model Used        | Purpose                                                                 |
|----------------------|-------------------|-------------------------------------------------------------------------|
| AI ChatBot           | Gemini 1.5 Flash  | Text-based conversational AI, generating responses to user input.      |
| Image Captioning     | Gemini 1.5 Flash  | Generates captions for uploaded images.                                |
| Text Generation      | Gemini 1.5 Flash  | Generates text based on a given prompt.                                |
| Text Summarization   | Gemini 1.5 Flash  | Summarizes a long piece of text into a concise version.                 |
| OCR Text Extraction  | Gemini 1.5 Flash  | Extracts text from images that contain textual content.                 |
| Embeddings           | Gemini 1.5 Flash  | Converts input text into numerical embeddings for retrieval or similarity tasks. |

## Setup Instructions

### Prerequisites

1. **Python 3.11**: Ensure Python is installed on your machine.
2. **Streamlit**: Install Streamlit using `pip install streamlit`.
3. **Google Gemini API**: You need an API key from Google to use the Gemini API. You can get it by registering on the [Google Cloud platform](https://cloud.google.com/) and enabling the Gemini API.
4. **Tesseract OCR**: Install the Tesseract OCR library by following the [installation guide](https://github.com/tesseract-ocr/tesseract).
5. **Other dependencies**: Install necessary libraries by running `pip install -r requirements.txt`.

### Required Libraries

Below are the required libraries for this app:

| Library              | Version    |
|----------------------|------------|
| streamlit            | 1.14.0     |
| google-generativeai  | 1.0.0      |
| pillow               | 9.2.0      |
| pytesseract          | 0.3.9      |
| tesseract            | 4.1.1      |

### Installation

1. Clone the repository:
    ```bash
    git clone "https://github.com/shreymukh2020/Gemini-Multimodal-AI-Chatbot"
    cd gemini-ai-suite
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your **Gemini API key**:
    - Get your Gemini API key from the [Google Cloud platform](https://cloud.google.com/).
    - Place your API key in a file named `config.json` in the root directory of the project.

    Example `config.json`:
    ```json
    {
        "GOOGLE_API_KEY": "your-api-key-here"
    }
    ```

5. Install Tesseract OCR:
    - On **Windows**, download the installer from [here](https://github.com/UB-Mannheim/tesseract/wiki).
    - On **macOS**, use `brew install tesseract`.
    - On **Linux**, use `sudo apt-get install tesseract-ocr`.

6. Run the app:
    ```bash
    streamlit run app.py
    ```

### Usage

Once the app is running, you will be able to interact with it through a simple and intuitive interface. Each feature is accessible via the sidebar, where you can choose between:

- **AI ChatBot**: 🤖 Chat with the Gemini AI chatbot.
- **Image Captioning**: 🖼️ Upload an image and get a caption.
- **Text Generation**: ✍️ Provide a prompt and generate text.
- **Text Summarization**: 📄➡️📃 Input text for summarization.
- **OCR Text Extraction**: 📸➡️📝 Upload an image and extract the text.


