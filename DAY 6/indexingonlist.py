#homogeneous eg
li=1[10,20,98]
print(li)

li=[10,20,98]
print(type(li))

#heterogeneous eg
l2=[10,'smith',True,(1,2,3),[98,100]]
print(l2)

l2=[10,'smith',True,(1,2,3),[98,100]]
print(type(l2))

# Indexing on list

list=[10,20,40,70,98,270]
print(list[0])   #10
print(list[1])   #20
print(list[3])   #70
print(list[5])   #270
print(list[-1])  #270
print(list[-3])  #70
print(list[9])   # IndexError: list index out of range

#example for nested list

list=[10,20,['smith',100,200],98,270]
print(list[2][0])   
print(list[2][1])  
print(list[2][-1]) 
print(list[2][-2]) 
print(list[2][-3]) 
print(list[2][2]) 

