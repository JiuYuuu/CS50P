import sys
import requests

try:
    response = requests.get(" rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit()

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
print(f"${n * price:,.4f}")
