import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_price(coin_id):
    """Fetches the price of a cryptocurrency from the CoinGecko API."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes (HTTP errors like 404 or 500)
    price_data = response.json()
    return price_data[coin_id]['usd']

cyrpto_data = {'Name': [], 'Price': []}
frame = pd.DataFrame(cyrpto_data)  # Creates an empty DataFrame

def add_to_frame(name, coin_id, data_frame):
    """Adds a cryptocurrency's name and price to the DataFrame.

    Args:
        name (str): The display name of the cryptocurrency (e.g., "Bitcoin", "Ethereum").
        coin_id (str): The lowercase ID used for the API call (e.g. bitcoin, ethereum, xrp).
        data_frame (pd.DataFrame): The DataFrame to add data to.

    Returns:
        pd.DataFrame: The updated DataFrame.
    """
    try:
        price = get_price(coin_id)
        data_frame.loc[len(data_frame)] = [name, price]
        print(data_frame)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {name}: {e}")
    except KeyError as e:
        print(f"Error: Invalid coin ID or API response format for {name}. Key error: {e}")

    return data_frame

def plot_prices(data_frame):
    """Plots the price data on a bar graph."""
    if data_frame.empty:
        print("The DataFrame is empty. No data to plot.")
        return

    data_frame.plot(kind='bar', x='Name', y='Price')
    plt.xlabel('Cryptocurrency')
    plt.ylabel('USD Price')
    plt.title('Current Crypto Prices')
    plt.show()

# Example Usage:
frame = pd.DataFrame(cyrpto_data)

# Correct coin ids used
frame = add_to_frame("Bitcoin", "bitcoin", frame)
frame = add_to_frame("Ethereum", "ethereum", frame)
frame = add_to_frame("Dogecoin", "dogecoin", frame)

plot_prices(frame)
