import streamlit as st
from streamlit_extras.colored_header import colored_header

# Função para renderizar cabeçalho estilizado
def render_header():
    st.title(":violet[Assistente Proativo Bemobi 🚀]")
    colored_header(label='', description='', color_name='gray-30')

# Função para inicializar variáveis de estado da sessão
def initialize_session_state():
    if 'user_responses' not in st.session_state:
        st.session_state['user_responses'] = []
    if 'bot_responses' not in st.session_state:
        st.session_state['bot_responses'] = []
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

# Função para capturar e exibir as mensagens do chat
def display_chat():
    # Mostrar histórico de conversação
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f"**Você**: {message['content']}")
        elif message['role'] == 'assistant':
            st.markdown(f"**Jarvis**: {message['content']}")

    # Input do usuário
    user_input = st.text_input("Digite sua resposta", "")
    if user_input:
        # Adicionar a mensagem do usuário ao histórico
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.markdown(f"**Você**: {user_input}")

        return user_input
    return None
