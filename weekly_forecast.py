import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error

# -----------------------------
# 1. CONNECT TO DATABASE
# -----------------------------
engine = create_engine('mysql+pymysql://root:sojah@localhost/inventory')

# Load sales data
query = "SELECT SaleDate, SalesQuantity FROM fact_sales"
df = pd.read_sql(query, engine)

# Ensure datetime
df['SaleDate'] = pd.to_datetime(df['SaleDate'])

# -----------------------------
# 2. CREATE WEEKLY SALES DATA
# -----------------------------
weekly_sales = df.resample('W-MON', on='SaleDate').sum().reset_index()
weekly_sales.columns = ['ds', 'y']

# -----------------------------
# 3. DATA CLEANING FOR FORECAST
# -----------------------------
recent = weekly_sales[weekly_sales['ds'] >= '2024-04-01'].copy()

# Clip extreme outliers
recent['y'] = recent['y'].clip(lower=700000)

# Log-transform
recent['y_log'] = np.log1p(recent['y'])

# -----------------------------
# 4. TRAIN-TEST SPLIT
# -----------------------------
train = recent.iloc[:-4].copy()
test = recent.iloc[-4:].copy()

# Prophet requires ds + y
train_prophet = train[['ds', 'y_log']].rename(columns={'y_log': 'y'})

# -----------------------------
# 5. TRAIN PROPHET MODEL
# -----------------------------
model = Prophet(weekly_seasonality=True, daily_seasonality=False)
model.fit(train_prophet)

# -----------------------------
# 6. FORECAST NEXT 4 WEEKS
# -----------------------------
future = model.make_future_dataframe(periods=4, freq='W-MON')
forecast = model.predict(future)

# Convert predictions back to original scale
forecast['yhat_original'] = np.expm1(forecast['yhat'])

# -----------------------------
# 7. MATCH TEST WITH PREDICTIONS
# -----------------------------
pred = forecast[['ds', 'yhat_original']].tail(4)
merged = test.merge(pred, on='ds')

# -----------------------------
# 8. PERFORMANCE METRICS
# -----------------------------
y_true = merged['y']
y_pred = merged['yhat_original']

mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100

print("\n=== MODEL PERFORMANCE ===")
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)

# Save forecast
forecast.to_csv("forecast_output.csv", index=False)
print("\nForecast saved as forecast_output.csv")
