# SET methods
# Add method
#1
s1={'smith','martin'}
s1.add('king')
print(s1)

#Remove method
#1
s2={'smith','martin'}
s2.remove('martin')
print(s2)

#Update method
#1
my_set={1,2,3}
another_set={3,4,5,6}
my_set.update(another_set)
print(my_set)

#POP method
#1
s1={10,20,30,40,98,100}
s1.pop()
print(s1)

#Clear method
#1
s1={10,20,30,40,98,100}
s1.clear()
print(s1)

#Union method
#1
my_set={1,2,3}
another_set={3,4,5,6}
res=my_set.union(another_set)
print(res)

#Intersection method
#1
my_set={1,2,3,4}
another_set={3,4,5,6}
res=my_set.intersection(another_set)
print(res)

#difference method
#1
my_set={1,2,3}
another_set={3,4,5,6}
res=my_set.difference(another_set)
print(res)

#Symmetric difference
#1
my_set={1,2,3}
another_set={3,4,5,6}
res=my_set.symmetric_difference(another_set)
print(res)

