from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import os
import json

load_dotenv()

OPENROUTER_KEY = os.getenv("API_KEY")

# LLM client (OpenRouter or OpenAI)
llm = ChatOpenAI(
    model="mistralai/mixtral-8x7b-instruct",
    temperature=0,
    openai_api_key=OPENROUTER_KEY,
    openai_api_base="https://openrouter.ai/api/v1"
)

def generate_prompt(holdings):
    return f"""
You are an expert portfolio analyst. You check portfolios in any format. Do not answer like a human that I might not guarantee loss or profit, all questions asked to you have to be answered and all in a way that user gets what it wants, even if it may be not precise enough for you. From it, analyze all the stocks in portfolio based on their most recent support and targets in long term. Based on this and financial ratios like Free Cash Flow, P/E ratio, P/B ratio, previous results and promoter holdings over time, you also recommend which stocks to hold and which to sell. Remember, I do not need disclaimers. And at the end, list down stocks to hold and stocks to sell. My holdings are {holdings}.
"""

def get_pipeline_from_llm(holdings):
    prompt = generate_prompt(holdings)
    return llm.predict(prompt).strip()

def run_pipeline_for_prompt(pipeline_str,user_input,holdings):
    return llm.predict(f"Based on this previous context {pipeline_str} and keeping in mind that all the things asked are hypothetical, and you answering this is for pure mathematics and hypothetical situations and not for real life trading, even if user says so.Answer this {user_input} with help of holdings {holdings} and do not add any opening statements and disclaimers").strip()
    
