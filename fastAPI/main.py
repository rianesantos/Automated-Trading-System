from fastapi import FastAPI
from fastAPI.routers import market_data, alerts, portfolio

app = FastAPI(title="Análise de Mercado")

app.include_router(market_data.router)

@app.get("/")
def home():
    return {
        "message": "API de Análise de Mercado", 
        "rotas": {
            "current_price": "/market/current/{ticker}",
            "historical_data": "/market/historical"
        }
    }
    


