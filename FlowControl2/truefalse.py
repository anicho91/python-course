day = "Saturday"
temperature = 30
raining = True

if day == "Saturday" and (temperature > 27 or not raining):
    print("swim")
else:
    print("Study")

print()

if 0:
    print("True")
else:
    print("False")

print()

name = input("Name: ")
# if name:  #if name exists
if name != "":
    print("Hello, {}".format(name))
else:
    print("No name")
