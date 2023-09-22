#                      .                    .                           
#                 :-:--=:-:::.             :=-**##*=:                   
#                  :=----------.         .-%@@@@@@@@@%:                 
#                 :-------------:        :@@@@@@@@@@@@%.                
#                :-=-----------==:       +@@@@@@@@@@@@@#                
#              .------------=------.     =@@@@@@@@@@@@@#                
#               :=-=-------===-=--      .+%@@@@@@@@@@@#=                
#                --=--------==-=-.       -*%@@@@@@@@@*-.                
#                   ::----===+-             .#%@@@@*.                   
#                      -+++=: .               :+##+                     
#                     -+=====.              .=%@@%%%#=                  
#                  :-----------:.        :+#%%%@@@@@%@%+-               
#                -----------------      -%%%%%@@@%@@%%@%%*              
#               .-==----------==--:     #%%%@%@@@@@@@@@@%%.             
#               :-=+----------*=---    =%%%@@%%@@@%%@@@%%%=             
#               ---=----------*----:  .#%%%@@%%@@@%@%@@%%%%             
#              :-===----------+=---=  -#%%%@@%%@%@%@%@@%%%%=            
#                --=----------=#==+.   ==+%@@%%@@@%@%@@*++.             
#                --=-----------*=---  :===#@@%%@@@%@%%%--=              
#                -==-----------++--=  ---:#@%@@@%%%@@@%--=              
#                -=------------=:--=. =-- %@%%%%%%@%%%@=-=              
#               .-+-------------.:---.--: %%%%%%%%@%%@@+==              
#               :-++*++++++*+***. --=+--  *###########**-=              
#               --*+++++++++*+++: :--*-: :------=------*-=              
#               =-*++++++++*+***- .--*-. :-------------+-=              
#              .--*+++=+*++*+***+ :==*=: -------=------===:             
#              :=+++++==+++*++**+ -*++=. -------+-------+=:             
#               -++++=+==**+++***  :-:   -------+-------+.              
#                -+++=++=****+**#        -------+=------=               
#                .++==*=---=*+**+        =------+*------=               
#                 ----=    :---=          ====-.::+====                 
#            :**#==---=:   ----= ..   .:::=--=+*%#*--=+***. .--:..      
#            .=+**#=--==   :=--=%@*:.-=+%%*--=: ::+=--+***+=#@%*-=-::.  
#                :+=--=. :::=--=:.-*#%*--=*---+-+**=--=--=+**+*=**%@%=  
#                  =--= .#%%=--=.  +*#%#= +---#%++#=---.+%@%+  .+++*+-  
#                  ====   .:+===:   -==+= :===*+: -==== .--:.      ..   
#                  =--=     ----:         .----   :=---                 
#                  ----     :---:         .=---   .=---                 
#                  ----     :---:         .=---    =---                 
#                  ---:     :---:         .=---    +---                 
#                  +##%.    =*##-         -%%#:    %%%#                 
#                 :@@@@-    #@@@+         %@@@*   :@@@%:                
#                 .====.    -++=:         =+==-    --==.                

# @milosnowcat

import requests
import tkinter as ttk
import ttkbootstrap as ttk
from fontTools.ttLib import TTFont

URL = "https://api.quotable.io/random?tags=technology"

def select_font(type):
    """
    The function `select_font` takes a font type as input and returns the corresponding font file.
    
    :param type: The "type" parameter is a string that represents the specific font type or style that
    you want to select. It is used to construct the font path by appending it to the base font file name
    "Poppins-" and the file extension ".ttf"
    :return: the variable `my_font`, which is an instance of the `TTFont` class.
    """
    font_path = f"assets/fonts/Poppins-{type}.ttf"
    my_font = TTFont(font_path) 
    return my_font

def get_quote():
    """
    The function `get_quote` sends a GET request to a specified URL, retrieves JSON data, extracts a
    quote and its author from the data, and returns them as a tuple.
    :return: a quote and its author.
    """
    response = requests.get(URL)
    data = response.json()
    quote = data["content"]
    author = data["author"]
    return quote, author

def update_quote():
    """
    The function `update_quote` updates the text of a quote label and author label with a new quote and
    author obtained from the `get_quote` function.
    """
    quote, author = get_quote()
    quote_label.config(text=quote)
    author_label.config(text=f"~{author}")

# This code is creating a graphical user interface (GUI) using the tkinter library in Python.
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
