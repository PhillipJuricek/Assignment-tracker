from datetime import datetime as dt
import numpy as np
import json as js

#list to store assignment
assignments = []
gi
class assignment:
    def __init__(self, name, subject, due_date, weight, priority, completion=False):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.completion = completion
        self.subject = subject
        self.weight = weight

    def calculate_priority(self):

        days_remaining = (self.due_date - dt.now()).days

        days_remaining = max(days_remaining, 1)

        return self.weight / days_remaining

    
    def mark_completed(self):
        
        self.completion = True
    
    def __str__(self):
        status = 'Completed' if self.completion else "due"
        return (f"Assignment: {self.name}\n" 
        f"Subject: {self.subject}\n" 
        f"Due:{self.due_date.strftime('%Y-%m-%d')}\n" 
        f"Weight: {self.weight}\n" 
        f"priority: {self.priority:.2f}\n" 

        f"Status: {status}\n")

#add assignment function
def get_date(prompt):
    while True:
        date_str = input(prompt)
        try:

            return dt.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print('invalid date format. Please use  YYYY-MM-DD.')

def add_assignment():
    name = input('Enter assignment name: ')
    subject = input('Enter subject: ')
    due_date = get_date('Enter due date (YYYY-MM-DD): ')
    weight = float(input('Enter weight: (%) '))

    new_assignment = assignment(name, subject, due_date, weight, priority=0)

    new_assignment.priority = new_assignment.calculate_priority()

    assignments.append(new_assignment)
    print('Assignment added succssfully!')
    print(assignments[0])

def sort_assignments():
    assignments.sort(key=lambda x: x.priority, reverse=False)
    
#view function
def view_assignments():
    if not assignments:
        print("No assignments found.")
    else:

        sorted_assignments = assignments.sort(key=lambda x: x.priority, reverse=True)
        sort_assignments() #sort by priority
        for i, assignment in enumerate(assignments, 1):
            print(f"{i}. {assignment}")



def view_assignments_by_subject():
    subject = input('enter subject to filter by: ')
    filtered_assignments = [a for a in assignments if a.subject.lower() == subject.lower()]
    if not filtered_assignments:
        print(f"No assignments found for {subject}")
    else:
        for i, assignment in enumerate(filtered_assignments, 1):
            print(f"{i}. {assignment}")
    
def mark_completed():
    view_assignments()
    try:
        index = int(input('Enter the number of the assignment to mark as completed: ')) - 1
        assignments[index].completed = True
        print("Assignment marked as completed!")
    except (IndexError, ValueError):
        print("Invalid Input.")

def delete_assignment():
    view_assignments()
    try:
        index = int(input('Enter the number of the assignment to delete: ')) - 1
        assignments.pop(index)
        print('Assignment deleted!')
    except (IndexError, ValueError):
        print('Invalid input.')

#file saving function
def save_assignments():
    with open("assignments.json", "r") as file:
        json.dump([a.__dict__ for a in assignments], file)

#function to load assignments from a file
def load_assignments():
    try:
        with open("assignments.json", "r") as file:
            data = json.load(file)
            assignments.clear()
            for item in data:
                assignment = assignment(item["name"], item["subject"], item["due_date"], item["weight"])
                assignmment.completed = item["completed"]
                assignments.append(assignment)
    except FileNotFoundError:
        print("No saved assignments found.")

#function to check for reminders
def check_reminders():
    today = dt.today().date()
    for assignment in assignments:
        due_date = datetime.strptime(assignment.due_date, "%Y-%m-%d").date()
        if due_date == today and not assignment.completed:
            print(f"reminder: {assignment.name} is due today!")

#main menu function
def main_menu():
    while True:
        print("\n--- Assignment Tracker ---")
        print("1. Add Assignment")
        print("2. View all Assignments")
        print("3. View Assignments by Subject")
        print("4. Mark assignment as completed")
        print("5. Delete assignment")
        print("6. Check Reminders")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
           add_assignment()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            view_assignments_by_subject()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            delete_assignment()
        elif choice == "6":
            check_reminders()
        elif choice == "7":
            print("Exiting...")
        else:
            print("Invalid Input. Try again.")

#load assignments when code starts
load_assignments()

#run main menu

if __name__ == "__main__":
    main_menu()
    save_assignments()