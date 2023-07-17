import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html

# Step 1: Fetch historical stock data
ticker = 'AAPL'
start_date = '2010-01-01'
end_date = '2021-12-31'

data = yf.download(ticker, start=start_date, end=end_date)

# Step 2: Data cleaning and preprocessing
# Remove unwanted columns
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

# Remove rows with missing values
data = data.dropna()

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data.index)

# Step 3: Data visualization
# Example 1: Line plot of stock prices over time using seaborn and matplotlib
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Date', y='Close')
plt.title('Stock Prices over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Example 2: Line plot of stock prices over time using Plotly Express
fig = px.line(data, x='Date', y='Close', title='Stock Prices over Time')
fig.show()

# Example 3: Interactive candlestick chart using Plotly Graph Objects and Dash
app = dash.Dash(__name__)

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                    open=data['Open'],
                                    high=data['High'],
                                    low=data['Low'],
                                    close=data['Close'])])

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
