import requests
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=5083c964fb82e7838ed2913a3c79ff6d10159117dd551a41813700b4aaf1be67")
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        pass

    value = price * amount
    print(f'${value:,.4f}')


if __name__ == "__main__":
    main()
