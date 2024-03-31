menu = {"1": 15, "2": 20, "3": 50 , "4": 40}
bill = {}
while (True):
    print("0. Generate Bill\n1. tea\n2. coffee\n3. pasta\n5. maggie")
    ch = input("->  ")
    if ch == "0":
        break
    price = menu.get(ch)
    quantity = int(input("enter quantity -> "))
    menu_bill = {f"{ch} x {quantity}":quantity*price}
    bill.update(menu_bill )
print(bill)