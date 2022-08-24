from tkinter import *
from tkinter import filedialog, messagebox, colorchooser, font


class new_window:
    def __init__(self, path):
        self.edit_window = Tk()
        self.edit_window.attributes("-fullscreen", True)
        self.edit_window.title("DYEDIT")


        menu = Menu(self.edit_window)
        self.edit_window.config(menu=menu)

        self.text = Text(self.edit_window)

        self.path = path
        self.new_window_label = Label(self.edit_window, text=self.path)
        self.new_window_label.pack()

        file_menu = Menu(menu, tearoff=0, font=("Arial", 15))
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New File", command=self.newFile)
        file_menu.add_command(label="Open File", command=self.openFile)
        file_menu.add_command(label="Save File", command=self.saveFile)
        file_menu.add_command(label="EXIT", command=self.edit_window.destroy)

        edit_menu = Menu(menu, tearoff=0, font=("Arial", 15))
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Font", command=self.setFont)
        edit_menu.add_command(label="Size", command=self.setFontSize)
        edit_menu.add_command(label="Color", command=self.setColor)

        self.font_name = StringVar(self.edit_window)
        self.font_name.set("Arial")

        self.font_size = StringVar(self.edit_window)
        self.font_size.set("20")
        self.text.pack()
        if self.path == " ":
            self.new_window_label.config(text="untitled.txt")
        else:
            self.open_File()

    def newFile(self):
        if messagebox.askokcancel(title="ask ok cancel", message="Unsaved content will be deleted. Are you sure?"):
            self.text.delete('1.0', END)
            self.new_window_label.config(text="Untitled.txt")

    def openFile(self):
        if messagebox.askokcancel(title="ask ok cancel", message="Unsaved content will be deleted. Are you sure?"):
            filePath = filedialog.askopenfilename(initialdir="\\textEditor",
                                                  title="Open file okay?",
                                                  filetypes=(("text files", "*.txt"),
                                                             ("all files", "*.*")))
            if not filePath:
                return
            file = open(filePath, 'r')
            self.text.delete('1.0', END)
            self.text.insert('1.0', file.read())
            self.new_window_label.config(text=filePath)
            file.close()

    def saveFile(self):
        file = filedialog.asksaveasfile(initialdir="\\textEditor",
                                        defaultextension='.txt',
                                        filetypes=[
                                            ("Text file", ".txt"),
                                            ("HTML file", ".html"),
                                            ("All files", ".*"),
                                        ])
        if file is None:
            return
        fileText = str(self.text.get("1.0", END))
        file.write(fileText)
        file.close()

    def setColor(self):
        color = colorchooser.askcolor()
        colorHex = color[1]
        self.text.config(fg=colorHex)

    def setFont(self):
        def font_view(*args):
            font_label.config(font=(self.font_name.get(), self.font_size.get()))
            self.text.config(font=(self.font_name.get(), self.font_size.get()))

        font_window = Tk()
        frame = Frame(font_window)
        frame.grid()
        font_List = OptionMenu(frame, self.font_name, *font.families(), command=font_view)
        font_List.grid(row=0, column=0)
        font_label = Label(font_window, text="This is how the font looks like.",
                           font=(self.font_name.get(), self.font_size.get()))
        font_label.grid(row=1, column=0)

    def setFontSize(self):
        def changeSize():
            self.font_size.set(fontSize.get())
            self.text.config(font=(self.font_name.get(), self.font_size.get()))

        font_window = Tk()
        frame = Frame(font_window)
        frame.grid()
        fontSize = Spinbox(frame, from_=self.font_size.get(), to=1000, textvariable=self.font_size, command=changeSize)
        fontSize.grid(row=0, column=0)

    def open_File(self):
        file = open(self.path, 'r')
        self.text.insert('1.0', file.read())
        file.close()



def openFile():
    path = filedialog.askopenfilename(initialdir="\\textEditor",
                                      title="Open file okay?",
                                      filetypes=(("text files", "*.txt"),
                                                 ("all files", "*.*")))
    print("path is " + path)
    if not path:
        return
    new = new_window(path)
    main_window.destroy()


def newFile():
    new = new_window(" ")
    main_window.destroy()


main_window = Tk()
main_window.config(bg="blue")
main_window.resizable(False, False)
main_window.title("DYEDIT")
logo = PhotoImage(file='DyCompanyLogo.png')
main_window.iconphoto(True, logo)

welcome_label = Label(main_window, image=logo, text="Welcome To DYEditor", bg="blue", fg="#F5F5DC", compound="top", font=('Arial', 30))
welcome_label.pack()

open_button = Button(main_window, text="Open File", bg="dark blue", fg="#F5F5DC", command=openFile, font=('Arial', 30), width=17)
open_button.pack()

new_button = Button(main_window, text="New File", bg="dark blue", fg="#F5F5DC", command=newFile, font=('Arial', 30), width=17)
new_button.pack()

exit_button = Button(main_window, text="EXIT", bg="purple", fg="#F5F5DC", command=main_window.destroy, font=('Arial', 30), width=17)
exit_button.pack()
main_window.mainloop()
