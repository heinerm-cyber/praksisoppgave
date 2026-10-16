# Make Your Own Pizza - Price Calculator - www.101computing.net/build-your-own-pizza-price-calculator/

print("O-O-O-O-O-O-O-O-O-O-O-O")
print("|        BUILD        |")
print("O   YOUR OWN PIZZA    O")
print("|  PRICE CALCULATOR   |")
print("O-O-O-O-O-O-O-O-O-O-O-O")
print("")

# variabel til og lagre prisen på pizzaen mens du bestiller 
price = 0

print("Order a pizza in 5 easy steps:")

#printer ut det du kan velge mellom i første spørsmål
print("""We have three sizes of pizza:
    - Small (£6)
    - Medium (£8)
    - Large (£10)""")
#spør om hvilken størelse du vil ha 
size = input("Enter the size of your pizza: S, M or L?").upper()
#while løkke til og la deg prøve på nytt om du skriver feil 
while size not in ["S", "M", "L"]:
   print("Invalid option, please try again!")
   size = input("Enter the size of your pizza: S, M or L?").upper()
#if og elif til og besteme pricen på de forskjellige størelsene
if size=="S":
   price = price + 6
elif size=="M":
   price = price + 8
elif size=="L":
   price = price + 10
#printer den  pries du ligger på så lagt i bestilingen
print("Pizza price so far: £" + str(price))

# spør deg hvilken bunn du vil ha 
base = input("choose the base you would like on your pizza: classic crust, thin Crust or deep Pan?").lower()
while base not in ["classic crust", "thin crust", "deep pan"]:
   print("invalid option, please selcet again!")
   base = input("classic crust, thin crust or deep pan?").lower()
#if og elif til og besteme pricen på de forskjellige bunene
if base=="classic crust":
   price = price + 0
elif base=="thin crust":
   price = price + 1
elif base=="deep pan":
   price = price + 2

print("Pizza price so far: £" + str(price))


# liste med alle de forskjelige toppingene du kan velge mellom og prisen dies 
toppings = [("cheese", 1.50), ("pepperoni", 1.50), ("mushrooms", 1.50), ("onions", 1.50), ("pinnaple" , 1.50)]
# en for løkke så går gjennom ett og ett element i listen og spør deg om du vil ha en og en topping 
for topping, cost in toppings:
    choice = input("do you want " + topping + " yes or no?").upper()
    while choice not in ["YES", "NO"]:
        print("invalid option please selcet again!")
        choice = input("do you want " + topping + " yes or no?").upper()
#if og elif til og besteme svarene du kan svare på toppingene 
    if choice == "YES":
        price = price + cost
    elif choice == "NO":
        price = price + 0

    print("Pizza price so far: £" + str(price))

# spør deg om du vil ha takeaway
takeaway = input("do you want takeaway yes or no?").lower().strip()
while takeaway not in ["yes", "no"]:
   print("invalid option please selcet again!")
   takeway = input("do you want takeaway yes or no?").lower().strip()
#if og elif til og besteme pricen på om du vil eller om du ikke vil ha takeaway
if takeaway=="yes":
   price = price + 2
elif takeaway=="no":
   price = price + 0

print("Pizza price so far: £" + str(price))


# spør om du kan den hemmelie discount koden 
discount_code = input("Do you have a discount code? ").upper()
#if til og lage en hemmelig kode som bruker en float til og forminske total prisen med 20%/ganger total prisen med 0.8
if discount_code == "P1ZZ4":
    price = price * 0.8  
    print("Discount applied! You saved 20%.")
#printer ut total prisen
print("Final Pizza price: £" + str(price))