shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)


string = "kittent"
n = 6

newChar = string[n]
print(string.replace(newChar, "", 1))

first = string[0:n]
second = string[n+1:]  # plus 1 to not include character at n

print(first + second)

print()

str2 = "code"

num = len(str2) - 1
beg = str2[0]
end = str2[num]
middle = str2[1:num]
print(end + middle + beg)
