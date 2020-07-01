age = int(input("How old?"))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Not valid")

print("-" * 80)

if age < 16 or age > 65:
    print("Not valid")
else:
    print("Have a good day at work")

