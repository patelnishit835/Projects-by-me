from tkinter import Tk,scrolledtext,Menu,filedialog,END,messagebox,simpledialog

#root for main window
root = Tk(className = "Text Editor")
textArea = scrolledtext.ScrolledText(root, width=100, height=80)
textArea.pack()

#
#functionalities
#

def new():

    if len(textArea.get('1.0',END+'-1c')) > 0:
        if messagebox.askyesno("Override","Do you want to save the existing content?"):
            saveFile()
            textArea.delete('1.0', END)
        else:
            textArea.delete('1.0', END)

def openFile():
    file = filedialog.askopenfile(parent = root, mode = "rb", title="Select a text file")

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode = 'w')

    if file!=None:
        data = textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()

def find():
    val = simpledialog.askstring("Find...", "Enter text:")

    data = textArea.get('1.0',END)

    messagebox.showinfo("Found", "Count: " + str(data.upper().count(val.upper())))

def exitRoot():
    if messagebox.showinfo("Quit","Are you sure?"):
        root.destroy()

def about():
    label = messagebox.showinfo("About","A pythonic notepad!!!")



#menu options
menu = Menu(root)
root.config(menu = menu)
fileMenu = Menu(menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label="New", command = new)
fileMenu.add_command(label="Open", command = openFile)
fileMenu.add_command(label="Save", command = saveFile)
fileMenu.add_command(label="Find", command = find)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = exitRoot)

helpMenu = Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About", command = about)

#keep the window open
root.mainloop()
