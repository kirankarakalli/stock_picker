from src.stock_picker.tools.custom_tool import StockDataTool

tool = StockDataTool()

print(tool.run(ticker="AAPL"))