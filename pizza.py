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
pizza_sizes = {
   "S": 6,
   "M": 8,
   "L": 10
}


while size not in pizza_sizes:
   print("Invalid option, please try again!")
   size = input("Enter the size of your pizza: S, M or L?").upper()

price = price + pizza_sizes[size]

print("Pizza price so far: £" + str(price))

# Step 2 - Choose a base
base = input("choose the base you would like on your pizza: classic crust, thin Crust or deep Pan?").lower()

pizza_base = {
    "classic crust":0,
    "thin crust":1,
    "deep pan":2
}

while base not in ["classic crust", "thin crust", "deep pan"]:
   print("invalid option, please selcet again!")
   base = input("classic crust, thin crust or deep pan?").lower()

price = price + pizza_base[base]

print("Pizza price so far: £" + str(price))


# Step 3 - Decide how many toppings you would like
toppings = [("cheese", 1.50), ("pepperoni", 1.50), ("mushrooms", 1.50), ("onions", 1.50), ("pinnaple" , 1.50)]

for topping, cost in toppings:
    choice = input("do you want " + topping + " yes or no?").upper()
    while choice not in ["YES", "NO"]:
        print("invalid option please selcet again!")
        choice = input("do you want " + topping + " yes or no?").upper()

    if choice == "YES":
        price = price + cost
    elif choice == "NO":
        price = price + 0

    print("Pizza price so far: £" + str(price))

# Step 4 - Eat in or Takeaway?
takeaway = input("Do you want takeaway yes or no? ").strip().lower()

takeaway_options = {
    "yes": 2,
    "no": 0
}

while takeaway not in takeaway_options:
    print("Invalid option, please select again!")
    takeaway = input("Do you want takeaway yes or no? ").strip().lower()

price = price + takeaway_options[takeaway]

print("Pizza price so far: £" + str(price))

# Step 5 - Enter Discount Code
discount_code = input("Do you have a discount code? ").upper()

secret_discount = {
    "P1ZZ4" * 0.8
}

print("Final Pizza price: £" + str(price))

