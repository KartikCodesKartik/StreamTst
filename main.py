import streamlit as st
import time
import requests
from bs4 import BeautifulSoup

def get_stock_price(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Adjust the selector to target the price element
    price = soup.select_one('.YMlKec.fxKbKc').text
    return price

if __name__ == "__main__":
    st.title("Real-Time Stock Price Dashboard")

    url = "https://www.google.com/finance/quote/IREDA:NSE"

    # Create a placeholder for dynamic updates
    price_placeholder = st.empty()

    while True:
        price = get_stock_price(url)
        price_placeholder.write(f"Current Price: {price}")
        time.sleep(60)  # Update every 60 seconds
