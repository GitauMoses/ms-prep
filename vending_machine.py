# Task 2 — The Vending Machine 🎰
# Build a vending machine function. It has a stock of items with prices. A user passes in an item and the amount they are paying. It should:

# Reject if item does not exist
# Reject if not enough money
# Dispense the item and return the change if payment is enough

pythonstock = {
    "coke":   {"price": 50,  "quantity": 3},
    "chips":  {"price": 30,  "quantity": 0},
    "water":  {"price": 20,  "quantity": 5},
}

def buy(item, money):
    # response = ''
    # if item in pythonstock.keys() and pythonstock[item]["quantity"] == 0 and money < pythonstock[item]["price"]:
    #     response = f"Sorry, chips is out of stock"
    # if item not in pythonstock.keys():
    #     response = f"Sorry, {item} does not exist"
    # if item in pythonstock.keys() and pythonstock[item]["quantity"] > 0 and money >= pythonstock[item]["price"]:
    #     pythonstock[item]["quantity"]-=1
    #     change = money - pythonstock[item]["price"]
    #     response = f"Dispensing {item}. Change is {change}"
    
    # if item in pythonstock.keys() and pythonstock[item]["quantity"] > 0 and money < pythonstock[item]["price"]:
    #     response = f"Sorry, not enough money"
    if item not in pythonstock.keys():
        response = f"Sorry, {item} does not exist"
    elif pythonstock[item]["quantity"] == 0:
        response = response = f"Sorry, chips is out of stock"
    elif money < pythonstock[item]["price"]:
        response = f"Sorry, not enough money"
    else:
         pythonstock[item]["quantity"]-=1
         change = money - pythonstock[item]["price"]
         response = f"Dispensing {item}. Change is {change}"



    print(response)

buy("coke", 100)   # Dispensing coke. Change: 50 .
buy("chips", 50)   # Sorry, chips is out of stock
buy("juice", 50)   # Sorry, juice does not exist .
buy("water", 10)   # Sorry, not enough money .