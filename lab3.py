marks = float(input("Enter your marks (%):"))
age = int(input("Enter your age:"))

if 17 <= age <= 25:
    if marks >=60:
         print("Congratulations! You are eligible for admission.")
         
         
        
    else:
        print("Sorry! You Are Not Eligible because your marks are below 60%.")
          
          
else:
    print("Sorry! You Are Not Eligible because your age is below 17 or your age is above 25.")     