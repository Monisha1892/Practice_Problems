weight = float(input("enter your weight: "))
unit = input("enter L for pounds or K for Kg: ")

if unit.upper() == 'L':
    print("weight in kg is: ", (weight*0.45))
elif unit.upper() == 'K':
    print("weight in lbs is: ", (weight*2.205))
else:
    print("invalid unit")