from tkinter import * # (python GUI)
from tkinter import messagebox
from tkinter import filedialog
from encryption_decryption import encrypt_data, decrypt_data
import bcrypt



def submitKey_window():
    """
        Window where user must submit the private key to decrypt and acces to the database.
    """

    global pvKey


    def openFromFile(): # Nested function to get key from a file.

        filename = filedialog.askopenfilename(title="Open your file",filetypes=[('txt files','.txt'),('all files','.*')])

        if not filename: # if user cancels inside the file selection, do nothing
            return

        else:
            fichier = open(filename, "r")
            content = fichier.read()
            fichier.close()

            inputKey.insert(0, content)



    # main window settings
    window = Tk()
    window.title('Your Key')
    #center window
    windowWidth = 250
    windowHeight = 100
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2.5 - windowHeight/2)
    window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
    window.resizable(width=FALSE, height=FALSE)


    # window frames
    frame = Frame(window, borderwidth=2)
    btnsFrame = Frame(frame)


    # window widgets
    title = Label(frame, text="Please enter the your private key : ", font=("Verdana", 8), height=2)

    pvKey = StringVar()
    inputKey = Entry(frame, textvariable = pvKey, width=35, show='*')

    submitBtn = Button(frame, text="Submit", width=10, bg="black", fg="white", command=submitKey)
    openFileBtn = Button(frame, text="Open", width=10, bg="black", fg="white", command=openFromFile)

    # location on the frame
    frame.pack()
    title.pack()
    inputKey.pack()

    btnsFrame.pack(pady=5)

    submitBtn.pack(side = RIGHT)
    openFileBtn.pack(side = LEFT)

    window.mainloop()





def submitKey():
    """
        Function checking if private key is the right one that can decrypt the database.
    """

    msg = 'Hello how ya doin ?'

    encoded_pvKey = pvKey.get().encode()

    crypt_msg = encrypt_data(msg, encoded_pvKey)
    print(crypt_msg)

    decrypted_msg = decrypt_data(crypt_msg, encoded_pvKey)
    print(decrypted_msg)

    # f = Fernet(pvKey)
    #
    # ciphertext = f.encrypt(msg)
    # print(ciphertext)
    #
    # txt = f.decrypt(ciphertext)
    # print(txt.decode())
    #
    #
    # print(pvKey.get())
    #
    # hashed = b'$2b$12$q3W5AOX8wFrXm2RqtNt3D.iqqvdL2EDyM3Be3tAQi3Ifbh3dU5C2q' # TO STORE IN DATABASE
    # input_pw = password.get().encode('utf-8')
    #
    # print("Trying to login... Please wait.")
    #
    # if identifier.get() == "Alex" and bcrypt.checkpw(input_pw, hashed):
    #     messagebox.showinfo("Login succeed !", "You have now logged in.", icon="info")
    #
    #     window.destroy()
    #     submitKey_window()
    #
    # elif identifier.get() == "" or password.get() == "":
    #     messagebox.showinfo("Login failed !", "Please fill all fields !", icon="warning")
    #
    # else:
    #     messagebox.showinfo("Login failed !", "Id or password is wrong.", icon="error")
    #








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
        submitKey_window()

    elif identifier.get() == "" or password.get() == "":
        messagebox.showinfo("Login failed !", "Please fill all fields !", icon="warning")

    else:
        messagebox.showinfo("Login failed !", "Id or password is wrong.", icon="error")



submitKey_window()
