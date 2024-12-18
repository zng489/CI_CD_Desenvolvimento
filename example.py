
def greet(name):
    print(f"teste, {name}")


greet("Alice")

import requests
import json

# URL do webhook do Discord
webhook_url = 'https://discord.com/api/webhooks/1285654063169540156/NnZO27R4tdxsJp-j9fDa8cOjcGIg1l7sGzm_sZs95E4KY7D360CR8UOVo6Omyyxk4zOv'

# Mensagem que você quer enviar
message = {
    "content": "Sua mensagem aqui!"
}

# Enviando a requisição POST para o webhook
response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

# Verificando se a requisição foi bem-sucedida
if response.status_code == 204:
    print("Mensagem enviada com sucesso!")
else:
    print(f"Falha ao enviar mensagem. Status Code: {response.status_code}")

