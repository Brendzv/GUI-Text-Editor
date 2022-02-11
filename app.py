
from cgitb import text
import tkinter as tk
from tkinter import Frame, Menu, Tk, ttk, filedialog

#functions
def themeModifier():
    whiteMode = 0
    if whiteMode == 0:
        window.config(bg="#252526")
        inText.config(bg="#1E1E1E", fg="white")
        whiteMode = 1

    #working on a better system for theme changing

def newFile():
    pass

def saveFile():
    files = [('All Files', '*.*'), ('HTML Files', '*.html*'), ('CSS Files', '*.css*'), ('JavaScript Files', '*.js*'), ('Python Files', '*.py*'), ('Text Document', '*.txt*')]
    txtSaving = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
    if txtSaving is None:
        return
    text2save = str(text.get(1.0, tk.END))
    txtSaving.write(text2save)
    txtSaving.close()


#window config
window = Tk()
window.title("text editor")
window.geometry("1280x720")
window.config(bg="#E7E7E7")
window.minsize(1280, 720)



#frame
main_frame = Frame(window)
main_frame.pack(pady=15)


#inputBox

inText = tk.Text(main_frame, width=100, height=35, font=("monospace", 16), fg='black', undo=True)
inText.config(bg="#FFFFFF")
inText.pack()



#menubar system
menubar = Menu(main_frame)
btn_files = Menu(menubar, tearoff=0)
btn_files.add_command(label="New", command=newFile)
btn_files.add_command(label="Save", command=saveFile)
menubar.add_cascade(label="FIle", menu=btn_files)

btn_edit = Menu(menubar, tearoff=0)
btn_edit.add_command(label="ChangeTheme", command=themeModifier)
menubar.add_cascade(label="Edit", menu=btn_edit)

window.config(menu=menubar)
window.mainloop()