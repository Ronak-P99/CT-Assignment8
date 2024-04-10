'''
4. Python Essentials for Business Analytics

Objective:
This assignment aims to strengthen your proficiency in Python by tackling challenges that simulate real-world business analytics scenarios. 
You'll practice copying dictionaries, utilizing built-in methods, managing nested collections, and implementing try-except blocks for error handling.

Task 1: Sales Data Cloning and Modification
Gain practical experience in copying dictionaries and modifying data, crucial skills in data analysis.

Problem Statement:
You have a dictionary representing weekly sales data for a store. 
Your task is to create a deep copy of this data and update the sales figures for a specific week.

Given Sales Data:

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

Create a deep copy of weekly_sales.
Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.
'''
import copy

def deep_copy_sales(sales):
   copy_sales = copy.deepcopy(sales)
   return copy_sales

new_sale = 18000
week = "Week 2"
category = "Electronics"

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

new_weekly_sales = deep_copy_sales(weekly_sales)
weekly_sales[week].update({category: new_sale})

print(new_weekly_sales)
print(weekly_sales)