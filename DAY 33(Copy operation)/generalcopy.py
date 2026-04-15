# Copy Operations
#General copy
#1
list1=[10,20,30,40]
list2=list1
print(list1)
print()
print(list2)

#2
list1=[10,20,30,40]
list2=list1
print(id(list1))
print()
print(id(list2))

#3 modification of element in copied object

list1=[10,20,30,40]
list2=list1
list2[3]=98
print(list1)
print()
print(list2)

