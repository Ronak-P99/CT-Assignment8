'''
1. Real-World Python Dictionary Applications
Objective:
The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, 
and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, 
demonstrating your ability to manipulate and manage complex data structures.

Task 1: Restaurant Menu Update
You are given an initial structure of a restaurant menu stored in a nested dictionary. 
Your task is to update this menu based on given instructions. 
This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

Problem Statement:
Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
Add a new category called "Beverages" with at least two items.
Update the price of "Steak" to 17.99.
Remove "Bruschetta" from "Starters".
'''

def add_category(catalog, category):
    if category not in catalog:
        catalog[category] = {}
        print(f"Category: {category} added!")
    else:
        print(f"Category: {category} already exists!")

def add_product(catalog, category, product):
    if category in catalog:
        if product not in catalog[category]:
            catalog[category][product] = 1.99
            print(f"Bev added is {product} to {category}")
        else:
            print(f"{product} already exists in {category}")
    else:
        print(f"The category: {category} does not exist!")



restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

add_category(restaurant_menu, "Beverages")
add_product(restaurant_menu, "Beverages", "Coke")
add_product(restaurant_menu, "Beverages", "Sprite")

user_settings = {"Main Course": {"Steak": 17.99, "Salmon": 13.99}}
restaurant_menu.update(user_settings)
restaurant_menu['Starters'].pop("Bruschetta")


print(restaurant_menu)