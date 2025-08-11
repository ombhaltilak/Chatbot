import streamlit as st
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os

MODEL_PATH = r"C:\Users\om\Downloads\llama-2-7b-chat.Q2_K.gguf"  # Faster quantization

def init_page():
    st.set_page_config(page_title="Personal Chatbot")
    st.header("Personal Chatbot")
    st.sidebar.title("Options")

def select_llm():
    return LlamaCPP(
        model_path=MODEL_PATH,
        temperature=1.9,
        max_new_tokens=150,
        context_window=4096,
        model_kwargs={
            "n_threads": max(1, os.cpu_count() - 2),
            "n_batch": 8,
            "n_gpu_layers": 20,
            "verbose": False
        },
        messages_to_prompt=messages_to_prompt,
        completion_to_prompt=completion_to_prompt,
        verbose=False,
    )


def init_messages():
    if st.sidebar.button("Clear Conversation", key="clear") or "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant. Reply in markdown format.")
        ]

def get_answer(llm, messages):
    # Turn all stored messages into one prompt string
    prompt = ""
    for msg in messages:
        role = "System" if isinstance(msg, SystemMessage) else \
               "User" if isinstance(msg, HumanMessage) else \
               "Assistant"
        prompt += f"{role}: {msg.content}\n"

    # Send full conversation to the model
    response = llm.complete(prompt)
    return response.text

def main():
    init_page()
    llm = select_llm()
    init_messages()

    if user_input := st.chat_input("Input your question!"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Bot is typing..."):
            # Pass full messages list here instead of just user_input
            answer = get_answer(llm, st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=answer))

    for message in st.session_state.get("messages", []):
        role = "assistant" if isinstance(message, AIMessage) else "user"
        with st.chat_message(role):
            st.markdown(message.content)

if __name__ == "__main__":
    main()
