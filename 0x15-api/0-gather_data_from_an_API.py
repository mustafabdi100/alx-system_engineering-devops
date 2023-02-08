#!/usr/bin/python3
import requests as rq
import sys
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""

users=rq.get("https://jsonplaceholder.typicode.com/users").json()
tasks=rq.get("https://jsonplaceholder.typicode.com/todos").json()

userid=int(sys.argv[1])
total_tasks = 0
completed =0
pending=0
users_id_by_name={}
completed_title=[]

for i in users:
	users_id_by_name[i['id']]=i['name']

for task in tasks:
	if task['userId']==userid:
		total_tasks+=1
		if task['completed']==False:
			pending+=1
		else:
			completed+=1
			completed_title.append(task['title'])

print(f"Employee {users_id_by_name[userid]} is done with tasks({completed}/{total_tasks}):")
for i in completed_title:
    print(f'\t {i}')


