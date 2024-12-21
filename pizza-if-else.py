size=(input("Enter the size of the pizza do you want(s/m/l); "))
bill=0
if(size == 's' or size== 'S'):
    bill+=100
elif( size == "m" or size == "M"):
    bill+=200
else:
    bill+=300
want_pepperoni=(input("do you want pepperoni (yes/no); "))
if(want_pepperoni=="yes"):
    bill+=50
else:
    bill+=30
extra_cheese=(input("do you want cheese(yes/no)"))
if(extra_cheese=="yes"):
    bill+=20
print(f"this is your bill{bill}")

