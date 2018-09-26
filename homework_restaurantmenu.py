
menu = {}

while True:
    dish = raw_input("What dish would you like to offer today?")
    price = raw_input("How much should it cost?")
    menu[dish] = price

    new = raw_input("Would you like to enter another dish? Please type yes or no; ")

    if new.lower() == "yes":
        continue
    if new.lower() == "no":
        break

with open("menu.txt", "w+") as f:
    for dish in menu:
        f.write("%s, %s EUR\n" % (dish, menu[dish]))

print "Thank you!"