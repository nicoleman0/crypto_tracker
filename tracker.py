import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_price(bitcoin):
    """fetches price of bitcoin from coingecko API"""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=" + bitcoin + '&vs_currencies=usd'
    response = requests.get(url)
    price_data = response.json()
    return price_data[bitcoin]['usd']

cyrpto_data = {'Name': [], 'Price': []}
frame = pd.DataFrame(cyrpto_data) # Creates empty dataframe using crypto_data

def add_to_frame(name, price, data_frame):
    """creates a DataFrame to display prices"""
    data_frame.loc[len(data_frame)] = [name, price] # Add the data as a row to the existing data frame
    print(data_frame)
    return data_frame

def plot_prices(data_frame):
    """plots the price data on a bar graph"""
    if data_frame.empty:
        print("The DataFrame is empty. No data to plot.")
        return

    data_frame.plot(kind='bar', x='Name', y='Price')
    plt.xlabel('Cryptocurrency')
    plt.ylabel('USD Price')
    plt.title('Current Crypto Prices')
    plt.show()


# Example Usage:
# Create a new Dataframe in the main area.
frame = pd.DataFrame(cyrpto_data)

# Add some data
frame = add_to_frame("bitcoin", get_price("bitcoin"), frame)
frame = add_to_frame("ethereum", get_price("ethereum"), frame)
frame = add_to_frame("dogecoin", get_price('dogecoin'), frame)

#plot prices, now the dataframe is passed in.
plot_prices(frame)
