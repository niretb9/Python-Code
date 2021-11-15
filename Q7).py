# Python program to find sum of elements in list
total = 0
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
 
for ele in range(0, len(numbers)):
    total = total + numbers[ele]
 
print("Sum of all elements in given list: ", total)