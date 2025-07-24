#!/usr/bin/python3
"""
Script that exports all employees TODO lists to JSON format
"""

import json
import requests

if __name__ == "__main__":
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:
        # Get all users
        users_url = "{}/users".format(base_url)
        users_response = requests.get(users_url)
        
        if users_response.status_code != 200:
            exit()
        
        users_data = users_response.json()
        
        # Get all todos
        todos_url = "{}/todos".format(base_url)
        todos_response = requests.get(todos_url)
        
        if todos_response.status_code != 200:
            exit()
        
        todos_data = todos_response.json()
        
        # Create dictionary to store all user data
        all_users_data = {}
        
        # Process each user
        for user in users_data:
            user_id = str(user['id'])
            username = user['username']
            
            # Find todos for this user
            user_todos = []
            for todo in todos_data:
                if todo['userId'] == user['id']:
                    task_data = {
                        "username": username,
                        "task": todo['title'],
                        "completed": todo['completed']
                    }
                    user_todos.append(task_data)
            
            all_users_data[user_id] = user_todos
        
        # Write to JSON file
        filename = "todo_all_employees.json"
        with open(filename, 'w') as jsonfile:
            json.dump(all_users_data, jsonfile)
                
    except:
        exit()
