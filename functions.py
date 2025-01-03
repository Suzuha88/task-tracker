import os
import json
from datetime import datetime



def get_data(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w") as file:
            file.write("[]")
            data = []
    else:
        with open(path, "r") as file:
            data = json.load(file) 
    return data
 


def add(data, message):
    time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    new_task = {
        "id": len(data) + 1,
        "description": message,
        "status": "todo",
        "createdAt": time,
        "updatedAt": time
    }

    data.append(new_task)


def update(data, id, message):
    time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    
    data[id - 1]["description"] = message
    data[id - 1]["updatedAt"] = time




def delete(data, id):
    del data[id - 1]

def mark_in_progress(data, id):
    time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    data[id - 1]["status"] = "in-progress"
    data[id - 1]["updatedAt"] = time

def mark_done(data, id):
    time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    data[id - 1]["status"] = "done"
    data[id - 1]["updatedAt"] = time


def list_all(data, category=None):
    for i, todo in enumerate(data):
        todo["id"] = i + 1
        
        if not category or category == todo["status"]:
            print(todo)


