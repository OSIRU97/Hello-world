cartItems = []
cartTotal = 0

def addItem(itemName, itemPrice):
    cartItems.append(itemName)
    return(itemPrice)

cartTotal += addItem("shirt", 200)
cartTotal += addItem("shirt", 200)
cartTotal += addItem("vest", 150)
cartTotal += addItem("socks", 100)
cartTotal += addItem("shirt", 200)
cartTotal += addItem("Trouser", 500)
cartTotal += addItem("shirt", 200)
cartTotal += addItem("Trouser", 500)
cartTotal += addItem("Jacket", 700)

cartSummary = dict((item,cartItems.count(item))for item in cartItems)

print(cartSummary)
print(cartTotal)

