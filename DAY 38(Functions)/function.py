#3 WAP To check given number is +ve,-ve or zero
def check_number(num):
    if num>0:
        return f'{num} is positive'
    elif num<0:
        return f'{num} is negative'
    else:
        return f'{num} is zero'
print(check_number(98))

#4 WAP to find the factorial of given number
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(factorial(5))

#5 WAP to check the given number is prime number or not
def is_prime(num):
    if num<=1:
        return f'{num} is not a prime number'
    for i in range(2,num):
        if num%i==0:
            return f'{num} is not prime'
    return f'{num} is prime'
print(is_prime(7))

#or
def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        return f'{num} is prime'
    else:
        return f'{num} is not a prime number'
print(prime(7))

# WAP to Reverse a number
def reverse(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev
print(reverse(34))

# WAP to find the sum of digits
def sum_digit(num):
    sum=0
    while num>0:
        digit=num%10
        sum=sum+digit
        num=num//10
    return sum
print(sum_digit(123))

# WAP to check number is palindrome or not
def palindrome(num):
    temp=num
    rev=0
    for i in str(num):
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if temp==rev:
        return f'{temp} is palindrome'
    else:
        return f'{temp} is not palindrome'
print(palindrome(121))

# WAP To find largest of two numbers
def largest(num1,num2):
    if num1>num2:
        return f'{num1} is largest number'
    else:
        return f'{num1} is smaller number'
print(largest(20,30))
    
# WAP TO CHECK ARMSTRONG NUMBER
def armstrong(num):
    temp=num
    sum_cubes=0
    length=len(str(num))
    while num>0:
        digit=num%10
        sum_cubes=sum_cubes+digit**length
        num=num//10
    if sum_cubes==temp:
        return f'{temp} is armstrong number'
    else:
        return f'{temp} is not a armstrong number'
print(armstrong(153))

# WAP to check number is strong number or not
def strong(num):
    sum=0
    for i in str(num):
        fact=1
        for j in range(1,int(i)+1):
            fact=fact*j
        sum=sum+fact
    if sum==num:
        return f'{num} is strong number'
    else:
        return f'{num} is not a strong number'
print(strong(145))

# WAP to check number is perfect number or not
def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        return f'{num} is perfect number'
    else:
        return f'{num} is not perfect number'
print(perfect(6))

#WAP to print fibonacci of n term
def fibonacci(num):
    a=0
    b=1
    for i in range(num):
        print(a)
        a,b=b,a+b
fibonacci(5)

#WAP TO FIND THE COUNT OF DIGITS
def count_digits(num):
    count=0
    for i in str(num):
        count=count+1
    return count
print(count_digits(1234))

# WAP To find sum of starting natural numbers
def sum_natural(num):
    sum=0
    for i in range(1,num+1):
            sum=sum+i
    return sum
print(sum_natural(5))

#WAP to find power of number
def power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result
print(power(2, 3))

#WAP to check the number is neon number or not
def neon(num):
    sq=num*num
    sum=0
    for i in str(sq):
        sum=sum+int(i)
    if sum==num:
        return f'{num} is neon number'
    else:
        return f'{num} is not a neon number'
print(neon(5))

#WAP to check the number is SPY number or not
def spy(num):
    sum=0
    prod=1
    for i in str(num):
        sum=sum+int(i)
        prod=prod*int(i)
    if sum==prod:
        return f'{num} is spy number'
    else:
        return f'{num} is not a spy number'
print(spy(1124))


#imp
# STRING PROGRAMS


# 1) ASCII Value of a Single Character
def ascii_value(ch):
    return ord(ch)  

print(ascii_value('A'))  # Output: 65


# 2) ASCII Value of Total Characters in a String
def ascii_string(s):
    return [ord(c) for c in s]

print(ascii_string("ABC"))  # Output: [65, 66, 67]


# 3) Concatenate Strings
def concat_strings(a, b):
    return a + b

print( concat_strings("Hello ", "World"))  # Output: Hello World


# 4) Convert String to Uppercase
def to_upper(s):
    return s.upper()

print(to_upper("hello"))  # HELLO


# 5) Convert String to Lowercase
def to_lower(s):
    return s.lower()

print(to_lower("HELLO"))  # hello


# 6) Copy a String
def copy_string(s):
    return s[:]

print(copy_string("Python"))  # Python


# 7) Count Occurrence of a Character
def count_char(s, ch):
    return s.count(ch)

print(count_char("banana", "a"))  # 3


# 8) Count Total Characters
def total_chars(s):
    return len(s)

print(total_chars("Python"))  # 6


# 9) Count Words
def count_words(s):
    return len(s.split())

print(count_words("I love Python"))  # 3


# 10) Count Vowels
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

print(count_vowels("Hello"))  # 2


# 11) Count Vowels and Consonants
def vowels_consonants(s):
    v = c = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                v += 1
            else:
                c += 1
    return v, c

print(vowels_consonants("Hello"))  # (2, 3)


# 12) Count Alphabets, Digits, Special Characters
def count_all(s):
    a = d = sp = 0
    for ch in s:
        if ch.isalpha():
            a += 1
        elif ch.isdigit():
            d += 1
        else:
            sp += 1
    return a, d, sp

print(count_all("abc123!@"))  # (3, 3, 2)


# 13) First Occurrence of Character
def first_occurrence(s, ch):
    return s.find(ch)

print(first_occurrence("banana", "a"))  # 1


# 14) Last Occurrence
def last_occurrence(s, ch):
    return s.rfind(ch)

print(last_occurrence("banana", "a"))  # 5


# 15) Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True


# 16) Print Characters
def print_chars(s):
    for ch in s:
        print(ch, end=" ")
    print()

print(end=" ")
print_chars("ABC")  # A B C


# 17) Replace Space with Hyphen
def replace_space(s):
    return s.replace(" ", "-")

print(replace_space("Hello World"))  # Hello-World


# 18) Replace Characters
def replace_char(s, old, new):
    return s.replace(old, new)

print(replace_char("banana", "a", "x"))  # bxnxnx


# 19) Remove Odd Characters
def remove_odd_chars(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 == 0)

print(remove_odd_chars("abcdef"))  # ace


# 20) Remove Odd Index Characters
def remove_odd_index(s):
    return s[::2]

print(remove_odd_index("abcdef"))  # ace


# 21) Remove First Occurrence
def remove_first(s, ch):
    return s.replace(ch, "", 1)

print(remove_first("banana", "a"))  # bnana


# 22) Remove Last Occurrence
def remove_last(s, ch):
    idx = s.rfind(ch)
    return s[:idx] + s[idx+1:] if idx != -1 else s

print(remove_last("banana", "a"))  # banan


# 23) Reverse String
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))  # nohtyP


