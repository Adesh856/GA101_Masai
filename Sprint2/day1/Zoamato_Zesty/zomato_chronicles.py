import json


with open("./data.json","r") as file:
    JsonData=json.load(file)
    menu=JsonData["menu"]
    orders=JsonData["orders"]
       
    
def display_menu(menu):
 
    print("\n----------Menu------------|||")  
    for dish in menu: 
         print("\n"+"ID :"+dish["dish_id"])
         print("name :"+dish["name"])
         print("price :"+ str(dish["price"]))
         print("availability :"+('Yes' if dish["availability"] else 'No'))
           
    print("------------------------------|||")        
 
        
def add_dish(menu):
    new_dish = {}
    new_dish["dish_id"] = input("Enter dish ID: ")
    new_dish["name"] = input("Enter dish name: ")
    new_dish["price"] = float(input("Enter dish price: "))
    new_dish["availability"] = input("Is the dish available? (yes/no): ").lower() == "yes"
    
    menu.append(new_dish)
    print("Dish has been added to the menu")

def remove_dish(menu):
    display_menu(menu)  # Display the menu first

    dish_id_to_remove = input("Enter the dish ID to remove: ")
    for dish in menu:
        if dish["dish_id"] == dish_id_to_remove:
            menu.remove(dish)
            print(f"Dish with ID {dish_id_to_remove} removed from the menu.")
            break
    else:
        print(f"No dish with ID {dish_id_to_remove} found.")

# Call the remove_dish function to remove a dish from the menu

def update_availability(menu):
    display_menu(menu)  # Display the menu first

    dish_id_to_update = input("Enter the dish ID to update availability: ")
    new_availability = input("Is the dish available? (yes/no): ").lower() == "yes"

    for dish in menu:
        if dish["dish_id"] == dish_id_to_update:
            dish["availability"] = new_availability
            print(f"Availability of dish {dish_id_to_update} updated.")
            break
    else:
        print(f"No dish with ID {dish_id_to_update} found.")


def take_order(menu,orders):
    display_menu(menu)
    customer_name=input("Enter customer's name: ")
    order_dish_ids = input("Enter dish IDs (comma-separated): ").split(',')
    print(order_dish_ids)
    order={"customer_name":customer_name,"order_dishes_id":[]}
    for order_id in order_dish_ids:
        for dish in menu:
            if dish["dish_id"]==order_id.strip() and dish["availability"]:
                order["order_dishes_id"].append(dish)
                break
        else:  
            print(f"Invalid or unavailable dish ID: {order_id.strip()}")
    
    if order["order_dishes_id"]:
        order["order_id"]=len(order)+1
        order["status"]="received"
        print(order)
        orders.append(order)
        updatedata(orders) 
        print("Order placed successfully!")
    else:
        print("Order could not be placed due to invalid or unavailable dish IDs.") 

def update_order_status(orders):
    print("\n----------Orders------------")  
    for order in orders:
        print(f"\nOrder ID: {order['order_id']}")
        print(f"Customer: {order['customer_name']}")
        print("Ordered Dishes:")
        for dish in order["order_dishes_id"]:
            print(f"- {dish['name']}")

        print(f"Status: {order['status']}")

    order_id_to_update = int(input("Enter the order ID to update status: "))
    new_status = input("Enter the new status for the order: ")

    for order in orders:
        if order["order_id"] == order_id_to_update:
            order["status"] = new_status
            print(f"Status of order {order_id_to_update} updated.")
            updatedata(orders) 
            break
    else:
        print(f"No order with ID {order_id_to_update} found.")




def updatedata(orders=orders,menu=menu):
    JsonData["menu"] = menu
    JsonData["orders"] = orders
    
    with open("./data.json", "w") as file:
        json.dump(JsonData, file, indent=4)      
    
updatedata()    
    
def main():    
    while True:
        print("\n===== Zomato Chronicles: The Great Food Fiasco =====")
        print("1. Display Menu")
        print("2. Add Dish")
        print("3. Remove Dish")
        print("4. Update Dish Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ")
        
        if choice == "1":
            display_menu(menu)
        elif choice == "2":
            add_dish(menu)
        elif choice == "3":
            remove_dish(menu)
        elif choice == "4":
            update_availability(menu)
        elif choice == "5":
            take_order(menu, orders)
        elif choice == "6":
            update_order_status(orders)
        elif choice == "7":
            print("Exiting Zomato Chronicles. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")    

main()        