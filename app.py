import streamlit as st # type: ignore

st.title("To-Do List")

tasks = []  # Empty list

task = st.text_input("Enter new task")
if st.button("Add Task") and task:
    tasks.append(task)

st.write("Your tasks:")
for i, task in enumerate(tasks):
    if st.checkbox(f"{i+1}. {task}"):
        tasks.pop(i)
        st.experimental_rerun()  # To update the list