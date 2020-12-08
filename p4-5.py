"""
Write a program that reads a set of floating numbers and print:
    * the largest
    * the smallest
    * the average
    * difference largest, smallest
"""
import integerExercises

arr = []
while True:
    user = input("Enter values to calculate: ")
    if not user:
        break
    arr.append(int(user))

small, large = integerExercises.smallLarge(arr)
print(f"Smallest: {small} and largest: {large}")
print("Difference between largest and smallest: " + str(round(large - small, 2)))
print("Average value: " + str(round(integerExercises.averageValue(arr), 2)))

