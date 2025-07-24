#!/usr/bin/python3
"""
Script that fetches employee TODO list progress from REST API
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        exit()
    
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:
        # Get employee information
        user_url = "{}/users/{}".format(base_url, employee_id)
        user_response = requests.get(user_url)
        
        if user_response.status_code != 200:
            exit()
        
        user_data = user_response.json()
        employee_name = user_data['name']
        
        # Get employee's todos
        todos_url = "{}/todos?userId={}".format(base_url, employee_id)
        todos_response = requests.get(todos_url)
        
        if todos_response.status_code != 200:
            exit()
        
        todos_data = todos_response.json()
        
        # Calculate completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = []
        
        for todo in todos_data:
            if todo['completed'] is True:
                completed_tasks.append(todo)
        
        number_of_done_tasks = len(completed_tasks)
        
        # Print the required format
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_tasks))
        
        # Print completed task titles with proper formatting
        for task in completed_tasks:
            print("\t {}".format(task['title']))
            
    except:
        exit()
