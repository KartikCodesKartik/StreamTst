import streamlit as st
import time
import requests
from bs4 import BeautifulSoup

def get_stock_price(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Adjust the selector to target the price element
        price = soup.select_one('.YMlKec.fxKbKc')
        if price:
            return price.text
        else:
            return None
    except Exception as e:
        return None

if __name__ == "__main__":
    st.title("Real-Time Stock Price Dashboard")

    # User input for the stock ticker
    stock_ticker = st.text_input("Enter Stock Ticker (e.g., IREDA:NSE):", "")
    
    if stock_ticker:
        # Construct the URL based on user input
        url = f"https://www.google.com/finance/quote/{stock_ticker}:NSE"

        # Create a placeholder for dynamic updates
        price_placeholder = st.empty()

        while True:
            stock_price = get_stock_price(url)
            if stock_price:
                price_placeholder.write(f"Current Price of {stock_ticker}: {stock_price}")
            else:
                price_placeholder.write("Didn't find any stock of this name.")
            time.sleep(2)  # Update every 2 seconds
