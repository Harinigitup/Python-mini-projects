print("currency converter")
print("US Dollar-USD, British Pound-BP, Australian Dollar-AUD, Canadian Dollar-CAD, Singapore Dollar-SGD, Swiss Franc-CHF, Malaysian Ringgit-MYR, Japanese Yen-JPY, Chinese Yuan Renminbi-CNY")

def currency_converter(amount, from_currency, to_currency, exchange_rates):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return "Invalid currency code."

# Example exchange rates (replace with actual rates)
exchange_rates = {'USD': 0.012031, 'BP': 0.009481, 'AUD': 0.017721, 'CAD': 0.015950, 'SGD': 0.015926, 'CHF': 0.010316, 'MYR': 0.055727, 'JPY': 1.713309, 'CNY': 0.085804}

# Example usage
amount_to_convert = float(input("Enter the amount you want to convert: "))
from_currency_code = input("Enter the source currency code to convert from: ")
to_currency_code = input("Enter the target currency code: ")
from_currency_code=from_currency_code.upper() 
to_currency_code=to_currency_code.upper()
result = currency_converter(amount_to_convert, from_currency_code, to_currency_code, exchange_rates)
print(f"{amount_to_convert} {from_currency_code} is equal to {result:.2f} {to_currency_code}")
