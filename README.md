**📈 Stock Price Forecasting using ARIMA and SARIMA**

  This project focuses on forecasting stock prices using time-series analysis techniques — specifically ARIMA (AutoRegressive Integrated Moving Average) and SARIMA (Seasonal ARIMA) models.

  It demonstrates how data science and statistical modeling can be used to predict future stock trends based on historical data fetched via the yfinance API.

**🎯 Objectives**

  Analyze historical stock price data

  Build ARIMA and SARIMA models for forecasting

  Compare and visualize model performance

  Evaluate forecast accuracy using standard metrics

**🧠 Features**

 📊 Data Collection from Yahoo Finance using yfinance

  🧹 Data Cleaning & Preprocessing with pandas

  🧮 Model Building using statsmodels (ARIMA & SARIMA)

  📉 Visualization of actual vs predicted prices using matplotlib

  📈 Model Evaluation with RMSE (Root Mean Squared Error)

  💻 Streamlit App for User-friendly interface to test any stock ticker
  

🧰 **Technologies Used**

  Tool / Library	Purpose
  
  Python :	Core programming language
  
  Pandas :	Data manipulation
  
  NumPy	 : Numerical computations
  
  Matplotlib :	Data visualization
  
  yfinance :	Stock market data extraction
  
  Statsmodels :	ARIMA & SARIMA modeling
  
  Scikit-learn :	Evaluation metrics
  
  Jupyter Notebook :	Interactive analysis environment
  
  Streamlit App : Web App interface

**🗂️ Project Structure**
Stock-Price-Forecasting/

├── app.py         # Streamlit app for interactive forecasts

├── stock_forecast.ipynb        # Jupyter Notebook (ARIMA/SARIMA analysis)

├── requirements.txt             # Dependencies

└── README.md                    # Project overview (this file)
            

**⚙️ Environment Setup:**

  1️⃣ Create a Virtual Environment
  python -m venv venv

  2️⃣ Activate It

  Windows:

  >> venv\Scripts\activate

  macOS / Linux:

  >> source venv/bin/activate

  3️⃣ Install Dependencies
   pip install -r requirements.txt

  4️⃣ Running the Streamlit App

    >> streamlit run app.py

    Then open your browser at the URL shown (usually http://localhost:8501).

    Features in the App:

     Enter any stock symbol (e.g., AAPL, TSLA, MSFT)

     View historical data and interactive charts

     Get 30-day price forecasts

    Download or screenshot forecast tables

    Then open stock_forecast.ipynb to view and execute the code.

**🧾 Sample Workflow**

1. Fetch stock data (e.g., AAPL, TSLA, GOOG)

2. Visualize price trends and autocorrelation plots

3. Fit ARIMA and SARIMA models

4. Forecast future prices

5. Plot predictions vs actual values

6. Calculate RMSE for accuracy comparison


**🚀 Future Enhancements**

  >> Integrate Sentiment Analysis from news or tweets.

  >> Compare with LSTM / Prophet models for deep learning approaches.

**👩‍💻 Author**

  Shreya Devanapalli
  
  Data Science Enthusiast | Machine Learning | Predictive Analytics

📫 LinkedIn Profile : www.linkedin.com/in/shreya-devanapalli

📂 GitHub Portfolio : https://github.com/Shreya-devanapalli

**🏁 Quick Summary**


  This project is an end-to-end demonstration of stock price forecasting using classical time-series models. It highlights the process of data-driven prediction, model evaluation, and result visualization — valuable skills for data analyst and machine learning roles.
