#!/usr/bin/python3
"""
Script that exports employee TODO list to CSV format
"""

import csv
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
        
        # Create CSV file
        filename = "{}.csv".format(employee_id)
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            
            for todo in todos_data:
                writer.writerow([
                    str(employee_id),
                    username,
                    str(todo['completed']),
                    todo['title']
                ])
                
    except:
        exit()
