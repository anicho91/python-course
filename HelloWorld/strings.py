print("Today is a good day")
print("stuff")
print("python's string are easy to use")
print('We can even include "quotes"')

greeting = "Hello"
name = "Anna"

print(greeting + " " + name)

age = 24
print(age)
print(type(greeting))
print(type(age))

ageInWords = "2 years"
print(name + f" is {age} years old")
# Traceback (most recent call last):
#   File "C:/Users/Perse/pyCode/HelloWorld/strings.py", line 17, in <module>
#     print(name + " is " + age + "years old")
# TypeError: can only concatenate str (not "int") to str

print(type(age))

print(f"Pi is approx. {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approx. {pi:12.50f}")
