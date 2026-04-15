s='aaabbaabcc'
count=1

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count=count+1
    else:
        print(s[i]+str(count),end='')
        count=1
print(s[-1]+str(count)) 
              


# l=[100,700,100,300,900,200]
# n=1000
