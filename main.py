import requests
url = 'https://data.fixer.io/api/latest?access_key=7370ff2962d49abefc56c32f5bc74aa8'

def currency_conversion():
    from_currency = input('From currency: ')
    to_currency = input('To currency: ')
    amount = int(input('Amount: '))
    response = requests.get(url)
    rate = response.json()['rates'][from_currency]
    amount_in_EUR = amount/rate
    amount = amount_in_EUR*(response.json()['rates'][to_currency])
    amount = round(amount, 2)
    print(amount)
    again = input('Again? Y/N: ')
    if again == 'Y':
        currency_conversion()

currency_conversion()