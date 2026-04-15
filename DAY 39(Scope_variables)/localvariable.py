#Local variable
#1
def display():
    num=25
    print(f'inside function number value:{num}')
display()

#2
# def display():
#     num=25
# display()
# print(f'accessing outside function:{num}')

#3
def display():
    global num
    num=25
display()
print(f'accessing outside function:{num}')

#nonlocal keyword
#1
def outer():
    num=98
    def inner():
        nonlocal num
        num=num+2
        print(num)
    inner()
outer()
