from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("SQL Front End")
root.iconbitmap
root.geometry("600x600")


conn = sqlite3.connect("phonedatabase.db")

c = conn.cursor()






Column1 = Entry(root, width=30)
Column1.grid(row=1, column=1, padx=20)
Column2 = Entry(root, width=30)
Column2.grid(row=2, column=1, padx=20)
Column3 = Entry(root, width=30)
Column3.grid(row=3, column=1, padx=20)
Column4 = Entry(root, width=30)
Column4.grid(row=4, column=1, padx=20)
Column5 = Entry(root, width=30)
Column5.grid(row=5, column=1, padx=20)

c.execute("""CREATE TABLE IF NOT EXISTS phones (
    Column1 text
    Columm2 text
    Column2 int
    Column3 int
    Column4 int
    Column5 text
)
""")


#text box labels 

Column1_label = Label(root, text="phone class")
Column1_label.grid(row=1, column=0)
Column2_label = Label(root, text="phone type")
Column2_label.grid(row=2, column=0)
Column3_label = Label(root, text="RFD")
Column3_label.grid(row=3, column=0)
Column4_label = Label(root, text="Clear")
Column4_label.grid(row=4, column=0)
Column5_label = Label(root, text="Pink bagged")
Column5_label.grid(row=5, column=0)

conn.commit()

conn.close()

root.mainloop()
