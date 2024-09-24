import os
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Carregar variáveis de ambiente
load_dotenv()
# Configure a chave de API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class Message(BaseModel):
    message: str = Field(..., example="Hello World")

@app.post("/response")
def process_message(message: Message):
    print(message)
    try:
        # Criar um modelo generativo com o nome correto do modelo
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Gerar conteúdo baseado na mensagem do usuário
        response = model.generate_content(message.message)

        # Retornar o texto gerado
        return response.text
    except Exception as e:
        return f"Ocorreu um erro ao processar sua solicitação: {e}"
    
    