Trial Code:

expanses=0.0
while True:
    value=float(input("Enter A Value:"))
    if value==-1:
        break
    expanses=expanses+value 
    print(expanses)
-----------------------------------------------------------------------------------------

Practical No.5:


print("====Expanses====")
food=0
travel=0
shopping=0
total=0
other=0

while True:
    value=float(input("Enter Your Amount:"))
    if value==-1:
        break

    category=str(input("Enter a category(food/shopping/travel/others):")).lower()

    if category=="food":
        food=food+value

    elif category=="shopping":
        shopping=shopping+value
    elif category=="travel":
        ttravel=travel+value
    elif category=="other":
        other=other+value

total=food+shopping+travel+other
       


print("====Expenses summary====")
print("Food:",food)
print("Travel:",travel)
print("Shopping:",shopping)
print("Other",other)
print("Total",total)

