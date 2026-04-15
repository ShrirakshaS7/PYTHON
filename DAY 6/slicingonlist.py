#slicing on list
#+ve slicing

list=[10,"python",3.14,True,[1,2],{"a":1},(5,6)]
print(list[0:3:1])
print(list[1:4:1])
print(list[2:6:1])
print(list[3:7:1])
print(list[0:4:1])
print(list[2:7:1])
print(list[0:7:2])
print(list[1:6:2])
print(list[0:7:3])
print(list[4:7:1])

#-ve slicing
list=[10,"python",3.14,True,[1,2],{"a":1},(5,6)]
print(list[-7:-4:1])
print(list[-6:-3:1])
print(list[-5:-2:1])
print(list[-4:-1:1])
print(list[-3:7:1])
print(list[-7:7:2])
print(list[-6:6:2])
print(list[-5:6:1])
print(list[-4:6:1])
print(list[-7:-1:1])

# reverse slicing
list=[10,"python",3.14,True,[1,2],{"a":1},(5,6)]
print(list[6::-1])
print(list[6:0:-1])
print(list[5:1:-1])
print(list[4::-1])
print(list[6:2:-2])