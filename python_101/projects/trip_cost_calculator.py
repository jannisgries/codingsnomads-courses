# Kilometers to drive
km = float(input("How many kilometers do you plan to drive? (type just the number): "))
# Liters-per-kilometer usage of the car
consumption_rate = float(input("How many liters is your car using per km (just type the number): "))
# Price per liter of fuel
price_per_liter = float(input("How much did a liter of fuel cost?"))

result = km * consumption_rate * price_per_liter
print(result)