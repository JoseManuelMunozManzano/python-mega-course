import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


# Para ejecutar:
# streamlit run web.py [ARGUMENTS]
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # Se borra ese to-do también de la sesión
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Add a Todo", label_visibility='hidden', placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# Descomentar para ver en la web el diccionario de st
# st.session_state
