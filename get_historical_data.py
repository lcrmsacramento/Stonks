#importing Library
import yfinance as yf#setting the ticker 
hindpetro = yf.Ticker("MSFT")#Display stock information
hindpetro.info


#Display Dividends
hindpetro.dividends#Display Splits
hindpetro.splits

df = hindpetro.history(period="max")

import plotly.graph_objects as go
import pandas as pd

#Reseting the index
df = df.reset_index()#Converting the datatype to float
for i in ['Open', 'High', 'Close', 'Low']:
    df[i] = df[i].astype('float64')
'''
fig = go.Figure([go.Scatter(x=df['Date'], y=df['High'])])
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month",                                        
                 stepmode="backward"),
            dict(count=6, label="6m", step="month",  
                 stepmode="backward"),
            dict(count=1, label="YTD", step="year", 
                 stepmode="todate"),
            dict(count=1, label="1y", step="year", 
                 stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.show()

'''
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Low'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.show()

import chart_studio.tools as tls

tls.get_embed('https://plotly.com/~chris/1638')


'''
figure = go.Figure(
    data = [
        go.Candlestick(
            x = df.index,
            low = df['Low'],
            high = df['High'],
            close = df['Close'],
            open = df['Open'],
            increasing_line_color = 'green',
            decreasing_line_color = 'red'
        )
    ]
)
figure.show()'''
