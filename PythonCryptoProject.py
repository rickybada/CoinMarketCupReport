import requests
import json
import os
from datetime import datetime


class CoinmarketcapApi:
    def __init__(self):
        # Connection with CoinMarketCap
        self.url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        self.params = {"start": "1", "limit": "100", "convert": "USD"}
        self.headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": "23cec648-0793-43a2-8b60-23ddbde0f138",
        }

    def CurrencyDataRequestToday(self):
        # Executes an HTTP request to get data for the previous day
        today_response = requests.get(
            url=self.url, headers=self.headers, params=self.params
        ).json()
        return today_response["data"]


report = CoinmarketcapApi()

# Call the CurrencyDataRequestToday method
CurrenciesToday = report.CurrencyDataRequestToday()

# Returns the cryptocurrency with the highest volume in the last 24 hours
CryptoMaxVolume24h = max(CurrenciesToday, key=lambda x: x["quote"]["USD"]["volume_24h"])

# Generates a sorted tuple for cryptocurrencies that have had a percentage increase in the last 24 hours
SortedCurrencies = sorted(
    CurrenciesToday, key=lambda x: x["quote"]["USD"]["volume_24h"], reverse=True
)

Best10 = {}
# Adds the first 10 cryptocurrencies sorted by decreasing volume in US dollars to the dictionary
for Currency in SortedCurrencies[:10]:
    Best10[Currency["name"]] = Currency["quote"]["USD"]["volume_24h"]

Worst10 = {}
# Adds the last 10 cryptocurrencies sorted by decreasing volume in US dollars to the dictionary
for Currency in SortedCurrencies[-10:]:
    Worst10[Currency["name"]] = Currency["quote"]["USD"]["volume_24h"]

# Returns the sum of the amount of money needed to buy one unit of each of the top 20 cryptocurrencies
Money20Crypto = sum(
    [Currency["quote"]["USD"]["price"] for Currency in SortedCurrencies]
)

# Create a list of cryptocurrencies filtered for volume_24h > 76000000
FilterCrypto24 = [
    Currency
    for Currency in CurrenciesToday
    if Currency["quote"]["USD"]["volume_24h"] > 76000000
]
# Returns the sum of all cryptocurrencies in filter_crypto24
MoneyAllCrypto = sum(Currency["quote"]["USD"]["price"] for Currency in FilterCrypto24)

# Sorts cryptocurrencies by market capitalization
CurrenciesMarketcapToday = sorted(
    CurrenciesToday, key=lambda x: x["quote"]["USD"]["market_cap"], reverse=True
)[:20]

CurrenciesPricesToday = []
CurrenciesPricesYesterday = []

# Calculation of yesterday’s price
for Currency in CurrenciesMarketcapToday:
    PercentChange24h = Currency["quote"]["USD"]["percent_change_24h"]
    PriceToday = Currency["quote"]["USD"]["price"]
    CurrenciesPricesToday.append(PriceToday)
    PriceYesterday = PriceToday / (1 + (PercentChange24h / 100))
    CurrenciesPricesYesterday.append(PriceYesterday)

# % Profit/loss buying one of each top 20 Crypto both today and yesterday (assuming the same rank)
ValueWalletYesterday = sum(CurrenciesPricesYesterday)
ValueWalletToday = sum(CurrenciesPricesToday)

ProfitLossWallet = (
    (ValueWalletToday - ValueWalletYesterday) / ValueWalletYesterday
) * 100

# Define the file name
Filename = f'{datetime.now().strftime("CryptoMarketCupReport_%Y-%m-%d_%H-%M-%S")}.json'

# Define the file path
DestinationDir = os.path.join(os.path.expanduser(r"~\Desktop"), Filename)

# Check if the file already exists
if os.path.exists(DestinationDir):
    print(
        f"Successfully created file! <{Filename}>\nIt's located in the folder {DestinationDir}"
    )
else:
    # Creation of the dictionary with the information
    report = {
        f"1) Best volume 24h <{CryptoMaxVolume24h['name']}>": f"{CryptoMaxVolume24h['quote']['USD']['volume_24h']:.2f}",
        f"2) Best % increment 24h": f"{Best10}",
        f"2) Worst % increment 24h": f"{Worst10}",
        f"3) $ per Top 20 Crypto": f"{Money20Crypto:.2f}",
        f"4) $ per Crypto with 76.000.000 volume min threshold 24h": f"{MoneyAllCrypto: .2f}",
        f"5) Profit/loss timedelta = 1": f"{ProfitLossWallet: .2f}%",
    }

    # Writing the information to the JSON file
    with open(DestinationDir, "w") as f:
        json.dump(report, f, indent=4)

    print(
        f"Hi there!\nThis is a li'l recap of your JSON Crypto-Report, based on CoinMarketCap API.\n\nLet's get into "
        f"it!\n\n"
    )
    print(
        f"Successfully created file! <{Filename}>\nIt's located in the folder {DestinationDir}"
    )
    print(f"\n\n*** Start2impact Python Project, By Riccardo Badanai ***\n\n")
