print("---- Exercise 1 ----")
my_profile = {
    "first_name": "[First]",
    "last_name": "[Last]", 
    "age": "[Age]", 
    "city": "[City]"}

print(f"My name is {my_profile['first_name']}")

print("---- Exercise 2 ----")
server = {"host_name": "web-01", "status": "offline"}
print(server)

server["status"] = "active"
server["ip_adress"] = "192.168.1.5"
print(server)

print("---- Exercise 3 ----")
stock = {"apples": 10, "bananas": 5, "oranges": 0}
for item, quantity in stock.items():
    if quantity > 0:
        print(f"{item} is in stock")
    if quantity == 0:
        print(f"{item} is OUT of stock")

print("---- Exercise 4 ----")
transactions = [
    {"item": "Laptop", "price": 1000}, 
    {"item": "Mouse", "price": 20}, 
    {"item": "Monitor", "price":150}]

total = 0

for transaction in transactions:
    total = total + transaction['price']
    print(total)
print(total)

print("----Exercise 5----")
employees = [
    {"name": "Alice", "role": "Engineer"},
    {"name": "Bob", "role": "Manager"},
    {"name": "Charlie", "role": "Engineer"}
]
for employee in employees:
    if employee['role'] == "Engineer":
        print(employee['name'])

#Week 2 Day 2
print("---- Exercise 1 ----")

scores = [50, 10, 90, 30, 70, 20]
scores.sort()
print(scores[3:6])

print("---- Exercise 2 ----")

inputs =["clean", "clean", "DIRTY", "clean", "DIRTY"]
inputs.pop(2)
inputs.pop(3)
print(inputs)

#or

print("---- Exercise 2 ----")

inputs =["clean", "clean", "DIRTY", "clean", "DIRTY"]
for input in inputs:
    inputs.remove("DIRTY")
    while "DIRTY" in inputs:
        continue

print(inputs)