import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return {int(k): v for k, v in data.items()}
    except FileNotFoundError:
        return {}


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)