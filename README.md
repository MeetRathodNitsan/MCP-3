# 📈 Financial Analyst MCP Tool

An AI-powered financial analysis agent using `yfinance` and MCP (`fastmcp`) to fetch and analyze stock data in real-time. Designed for seamless integration with local MCP servers and tools like CrewAI.

---

## 🚀 Features

- 📊 Real-time stock analysis using `yfinance`
- 🧠 Built-in AI tool interface via `@mcp.tool()`
- ⚡ Fast execution with [`uv`](https://github.com/astral-sh/uv)
- 📦 Structured JSON output for AI/LLM compatibility
- 🔒 Works in isolated environments with `.venv`

---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/financial-analyst-tool.git
   cd financial-analyst-tool
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the environment**
   - On **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install uv yfinance fastapi fastmcp pydantic
   ```

---

## 🧪 Run the Server

```bash
uv run server.py
```

> ✅ Make sure you run this inside the `.venv` where `yfinance` and `fastmcp` are installed.

---

## 🛠️ Tool Example

### Tool Signature

```python
@mcp.tool()
def analyze_stock(symbol: str) -> dict
```

### Example Usage (via MCP)

```json
{
  "tool": "analyze_stock",
  "args": {
    "symbol": "AAPL"
  }
}
```

### Example Response

```json
{
  "symbol": "AAPL",
  "longName": "Apple Inc.",
  "currentPrice": 192.31,
  "currency": "USD",
  ...
}
```

---

## 🔍 Dependencies

- [`yfinance`](https://pypi.org/project/yfinance/)
- [`fastmcp`](https://pypi.org/project/fastmcp/)
- [`uv`](https://github.com/astral-sh/uv)
- [`fastapi`](https://fastapi.tiangolo.com/)
- [`pydantic`](https://docs.pydantic.dev/)

