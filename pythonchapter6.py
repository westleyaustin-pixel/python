#1
for row in range(10):
    print("*",end=" ")
print()
print()
#2
for row in range(10):
    print("*", end=" ")
print()
#3
for row in range(5):
    print("*", end=" ")
print()
for row in range(20):
    print("*", end=" ")
print()
print()
#4
for row in range(8):
    for column in range(10):
        print("*", end=" ")
    print()
print()
#5
for row in range(10):
    for column in range(5):
        print("*", end=" ")
    print()
print()
#6
for row in range(5):
    for column in range(20):
        print("*", end=" ")
    print()
print()
#7
for row in range(10):
    for column in range(10):
        print(column, end=" ")
    print()
print()
#8
for row in range(10):
    for column in range(10):
        print(row, end=" ")
    print()
print()
#9
for row in range(10):
    for column in range(row+1):
        print(column, end=" ")
    print()
print()
#10
for row in range(10):
    for column in range(row):
        print(" ", end=" ")
    for column in range(10-row):
        print(column, end=" ")
    print()
print()

for row in range(10):
    for column in range(1,10):
        if row*column < 10:
            print(" ", end=" ")
        print(row*column, end=" ")
    print()
print()
#LAB
count = 10

for row in range(10):
    for column in range(row):
        print (count,end=" ")
        count += 1
    print()
