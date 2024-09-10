#Password Generator Project
import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
'''
password = ""
for char in range(1, nr_letters + 1 ):
    password += random.choice(letters)

for symb in range(1, nr_symbols + 1 ):
    password += random.choice(symbols)

for num in range(1, nr_numbers + 1 ):
    password += random.choice(numbers)

print(password)
'''
#hard level
password = []
for char in range(1, nr_letters + 1 ):
    password.append(random.choice(letters))

for symb in range(1, nr_symbols + 1 ):
    password.append(random.choice(symbols))

for num in range(1, nr_numbers + 1 ):
    password.append(random.choice(numbers))


random.shuffle(password)
#print(password)

pass_items = len(password)
gen_pass = ""
for i in password:
    gen_pass += i
print(f"GENERATED PASSWORD IS = {gen_pass}")







