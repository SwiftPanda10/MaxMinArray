#Author: Samuel Bennett
#Date: 4/14/2021
#:Discription: Prints the max and min of a user determined amount of integers

total = int(input("How many integers would you like to enter? "))

print("Please enter ", total, "integers: ")

l = list()
for i in range(total):
    num = int(input())
    l.append(num)

Min = min(l)
Max = max(l)


print("min: ", Min)
print("max: ", Max)