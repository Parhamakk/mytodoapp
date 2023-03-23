import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todoo = st.session_state["new_todo"]+'\n'
    todos.append(todoo)
    functions.write_todos(todos)


st.title("ToDoList")
st.subheader("Increase of productivity")
st.write(':)')
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder='add a todo...',
              on_change=add_todo, key="new_todo")
