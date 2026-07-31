print("===========Trafic Signal Rule===========")

signal=input("Enter The Signal Color:red/yellow/green:").lower()
if signal=="red":
    print("action : stop")
    
elif signal=="yellow":
    print("action:wait")
    
elif signal=="green":
    print("action:go")

else:("Invalid Color ! red,yellow or green.")

