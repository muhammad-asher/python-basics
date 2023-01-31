# if Statements

# temperature = 25
# if temperature > 30:
#     print("Hot Day Today")
#     print("Drink Water")
# elif temperature > 20:
#     print("It is a nice day")
# else:
#     print("its cold")

# Exercise
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == 'K':
    weight_converted = weight / 0.45
    print(f"Weight in Lbs: {str(weight_converted)}")
else:
    weight_converted = weight * 0.45
    print(f"Weight in kg: {str(weight_converted)}")
