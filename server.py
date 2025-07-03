from mcp.server.fastmcp import FastMCP
from finance_crew import run_financial_analysis
import yfinance as yf

# create FastMCP instance
mcp = FastMCP("financial-analyst")

@mcp.tool()
def analyze_stock(symbol: str) -> dict:
    """
    Fetch stock data for a given symbol using yfinance.
    
    Args:
        symbol (str): The stock ticker symbol, e.g., 'AAPL' or 'TSLA'.

    Returns:
        dict: Structured data about the stock.
    """
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        if not info or "currentPrice" not in info:
            return {"error": f"No data available for '{symbol}'."}

        return {
            "symbol": symbol.upper(),
            "longName": info.get("longName"),
            "currentPrice": info.get("currentPrice"),
            "currency": info.get("currency"),
            "marketCap": info.get("marketCap"),
            "previousClose": info.get("previousClose"),
            "open": info.get("open"),
            "dayHigh": info.get("dayHigh"),
            "dayLow": info.get("dayLow"),
            "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
            "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
            "volume": info.get("volume"),
            "website": info.get("website"),
            "exchange": info.get("exchange"),
        }

    except Exception as e:
        return {"error": f"Failed to fetch stock data: {str(e)}"}
    

@mcp.tool()
def save_code(code: str) -> str:
    """
    Expects a nicely formatted, working and executable python code as input in form of a string. 
    Save the given code to a file stock_analysis.py, make sure the code is a valid python file, nicely formatted and ready to execute.

    Args:
        code (str): The nicely formatted, working and executable python code as string.
    
    Returns:
        str: A message indicating the code was saved successfully.
    """
    try:
        with open('stock_analysis.py', 'w') as f:
            f.write(code)
        return "Code saved to stock_analysis.py"
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def run_code_and_show_plot() -> str:
    """
    Run the code in stock_analysis.py and generate the plot
    """
    with open('stock_analysis.py', 'r') as f:
        exec(f.read())

# Run the server locally
if __name__ == "__main__":
    mcp.run(transport='stdio')