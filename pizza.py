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


print("""We have three sizes of pizza:
    - Small (£6)
    - Medium (£8)
    - Large (£10)""")

#input som spør deg hvilken størelse du vil ha 
size = input("Enter the size of your pizza: S, M or L?").upper()
#dictionary som lagrer valgene og prisene til de forskjelige disse dictionaryene er i alle spørsmålene i koden
pizza_sizes = {
   "S": 6,
   "M": 8,
   "L": 10
}

#while løkke som lar deg prøve om igjen vis du skriver feil 
while size not in pizza_sizes:
   print("Invalid option, please try again!")
   size = input("Enter the size of your pizza: S, M or L?").upper()

price = price + pizza_sizes[size]

print("Pizza price so far: £" + str(price))

# input som spør deg om bunen du vil ha 
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


#en liste med alle toppingene 
toppings = [("cheese", 1.50), ("pepperoni", 1.50), ("mushrooms", 1.50), ("onions", 1.50), ("pinnaple" , 1.50)]

#en for løkke som går gjennom alle toppingene i listen og spør deg om hvilke av de du vil ha med ja eller nei spørsmål
for topping, cost in toppings:
    choice = input("do you want " + topping + " yes or no?").upper()
    while choice not in ["YES", "NO"]:
        print("invalid option please selcet again!")
        choice = input("do you want " + topping + " yes or no?").upper()
#if og elif til og velge om du vil ha en topping eller ikke 
    if choice == "YES":
        price = price + cost
    elif choice == "NO":
        price = price + 0

    print("Pizza price so far: £" + str(price))

#spør deg om du vil ha takeaway eller ikke
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

# spør deg om du har en kode som kan forminske total prisen med 20%
discount_code = input("Do you have a discount code? ").upper()

#dictionary med en hemmelig kode som bruker en float til og gange prisen med 0.8/forminske prisen med 20% vis du kan koden
secret_discount = {
    "P1ZZ4" * 0.8
}
#printer ut prisen av alle valgene dine til slutt 
print("Final Pizza price: £" + str(price))

