#!/usr/bin/python3
"""
Script that fetches employee TODO list progress from REST API
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        sys.exit(1)
    
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    # Get employee's todos
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        sys.exit(1)
    
    todos_data = todos_response.json()
    
    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    
    # Print the required format
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    
    # Print completed task titles with proper formatting
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
