from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import yfinance as yf


class NewsDataToolInput(BaseModel):
    """Input schema for NewsDataTool."""
    ticker: str = Field(
        ...,
        description="Stock ticker symbol like AAPL, MSFT, NVDA"
    )


class NewsDataTool(BaseTool):
    name: str = "news Data Tool"
    description: str = (
        "Fetches recent news headlines and publishers for a stock ticker."
    )
    args_schema: Type[BaseModel] = NewsDataToolInput

    def _run(self, ticker: str) -> str:
        try:
            stock = yf.Ticker(ticker)
            news = stock.news

            news_items=[]

            for item in news[:5]:
                content = item.get("content", {})

                news_items.append({
                "title": content.get("title"),
                "publisher": content.get("provider", {}).get("displayName"),
                "summary": content.get("summary"),
                "published_at": content.get("pubDate"),
                "url": content.get("canonicalUrl", {}).get("url"),
                })


            return ({'ticker':ticker,'news':news_items})

        except Exception as e:
            return f"Error fetching stock data: {str(e)}"