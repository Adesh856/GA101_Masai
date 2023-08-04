# 1. **Hello, World!**: Write a Python program that prints "Hello, World!" to the console.
#     - *Input*: None
#     - *Output*: "Hello, World!"

print("Hello, World!")





# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."

integer=1
string="Adesh"
var=42.5
isavailable=False
list=[1,5,"hey"]
tup=(1,5,32)
dict={
    "key":"value"
}
sett={1,5,8}

print(type(integer),integer)
print(type(string),string)
print(type(var),var)
print(type(isavailable),isavailable)
print(type(list),list)
print(type(dict),dict)
print(type(sett),sett)




# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."

list = []
i=1
while i<=10:
    list.append(i) 
    i=i+1

list.remove(5)
list.sort()
print(list)





# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

Numberli=[10, 20, 30, 40]
sum=0
for num in Numberli:
    sum+=num


print(sum)   
print(sum/len(Numberli)) 





# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

Input="Python"
rev="".join( reversed(Input))

# for s in Input:
#     rev=s+rev



print(rev)

# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

vowelstr="Hello"
count=0
for i in range(len(vowelstr)):
    changeitscasesentivess=vowelstr[i].lower()
    if changeitscasesentivess=="a"or changeitscasesentivess=="e" or changeitscasesentivess=="i" or changeitscasesentivess=="o" or changeitscasesentivess=="i":
        count+=1

print(f"Number of vowel : {count}")

# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

num=13
count=0
i=2
for n in range(i,num+1):
    if num%n==0:
       count+=1 

if count==1:
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
    
# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

num=5
product=1
for i in range(1,num+1):
    product*=i

print(product)    

# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        prev, curr = 0, 1
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr

num = 7
print(fibonacci(num))  # Output: 8 (fibonacci of 7)

# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"

list = [n*n for n in range(1,10+1)]
print(list)
