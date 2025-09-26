x = 0
print("Welcome to the quiz!")
print("First Question: Is pluto a planet?")
print("A. No it is not a planet")
print("B. It is a dwarf planet")
print("C. It is a full planet")
answer= input("Answer:")
if answer.lower() == "b":
    print("Correct!")
else:
    print("Wrong!")
    x = x + 1
print("Next question: What is the largest country in the world?")
print("A. Russia")
print("B. Canada")
print("C. United States")
answer= input("Answer:")
if answer.lower() == "a":
    print("Correct!")
else:
    print("Wrong!")
    x = x + 1
print("Next question: How much percent of the ocean have humans explored?")
print("A. 10%")
print("B. 15%")
print("C. 1%")
print("D. 5%")
answer= input("Answer:")
if answer.lower() == "d":
    print("Correct!")
else:
    print("Wrong!")
    x = x + 1
print("Next question: Which of these is a USA territory?")
print("A. Puerto Rico")
print("B. Easter Island")
print("C. Greenland")
answer= input("Answer:")
if answer.lower() == "a":
    print("Correct!")
else:
    print("Wrong!")
    x = x + 1
print("Last question! Which team has never won a championship in their league?")
print("A. Minnesota Twins")
print("B. Orlando Magic")
print("C. Los Angeles Angels")
print("D. Seattle Seahawks")
answer= input("Answer:")
if answer.lower() == "b":
    print("Correct!")
else:
    print("Wrong!")
    x = x + 1
print("Thank you for playing my quiz!")
print("Final score = ", x/5*100,"%")