with open("./take.txt","r") as file:
    content=file.read()

print(content)    

with open("./put.txt","w") as writefile:
    writefile.write(content)
    
print("Copied succesfully")    
with open("./put.txt","a") as appendfile:
    appendfile.write("\nHey this is Adesh")          
    
print("Added my name suucesfully")     



try:
   with open("./create.txt","x") as appendfile:
    appendfile.write("\nHey this is Adesh")
    print("file has been created and content has been added into it")        
except FileExistsError:
        print("File already exists")