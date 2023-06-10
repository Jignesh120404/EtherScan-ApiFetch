import csv
import requests
def get_ethereum_balance(address, api_key):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "1":
        balance = int(data["result"]) / 10 ** 18  # Convert balance from Wei to Ether
        return balance
    else:
        error_message = data["message"]
        raise ValueError(f"Error retrieving balance for address {address}: {error_message}")


with open('Filter1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    api_key = "5QHUUSBY5GHZ63SA3Q4SRJI7CIQMYRNNXX"
    for row in csv_reader:
        address = row[0]  # Assuming the address is in the first column
        try:
            balance = get_ethereum_balance(address, api_key)
            print(f"Address: {address}")
            print(f"Balance: {balance} ETH")
            print("---------------------------")
        except ValueError as e:
            print(str(e))
            print("---------------------------")
