product_name = []
product_price = []

while True:
    print("\n1. Add Product")
    print("2. Display Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Sort")
    print("7. Exit")

    choice = int(input("Enter Your choice: "))

    # Add Product
    if choice == 1:
        product = input("Enter Product Name: ")
        product_name.append(product)

        price = int(input("Enter a price: "))
        product_price.append(price)

        print("Product inserted successfully.")

    # Display Product
    elif choice == 2:
        if len(product_name) == 0:
            print("Product is not available.")
        else:
            print("\nProduct\tPrice")
            for i in range(len(product_name)):
                print(product_name[i], "\t", product_price[i])

    # Update Product
    elif choice == 3:
        product2 = input("Enter Your Product Name to Update: ")

        if product2 in product_name:
            index = product_name.index(product2)

            new_name = input("Enter New Product Name: ")
            new_price = int(input("Enter New Price: "))

            product_name[index] = new_name
            product_price[index] = new_price

            print("Product updated successfully.")
        else:
            print("Product not found.")

    # Delete Product
    elif choice == 4:
        product3 = input("Enter Product Name to Delete: ")

        if product3 in product_name:
            index = product_name.index(product3)

            product_name.pop(index)
            product_price.pop(index)

            print("Product deleted successfully.")
        else:
            print("Product not found.")

    # Search Product
    elif choice == 5:
        product4 = input("Enter Product Name to Search: ")

        if product4 in product_name:
            index = product_name.index(product4)

            print("Product Found")
            print("Product:", product_name[index])
            print("Price:", product_price[index])
        else:
            print("Product not found.")

    # Sort
    elif choice == 6:
        if len(product_name) == 0:
            print("Product is not available.")
        else:
            for i in range(len(product_name)):
                for j in range(i + 1, len(product_name)):
                    if product_name[i] > product_name[j]:
                        product_name[i], product_name[j] = product_name[j], product_name[i]
                        product_price[i], product_price[j] = product_price[j], product_price[i]

            print("Products sorted successfully.")

            print("\nProduct\tPrice")
            for i in range(len(product_name)):
                print(product_name[i], "\t", product_price[i])

    # Exit
    elif choice == 7:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
