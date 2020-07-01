name = input("Enter Name: ")
age = int(input("Enter age: "))

if age < 18 or age > 30:
    print("Sorry {}, not welcome".format(name))
else:
    print("Welcome {}".format(name))
