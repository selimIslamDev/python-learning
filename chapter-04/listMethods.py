#Methods in list

#indexing 
marks = [90, 80, 70, 60, 50];
print(marks)
print(marks[0]) #90
marks[0] = 95
print(marks) #[95, 80, 70, 60, 50]


#slicing
print(marks[1:4]) #[80, 70, 60]


print(max(marks))
print(min(marks))
marks.append(85)
print(marks)
marks.sort()
print(marks)



## strings are immutable but lists are mutable
# name = "john"
# name[0] = "h"
# print(name)