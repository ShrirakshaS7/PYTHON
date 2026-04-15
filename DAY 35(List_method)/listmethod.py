# List Method
#Append method
#1
my_list=[10,20,30]
my_list.append(98)
print(my_list)

#2
list=[]
list.append('hello')
print(list)

#Extend method
#1
my_list=[1,2,3]
my_list.extend([4,5,6])
print(my_list)

#Insert method
#1
my_list=[10,20,30,40,50]
my_list.insert(3,98)
print(my_list)

#Count method
#1
my_list=[10,20,20,30,20,20,50]
print(my_list.count(20))

#Index method
#1
my_list=[10,20,20,30,20,20,50]
first=my_list.index(20)
print(first)

#2 WAP to find the second occurence of specified element
my_list=[10,20,20,30,20,20,50]
first=my_list.index(20)
second=my_list.index(20, first+1)
print(second)

#Reverse method
#1
my_list= [1,2,3,4]
my_list.reverse()
print(my_list)

#Sort method
#Ascending order
#1
my_list=[50,40,90,30]
my_list.sort()
print(my_list)

#2
my_list=['sql','python','java']
my_list.sort()
print(my_list)

# based on string length
my_list=['sql','python','java']
my_list.sort(key=len)
print(my_list)

#Descending order
#1
my_list=[50,40,90,30]
my_list.sort(reverse=True)
print(my_list)

#2
my_list=['sql','python','java']
my_list.sort(reverse=True)
print(my_list)

# based on string length
my_list=['sql','python','java']
my_list.sort(key=len,reverse=True)
print(my_list)

#pop method
#1
my_list=[10,20,30,40]
my_list.pop()
print(my_list)

#2
my_list=[10,20,30,40]
my_list.pop(2)
print(my_list)

#Remove method
#1
my_list=[10,20,30,20,40]
my_list.remove(20)
print(my_list)

#Clear method
#1
my_list=[10,20,30,40]
my_list.clear()
print(my_list)

# WAP To find 4rth occurence of element using enumerate function
data=[10,20,30,20,40,20,50,20,98]
element=20
count=0
for index, value in enumerate(data):
    if value==element:
        count=count+1
        if count==4:
            print(index)
            break

# WAP to find 3rd highest from given list
data=[10,20,30,20,40,20,50,20,98]
num=list(set(data))
num.sort(reverse=True)
for index, value in enumerate(num,start=1):
    if index==3:
        print(f'third highest element:{value}')
        break

# WAP to find 2nd lowest element from given list collection
data=[10,20,30,20,40,20,50,20,98]
num=list(set(data))
num.sort()
for index, value in enumerate(num, start=1):
    if index==2:
        print(f'second lowest element:{value}')
        break

# WAP to separate even and odd numbers using list method
nums=[10,15,20,25,98,67,33]
even=[]
odd=[]
for num in nums:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(f'even number:{even}')
print(f'odd numbers:{odd}')

# WAP To remove all occurrence of specified element
nums=[10,15,20,25,98,67,20,33]
while 20 in nums:
    nums.remove(20)
print(nums)

#WAP to find frequency of each element
nums=[10,20,30,20,40,30,10,40]
unique=list(set(nums))
for i in unique:
    print(i,nums.count(i))
