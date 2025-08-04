from fastapi import APIRouter
from fastAPI.services.market_service import MarketService
from fastAPI.models.market_model import HistoricalDataRequest, CurrentPriceResponse

router = APIRouter(prefix = "/market", tags = ["Market Data"])

@router.post("/historical")
async def get_historical(request: HistoricalDataRequest):
    data = MarketService.get_historical_data(request)
    return {"data": data.to_dict(orient = "records")}

@router.get("/current/{ticker}", response_model=CurrentPriceResponse)
async def get_current_price(ticker: str):
    prices = MarketService.get_current_prices([ticker])
    return CurrentPriceResponse(ticker = ticker, price = prices.get(ticker))
