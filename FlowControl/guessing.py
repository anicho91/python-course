answer = 5

print("Guess a number")
guess = int(input())

# if guess < answer:
#     print("Guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("incorrect")
# elif guess > answer:
#     print("Guess lower")
#     if guess == answer:
#         print("Well done")
#     else:
#         print("incorrect")
# else:
#     print("correct")

# if guess != answer:
#     if guess < answer:
#         print("Higher")
#     else:
#         print("Lower")
#     guess = int(input())
#     if guess == answer:
#         print("Correct")
#     else:
#         print("incorrect")
# else:
#     print("correct")

if guess == answer:
    print("correct")
else:
    if guess < answer:
        print("Higher")
    else:
        print("Lower")
    guess = int(input())
    if guess == answer:
        print("Correct")
    else:
        print("incorrect")
