### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.

list =[1,2,3,4,5]
bag=""
for j in range(len(list)):
        bag+=str(list[j])+" "
        print(bag)
    
    
### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num>150:
        continue
    if num>500:
        break
    if num%5==0:
        print(num)
    
    
  ### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`. 
s1 = "Ault"
s2 = "Kelly"

midindex=len(s1)//2
newstring=s1[:midindex]+s2+s1[midindex:] 
print(newstring)


# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

str1 = "PyNaTive"
lc=""
uc=""
for s in str1:
    if s.islower():
        lc+=s
    else:
        uc+=s
        
print(f"{lc}{uc}")            


# Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
newlist=[]
for i in range(0,len(list1)):
    newlist.append(f"{list1[i]}{list2[i]}")

print(newlist)    


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
li=[]
for i in list1:
    bag=""
    for j in list2:
       li.append( f"{i} {j}")

print(li)        


# Problem 7: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

for i in range(len(list1)):
    print(f"{list1[i]} {list2[i]}")


#problem:-8
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
newdict={}
for name in employees:
    newdict[name]=defaults
    
print(newdict)    


##problem 9
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
sample_dict_output={}

for key,value in sample_dict.items():
    if key is "name" or key is "salary":
        sample_dict_output[key]=value
        
print(sample_dict_output)        
        
        # Problem 10: Modify the tuple

tuple1 = (11, [22, 33], 44, 55)
for ele in tuple1:
    if isinstance(ele, list):
         ele[0]=222
      
print(tuple1)       




 
        



