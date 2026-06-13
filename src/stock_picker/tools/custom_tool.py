from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import yfinance as yf


class StockDataToolInput(BaseModel):
    """Input schema for StockDataTool."""
    ticker: str = Field(
        ...,
        description="Stock ticker symbol like AAPL, MSFT, NVDA"
    )


class StockDataTool(BaseTool):
    name: str = "Stock Data Tool"
    description: str = (
        "Fetches stock fundamentals such as price, market cap, PE ratio, and revenue growth."
    )
    args_schema: Type[BaseModel] = StockDataToolInput

    def _run(self, ticker: str) -> str:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            data = {
                "ticker": ticker,
                "company_name": info.get("longName"),
                "current_price": info.get("currentPrice"),
                "market_cap": info.get("marketCap"),
                "pe_ratio": info.get("trailingPE"),
                "revenue_growth": info.get("revenueGrowth"),
                "profit_margin": info.get("profitMargins"),
                "debt_to_equity": info.get("debtToEquity"),
                "recommendation": info.get("recommendationKey"),
            }

            return str(data)

        except Exception as e:
            return f"Error fetching stock data: {str(e)}"