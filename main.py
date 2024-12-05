import os

import requests
import dotenv

dotenv.load_dotenv()

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

if not ALPHA_VANTAGE_API_KEY:
    raise ValueError("No Alpha Vantage API key provided!")


url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"from_currency": "BTC",
               "function": "CURRENCY_EXCHANGE_RATE", "to_currency": "USD"}

headers = {
	"x-rapidapi-key": ALPHA_VANTAGE_API_KEY,
	"x-rapidapi-host": "alpha-vantage.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response.raise_for_status()

response_json = response.json()

price = float(response_json['Realtime Currency Exchange Rate']['5. Exchange Rate'])

print(f"Bitcoin price right now is: {price:.2f} USD")
