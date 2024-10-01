from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from dashWindow import *

class log:
    # main window
    def __init__(self):
        self.window = Tk()
        self.window.title("Crime Incident Reporting System")
        self.x = (self.window.winfo_screenwidth() // 2) - (720 // 2)
        self.y = (self.window.winfo_screenheight() // 2) - (500 // 2)
        self.window.geometry('{}x{}+{}+{}'.format(720, 500, self.x, self.y))

    # window title
        self.title = Label(self.window,
                           text = "Crime Incident Reporting System",
                           font = ('Comic Sans MS', 20, 'bold'),
                           padx = 0,
                           pady = 50)
        self.title.pack()

    # window logFrame
        self.frame = Frame(self.window)
        self.frame.config(border = 10, highlightbackground= "black", highlightcolor= "black", highlightthickness= 2)
        self.frame.pack()

    # frame userLabel
        self.userName = Label(self.frame,
                              text = 'Username',
                              font = ('Comic Sans MS',15 ,'bold'),
                              padx = 50,
                              pady = 30)
        self.userName.grid(row = 1, column = 0)

    # frame userEntry
        self.userEntry = Entry(self.frame,
                               font = ('Arial',14))
        self.userEntry.grid(row = 1, column = 1)

    # frame passLabel
        self.password = Label(self.frame,
                              text = 'Password',
                              font = ('Comic Sans MS',15 ,'bold'),
                              padx = 50,
                              pady = 30)
        self.password.grid(row = 2, column = 0)

    # frame passEntry
        self.passEntry = Entry(self.frame,
                               font = ('Arial',14 ),
                               show = '*')
        self.passEntry.grid(row = 2, column = 1)

    # frame submitButton

        self.subButton = Button(self.frame,
                                text = 'Login',
                                command = self.login,
                                width = 20,
                                font = ('Comic Sans MS',12),
                                foreground = 'white',
                                background = '#333333')
        self.subButton.config(border=5, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.subButton.grid(row = 3, column = 1)

    # frame cancelButton

        self.cancelButton = Button(self.frame,
                                text = 'Cancel',
                                command = self.cancel,
                                width = 10,
                                font = ('Comic Sans MS',12),
                                foreground = 'white',
                                background = '#333333')
        self.cancelButton.config(border=5, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.cancelButton.grid(row = 3, column = 0)


        self.window.mainloop()

    # button functions

    def login(self):

        username = self.userEntry.get()
        password = self.passEntry.get()

    # Basic authentication check
        if username == "admin" and password == "123":
            self.window.destroy()  # Close the login window
            dash()  # Open dashboard window
        else:
            messagebox.showerror("Error", "Invalid Username or Password")


    def cancel(self):

        self.window.destroy()  # Close the login window

if __name__ == "__main__":
    log()