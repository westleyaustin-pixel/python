x = 0
print("Welcome to the team quiz")
print("What is 5 times 6?")
print("A. 19")
print("B. 30")
print("C. 36")
answer= input("Answer:")
if answer.lower() == "b":
    print("Correct!")
    x = x + 1
else:
    print("Wrong!")
print("What is 6 + 7?")
print("A. 13")
print("B. 10")
print("C. 15")
answer= input("Answer:")
if answer.lower() == "a":
    print("Correct!")
    x = x + 1
else:
    print("Wrong!")
print("What is 4 times 1?")
print("A. 5")
print("B. 9")
print("C. 1")
print("D. 4")
answer= input("Answer:")
if answer.lower() == "d":
    print("Correct!")
    x = x + 1
else:
    print("Wrong!")
print("What is 6/2(1+2)?")
print("A. 9")
print("B. 1")
print("C. 12")
answer= input("Answer:")
if answer.lower() == "a":
    print("Correct!")
    x = x + 1
else:
    print("Wrong!")
print("What is 9/3?")
print("A. 6")
print("B. 3")
print("C. 12")
answer= input("Answer:")
if answer.lower() == "b":
    print("Correct!")
    x = x + 1
else:
    print("Wrong!")
print("What is 8 - 3?")
print("A. 5")
print("B. 12")
print("C. 4")
answer= input("Answer:")
if answer.lower() == "a":
    print("Correct!")
    x = x + 1
else:
    print("Wrong!")
print("What is 2 + 2?")
print("A. fish")
print("B. 4")
print("C. 5")
answer= input("Answer:")
if answer.lower() == "b":
    print("Correct!")
    x = x + 1
else:
    print("Wrong!")
print("What is 10 - 4?")
print("A. 6")
print("B. 10")
print("C. 4")
answer= input("Answer:")
if answer.lower() == "a":
    print("Correct!")
    x = x + 1
else:
    print("Wrong!")

print("Thank you for playing the team quiz!")
print("You scored", x, "out of 8.")
if x >= 6:
    print("Great job! You passed the quiz.")
else:
    print("You need to study more. Better luck next time!")