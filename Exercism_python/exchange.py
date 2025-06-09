amount = 127.5
denomination = 20
def get_leftover_of_bills(amount, denomination):
    return (amount % denomination)

print(get_leftover_of_bills(127.5, 20))

def get_number_of_bills(amount, denomination):
    return int(amount / denomination)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    print('adjusted_rate', adjusted_rate)
    return (int(((budget/denomination) // (exchange_rate+((exchange_rate * spread)/100))))*denomination )

print(exchangeable_value(127.25, 1.20, 10, 5))
print(exchangeable_value(127.25, 1.20, 10, 20))

""" budget/denomination makes no sense: you're dividing the budget by denomination before conversion.

You're doing floor division // too early in the wrong place.

You are not calculating how much foreign currency the budget gets you properly.

✅ Correct version:
python
Copy
Edit
def exchangeable_value(budget, exchange_rate, spread, denomination):
    adjusted_rate = exchange_rate * (1 + spread / 100)
    total_foreign_currency = budget / adjusted_rate
    full_units = int(total_foreign_currency // denomination)
    return full_units * denomination
🧪 Example:
python
Copy
Edit
exchangeable_value(127.5, 1.2, 10, 20)
Adjusted rate: 1.2 * 1.10 = 1.32

Foreign currency: 127.5 / 1.32 = 96.59...

Full denominations of 20: 96.59 // 20 = 4

Final return: 4 * 20 = 80

✅ Correct output: 80 """