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
base = input("choose the base you would like on your pizza: classic crust, thin Crust or deep Pan?")
while base not in ["classic crust", "thin crust", "deep pan"]:
   print("invalid option, please selcet again!")
   base = input("classic crust, thin crust or deep pan?")

if base=="classic crust":
   price = price + 0
elif base=="thin crust":
   price = price + 1
elif base=="deep pan":
   price = price + 2

print("Pizza price so far: £" + str(price))


# Step 3 - Decide how many toppings you would like
toppings = [("cheese", 1.00), ("pepperoni", 1.50), ("mushrooms", 1.00), ("onions", 0.75), ("pinnaple" , 0.5)]

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
takeaway = input("do you want takeaway yes or no?")
while takeaway not in ["Yes", "No"]:
   print("invalid option please selcet again!")
   takeway = input("do you want takeaway yes or no?")

if takeaway=="Yes":
   price = price + 2
elif takeaway=="No":
   price = price + 0

print("Pizza price so far: £" + str(price))


# Step 5 - Enter Discount Code
discount_code = input("Do you have a discount code? ").upper()

if discount_code == "P1ZZ4":
    price = price * 0.8  
    print("Discount applied! You saved 20%.")

print("Final Pizza price: £" + str(price))