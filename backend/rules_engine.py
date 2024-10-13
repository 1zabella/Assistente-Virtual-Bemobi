from datetime import datetime
import json

def check_payment_problems(user_data):
    """Verifica se o cartão está prestes a vencer antes do próximo vencimento da fatura"""
    current_card_expiration = datetime.strptime(user_data['dados_assinatura']['meio_pagamento_cadastrado']['data_vencimento'], "%Y-%m-%d")
    next_due_date = datetime.strptime(user_data['dados_assinatura']['data_vencimento'], "%Y-%m-%d")
    
    # Verifica se o cartão expira antes do próximo vencimento
    return current_card_expiration < next_due_date

def get_payment_options(user_data):
    """Retorna os cartões cadastrados do cliente"""
    return [
        {
            "last_digits": card['numero_cartao'][-4:],
            "modalidade": card['modalidade']
        } for card in user_data['dados_cartao']
    ]

def load_user_data(user_id):
    """Carrega os dados do usuário pelo número de telefone ou ID"""
    with open('user_data.json') as file:
        data = json.load(file)
        for user in data:
            if user['dados_pessoais']['numero_telefone'] == user_id:
                return user
    return None
