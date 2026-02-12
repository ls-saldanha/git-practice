# A list of strings
users = ["Alice", "Bob", "Charlie"] 

# A list of numbers
prices = [10.50, 20.00, 5.00]

# The "Pythonic" way to loop
for user in users:
    print(f"Hello, {user}!") 
    # The variable 'user' automatically updates to the next item each time.
    
for user in range(3):
    print(f"Hi, {user}!") 
# Prints: 0, 1, 2, 3, 4 (Stops BEFORE the last number!)