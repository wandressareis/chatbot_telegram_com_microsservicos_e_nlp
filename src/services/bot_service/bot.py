import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv
import json
import requests

# Carregar variáveis de ambiente
load_dotenv()

def requisicao_api(message):
    url = 'http://nlp_service:8002/response'
    data = {"message": message }
    data_json = json.dumps(data)
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    print(response.json())
    return response.json()

# Função de start
async def start(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    nome = update.message.chat.first_name
    # salvar_usuario(user_id, nome)
    await update.message.reply_text(f'Bem-vindo, {nome}! Como posso ajudar?')

# Função para lidar com mensagens
async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    try:
        # Processa a mensagem usando a função de processamento com o Gemini
        # resposta = process_message(user_message)
        await update.message.reply_text(requisicao_api(user_message))
    except Exception as e:
        await update.message.reply_text(f"Desculpe, ocorreu um erro: {e}")

# Configuração do bot
def start_bot():
    token = os.getenv("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    application.run_polling()

# Inicializa o bot do Telegram
start_bot()