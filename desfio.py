from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import json

with open(r'dados.json') as arq_josn:
    d = json.load(arq_josn)

app = FastAPI()

@app.get('/index')

async def home():
    return 

ngrok_tunnel = ngrok.connect(8000)
print("Public URL:", ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)