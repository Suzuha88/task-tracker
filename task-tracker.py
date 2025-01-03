import os
import json
import sys
from datetime import datetime


def main():
    data = getData("tasks.json")          
    command = sys.argv[1]

    with open("tasks.json", "w") as file:

        if command == "add":
            add(data, sys.argv[2])
        if command == "update":
            update(data, int(sys.argv[2]), sys.argv[3])
        if command == "delete":
            delete(data, int(sys.argv[2]))
        if command == "mark-in-progress":
            markInProgress(data, int(sys.argv[2]))
        if command == "mark-done":
            markDone(data, int(sys.argv[2]))
        if command == "list":
            if len(sys.argv) > 2:
                list_all(data, sys.argv[2])
            else:
                list_all(data)

        json.dump(data, file)

def getData(path):
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

def markInProgress(data, id):
    time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    data[id - 1]["status"] = "in-progress"
    data[id - 1]["updatedAt"] = time

def markDone(data, id):
    time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    data[id - 1]["status"] = "done"
    data[id - 1]["updatedAt"] = time


def list_all(data, category=None):
    for i, todo in enumerate(data):
        todo["id"] = i + 1
        
        if not category or category == todo["status"]:
            print(todo)



if __name__ == "__main__":
    main()
