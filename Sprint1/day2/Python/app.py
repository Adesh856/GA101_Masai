import math
#exercise1
i = 1
sum=0
while i<=10:
    sum=sum+i
    i+=1

print(sum)

#exercise2
def farenitcalculator(c):
    print((c*9/5)+32)
    
farenitcalculator(37)    

#exercise3
def evensum(li):
    sum=0
    for i in li:
        if i%2==0:
            sum+=i
    return sum

res=evensum([1,2,3,4,5])
print(res)        

#exercise4

def makelistofeven(li):
    newlistevensquared=[n*n for n in li if n%2==0]
    return newlistevensquared
print(makelistofeven([1,2,3,4,5]))



#exercise5
# # Write a Python function that takes a list of strings as input and returns a dictionary containing the length of each string as the key and the list of strings with that length as the value. In other words, group the strings by their length in the input list.

# For example:
# Input: ["apple", "banana", "cherry", "pear", "orange"]
# Output: {5: ['apple', 'pear'], 6: ['banana', 'cherry', 'orange']}

# Try implementing Exercise 5, and let me know when you're ready to proceed to the next topic!


def findlengthoflist(li):
    dict={}
    for el in li:
        length=len(el)
        if(length not in dict):
            dict[length] = [el]
        else:
            dict[length].append(el)
    
    return dict
print(findlengthoflist( ["apple", "banana", "cherry", "pear", "orange"]))


# exercise 6
# Write a Python function that takes a list of numbers as input and returns a dictionary containing the count of each unique number in the list.

# Example:
# Input: [1, 2, 3, 2, 1, 4, 3, 5]
# Output: {1: 2, 2: 2, 3: 2, 4: 1, 5: 1}

def countuniques(list):
    dict={}
    for ele in list:
        if ele not in dict:
            dict[ele] = 1
        else:
            dict[ele]+=1
    return dict

print(countuniques([1, 2, 3, 2, 1, 4, 3, 5]))        


# Exercise 7:
# Write a Python function that takes two lists of equal length as input and returns a dictionary containing elements from the first list as keys and elements from the second list as values.

# Example:
# Input: ["a", "b", "c"], [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}

def makingdictwith2list(keys,values):
    dict={}
    
    for i in range(len(keys)):
        dict[keys[i]]=values[i]
       
    return dict

l1=["a", "b", "c"]
l2=[1,2,3]
print(makingdictwith2list(l1,l2))


##exercise 8
def mapingnoncaseing(list):
    dict={}
    for string in list:
        s=string.lower()
        if s not in dict:
            dict[s]=1
        else:
            dict[s]+=1
            
    return dict

print(mapingnoncaseing(["Hello", "hello", "world", "world", "python", "Python"]))
##exercise 9
def avgcountandtotalcount(list):
    newdict={}
    sum=0
    for dict in list:
      sum+=dict["age"]
    
    newdict["total_people"]=len(list)
    newdict["avgAge"]=round(sum/len(list),2)
    
    return newdict

print(avgcountandtotalcount([ {"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 28} ]))
# Input: {"apple": 1.5, "banana": 2.0, "cherry": 1.2, "pear": 1.8}
# Output: "banana"
##exercise 10
def findexpensivefood(dict):
    max=float("-inf")
    k=0
    for key,value in dict.items():
        if value>max:
            max=value
            k=key
    
    return  k

print(findexpensivefood({"apple": 1.5, "banana": 2.0, "cherry": 1.2, "pear": 1.8}))