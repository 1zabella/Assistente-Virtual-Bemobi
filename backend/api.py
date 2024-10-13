from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from rules_engine import check_payment_problems, get_payment_options, load_user_data

app = FastAPI()

class NotificationRequest(BaseModel):
    user_id: str

def send_proactive_message(user_data, message):
    # Lógica para enviar a mensagem ao usuário via chatbot ou outro canal
    print(f"Sending message to {user_data['dados_pessoais']['nome_usuario']}: {message}")

@app.post("/notify_payment/")
async def notify_payment(request: NotificationRequest, background_tasks: BackgroundTasks):
    user_data = load_user_data(request.user_id)
    if not user_data:
        return {"status": "user not found"}

    if check_payment_problems(user_data):
        message = f"Olá {user_data['dados_pessoais']['nome_usuario']}, seu cartão com final {user_data['dados_assinatura']['meio_pagamento_cadastrado']['numero_cartao'][-4:]} vencerá antes do próximo pagamento. Deseja atualizar as informações?"
        background_tasks.add_task(send_proactive_message, user_data, message)
        return {"status": "notification sent"}
    
    return {"status": "no issues"}

@app.get("/payment_options/{user_id}")
async def payment_options(user_id: str):
    user_data = load_user_data(user_id)
    if not user_data:
        return {"status": "user not found"}
    
    options = get_payment_options(user_data)
    return {"payment_options": options}
