try:
    age = int(input('Age: '))
    income = 30000
    risk = income / age
    print(f"Age= {age}")
except ZeroDivisionError:
    print("Age Cannot be 0")
except ValueError:
    print("Invalid Value")
