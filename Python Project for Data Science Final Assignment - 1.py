#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance')
#!pip install pandas
#!pip install requests
get_ipython().system('pip install bs4')
#!pip install plotly


# In[4]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[5]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# # Question 1 - Extracting Tesla Stock Data Using yfinance 

# In[6]:


Tesla = yf.Ticker('TSLA')


# In[7]:


tesla_data = Tesla.history(period = "max")


# In[8]:


tesla_data.reset_index(inplace = True)
tesla_data.head()


# # Question 2 - Extracting Tesla Revenue Data Using Webscraping 

# In[11]:


url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text


# In[12]:


soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')


# In[14]:


tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# In[15]:


tesla_revenue.tail()


# # Question 3: Extracting GameStop Stock Data Using yfinance

# In[16]:


GameStop = yf.Ticker("GME")


# In[17]:


gme_data = GameStop.history(period = 'max')


# In[18]:


gme_data.reset_index(inplace = True)
gme_data.head()


# # Question 4: Extracting GameStop Revenue Data Using Webscraping

# In[19]:


url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text


# In[20]:


soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')


# In[22]:


tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
gme_revenue.tail()


# # Question 5. Tesla Stock and Revenue Dashboard 

# In[23]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# # Question 6. GameStop Stock and Revenue Dashboard

# In[25]:


make_graph(gme_data, gme_revenue, 'GameStop')

