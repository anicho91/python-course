for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}"
          .format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}"
          .format(i, i ** 2, i ** 3))

print()

print("Pi is approx. {0:12}".format(22/7))  # default 15 digits with 12 width
print("Pi is approx. {0:12f}".format(22/7))  # default floating 6 digits with 12 width
print("Pi is approx. {0:12.50f}".format(22/7))  # percision of 50 decimals, python prefers percision over width
print("Pi is approx. {0:52.50f}".format(22/7))  # various widths with 50 percision
print("Pi is approx. {0:62.50f}".format(22/7))
print("Pi is approx. {0:<72.50f}".format(22/7))
print("Pi is approx. {0:<72.54f}".format(22/7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}"
          .format(i, i ** 2, i ** 3))