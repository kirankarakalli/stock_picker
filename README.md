#  CrewAI Stock Picker

An AI-powered Stock Picker application built using **CrewAI**, **yFinance**, and **Streamlit**. The system uses multiple AI agents and custom tools to analyze stock fundamentals, recent news, risk factors, and generate a ranked stock watchlist.

---

## Features

### Multi-Agent Workflow

* Market Analyst Agent
* News Analyst Agent
* Risk Analyst Agent
* Stock Picker Agent

### Custom Tools

* Stock Data Tool

  * Current Price
  * Market Cap
  * PE Ratio
  * Revenue Growth
  * Profit Margin
  * Debt-to-Equity Ratio
  * Analyst Recommendation

* News Data Tool

  * Latest stock-related news
  * Publisher information
  * News summaries
  * Publication dates

* Stock Scoring Tool

  * Growth Score
  * Margin Score
  * Valuation Score
  * Debt Score
  * Final Composite Score

### Dashboard

* Streamlit UI
* Enter custom stock tickers
* Generate ranked watchlist reports
* Interactive stock price charts
* Multiple chart periods:

  * 1 Month
  * 6 Months
  * 1 Year
  * 5 Years

---

##  Architecture

```text
User Input (Tickers)
          │
          ▼
 ┌─────────────────┐
 │ StockDataTool   │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ Market Analyst  │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ NewsDataTool    │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ News Analyst    │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ Risk Analyst    │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ Scoring Tool    │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ Stock Picker    │
 └─────────────────┘
          │
          ▼
 Ranked Stock Report
```

---

## Tech Stack

### AI & Agents

* CrewAI
* OpenAI

### Data Sources

* yFinance

### Frontend

* Streamlit

### Backend

* Python

---

## Stock Scoring Methodology

Stocks are scored using four key factors:

| Metric         | Weight |
| -------------- | ------ |
| Revenue Growth | 30%    |
| Profit Margin  | 30%    |
| PE Ratio       | 20%    |
| Debt-to-Equity | 20%    |

Final ranking is based on the combined score and risk analysis.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kirankarakalli/stock_picker.git
cd stock_picker
```

Install dependencies:

```bash
uv sync
```

---

## Run CrewAI

```bash
uv run run_crew AAPL MSFT TSLA
```

Example:

```bash
uv run run_crew NVDA AAPL MSFT
```

---

## Run Streamlit Dashboard

```bash
uv run streamlit run app.py
```

Open the URL shown in the terminal.

---

## Example Tickers

### US Stocks

```text
AAPL
MSFT
NVDA
TSLA
META
GOOGL
AMD
```

### Indian Stocks

```text
TCS.NS
INFY.NS
RELIANCE.NS
HDFCBANK.NS
ICICIBANK.NS
```

---

##  Sample Output

The system generates:

* Ranked Stock Watchlist
* Fundamental Analysis
* News Analysis
* Risk Assessment
* Stock Scores
* Educational Conclusion

---



👨‍💻 Author

Kiran Karakalli

Built to learn Agentic AI, CrewAI, Multi-Agent Systems, Financial Data Analysis, and Streamlit Application Development.
