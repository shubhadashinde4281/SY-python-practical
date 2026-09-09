product_name=[]
product_price=[]

while True:
    print("***** PRODUCT INVENTORY SYSTEM *****")
    print("1. Insert Product ")
    print("2. Display Product ")
    print("3. Update Product ")
    print("4. Delete Product ")
    print("5. Search Product ")
    print("6. Sort Product ")
    print("7. Exit ")

    choice=int(input("Enter Your Choice: "))

    if choice==1:
        product=input("Enter Your Product :-")
        product_name.append(product)

        price=float(input("Enter Your Product Price :-"))
        product_price.append(price)
        print("Product Inserted Successfully.")

    elif choice==2:
        if len(product_name)==0:
            print("Product Is Not Available")
        else:
            print("Produts\t\tprice")
            for i in range(len(product_name)):
                print(product_name[i],"\t\t",product_price[i])

    elif choice==3:
        product2=input("Enter Product Name To Update :")
        if product2 in product_name:
            index=product_name.index(product2)
            new_price=int(input("Enter Updated Price :"))
            product_price[index] = new_price
            print("Product Updated Successfully")
        else:
            print("Product Not Found.")            

    elif choice==4:
        product3=input("Enter Product Name To Delete :")
        if product3 in product_name:
            index=product_name.index(product3)
            product_name.pop(index)
            product_price.pop(index)
            print("Product Deleted Successfully.")
        else:  
            print("Product Not Found.")  

    elif choice==5:
        product4=input("Enter Product Name To Search :")
        if product4 in product_name:
            index=product_name.index(product4)
            print("Product Is Found.")
            print("Product Name :", product_name[index])
            print("Product Price :", product_price[index])
        else:
            print("Product Is Not Found.")
       
    elif choice==6:
     for i in range(len(product_name)):
      for j in range(i+1,len(product_name)):       
            if product_name[i] > product_name[j]:
              product_name[i], product_name[j] = product_name[j], product_name[i]
              product_price[i], product_price[j] = product_price[j], product_price[i]
              print("Product Sorted Successfully.")
              print("product_name :", product_name)
              print("product_price :", product_price)
            
    elif choice==7:
        print("Thank You For Visiting Inventory System.")
        break

    else:
        print("Invalid Choice. Please Try Again...!")