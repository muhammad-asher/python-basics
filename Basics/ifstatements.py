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
import weightconverter
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == 'K':
    weight_converted = weightconverter.kg_to_lbs(weight)
    print(f"Weight in Lbs: {str(weight_converted)}")
else:
    weight_converted = weightconverter.lbs_to_kg(weight)
    print(f"Weight in kg: {str(weight_converted)}")
