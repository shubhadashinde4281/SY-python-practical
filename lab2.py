print("**********Grossary Shop Billing Calculator********")
rice_qty = float(input("Enter The Quantity Of rice(in kg):"))
rice_price_per_kg =50
rice_total = rice_qty * rice_price_per_kg


sugar_qty = float(input("Enter The Quantity Of rice(in kg):"))
sugar_price_per_kg = 40
sugar_total = sugar_qty * sugar_price_per_kg


oil_qty = float(input("Enter The Quantity Of Oil(in litre):"))
oil_price_per_litre = 120
oil_total = oil_qty * oil_price_per_litre


print("******BILL DETAILS******")

print("rice :",rice_total)
print("sugar :",sugar_total)
print("oil :",oil_total)

Total_Bill = rice_total+sugar_total+oil_total
print("Total Bill:",Total_Bill)

Discount = 0
if Total_Bill >=1000:

    print("Discount:",Discount)
    Discount = Total_Bill = 0.1

elif Total_Bill >= 500:
    Discount = Total_Bill = 0.05
    print("Discount :",Discount)
    
    
else:
    print("No Discount")
    
    Final_Bill = Total_Bill - Discount
    
    print("Final Bill:",Final_Bill)