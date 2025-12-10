print("Welcome to SuperMarket\n")
print("Our Shopping Items")

items = ["Apple   : $2.00", "Sugar   : $5.25", "Coffee  : $7.50", "Flour   : $4.25", "Biscuit : $3.00", "Mango   : $2.75"]

for item in items:
    print(f"* {item}")

count = input("\nHow Many items do you pick: ")
print()

if count.isdigit():
    count = int(count)
    if 1 <= count <= 6:
        x = 1
        y = 0
        total = 0
        while x <= count:
            name = input("Enter the name of your choice: ")
            if name.isdigit():
                print("Invalid Input. Enter the Name of the Choices")
                y = 1
                break
            else:
                if name == "Apple":
                    num = input("okay. How many do you buy: ")
                    if num.isdigit():
                        num = float(num)
                        item_total = float(2.00 * num)
                        total = total + item_total
                    else:
                        print("Invalid Input. Enter the Integer Values.")

                elif name == "Sugar":
                    num = input("okay. How many kilo do you buy: ")
                    if num.isdigit():
                        num = float(num)
                        item_total = float(5.25 * num)
                        total = total + item_total
                    else:
                        print("Invalid Input. Enter the Integer Values.")

                elif name == "Coffee":
                    num = input("okay. How many packets do you buy: ")
                    if num.isdigit():
                        num = float(num)
                        item_total = float(7.50 * num)
                        total = total + item_total
                    else:
                        print("Invalid Input. Enter the Integer Values.")

                elif name == "Flour":
                    num = input("okay. How many kilo do you buy: ")
                    if num.isdigit():
                        num = float(num)
                        item_total = float(4.25 * num)
                        total = total + item_total
                    else:
                        print("Invalid Input. Enter the Integer Values.")

                elif name == "Biscuit":
                    num = input("okay. How many packets do you buy: ")
                    if num.isdigit():
                        num = float(num)
                        item_total = float(3.00 * num)
                        total = total + item_total
                    else:
                        print("Invalid Input. Enter the Integer Values.")

                elif name == "Mango":
                    num = input("okay. How many do you buy: ")
                    if num.isdigit():
                        num = float(num)
                        item_total = float(2.75 * num)
                        total = total + item_total
                    else:
                        print("Invalid Input. Enter the Integer Values.")

                else:
                    print("Invalid Input. Enter the Correct Names of the PickUps")
                    y = 2
                    break
            x = x + 1
        if y == 0:
            print()
            print(f"Total Bill Amount: ${total}")

    else:
        print("Invalid Input. Enter the Number of PickUps")
else:
    print("Invalid Input. Enter the Number of PickUps")

