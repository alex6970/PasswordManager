from tkinter import * # (python GUI)
from tkinter import messagebox

def home_wondow():
    # main window settings
    window = Tk()
    window.title('Your Password Manager')
    #center window
    windowWidth = 350
    windowHeight = 190
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2.5 - windowHeight/2)
    window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
    window.resizable(width=FALSE, height=FALSE)


def login_window():

    # User verification to login
    def login():
        print("Trying to login... Please wait.")
        if identifier.get() == "Alex":
            messagebox.showinfo("Login succeed !", "You Have Now Logged In.", icon="info")

            window.destroy()
            pm_home()

        else:
            messagebox.showinfo("Login failed !", "Id or password is wrong.", icon="error")


    # main window settings
    window = Tk()
    window.title('Your Password Manager')
    #center window
    windowWidth = 350
    windowHeight = 190
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2.5 - windowHeight/2)
    window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
    window.resizable(width=FALSE, height=FALSE)



    # window widgets
    title = Label(window, text="Welcome to your password manager.",font=("Verdana", 12), height=2)

    identifier = StringVar()
    id_label = Label(window, text="Identifier", height=2)
    id = Entry(window, textvariable = identifier)

    password = StringVar()
    password_log_label = Label(window, text="Main Password", height=2)
    password_log = Entry(window, textvariable = password, show="*")
    button = Button(window, text="Login", command=login, width=10, bg="black", fg="white")


    # location on the frame
    title.pack()
    id_label.pack()
    id.pack()
    password_log_label.pack()
    password_log.pack()
    button.pack()
    password_log.get()

    window.mainloop()


login_window()
