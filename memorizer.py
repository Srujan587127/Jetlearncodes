from tkinter import *
from tkinter.filedialog import *
master = Tk()
master.title("Memorizer")

def openfile():
    

    fin = askopenfile(title = "Open File")

    if fin is not None:

        listbox.delete(0, END)

        items = fin.readlines()

        for item in items:
            listbox.insert(END, item.strip())

def saveFile():

    fout=asksaveasfile(defualtextension = ".txt")

    if fout is not None:
        
        for item in listbox.get(0, END):
            print(item.strip(), file=fout)
        
        listbox.delete(0, END)

def addItem():
    listbox.insert(END, item.get())

    item.delete(0, END)

def deleteITEM():

    index  = listbox.curselection()
    if index:
        listbox.delete(index)


fOpen=Button(master, text="Open", command=openfile, width = 15)
lDelete=Button(master, text = "DELETE", command=deleteITEM, width = 15)
fSave=Button(master, text = "Save", command = saveFile, width = 15)
fOpen.pack(side = LEFT, padx =5, pady= 5)
lDelete.pack(side = RIGHT, padx = 5, pady = 5) 
fSave.pack(padx=5, pady=5)

lAdd=Button(master, text = "ADD", command = addItem, width = 15)
item=Entry(master, width=35)
item.pack(padx=5, pady =5)
lAdd.pack(padx = 5, pady = 5)


frame = Frame(master)
scrollbar= Scrollbar(frame, orient = "vertical")
scrollbar.pack(side = RIGHT, fill = Y)

listbox = Listbox(frame, width = 70, yscrollcommand=scrollbar.set, bg = 'red')
for i in range(1,100):
    listbox.insert(END, "LIST" + str(i))
    
listbox.pack(side = LEFT, padx = 5)
scrollbar.config(command=listbox.yview)

frame.pack(side = RIGHT)

mainloop()