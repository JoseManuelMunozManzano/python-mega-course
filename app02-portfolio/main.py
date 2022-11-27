# streamlit run main.py
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

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])