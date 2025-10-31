import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import timedelta
import warnings

warnings.filterwarnings("ignore")

# -----------------------------
# 🎯 App Title
# -----------------------------
st.set_page_config(page_title="Stock Price Forecasting", layout="wide")
st.title("📈 Stock Price Forecasting using ARIMA/SARIMA")
st.markdown("""
This app predicts **future stock prices** using classical **time-series models** — ARIMA and SARIMA.  
Enter a stock ticker below (e.g., `AAPL`, `GOOG`, `TSLA`) to generate forecasts.
""")

# -----------------------------
# 📥 User Input
# -----------------------------
ticker = st.text_input("Enter Stock Symbol:", "AAPL")
period = st.slider("Select forecast period (days):", min_value=7, max_value=90, value=30, step=1)

# -----------------------------
# 🧭 Data Fetching
# -----------------------------
st.subheader("📊 Fetching and Preparing Data...")
data = yf.download(ticker, start="2020-01-01")

if data.empty:
    st.error("❌ No data found. Please check the ticker symbol and try again.")
    st.stop()

# Reset index and ensure datetime
data.reset_index(inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Display last 5 entries
st.dataframe(data.tail())

# -----------------------------
# 📉 Plot Historical Prices
# -----------------------------
st.subheader("📉 Historical Closing Prices")
st.line_chart(data['Close'])

# -----------------------------
# 🔮 Forecasting with SARIMA
# -----------------------------
st.subheader(f"🔮 Forecasting Next {period} Days")

try:
    # Fit SARIMA model
    model = SARIMAX(data['Close'], order=(1,1,1), seasonal_order=(1,1,1,12))
    results = model.fit(disp=False)

    # Forecast for user-selected period
    forecast = results.forecast(steps=period)

    # Generate future date index
    future_dates = pd.date_range(start=data.index[-1] + timedelta(days=1), periods=period, freq='D')
    forecast = pd.Series(forecast.values, index=future_dates)

    # Combine historical + forecast
    combined = pd.concat([data['Close'], forecast.rename("Forecast")])

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data['Close'], label='Historical Prices', color='blue')
    ax.plot(forecast, label='Forecasted Prices', color='orange')
    ax.set_title(f"{ticker} - {period}-Day Forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()

    st.pyplot(fig)

    # -----------------------------
    # 🧾 Forecasted Values Table
    # -----------------------------
    st.subheader("🧾 Forecasted Price Data")
    forecast_df = pd.DataFrame({
        "Date": forecast.index.strftime("%Y-%m-%d"),
        "Predicted Price (USD)": forecast.values
    })
    st.dataframe(forecast_df.set_index("Date"))

except Exception as e:
    st.error(f"⚠️ Forecasting failed: {e}")

