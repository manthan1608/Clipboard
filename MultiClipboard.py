import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


def save_items(filepath, data):
    with open(filepath,"w")as f:
        json.dump(data,f)


def load_items(filepath):
    try:
        with open(filepath,"r")as f:
            data = json.load(f)
            return data
    except:
        return{}


#print(sys.argv) # everything after python all the command line arguements

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA,data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist")
    elif command == "deletedata":
        key = input("Enter a key: ")
        if key in data:
            data[key] = ''
            save_items(SAVED_DATA,data)
            print("Data deleted")
        else:
            print("Key does not exist")

    elif command == "deletekey":
        key = input("Enter a key: ")
        if key in data:
            data.pop(key)
            save_items(SAVED_DATA,data)
            print("Key deleted")
        else:
            print("Key does not exist")

    elif command == "deleteeverything":
        data.clear()
        clipboard.copy("")
        save_items(SAVED_DATA,data)
        print("Everything Deleted")

    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command")