library={}

while True:
    print("1.Store Data")
    print("2.Update Data")
    print("3.Exit")

    choice = int(input("Enter Your choice: "))

    if choice==1:
         book_id = int(input("Enter your book id: "))
         
         book_name=input("Book name:")

         author_Name=input("Enter Your Author Name:")

         book_price=float(input("Enter Your Price:"))

         library[book_id]={"Name":book_name , "Author":author_Name , "Price":book_price}
         print(library)

         print("Books Added Successfully..")


    elif choice==2:
         
         book=input("Enter Your Book Id to update :")

         if book_id in library:
              book_name=("Enter New Book Name:")
              author_Name=("Enter New Author Name:")
              book_price=("Enter New Book Price:")

              
              


         
         