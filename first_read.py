#read data
with open("message.txt", "r") as f:
    content = f.read()
    print(content)

print("---- Review-exercise 1 ----")
high_value = []
transactions = [50, 120, 15, 200, 90, 10]

for t in transactions:
    if t > 100:
        high_value.append(t)
print(high_value)

print("---- Review-exercise 2 ----")

staff = [
    {"name": "Alice", "dept": "Sales"},
    {"name": "Bob", "dept": "HR"},
    {"name": "Charlie", "dept": "Sales"},
    {"name": "Diana", "dept": "HR"}
]
hr_count = 0

for s in staff:
    if s['dept'] == 'HR':
        hr_count = hr_count + 1
print(f"total HR employees: [{hr_count}]")

print("---- Review-exercise 3 ----")

logs = [
    "INFO: System boot",
    "ERROR: Disk full",
    "INFO: User login",
    "ERROR: Connection lost",
    "INFO: Email sent"
]
with open("daily_log.txt", "a") as dl:
   dl.write("User Admin logged in.\n")
   dl.write("User Guest logged in.\n")

with open("filtered_errors.txt", "w") as filt_error:
    for log in logs:
        if log["ERROR".exist()]:
        filt_error.write("")

print("---- Review-exercise 3 ----")

logs = [
    "INFO: System boot",
    "ERROR: Disk full",
    "INFO: User login",
    "ERROR: Connection lost",
    "INFO: Email sent"
]

with open("filtered_errors.txt", "w") as filt_error:
    for log in logs:
        if log == "ERROR":
            filt_error.write(f"{log} \n")