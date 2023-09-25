
api_key = 'RV7XR1GtEaxvaqKPuWDomfMfq8ex95f0rjCsAQdSCSaSkWhhEnts1hQUKBQWH86O'
api_secret = 'JwvfW7vmjk17kt4fSXJG4aanN8QG3ZlRETv4IIjgXpbNeJSLPySodscgc6TDXUjS'

from binance.client import Client

client = Client(api_key, api_secret)

# Retrieve the account balance
balance = client.get_account()

# Print the balance
balancesList = []

for asset in balance['balances']:
    if float(asset['free']) > 0.0 or float(asset['locked']) > 0.0:
        balancesDict = {}
        balancesDict['asset'] = asset['asset']
        balancesDict['free'] = '{:.8f}'.format(float(asset['free']))
        balancesDict['locked'] = '{:.8f}'.format(float(asset['locked']))

        balancesList.append(balancesDict)

#print(balancesList[1]['free'])
#print(balancesList)

from binance.spot import Spot

currency_pairs = {
    "BTCUSDT": "Bitcoin",
    "ETHUSDT": "Ethereum",
    "ADAUSDT": "Cardano",
    "BNBUSDT": "Binance Coin",
    "DOTUSDT": "Polkadot",
    "XRPUSDT": "XRP",
    "SOLUSDT": "Solana",
    "LUNAUSDT": "Luna",
    "AVAXUSDT": "Avalanche",
    "ALGOUSDT": "Algorand"
}


def get_currency_price(pair):
    client = Spot()
    ticker = client.ticker_price(symbol=pair)
    price = float(ticker['price'])
    return price

for pair, name in currency_pairs.items():
    price = get_currency_price(pair)
    print(f"{name} price: {price}")