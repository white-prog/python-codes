import requests

def currency_converter(val, currency_from, to_currency):
  
    # API URL with placeholders for API key and currencies
    api_url = "https://v6.exchangerate-api.com/v6/{YOUR_API_KEY}/latest/{currency_from}"


    # Replace placeholders with actual values
    api_url = api_url.format(YOUR_API_KEY="241c79441ac7e2ace4c2f756", currency_from=currency_from)

    response = requests.get(api_url)
    data = response.json()
    
    # Extract the exchange rate for the target currency
    exchange_rate = data['conversion_rates'][to_currency]

    # Calculate the converted amount
    converted_amount = val * exchange_rate

    return round(converted_amount,2)




def main():
    print("CURRENCY CONVERTER")
    value = int(input("Enter number : "))
    currency_from = input("Enter country code your money is in : ")
    currency_to = input("Enter country code to convert this money: ")
    try:
        currenc = currency_converter(value,currency_from,currency_to)
        print(f"{value} {currency_from} = {currenc} {currency_to}")
    except: 
        print("Recheck inputs")


if __name__ == "__main__":
    main()