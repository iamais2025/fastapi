from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

# Defina sua chave de API aqui
API_KEY = "supabase123"  # você pode mudar para o que quiser

@app.get("/")
async def root():
    return {"greeting": "Hello, World", "message": "Welcome to FastAPI!"}

@app.get("/clientes")
async def get_clientes(request: Request):
    client_key = request.headers.get("x-api-key")
    if client_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    # Aqui você pode integrar com Supabase ou retornar dados mockados
    return [
        {"nome": "João", "serviço": "Corte"},
        {"nome": "Ana", "serviço": "Barba"}
    ]
