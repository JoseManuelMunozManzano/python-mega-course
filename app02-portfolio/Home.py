# streamlit run Home.py
import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("José Manuel Muñoz Manzano")
    content = """
    Hi, I am Jose Manuel! I am a RPG, Java, JavaScript and Python developer. 
I have experience with DB2 and MySql databases.
I have worked with companies such as ATOS and A.M.A. and currently I'm working in Diners Club.
I really love to code!
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have build in Python. Feel free to contact me!
"""
st.text(content2)

# Se pasa la ratio dimension de las columnas. La primera columna será 3 veces más ancha que la columna del medio.
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])