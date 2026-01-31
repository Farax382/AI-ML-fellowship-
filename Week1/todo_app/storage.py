FILE_NAME = "tasks.txt"


def save_task(task):
    try:
        with open(FILE_NAME, "a") as file:
            file.write(str(task) + "\n")
    except Exception as e:
        print("Error saving task:", e)


def load_tasks():
    tasks = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

    return tasks
