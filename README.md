# KiteGPT

KiteGPT is a Streamlit-based AI assistant that integrates with Zerodha's Kite Connect API and uses LLMs (like Mixtral via OpenRouter) to let you analyze your portfolio, query customer data, and make insights-driven decisions — all using **natural language**.

---

## 🚀 Features

- 🔐 **Zerodha Kite login** with auto token caching
- 📊 **Live holdings dashboard** with P&L and color-coded gain/loss
- 🤖 **Natural language queries** over customer order data using LLMs (LangChain + MongoDB)
- 🧠 Supports custom portfolio logic (strategy tags, symbol filters, etc.)
- 📁 Modular design: clean separation of Streamlit UI and business logic

---

## 🧰 Tech Stack

- 🧠 [LangChain](https://github.com/langchain-ai/langchain) (LLM integration)
- 🧾 [KiteConnect](https://github.com/zerodhatech/pykiteconnect) (Zerodha API)
- 🌐 [OpenRouter](https://openrouter.ai) for cost-effective access to GPT-4/Mixtral
- 💻 Streamlit for interactive UI

---

## 🧪 Setup Instructions

1. **Clone this repo**:
   ```bash
      git clone https://github.com/Jayneet123/KiteGPT.git
      cd KiteGPT
   ```
   
2. **Install Dependencies**
  ```bash
     pip install -r requirements.txt
```

3. **Create .env with your API keys:**
  ```bash
   KITE_API=your_kite_api_key
   KITE_API_SECRET=your_kite_api_secret
   OPENAI_API_KEY=your_openrouter_api_key
  ```

4. **Start the app:**
  ```bash
     streamlit run streamlit_app.py
  ```

First-time login:

Terminal will show a 🔗 Kite login URL

Login manually and paste the request_token when prompted

The access token will be saved in kite_token.json (auto reused later)

 
