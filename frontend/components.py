import streamlit as st
from streamlit_extras.colored_header import colored_header

# Função para renderizar cabeçalho estilizado
def render_header():
    col1, col2 = st.columns([1, 8])  # Ajuste a proporção das colunas para aproximar o ícone do texto
    with col1:
        st.image("assets/jarvis.png", use_column_width=True)  # Aumentar a imagem para preencher a coluna
    with col2:
        st.markdown("<h1 style='font-size: 2em; margin: 0; padding: 1.8; color: #8A2BE2;'>Jarvis, o assistente proativo!</h1>", unsafe_allow_html=True)
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
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            if message['role'] == 'user':
                st.markdown(f"<div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 10px 0;'>Você: {message['content']}</div>", unsafe_allow_html=True)
            elif message['role'] == 'assistant':
                st.markdown(f"<div style='background-color: #d3d3d3; padding: 10px; border-radius: 5px; margin: 10px 0;'>Jarvis: {message['content']}</div>", unsafe_allow_html=True)

    # Input do usuário
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("Digite sua mensagem:", key="user_input")
        submit_button = st.form_submit_button(label="Enviar")

    if submit_button and user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
# Função para lidar com a entrada do usuário
def handle_user_input():
    user_input = st.session_state.user_input
    if user_input:
        # Adicionar a mensagem do usuário ao histórico
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.user_input = ""  # Limpar o campo de entrada após enviar a mensagem

        # Aqui você pode adicionar a lógica para gerar a resposta do assistente
        # Por exemplo, chamando uma função para processar a entrada e retornar a resposta
        response_content = "Obrigado pela sua mensagem! (Resposta simulada)"
        st.session_state.chat_history.append({"role": "assistant", "content": response_content})