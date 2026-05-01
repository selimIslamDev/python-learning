#question on slicing
#take input and print middle 3 characters, last 2 characters

str = input("Enter a string: ")
mid = len(str) // 2
output1 = str[mid-1:mid+2]
print("Middle 3 characters: ", output1)

output2 = str[-2:]
print("Last 2 characters: ", output2)