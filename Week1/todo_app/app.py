import streamlit as st
from task import Task
from storage import save_task, load_tasks

st.title("📝 To-Do List Mini App")

menu = st.radio("Menu", ["Add Task", "View Tasks"])

if menu == "Add Task":

    st.subheader("Add New Task")

    title = st.text_input("Task Title")

    if st.button("Save Task"):
        if title.strip() == "":
            st.warning("Task title cannot be empty")
        else:
            task = Task(title)
            save_task(task)
            st.success("Task saved successfully")

elif menu == "View Tasks":

    st.subheader("Your Tasks")

    tasks = load_tasks()

    if tasks:
        for i, task in enumerate(tasks, start=1):
            st.write(f"{i}. {task}")
    else:
        st.info("No tasks found")
