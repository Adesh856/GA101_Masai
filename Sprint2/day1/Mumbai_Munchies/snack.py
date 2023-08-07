import json

## Step 1:- Implementing Object formation Snack 
#-----------------------------------------------------------------------
class Snack:
    def __init__(self,snack_id,name,price,availability) -> None:
        self.snack_id=snack_id
        self.name=name
        self.price=price
        self.availability=availability
     
#-----------------------------------------------------------------------     

#Step2:- Implement Inventory Managment
#-----------------------------------------------------------------------        
def load_inventory():
    try:
     with open("./snack_inventory.json","r") as jsonfile:
         Jsonloadedlist=json.load(jsonfile)
         return Jsonloadedlist
    except FileNotFoundError:
        return []
     
def check_inventory():
    try:
     with open("./snack_inventory.json","r") as jsonfile:
         Jsonloadedlist=json.load(jsonfile)
       
         print("\n----------Inventory------------")  
         for snack in Jsonloadedlist:
            print("\n"+"ID :"+snack["snack_id"])
            print("name :"+snack["name"])
            print("price :"+str(snack["price"]))
            print("availability :"+snack["availability"])
           
     print("----------------------")        
    except FileNotFoundError:
        print("File not found")
 
     
def add_snack():
    Inventory=load_inventory() 
    
    snack_id = input("Enter Snack ID: ")
    name = input("Enter Snack Name: ")
    price = float(input("Enter Snack Price: "))
    availability = input("Is Snack Available? (yes/no): ")
    new_snack=Snack(snack_id,name,price,availability.lower())
    
    Inventory.append(new_snack.__dict__)
    save_inventory(Inventory)
    print("Snack added to inventory!")
    
    
    
def save_inventory(inventory_data):
        with open("./snack_inventory.json","w") as jsonfile:
            json.dump(inventory_data,jsonfile,indent=4)
           
           

         
def remove_snack():
    Inventory = load_inventory()
    snack_id = input("Enter snack ID for Deleting: ")

    updated_inventory = [item for item in Inventory if item["snack_id"] != snack_id]
    
    if len(updated_inventory) < len(Inventory):
        print("Snack removed from inventory.")
        save_inventory(updated_inventory)
    else:
        print("Snack not found in inventory.")
   
       
       
       

def update_availability():
    inventory = load_inventory()
    
    snack_id_to_update = input("Enter Snack ID to update availability: ")
    new_availability = input("New Availability (yes/no): ")
    
    for snack in inventory:
        if snack["snack_id"] == snack_id_to_update:
            snack["availability"] = new_availability.lower()
            print("Snack availability updated!")
            save_inventory(inventory)
            return
    
    print("Snack not found in inventory.")          
 
 

#-----------------------------------------------------------------------    

#Step3:-Implement Sales Tracking

def load_sales_record():
    try:
        with open("./salesrecord.json","r") as salesfile:
            SalesJsondata=json.load(salesfile)
            return SalesJsondata
    except FileNotFoundError:    
          return {}
    

def record_sale(snack_id, quantity_sold):
    sales_record=load_sales_record()
    Inventory=load_inventory()
    
    for snack in Inventory:
        if snack["snack_id"]==snack_id:
            if snack["availability"]=="yes" and quantity_sold>0:
                if snack_id not in sales_record:
                    sales_record[snack_id]=quantity_sold
                else:
                      sales_record[snack_id]+=quantity_sold   
                save_inventory(Inventory) 
                save_sales_record(sales_record)
                print("Sale recorded successfully!")
                return
            else:
                print("Snack not available or invalid quantity.")
                return   

def save_sales_record(sales_record_data):
    with open('./', 'w') as file:
        json.dump(sales_record_data, file, indent=4)        
        
        
        
def main():
    while True:
        print("\n===== Canteen Snack Inventory Management =====")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Availability")
        print("4. Check Inventory")
        print("5. Record Sale")
        print("6. Quit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
         add_snack()  
        elif choice == "2":
           remove_snack()
        elif choice == "3":
            update_availability() 
        elif choice == "4":
            check_inventory()   
        elif choice == "5":
            snack_id = input("Enter Snack ID sold: ")
            quantity_sold = int(input("Enter Quantity Sold: "))
            record_sale(snack_id, quantity_sold)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()        