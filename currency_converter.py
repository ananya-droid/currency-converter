# currency_converter.py
"""
A simple currency converter that converts USD to INR using the ExchangeRate-API.
This script demonstrates API integration, error handling, and user input.
"""

import requests

# It's good practice to keep configuration variables at the top
API_KEY = "07d63dc01f5b998d829cf628"
BASE_URL = "https://v6.exchangerate-api.com/v6/"

def convert_usd_to_inr(amount):
    """
    Converts a given amount of US Dollars (USD) to Indian Rupees (INR).
    Fetches the latest exchange rate from ExchangeRate-API.

    Args:
        amount (float): The amount in USD to convert.

    Returns:
        float: The converted amount in INR if successful.
        str: An error message if the conversion fails.
    """
    # Construct the full API endpoint URL
    url = f"{BASE_URL}{API_KEY}/latest/USD"
    
    try:
        # Attempt to fetch data from the API
        print("Fetching the latest exchange rate...")
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the JSON response
        data = response.json()
        conversion_rate = data['conversion_rates']['INR']

        # Calculate and return the converted amount
        return amount * conversion_rate

    except requests.exceptions.RequestException as e:
        return f"Network Error: Could not fetch exchange rate. {e}"
    except KeyError:
        return "Error: Unexpected data format received from the API."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def main():
    """Main function to run the currency converter."""
    print("💰 USD to INR Currency Converter\n")

    try:
        # Get user input
        usd_amount = float(input("Enter the amount in USD to convert: "))
        
        # Perform the conversion
        result = convert_usd_to_inr(usd_amount)

        # Check if the result is a number (success) or a string (error)
        if isinstance(result, float):
            print(f"\n✅ Conversion Successful!")
            print(f"${usd_amount:.2f} USD = ₹{result:.2f} INR")
        else:
            print(f"\n❌ {result}")

    except ValueError:
        print("❌ Invalid input. Please enter a numerical value (e.g., 50.99).")

# This standard Python idiom checks if this script is being run directly.
# If it is, it executes the main() function.
if __name__ == "__main__":
    main()