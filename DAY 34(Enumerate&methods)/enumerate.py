#Enumerate function
#1
string='python'
for index, ch in enumerate(string):
    print(index, ch) 

#2 WAP to find the position of 3rd occurance of character a
msg='basavanagudi'
count=0
for index, ch in enumerate(msg):
    if ch=='a':
        count=count+1
        if count==3:
            print(index)
            break

#3
string='python'
for index, ch in enumerate(string, start=1):
    print(index, ch)

#4
msg='python'
print(msg.index('j'))