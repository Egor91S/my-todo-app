import streamlit as st
import functions

todos = functions.read_todo()
"""Give variable to the existing list"""

"""Define a new function by (session_state)(share variables between reruns)
where we return value from the st.text_input key and append to the list"""


def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")
"""remove an item from the list both from the text file and session state"""
for index, i in enumerate(todos):
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        todos.pop(index)  # remove from the text file
        functions.write_todo(todos)
        del st.session_state[i]  # remove from the session state
        st.experimental_rerun()

st.text_input(label="rrr", label_visibility="hidden", placeholder="Enter a todo",
              on_change=add_todo,
              key="new todo")

st.session_state
