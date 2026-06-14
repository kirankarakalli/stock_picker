from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel,Field
import yfinance as yf


class StockScoringToolInput(BaseModel):
    """Input schema for StockScoringTool"""
    ticker:str=Field(...,description="Stock ticker symbol like AAPL, MSFT, NVDA")


class StockScoringTool(BaseTool):
    name: str = "Stock Scoring Tool"
    description: str = "Calculates a stock score based on growth, margin, valuation, and debt."
    args_schema: Type[BaseModel] = StockScoringToolInput

    def _run(self,ticker:str)->str:
        try:
            stock=yf.Ticker(ticker)
            info=stock.info

            revenue_growth=info.get('revenueGrowth') or 0
            pe_ratio=info.get('trailingPE') or 0
            debt_to_equity=info.get('debtToEquity') or 0
            profit_margin=info.get('profitMargins') or 0

            growth_score = min(revenue_growth * 100, 30)
            margin_score = min(profit_margin * 100, 30)

            if pe_ratio == 0:
                valuation_score = 0
            elif pe_ratio <= 25:
                valuation_score = 20
            elif pe_ratio <= 40:
                valuation_score = 15
            elif pe_ratio <= 70:
                valuation_score = 10
            else:
                valuation_score = 5

            if debt_to_equity <= 30:
                debt_score = 20
            elif debt_to_equity <= 70:
                debt_score = 15
            elif debt_to_equity <= 120:
                debt_score = 10
            else:
                debt_score = 5

            final_score = growth_score + margin_score + valuation_score + debt_score

            return str({
                "ticker": ticker,
                "company_name": info.get("longName"),
                "growth_score": round(growth_score, 2),
                "margin_score": round(margin_score, 2),
                "valuation_score": valuation_score,
                "debt_score": debt_score,
                "final_score": round(final_score, 2),
            })



            return str(info)
        except Exception as e:
            return f"Error fetching stock data: {str(e)}"




