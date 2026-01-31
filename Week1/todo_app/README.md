# 📝 To-Do List Mini Application

This is a simple **To-Do List mini application** built using **Python and Streamlit**.

The purpose of this project is to apply the Python concepts learned so far, not to build a full-scale product.

---

## 🎯 Objective

- Practice Python programming concepts
- Apply basic Object-Oriented Programming (OOP)
- Use file handling to store data
- Handle common runtime errors
- Create a simple single-page Streamlit interface

---

## ✅ Concepts Demonstrated

- Functions
- Classes & Objects
- Basic OOP design
- File handling (read/write)
- Error handling (`try / except`)
- Clean and readable Python code
- Basic Streamlit integration

---

## 📁 Project Structure

todo_app/
│
├── app.py # Streamlit application
├── task.py # Task class (OOP)
├── storage.py # File handling logic
└── tasks.txt # Stores tasks

---

## 📘 File Description

### `app.py`
- Main Streamlit application
- Single-page interface
- Allows adding and viewing tasks

### `task.py`
- Contains the `Task` class
- Demonstrates basic OOP concepts

### `storage.py`
- Handles saving and loading tasks from file
- Includes error handling

### `tasks.txt`
- Stores tasks persistently
- Automatically created/updated

---

## ▶️ How to Run the Application

### 1️⃣ Install Streamlit
pip install streamlit
2️⃣ Run the app

Copy code
streamlit run app.py