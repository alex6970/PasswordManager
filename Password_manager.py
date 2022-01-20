from tkinter import * # (python GUI)
from tkinter import messagebox
import bcrypt

def home_window():
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

    # gloabl variables to use everywhere in this file
    global identifier
    global password

    global window

    # main window settings
    window = Tk()
    window.title('Sign In')
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



# User verification to login
def login(): # help(login)
    """
        Login function checking if stored hashed password is the same as the one submitted in the form.
    """

    hashed = b'$2b$12$q3W5AOX8wFrXm2RqtNt3D.iqqvdL2EDyM3Be3tAQi3Ifbh3dU5C2q' # TO STORE IN DATABASE
    input_pw = password.get().encode('utf-8')

    print("Trying to login... Please wait.")

    if identifier.get() == "Alex" and bcrypt.checkpw(input_pw, hashed):
        messagebox.showinfo("Login succeed !", "You have now logged in.", icon="info")

        window.destroy()
        home_window()
        
    elif identifier.get() == "" or password.get() == "":
        messagebox.showinfo("Login failed !", "Please fill all fields !", icon="warning")

    else:
        messagebox.showinfo("Login failed !", "Id or password is wrong.", icon="error")



login_window()
