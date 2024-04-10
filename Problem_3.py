'''
3. Python Programming Challenges for Customer Service Data Handling
Objective:
This assignment is designed to test and enhance your Python programming skills, 
focusing on real-world applications in customer service data management. You will practice correcting code, 
organizing customer data, and implementing a feedback system using Python dictionaries.

Task 1: Customer Service Ticket Tracker
Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement:
Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
'''
def new_ticket(tickets, ticket_num, name, issue):
    if ticket_num not in tickets:
        tickets[ticket_num] = {f"Customer": name, "Issue": issue, "Status": "open"}
        print(f"Ticket for {name} has been made!")
    else:
        print("Ticket already exists!")

def update_tix(tickets, ticket_num, stat, close):
    tickets[ticket_num].update({stat: close})

def display_tix(tickets):
    print("\nCurrent Tickets:")
    for tix, key in tickets.items():
        print(f"\n{tix}:")
        for stats, info, in key.items():
            print(f"{stats}: {info}")


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

new_ticket(service_tickets, "Ticket003", "Ronak", "very slow")
update_tix(service_tickets, "Ticket001", "Status", "closed")
display_tix(service_tickets)