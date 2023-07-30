import requests
import tkinter as ttk
import ttkbootstrap as ttk
from fontTools.ttLib import TTFont

URL = "https://api.quotable.io/random?tags=technology"

def select_font(type):
    font_path = f"assets/fonts/Poppins-{type}.ttf"
    my_font = TTFont(font_path) 
    return my_font

def get_quote():
    response = requests.get(URL)
    data = response.json()
    quote = data["content"]
    author = data["author"]
    return quote, author

def update_quote():
    quote, author = get_quote()
    quote_label.config(text=quote)
    author_label.config(text=f"~{author}")

root = ttk.Window(themename="vapor")
root.title("Quote.py")
root.geometry("700x250")

frm = ttk.Frame(root)
frm.pack(padx=30, pady=40)

quote_label = ttk.Label(frm, text="", font=(select_font("Medium"), 16), wraplength=650)
quote_label.pack()

author_label = ttk.Label(frm, text="", font=(select_font("Regular"), 12))
author_label.pack(pady=10)

ttk.Button(frm, text="Get Quote", command=update_quote).pack(pady=20)

root.mainloop()
