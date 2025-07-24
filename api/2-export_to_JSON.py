#!/usr/bin/python3
"""
Script that exports employee TODO list to JSON format
"""

import json
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
        username = user_data['username']
        
        # Get employee's todos
        todos_url = "{}/todos?userId={}".format(base_url, employee_id)
        todos_response = requests.get(todos_url)
        
        if todos_response.status_code != 200:
            exit()
        
        todos_data = todos_response.json()
        
        # Create data structure for JSON
        user_tasks = []
        for todo in todos_data:
            task_data = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
            user_tasks.append(task_data)
        
        # Create final JSON structure
        json_data = {str(employee_id): user_tasks}
        
        # Write to JSON file
        filename = "{}.json".format(employee_id)
        with open(filename, 'w') as jsonfile:
            json.dump(json_data, jsonfile)
                
    except:
        exit()
