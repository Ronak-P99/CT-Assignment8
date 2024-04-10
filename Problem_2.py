'''
2. Advanced Data Handling with Python
Objective:
The aim of this assignment is to deepen your knowledge and practical skills in handling complex data structures using Python. 
You will work on real-world inspired tasks that require advanced manipulation of dictionaries, nested collections, 
and implementing custom functions for specific data processing needs.

Task 1: Hotel Room Booking Tracker
Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

Problem Statement:
Develop a program that:

Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
Implement functions to:
Book a room (mark as booked and assign to a customer).
Check-out a customer (mark room as available and remove customer name).
Display the status of all rooms.
Start with this initial hotel room structure:

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

Task 2: E-commerce Product Search Feature
Put your data handling and string manipulation skills to the test by creating a product search feature for an e-commerce platform.

Problem Statement:
Create a system that:

Holds a dictionary of products where each product has attributes like name, category, and price.
Implement a search function that allows searching for products by name, returning a list of matching products (case-insensitive search).
Handle cases where no matches are found.
Example product dictionary:

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}
'''

def add_room(hotel, room_number, customer):
    status = "available"
    if room_number not in hotel:
        hotel[room_number] = {"status": "booked", "customer": customer}
    else:
        print("Room already exists!")

def check_out(hotel, room_number):
    status = "available"
    if room_number in hotel:
        hotel[room_number] = {"status": status, "customer": ""}
    else:
        print("No one is in the room!")

def display(hotel):
    for room_number, status in hotel.items():
        print(f"ROOM: {room_number}:")
        for availability, stat,  in status.items():
            print(f"{availability}: {stat}")

def search_product(catalog, product):
    found = False
    laptop = ["intel", "dell", "mac"]
    shirt = ["nike", "hollister", "northface"]

    for category, products in catalog.items():
        for name, cat in products.items():
            if product.lower() in str(cat).lower():
                if product.lower() == "laptop":
                    laptops = ', '.join(laptop)
                    print(f"Product: '{product}' found. Some products include: {laptops}.")                    
                    found = True
                    break
                
                elif product.lower() == "shirt":
                    shirts = ', '.join(shirt)
                    print(shirts)
                    print(f"Product: '{product}' found. Some products include: {shirts}.")
                    found = True
                    break
    if not found:
        print(f"Product: {product} not found!")


hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

add_room(hotel_rooms, "103", "Ronak Patel")
check_out(hotel_rooms, "102")
display(hotel_rooms)

#Task 2
products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

search_product(products, "laptop")
