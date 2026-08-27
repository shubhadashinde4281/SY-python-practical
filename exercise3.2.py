
percentage = float(input("Enter graduation percentage: "))
backlog = input("Do you have any active academic backlog? (yes/no): ").lower()

if percentage >= 70 and backlog == "no":
    print("\nCongratulations!")
    print("You are eligible for placement.")
else:
    print("\nSorry!")
    print("You are not eligible for placement.")