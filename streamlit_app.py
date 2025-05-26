import streamlit as st
from utils import get_pipeline_from_llm, run_pipeline_for_prompt
from kite_utils import initialize_kite
import pandas as pd

st.set_page_config(page_title="Kite LLM Assistant", layout="wide")
st.title("📊 LLM-Powered Stock Assistant")
st.markdown("Ask any question over your holdings.")

kite = initialize_kite()

if kite:
    print("📦 Orders:", kite.orders())
    print("📊 Holdings:", kite.holdings())
    holdings = kite.holdings()

# Clean & transform data
df = pd.DataFrame(holdings)
df = df[["tradingsymbol", "quantity", "average_price", "last_price"]]
df["invested_value"] = df["quantity"] * df["average_price"]
df["current_value"] = df["quantity"] * df["last_price"]
df["pnl"] = df["current_value"] - df["invested_value"]
df["pnl_pct"] = (df["pnl"] / df["invested_value"]) * 100

# Format ₹ values
def format_currency(x):
    return f"₹{x:,.2f}"

df_display = df.copy()
df_display["invested_value"] = df_display["invested_value"].apply(format_currency)
df_display["current_value"] = df_display["current_value"].apply(format_currency)
df_display["average_price"] = df_display["average_price"].apply(format_currency)
df_display["last_price"] = df_display["last_price"].apply(format_currency)
df_display["pnl"] = df_display["pnl"].apply(format_currency)
df_display["pnl_pct"] = df["pnl_pct"].apply(lambda x: f"{x:.2f}%")

total_invested = round(sum(df["invested_value"]),2)
current_value = round(sum(df["current_value"]),2)
pnl = round(current_value - total_invested,2)

# Color-coded P&L
def color_pnl(val):
    try:
        return 'color: green' if float(val.replace("₹", "").replace(",", "")) > 0 else 'color: red'
    except:
        return ''

styled_df = df_display.style.applymap(color_pnl, subset=["pnl", "pnl_pct"])

# Display
st.subheader("Your Holdings")
st.dataframe(styled_df, use_container_width=True)

st.text(f"Total Invested Value: {total_invested}")
st.text(f"Current Value: {current_value}")
st.text(f"Overall P&L: {pnl}")


with st.spinner("🔍 Generating holdings report..."):
    pipeline_str = get_pipeline_from_llm(holdings)
    
st.subheader("🧱 Kite Holdings")
st.text(pipeline_str)

user_input = st.text_input("💬 Ask a question:")

if user_input: 
    st.subheader("📈 Feedback")
    results = run_pipeline_for_prompt(pipeline_str,user_input,holdings)
    st.text(results)
