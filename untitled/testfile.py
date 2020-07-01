name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age < 18:
    print("{0} years until 18".format(18 - age))
elif age == 900:
    print("Incorrect age")
else:
    print("Old enough to vote")
    print("Please put an X in the box")
