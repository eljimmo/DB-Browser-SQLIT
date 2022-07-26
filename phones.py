from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
#need to set submit button, connect sqlite and text to box text 
## make clearner code, reformat 



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

## update the db 
c.execute("""UPDATE phones SET Column1 = ''

"""

)


#text box labels 

Column1_label = Label(root, text="Column 1")
Column1_label.grid(row=1, column=0)
Column2_label = Label(root, text="Column 2")
Column2_label.grid(row=2, column=0)
Column3_label = Label(root, text="Column 3")
Column3_label.grid(row=3, column=0)
Column4_label = Label(root, text="Column 4")
Column4_label.grid(row=4, column=0)
Column5_label = Label(root, text="Column 5")
Column5_label.grid(row=5, column=0)

my_menu = Menu(root)
root.config(menu=my_menu)



#defining queries 
query_1 = c.execute("SELECT * FROM phones")
items = c.fetchall()

for item in items:
    print(item)


file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Queries", menu=file_menu)
file_menu.add_command(label="Query_1_formula", command=query_1)
file_menu.add_command(label="Query_2_formula", command='')
file_menu.add_command(label="Query_3_formula", command='')
file_menu.add_command(label="Query_4_formula", command='')
file_menu.add_command(label="Query_5_formula", command='')


conn.commit()

conn.close()

root.mainloop()
