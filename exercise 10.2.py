
products = ["Laptop", "Mobile", "Keyboard", "Mouse", "Printer"]

item = input("Enter product name to search: ")

if item in products:
    index = products.index(item)
    print("Item found!")
    print("Product:", item)
    print("Index location:", index)
else:
    print("Item not found in inventory.")