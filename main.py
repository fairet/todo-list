__version__ = (0, 0, 1)

import json

def main():
    with open('tasks.json', 'w') as file:
        data = """{"tasks": {"task11": "Лол","Task2": "xz"}}"""
        json.dump(data, file, indent=2, ensure_ascii=True)

    with open('tasks.json', 'r') as file:
        parsed_data = json.load(file) 


    print(parsed_data["tasks"])

def parse_tasks():

    with open('tasks.json', 'r') as file:
        parsed_data = json.load(file) 

    file.close()
    return parsed_data["tasks"]


if __name__ == '__main__':
    main()
