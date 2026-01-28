# student_records.py

students = []


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully.")


def update_student():
    roll = input("Enter roll number to update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")
            student["marks"] = float(input("Enter new marks: "))
            print("Record updated.")
            return

    print("Student not found.")


def display_students():
    if not students:
        print("No records available.")
        return

    for s in students:
        print(s)


while True:
    print("\n1. Add Student")
    print("2. Update Student")
    print("3. Display Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        display_students()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
