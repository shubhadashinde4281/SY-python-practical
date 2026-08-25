marks=[]
while True:
    print("\n Students Marks Managemen System")
    print("1.Inserts MARKS")
    print("2.Display Marks")
    print("3.Update Marks")
    print("4.Delete Marks")
    print("5.Exit")

    choice=int(input("Enter Your Choice:"))

    #insertion
    if choice==1:
        mark=int(input("Enter Students Marks:"))
        marks.append(mark)
        print("Marks inserted successfully.")

    #traversal
    elif choice==2:
        if len(marks)==0:
            print("No marks available")

        else:
            print("Students Marks")
            for i in range(len(marks)):
                print("student",i+1,":",marks[i])

    elif choice==3:
        student=int(input("Enter Student No to update:"))
        if 1<=student <=len(marks):
            new_mark=int(input("Enter New Marks:"))
            marks[student-1]=new_mark
            print("Marks updated successfully.")

        else:
            print("Invalid student no.")

    #deletion
    elif choice==4:
        student=int(input("Enter student No to delete:"))
        if 1<=student<=len(marks):
            marks.pop(student-1)
            print("Marks deleted successfully.")

        else:
            print("Invalid Studnt No.")

        #Exit

    elif choice==5:
        print("Program Ended.")

        break

    else:
        print("Invalid Choice.")


