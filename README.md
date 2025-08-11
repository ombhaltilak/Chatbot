
# 🤖 Personal Chatbot with LlamaCPP & Streamlit

---

## Overview

This is a **Personal Chatbot** web application built with **Streamlit** that leverages the **LlamaCPP** model for conversational AI. The bot interacts via a chat interface and processes conversations using a local quantized LLaMA 2 7B model (`.gguf` format) for fast, efficient inference.

The bot maintains chat history and supports conversation clearing from the sidebar.

---

## 🌟 Key Features

- 💬 **Streamlit Chat Interface**  
  Interactive chat UI with messages displayed in user/assistant style bubbles.

- 🦙 **LlamaCPP Integration**  
  Uses a local LLaMA 2 7B quantized model (`.gguf`) for generating responses.

- 🔄 **Persistent Conversation**  
  Maintains chat history within the session and allows clearing the conversation.

- ⚙️ **Configurable Model Parameters**  
  Includes temperature, max tokens, threading, batch size, and GPU layer options.

---

## ⚙️ How It Works

- The conversation is stored as a list of messages (System, Human, AI) in Streamlit's session state.

- On user input, the entire conversation is converted into a prompt string with roles indicated.

- The prompt is passed to the LlamaCPP model to generate a reply.

- The assistant's response is appended back to the chat history for display.

---

## 📂 Project Structure

```

├── app.py              # Main Streamlit chatbot app script
├── llama-2-7b-chat.Q2\_K.gguf  # Quantized LLaMA 2 7B model file (local path)
└── README.md           # Documentation file (this file)

````

---

## 📦 Setup & Installation

1. **Clone the repository:**

   ````
   git clone <your-repo-url>
   cd <your-repo-name>
````

````
2. **Ensure you have the LLaMA 2 7B quantized model file (`.gguf`)**
   Download and place it locally. Update the `MODEL_PATH` in `app.py` accordingly.

3. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**

   ```bash
   pip install streamlit llama-index langchain
   ```

   *(Add any additional required packages depending on your environment.)*

---

## ▶️ How to Run

Run the Streamlit app from your terminal:

```bash
streamlit run app.py
```

Open your browser to the URL provided (usually `http://localhost:8501`).

---

## ⚙️ Configuration Notes

* The model parameters in `select_llm()` can be tuned, e.g.:

  * `temperature` controls randomness (higher = more creative responses).
  * `max_new_tokens` controls response length.
  * `n_threads`, `n_batch`, and `n_gpu_layers` control CPU/GPU usage for inference speed.

* The `Clear Conversation` button in the sidebar resets the chat history.

---

Enjoy chatting with your own personal AI assistant! 🚀

Let me know if you want me to generate the `README.md` file for you or help with anything else!
````
