parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("Not in parrot")

activity = input("What would you like to do? ")

if "cinema" not in activity.casefold():
    print("No")
