# streamlit run main.py
import streamlit as st
import requests
import os

api_key = os.getenv("API_KEY_NASA")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)
data = response.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# download de image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.header(title)
st.image(image_filepath)
st.write(explanation)
