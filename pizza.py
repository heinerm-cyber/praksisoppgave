# Make Your Own Pizza - Price Calculator - www.101computing.net/build-your-own-pizza-price-calculator/

print("O-O-O-O-O-O-O-O-O-O-O-O")
print("|        BUILD        |")
print("O   YOUR OWN PIZZA    O")
print("|  PRICE CALCULATOR   |")
print("O-O-O-O-O-O-O-O-O-O-O-O")
print("")

# Initialise a variable used to store the price of our pizza
price = 0

print("Order a pizza in 5 easy steps:")

# Step 1 - Pick a size
print("""We have three sizes of pizza:
    - Small (£6)
    - Medium (£8)
    - Large (£10)""")

size = input("Enter the size of your pizza: S, M or L?").upper()
while size not in ["S", "M", "L"]:
   print("Invalid option, please try again!")
   size = input("Enter the size of your pizza: S, M or L?").upper()

if size=="S":
   price = price + 6
elif size=="M":
   price = price + 8
elif size=="L":
   price = price + 10

print("Pizza price so far: £" + str(price))

# Step 2 - Choose a base


# Step 3 - Decide how many toppings you would like


# Step 4 - Eat in or Takeaway?


# Step 5 - Enter Discount Code



