# # S1 D3 Assignment - Set 3

# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

packing_list=[]

packing_list.append(("John",25))
packing_list.append(("Jone",30))

upackingbag=""

for n,a in packing_list:
    upackingbag+=f"{n} is {a} years old."

print(upackingbag)




# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

dictmanupulation={}
def Addnewkeyvalue(name,age):
    dictmanupulation[name]=age

def Updatekeyvalue(name,age):
    if name in dictmanupulation:
        dictmanupulation[name]=age

def deletekeyvalue(name):
    if name in dictmanupulation:
        del dictmanupulation[name]

Addnewkeyvalue("John",25)
print(dictmanupulation)

Updatekeyvalue("John",26)
print(dictmanupulation)

deletekeyvalue("John")
print(dictmanupulation)

# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"

twosumlist=[2, 7, 11, 15]
target = 9

    
def twoSum(n, t, arr): 
    l = 0
    r = n - 1
    while l < r: 
        sum = arr[l] + arr[r] 
        if sum == t: 
            return [l, r] 
        elif sum < t: 
            l += 1
        else: 
            r -= 1
    return [-1, -1]

 
 
print(twoSum(len(twosumlist),target,twosumlist))
# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

inputpalindromstring="madam"

newrevstring = ""

for i in range(len(inputpalindromstring)-1,-1,-1):
   newrevstring+=inputpalindromstring[i]
    
res = f"The word {inputpalindromstring} is a palindrome." if newrevstring==inputpalindromstring else f"The word {inputpalindromstring} is not a palindrome."

print(res)
# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def solve(N, arr): 
    for i in range(0, N-1): 
        min = i 
        for j in range(i+1, N): 
            if arr[j] < arr[min]: 
                min = j 
        temp = arr[i] 
        arr[i] = arr[min] 
        arr[min] = temp 
    
    return arr 
  
# Driver code 
arr = [12,85,865,5, 22] 
N = len(arr) 
print(solve(N, arr))
# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, val):
        self.queue1.put(val)

    def pop(self):
        if self.queue1.empty():
            return None

        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        top_element = self.queue1.get()

        # Swap the queues to maintain the main storage queue
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

# Test the implementation
stack = StackUsingQueue()
output = []

stack.push(1)
stack.push(2)
output.append(stack.pop())
stack.push(3)
output.append(stack.pop())
output.append(stack.pop())

print(", ".join(str(x) for x in output))  # Output: "1, None, 3, None, None"


# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."

for i in range(1,100+1):
    if(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)            


# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

with open("./input.txt","r") as readfile:
    content=readfile.read()
    
content=content.split()

print(len(content))

try:
 with open("/out.txt","x") as addandwrite:
    addandwrite.write(str(len(content)))
    print("File Added and count updated")
except FileExistsError:
    print("File already present")   


# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero.

def dividetwonumber(a,b):
    try:
       return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(dividetwonumber(5,0))    