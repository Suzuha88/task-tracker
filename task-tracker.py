import json
import sys

import functions


def main():
    data = functions.get_data("tasks.json")
    command = sys.argv[1]

    with open("tasks.json", "w") as file:

        if command == "add":
            functions.add(data, sys.argv[2])
        if command == "update":
            functions.update(data, int(sys.argv[2]), sys.argv[3])
        if command == "delete":
            functions.delete(data, int(sys.argv[2]))
        if command == "mark-in-progress":
            functions.mark_in_progress(data, int(sys.argv[2]))
        if command == "mark-done":
            functions.mark_done(data, int(sys.argv[2]))
        if command == "list":
            if len(sys.argv) > 2:
                functions.list_all(data, sys.argv[2])
            else:
                functions.list_all(data)

        json.dump(data, file)


if __name__ == "__main__":
    main()
