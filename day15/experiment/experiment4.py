# Modulos starndard importantes:
# webbrowser -Easy-to-use controller for web browsers.

import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")

webbrowser.open(f"https://google.com/search?q={user_term}")
