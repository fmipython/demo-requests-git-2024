import os

import requests
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("No Alpha Vantage API key provided!")


url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"from_currency": "BTC",
               "function": "CURRENCY_EXCHANGE_RATE", "to_currency": "USD"}

headers = {
	"x-rapidapi-key": API_KEY,
	"x-rapidapi-host": "alpha-vantage.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response.raise_for_status()

response_json = response.json()

price = float(response_json['Realtime Currency Exchange Rate']['5. Exchange Rate'])

print(f"Bitcoin price right now is: {price:.2f} USD")

print("Searching for latest news...")

url = "https://google-news13.p.rapidapi.com/search"

querystring = {"keyword": "bitcoin", "lr": "en-US"}

headers = {
	"x-rapidapi-key": API_KEY,
	"x-rapidapi-host": "google-news13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response_json = response.json()


urls: list[tuple[str, str]] = [
    (item["title"], item["newsUrl"]) for item in response_json["items"][:10]
]

print("\n".join(f"{title}: {url}" for title, url in urls))


