import sys
import requests

def main():
    # Check for command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Try to convert the argument to a float (number of Bitcoins)
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Make API request to CoinCap
    try:
        api_key = "YourApiKey"  # Replace with your CoinCap API key
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the request
        data = response.json()
        bitcoin_price = float(data['data']['priceUsd'])
    except requests.RequestException:
        sys.exit("Request failed")
    except KeyError:
        sys.exit("Failed to retrieve data from the API")

    # Calculate the total cost of the requested Bitcoins
    total_cost = num_bitcoins * bitcoin_price

    # Format the output with commas as thousands separators and four decimal places
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
