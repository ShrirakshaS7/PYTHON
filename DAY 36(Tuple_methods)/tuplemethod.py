#Tuple method
#Count method
#1
t1=(10,20,30,10,50,30,10,20,10)
print(t1.count(10))

#Index method
#1
t2=(10,20,30,10,50,30,10,20,10)
print(t2.index(30))

#2
t3=(10,20,30,10,50,30,10,20,10)
print(t2.index(300))

#WAP to find the position of 3rd occurrence of specified element(using enumerate function)
t4=(10,20,30,10,50,30,10,20,10)
count=0
value=10
for index, num in enumerate(t4):
    if num==value:
        count=count+1
        if count==3:
            print(index)
            break

