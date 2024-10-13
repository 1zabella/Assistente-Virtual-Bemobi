import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_chat import message
import openai
import json
from openai import OpenAI

# Importar funções do arquivo de components
from components import render_header, initialize_session_state

# Carregar a chave da API do arquivo config.json
def load_api_key():
    with open("../utils/config.json", "r") as file:
        config = json.load(file)
    return config["openai_api_key"]

# Inicializando cliente OpenAI
client = OpenAI(api_key=load_api_key())

# Carregar dados do arquivo JSON
def load_user_data():
    with open("../utils/user_data.json", "r") as file:
        return json.load(file)

data = load_user_data()

# Função principal para inicializar a interface do chatbot
def main():
    # Configuração da página
    st.set_page_config(page_title="Assistente Proativo Bemobi", page_icon="🚀", layout="wide")

    # Inicializar variáveis de sessão
    initialize_session_state()

    # Renderizar cabeçalho
    render_header()

    # Estilo personalizado para simular layout do WhatsApp
    st.markdown("""
    <style>
    .user-message {
        text-align: right;
        background-color: #D3D3D3;
        border-radius: 15px 15px 0px 15px;
        padding: 10px;
        margin: 10px;
        max-width: 70%;
        float: right;
        clear: both;
    }
    .assistant-message {
        text-align: left;
        background-color: #D3D3D3;
        border-radius: 15px 15px 15px 0px;
        padding: 10px;
        margin: 10px;
        max-width: 70%;
        float: left;
        clear: both;
    }
    </style>
    """, unsafe_allow_html=True)

    # Selecionar dados do cliente (simulando uma busca pelo telefone)
    user_phone = "5541934567890".replace(' ', '')
    cliente = next((item for item in data if item["dados_pessoais"]["numero_telefone"] == user_phone), None)

    # Validar se o cliente foi encontrado
    if cliente:
        # Iniciar a conversa automaticamente
        if not st.session_state.chat_history:
            nome_cliente = cliente["dados_pessoais"]["nome_usuario"]
            nome_empresa = cliente["empresa"]["nome_empresa"] if "empresa" in cliente else "Bemobi"
            assinatura_status = cliente["dados_assinatura"]["status_conta"]

            if assinatura_status == "paga":
                response_content = f"""Olá {nome_cliente}, tudo bem? 
                Aqui é o Jarvis, seu assistente virtual da {nome_empresa}. 
                Estou aqui para ajudar no que for preciso! 
                Tudo está em dia com sua conta, mas se precisar de algo, estarei por aqui!"""
            elif assinatura_status == "prestes a vencer":
                response_content = f"""Olá {nome_cliente}, tudo bem? 
                Aqui é o Jarvis, seu assistente virtual da {nome_empresa}. 
                Notamos que seu pagamento está prestes a vencer.
                Gostaria de usar algum dos cartões cadastrados para realizar o pagamento e evitar qualquer problema?"""
            elif assinatura_status == "atrasada":
                response_content = f"""Olá {nome_cliente}, tudo bem? 
                Aqui é o Jarvis, seu assistente virtual da {nome_empresa}.
                Notamos que sua conta está atrasada. 
                Gostaria de regularizar agora usando um dos meios de pagamento cadastrados para evitar qualquer interrupção no serviço?"""

            st.session_state.chat_history.append({"role": "assistant", "content": response_content})
    else:
        st.warning("Cliente não encontrado. Verifique o número de telefone e tente novamente.")

    # Mostrar histórico de conversação
    response_container = st.container()
    with response_container:
        if st.session_state.chat_history:
            for i, message_data in enumerate(st.session_state.chat_history):
                is_user = message_data["role"] == "user"
                if is_user:
                    st.markdown(f"<div class='user-message'>{message_data['content']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='assistant-message'>{message_data['content']}</div>", unsafe_allow_html=True)

    # Capturar entrada do usuário
    user_input = st.text_input("Digite sua mensagem aqui:", "", key="user_input")
    if st.button("Enviar") and user_input:
        send_message(user_input, cliente)
        st.session_state["user_input"] = ""  # Limpar a caixa de texto após o envio

# Função para processar e enviar a mensagem
def send_message(user_input, cliente):
    # Adicionar a mensagem do usuário ao histórico
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Gerar resposta usando OpenAI
    response_content = get_openai_response(st.session_state.chat_history, cliente)
    st.session_state.chat_history.append({"role": "assistant", "content": response_content})

    # Atualizar a interface com a nova mensagem
    st.rerun()

# Função para obter resposta da OpenAI
def get_openai_response(chat_history, cliente):
    try:
        # Criar uma descrição completa do cliente para ser enviada como contexto
        cliente_context = f"""
        Nome: {cliente['dados_pessoais']['nome_usuario']}
        Telefone: {cliente['dados_pessoais']['numero_telefone']}
        CPF: {cliente['dados_pessoais']['cpf']}
        Data de Nascimento: {cliente['dados_pessoais']['data_nascimento']}
        Empresa: {cliente['empresa']['nome_empresa'] if 'empresa' in cliente else 'Bemobi'}
        Segmento: {cliente['empresa']['segmento'] if 'empresa' in cliente else 'N/A'}
        Status da Conta: {cliente['dados_assinatura']['status_conta']}
        Valor da Assinatura: R$ {cliente['dados_assinatura']['valor_assinatura']}
        Meio de Pagamento Atual: Cartão com final {cliente['dados_assinatura']['meio_pagamento_cadastrado']['numero_cartao'][-4:]}
        Data de Vencimento da Assinatura: {cliente['dados_assinatura']['data_vencimento']}
        """

        # Adicionar o contexto do cliente ao histórico
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente proativo que ajuda a resolver problemas de pagamento recorrente."},
                {"role": "system", "content": f"Aqui estão informações relevantes do cliente: {cliente_context}"},
                *[{"role": msg["role"], "content": msg["content"]} for msg in chat_history]
            ]
        )

        # Processar a resposta para incluir funcionalidades proativas
        generated_response = response.choices[0].message.content
        return generated_response
    except Exception as e:
        return f"Erro ao se comunicar com o OpenAI: {str(e)}"

# Executar aplicação
if __name__ == "__main__":
    main()