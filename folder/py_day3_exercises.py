print("----Exercise 1----")

students = ["joao","maria","antonio","josé","benjamin"]

for student in students:
    print(f"Student: {student}".title())

print("----Exercise 2----")
daily_expenses = [10, 50, 15, 5, 20]
total = 0

for daily_expense in daily_expenses:
    total = total + daily_expense
print(total)

print("----Exercise 3----")

n_list = range(1, 21)

for n in n_list:
    if n > 10:
        print(n)
    else:

        continue

print("----Exercise 4----")

cart = []

while True:
    answer = input("Add item (or type 'done')")
    if answer == "done":
        break
    else:
        cart.append(answer)
for item in cart:
    print(item.title())

print("----Exercise 5A----")
x = range(1, 6)
y = range(1, 6)

for x in range(1, 6):
    for y in range(1, 6):
        print(x*y, end="\t")

print("----Exercise 5B----")
x = range(1, 6)
y = range(1, 6)
for n in x:
    for o in y:
        print(n*o, end="\t")

print("----Exercise 5c----")
x = range(1, 6)
y = range(1, 6)
for n in x:
    for o in y:
        x.y = x*y
        print(x.y, end="\t")

range_rows = range(1, 6)
range_cols = range(1, 6)

print("----Exercise 5d----")
for x in range(1, 6):
    for y in range(1,6):
        product = x*y
        print(product, end="\t")
    print()

range_rows = range(1, 6)
range_cols = range(1, 6)

for row in range_rows:
    for col in range_cols:
        # Multiply current row number by current column number
        product = row * col
        # Use end="\t" to print in a tab-separated grid format
        print(product, end="\t")
    # Print a newline after each row is finished
    print()