# 24) String Length
def string_length(s):
    return len(s)

print(string_length("Hello"))  # 5


# 25) Total Occurrence of Character
def total_occurrence(s, ch):
    return s.count(ch)

print(total_occurrence("banana", "a"))  # 3


# 26) Toggle Case
def toggle_case(s):
    return s.swapcase()

print(toggle_case("HeLLo"))  # hEllO


# LIST PROGRAMS 


# 1) Access List Index and Values
def access_list(lst):
    result = []
    for i in range(len(lst)):
        result.append((i, lst[i]))
    return result

print(access_list([10, 20, 30]))


# 2) Add Two Lists
def add_lists(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

print(add_lists([1,2], [3,4]))  # [4,6]


# 3) Arithmetic Operations
def list_arithmetic(a, b):
    add = []
    sub = []
    mul = []
    for i in range(len(a)):
        add.append(a[i] + b[i])
        sub.append(a[i] - b[i])
        mul.append(a[i] * b[i])
    return add, sub, mul

print(list_arithmetic([4,5], [1,2]))


# 4) Check List Empty
def is_empty(lst):
    count = 0
    for _ in lst:
        count += 1
    return count == 0

print(is_empty([]))  # True


# 5) Copy List
def copy_list(lst):
    result = []
    for i in lst:
        result.append(i)
    return result

print(copy_list([1,2,3]))


# 6) Count Even and Odd
def even_odd(lst):
    e = 0
    o = 0
    for x in lst:
        if x % 2 == 0:
            e += 1
        else:
            o += 1
    return e, o

print(even_odd([1,2,3,4]))  # (2,2)


# 7) Positive and Negative
def pos_neg(lst):
    p = 0
    n = 0
    for x in lst:
        if x >= 0:
            p += 1
        else:
            n += 1
    return p, n

print(pos_neg([-1,2,-3,4]))


# 8) Largest Number
def largest(lst):
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

print(largest([1,9,3]))  # 9


# 9) Largest and Smallest
def large_small(lst):
    max_val = lst[0]
    min_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x
    return max_val, min_val

print(large_small([1,9,3]))


# 10) Length of List
def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

print(list_length([1,2,3]))


# 11) List Difference
def list_diff(a, b):
    result = []
    for x in a:
        found = False
        for y in b:
            if x == y:
                found = True
                break
        if not found:
            result.append(x)
    return result

print(list_diff([1,2,3], [2]))


# 12) List Multiplication
def list_multiply(lst):
    result = 1
    for x in lst:
        result *= x
    return result

print(list_multiply([1,2,3]))  # 6


# 13) Print Elements
def print_list(lst):
    for x in lst:
        print(x, end=" ")
    print()

print_list([1,2,3])


# 14) Even Numbers
def even_list(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x)
    return result

print(even_list([1,2,3,4]))


# 15) Odd Numbers
def odd_list(lst):
    result = []
    for x in lst:
        if x % 2 != 0:
            result.append(x)
    return result

print(odd_list([1,2,3,4]))


# 16) Positive Numbers
def positive_list(lst):
    result = []
    for x in lst:
        if x >= 0:
            result.append(x)
    return result

print(positive_list([-1,2,-3,4]))


# 17) Negative Numbers
def negative_list(lst):
    result = []
    for x in lst:
        if x < 0:
            result.append(x)
    return result

print(negative_list([-1,2,-3,4]))


# 18) Separate Even and Odd
def even_list(lst):
    return [x for x in lst if x % 2 == 0]

def odd_list(lst):
    return [x for x in lst if x % 2 != 0]

def separate_even_odd(lst):
    return even_list(lst), odd_list(lst)

print(separate_even_odd([1,2,3,4]))


# 19) Separate Positive and Negative
def positive_list(lst):
    return [x for x in lst if x >= 0]

def negative_list(lst):
    return [x for x in lst if x < 0]

def separate_pos_neg(lst):
    return positive_list(lst), negative_list(lst)

print(separate_pos_neg([-1,2,-3,4]))

# 20) Remove Duplicates
def remove_duplicates(lst):
    result = []
    for x in lst:
        duplicate = False
        for y in result:
            if x == y:
                duplicate = True
                break
        if not duplicate:
            result.append(x)
    return result

print(remove_duplicates([1,2,2,3]))


# 21) Remove Even Numbers
def remove_even(lst):
    result = []
    for x in lst:
        if x % 2 != 0:
            result.append(x)
    return result

print(remove_even([1,2,3,4]))


# 22) Reverse List
def reverse_list(lst):
    result = []
    i = 0
    while i < len(lst):
        result = [lst[i]] + result
        i += 1
    return result

print(reverse_list([1,2,3]))


# 23) Second Largest
def second_largest(lst):
    first = second = -10**9
    for x in lst:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
    return second

print(second_largest([1,5,3,9]))


# 24) Sort Ascending
def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(sort_list([3,1,2]))


# 25) Smallest Element
def smallest(lst):
    min_val = lst[0]
    for x in lst:
        if x < min_val:
            min_val = x
    return min_val

print(smallest([3,1,2]))




# 1. Reverse Number
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

num = int(input("Enter a number to reverse: "))
print("Reversed number:", reverse_number(num))


# 2. Find Sum of Digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

num = int(input("Enter a number to find sum of digits: "))
print("Sum of digits:", sum_of_digits(num))


# 3. Check Palindrome
def is_palindrome(n):
    return n == reverse_number(n)

num = int(input("Enter a number to check palindrome: "))
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")


# 4. Find Largest of Two Numbers
def largest_of_two(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Largest number is:", largest_of_two(a, b))


# 5. Check Armstrong Number
def is_armstrong(n):
    temp = n
    sum = 0
    digits = 0
    t = n
    while t > 0:
        digits += 1
        t = t // 10
    while temp > 0:
        r = temp % 10
        sum += r ** digits
        temp = temp // 10
    return sum == n

num = int(input("Enter a number to check Armstrong: "))
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# 6. Check Strong Number
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def is_strong(n):
    temp = n
    sum = 0
    while temp > 0:
        sum += factorial(temp % 10)
        temp = temp // 10
    return sum == n

num = int(input("Enter a number to check Strong number: "))
if is_strong(num):
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")


# 7. Check Perfect Number
def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

num = int(input("Enter a number to check Perfect number: "))
if is_perfect(num):
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")


# 8. Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

n = int(input("Enter number of terms for Fibonacci: "))
print("Fibonacci series:", fibonacci(n))


# 9. Count of Digits
def count_digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n = n // 10
    return count

num = int(input("Enter a number to count digits: "))
print("Number of digits:", count_digits(num))


# 10. Sum of First n Natural Numbers
def sum_natural(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

n = int(input("Enter number to sum first n natural numbers: "))
print("Sum of first", n, "natural numbers:", sum_natural(n))


# 11. Power of Number
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print(f"{base}^{exp} =", power(base, exp))


# 12. Check Neon Number
def is_neon(n):
    sq = n * n
    sum_digits = 0
    while sq > 0:
        sum_digits += sq % 10
        sq = sq // 10
    return sum_digits == n

num = int(input("Enter a number to check Neon: "))
if is_neon(num):
    print(num, "is a Neon number")
else:
    print(num, "is not a Neon number")


# 13. Check Spy Number
def is_spy(n):
    sum_digits = 0
    product_digits = 1
    temp = n
    while temp > 0:
        r = temp % 10
        sum_digits += r
        product_digits *= r
        temp = temp // 10
    return sum_digits == product_digits

num = int(input("Enter a number to check Spy number: "))
if is_spy(num):
    print(num, "is a Spy number")
else:
    print(num, "is not a Spy number")