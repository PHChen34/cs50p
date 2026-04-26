import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    num = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")



try:
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=6a56d23d5543276f97a0710bcd00820f643c091422aa3638e87d3a12e8ddf912"

    response = requests.get(url)
    a = response.json()

    
    price = float(a["data"]["priceUsd"])
    total = price * num

    print(f"${total:,.4f}")



except requests.RequestException:
    print("RequestException")
    sys.exit(1)

