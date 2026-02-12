#Exercise 1
age = int(input("Provide your age:"))

if age >= 18:
    print("Entry granted.")
else:
    print("You are too young to enter.")
    
#Exercise 2
cpu_usage = int(input("Provide your CPU usage at the moment of the error:"))
if cpu_usage >= 90:
    print("High Load! Scaling up.")
elif 50 <= cpu_usage <= 90:
    print("Moderate Load.")
elif cpu_usage <= 50:
    print("Normal.")

#Exercise 3
while True:
    username = input("Provide your username:")
    if username == "admin":
        password = input("Provide your password:")
        if password == "1234":
            print("Login Successful.")
            break  # Exit loop on success
        else:
            print("Invalid password, try again.")
    else:
        print("Unknown user, please try again")

#Exercise 4
print("--- Exercise 4 ---")

order_amount = float(input("Provide your order amount:"))
if order_amount >= 100:
    print("You got free shipping!")
if 50 <= order_amount <= 99: #same doubt as the last one, which is the more accurate one elif or if?
    print("The shipping will be $5.")
if order_amount <= 50:
    print("Shipping will be $10") 


input_answer = input("Are you a member?").lower().strip()
if input_answer == "yes" or input_answer == "y": #why do i need == and not = ?
    member = True
    print("You got free shipping!") #and if i wanted to adjust for the answer to be anything that contains yes?
else:
    print("You're not a member, so shipping will cost you, you can become a member and gain free shipping bonus!")

print("---- Exercise 5 ----")

number = int(input("Please insert a number"))
if number % 15 == 0:
    print("FizzBuzz")
    
elif number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")

