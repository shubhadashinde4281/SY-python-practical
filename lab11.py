bus=[["A","A","A"],
      ["A","A","A"],
      ["A","A","A"]]


for i in range(3):
    print(bus[i])

print("Select Your Seat")

row=int(input("Enter Your Row Number:"))
seat=int(input("Enter Your Seat Number:"))

if bus [row-1][seat-1]=="A":
   bus [row-1][seat-1]="R"
   print ("Your Seat is Reserved")

else:
    print("Your Seat is already Reserved")

for i in range(3):
    print(bus[i])




