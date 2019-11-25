

# taking two inputs at a time 


Area, DollarAmount = [int(x) for x in input("Enter two numbers here: ").split()]

print("Area: m^2", Area) 
print("Dollar Amount: $", DollarAmount) 

if Area>=50 and DollarAmount>=10000:
    print ("A")
elif Area<50 and DollarAmount>=10000:
    print ("B")
elif Area>=50 and DollarAmount<10000:
    print ("C")
elif Area<50 and DollarAmount<10000:
    print ("D")
else:
    print("F")

type(Area)



