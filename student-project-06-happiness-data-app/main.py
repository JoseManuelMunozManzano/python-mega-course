import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))
st.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv("happy.csv")

figure = px.scatter(data_frame=df,
                    x=df[f"{x_axis.lower()}"],
                    y=df[f"{y_axis.lower()}"],
                    labels={"x": f"{x_axis}", "y": f"{y_axis}"})
st.plotly_chart(figure)
