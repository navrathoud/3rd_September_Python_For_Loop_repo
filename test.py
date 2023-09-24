#assignment ForLoop
print(" Basic Level:")
print(" 1. Write a Python program to print the numbers from 1 to 10 using a `for` loop.")
for i in range(1,11):
    print(i,end=' ')
print()

print(" 2. Create a program that calculates the sum of all numbers in a list using a `for` loop.")
sum=0
LIST = [1,4,5,7,2]
for i in LIST:
    sum+=i
print("sum of all numbers in a list",sum)

print(" 3. Write a program to print the characters of a string in reverse order using a `for` loop.")
STRING = 'iambestintheworld!'
r_string=''
for i in STRING:
    r_string=i+r_string
print("reverse of string",r_string)

print(" 4. Develop a program that finds the factorial of a given number using a `for` loop.")
number = 5
fact = number
for i in range(1,5):
    fact = fact*i
print("factorial of a given number {}! is {}".format(number,fact))

print(" 5. Create a program to print the multiplication table of a given number using a `for` loop.")
mul=3
print("Table of",mul,'is',end=' ')
for i in range(1,11):
    table=mul*i
    print(table,end=' ')
print()
print(" 6. Write a program that counts the number of even and odd numbers in a list using a `for` loop.")
LIST=[1,3,5,2,8,10,19,0]
even_count=0
for i in LIST:
    if i%2==0:
        even_count+=1
print("Even numbers {}, Odd numbers {}".format(even_count,len(LIST)-even_count))

print(" 7. Develop a program that prints the squares of numbers from 1 to 5 using a `for` loop.")
print("squares of numbers",end=' ')
for i in range(1,6):
    print(i**2,end=' ')
print()
print(" 8. Create a program to find the length of a string without using the `len()` function.")
STRING='pwskillsisgood'
length=len(STRING)
print("length of a string",length)

print(" 9. Write a program that calculates the average of a list of numbers using a `for` loop.")
LIST=[2,4,3,6,11,222,3,4]
for i in LIST:
    sum+=i
avg = sum/len(LIST)
print("average",avg)
print(" 10. Develop a program that prints the first `n` Fibonacci numbers using a `for` loop")
nth=10
first=0
second=1
print("prints the first `n` Fibonacci `number:",first,second,end=' ')
for i in range(nth-2):
    number = first+second
    first = second
    second = number
    print(number,end=' ')
