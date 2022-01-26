from tkinter import * # (python GUI)
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import bcrypt

from encryption_decryption import encrypt_data, decrypt_data, check_key
from database_management import *



# --------------------------------------------LOGIN-WINDOW-------------------------------------------------

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

    if identifier.get() == "Alex" and bcrypt.checkpw(input_pw, hashed):
        messagebox.showinfo("Login succeed !", "You have now logged in.", icon="info")

        window.destroy()
        submitKey_window()

    elif identifier.get() == "" or password.get() == "":
        messagebox.showinfo("Login failed !", "Please fill all fields !", icon="warning")

    else:
        messagebox.showinfo("Login failed !", "Id or password is wrong.", icon="error")







# --------------------------------------------KEY-WINDOW-------------------------------------------------

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


    global window_sub
    # main window settings
    window_sub = Tk()
    window_sub.title('Your Key')
    #center window
    windowWidth = 250
    windowHeight = 100
    positionRight = int(window_sub.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window_sub.winfo_screenheight()/2.5 - windowHeight/2)
    window_sub.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
    window_sub.resizable(width=FALSE, height=FALSE)


    # window frames
    frame = Frame(window_sub, borderwidth=2)
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

    window_sub.mainloop()





def submitKey():
    """
        Function checking if private key is the right one that can decrypt the database.
    """

    if check_key(pvKey.get().encode()):

        global encoded_pvKey
        encoded_pvKey = pvKey.get().encode()

        window_sub.destroy()
        home_window()

    else:
        messagebox.showinfo("Wrong key", "The provided private key is invalid !", icon="error")








# --------------------------------------------HOME-WINDOW------------------------------------------------

def home_window():

    global window_home

    window_home = Tk()
    window_home.title('Welcome the PassMan home screen.')
    #center window
    windowWidth = 500
    windowHeight = 350
    positionRight = int(window_home.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window_home.winfo_screenheight()/2.5 - windowHeight/2)
    window_home.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
    window_home.resizable(width=FALSE, height=FALSE)
    window_home['bg']='#130f40'

    frame = Frame(window_home, borderwidth=2)
    frame.pack(pady=10)

    title = Label(frame, text="Welcome to PassMan. What do you want to do ?",font=("Verdana", 12), height=2, bg='#130f40', fg='white')
    title.pack()



    frame2 = Frame(window_home, borderwidth=5, height=2, bg='#130f40')
    frame2.pack(pady=10)

    btnRead = Button(frame2, text="Passwords library",font=("Verdana", 12), height=2, width = 30,bg='#30336b', fg='white', command=readPassLibrary)
    btnRead.pack(pady=5)

    btnCreate = Button(frame2, text="Add new password",font=("Verdana", 12), height=2, width = 30, bg='#30336b', fg='white', command=addNewPass)
    btnCreate.pack(pady=5)

    btnUpdate = Button(frame2, text="Update password/account info",font=("Verdana", 12), height=2, width = 30,bg='#30336b', fg='white')
    btnUpdate.pack(pady=5)

    btnDelete = Button(frame2, text="Delete account/passwords",font=("Verdana", 12), height=2, width = 30,bg='#30336b', fg='white')
    btnDelete.pack(pady=5)



    window_home.mainloop()








# --------------------------------------------CRUD------------------------------------------------


# --------------------------------------------READ------------------------------------------------

def readPassLibrary():

    global window_read

    window_read = Tk()
    window_read.title('Your accounts and passwords.')
    #center window
    windowWidth = 700
    windowHeight = 500
    positionRight = int(window_read.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window_read.winfo_screenheight()/2.3 - windowHeight/2)
    window_read.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
    window_read.resizable(width=FALSE, height=FALSE)
    window_read['bg']='#130f40'

    frame = Frame(window_read, bg='#130f40') #bg='white' to undeerstand better the placement
    frame.pack(side=TOP, padx=(20,180))

    btnBack = Button(frame, text="Back",font=("Verdana", 12),bg='#30336b', fg='white', command=backButtonRead)
    btnBack.pack(side=LEFT,padx=(0, 100), pady=(20,))

    title = Label(frame, text="All your accounts and passwords.",font=("Verdana", 14), height=2, bg='#130f40', fg='white')
    title.pack(side=RIGHT, padx=(20,5), pady=(20,))



    treeview_frame = Frame(window_read, borderwidth=3, bg='white')
    treeview_frame.pack()

    tree_scroll = Scrollbar(treeview_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Treeview (box) settings
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview', rowheight=25)
    style.map('Treeview', background=[('selected', '#130f40')])

    dataBox = ttk.Treeview(treeview_frame, yscrollcommand=tree_scroll.set, selectmode='extended', show='headings', columns=['Website', 'Username', 'Email', 'Password'])
    dataBox.pack()

    tree_scroll.config(command=dataBox.yview)

    dataBox.column('Website', anchor=W, width=140)
    dataBox.column('Username', anchor=CENTER, width=140)
    dataBox.column('Email', anchor=CENTER, width=140)
    dataBox.column('Password', anchor=CENTER, width=140)

    dataBox.heading('Website', text="Website", anchor=CENTER)
    dataBox.heading('Username', text="Username", anchor=CENTER)
    dataBox.heading('Email', text="Email", anchor=CENTER)
    dataBox.heading('Password', text="Password", anchor=CENTER)

    # Access database to fecth all data
    try:
        co, cur = create_connection()

        cur.execute(""" SELECT website, username, email, password FROM passwords """)
        fetch = cur.fetchall()


    except Exception as e:

        messagebox.showinfo("Something went wrong.", "Error is : {}".format(e), icon="error")
        close_connection(co)

    dataBox.tag_configure('oddrow', background='white')
    dataBox.tag_configure('evenrow', background='lightblue')

    # insert data inside treeview
    count = 0

    for record in fetch:
        if count % 2 == 0:
            dataBox.insert(parent='', index='end', iid=count, text='', values=(decrypt_data(record[0], encoded_pvKey),decrypt_data(record[1], encoded_pvKey), decrypt_data(record[2], encoded_pvKey), decrypt_data(record[3], encoded_pvKey)), tags=('evenrow',))
        else:
            dataBox.insert(parent='', index='end', iid=count, text='', values=(decrypt_data(record[0], encoded_pvKey),decrypt_data(record[1], encoded_pvKey), decrypt_data(record[2], encoded_pvKey), decrypt_data(record[3], encoded_pvKey)), tags=('oddrow',))

        count = count + 1





    window_read.mainloop()








# --------------------------------------------CREATE---------------------------------------------------

def addNewPass():

    global window_create

    window_create = Tk()
    window_create.title('Create a new account with password')
    #center window
    windowWidth = 550
    windowHeight = 400
    positionRight = int(window_create.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window_create.winfo_screenheight()/2.3 - windowHeight/2)
    window_create.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
    window_create.resizable(width=FALSE, height=FALSE)
    window_create['bg']='#130f40'



    frame = Frame(window_create, bg='#130f40') #bg='white' to undeerstand better the placement
    frame.pack(side=TOP)

    btnBack = Button(frame, text="Back",font=("Verdana", 12),bg='#30336b', fg='white', command=backButtonAdd)
    btnBack.pack(side=LEFT, padx=(10, 80), pady=(10,))

    title = Label(frame, text="All your accounts and passwords.",font=("Verdana", 12), height=2, bg='#130f40', fg='white')
    title.pack(side=RIGHT, padx=(0,130), pady=(10,))



    # Creation Form
    labelFrame = LabelFrame(window_create, text="New password form", bg='#130f40',fg='white', font=('Verdana', 8))
    labelFrame.pack(side=TOP, pady=(10,), ipady=20)


    frameLabels = Frame(labelFrame, bg='#130f40')
    frameLabels.pack(side=LEFT, padx=(35,30))

    frameInputs = Frame(labelFrame, bg='#130f40')
    frameInputs.pack(side=RIGHT, padx=(0,35))


    # LABELS
    labelWebsite = Label(frameLabels, text="Website :", font=("Verdana", 11), bg='#130f40', fg='white')
    labelWebsite.pack(pady=(0,20), padx=(0,20))

    labelUsername = Label(frameLabels, text="Username :", font=("Verdana", 11), bg='#130f40', fg='white')
    labelUsername.pack(padx=(0,3))

    labelEmail = Label(frameLabels, text="Email :", font=("Verdana", 11), bg='#130f40', fg='white')
    labelEmail.pack(pady=20, padx=(0,40))

    labelPass = Label(frameLabels, text="Password :", font=("Verdana", 11), bg='#130f40', fg='white')
    labelPass.pack(padx=(0,8))

    # ENTRIES
    websiteVar = StringVar()
    usernameVar = StringVar()
    emailVar = StringVar()
    passVar = StringVar()
    inputWebsite = Entry(frameInputs, textvariable = websiteVar, width=35)
    inputWebsite.pack(ipady=2,pady=(0,20))

    inputUsername = Entry(frameInputs, textvariable = usernameVar, width=35)
    inputUsername.pack(ipady=2)

    inputEmail = Entry(frameInputs, textvariable = emailVar, width=35)
    inputEmail.pack(ipady=2,pady=20)

    inputPass = Entry(frameInputs, textvariable = passVar, width=35)
    inputPass.pack(ipady=2)


    # Buttons
    frameBtns = Frame(window_create, bg='#130f40')
    frameBtns.pack(side=BOTTOM, pady=(0,40))



    # Clear button function
    def clearData():
        if len(inputWebsite.get()) == 0 and len(inputUsername.get()) == 0 and len(inputEmail.get()) == 0 and len(inputPass.get()) == 0:
            messagebox.showinfo("Empty fields", "All your fields are empty !", icon="error")
        else:
            MsgBox = messagebox.askquestion ('Clear entries','Really wanna clear all ?',icon = 'warning')
            if MsgBox == 'yes':

                inputWebsite.delete(0, 'end')
                inputUsername.delete(0, 'end')
                inputEmail.delete(0, 'end')
                inputPass.delete(0, 'end')


    btnClear = Button(frameBtns, text="Clear",font=("Verdana", 12), bg='#30336b', fg='white', command=clearData)
    btnClear.pack(side=LEFT, padx=(0,273))

    # Add data button function
    def addData():
        if len(inputWebsite.get()) == 0 and len(inputUsername.get()) == 0 and len(inputEmail.get()) == 0 and len(inputPass.get()) == 0:
            messagebox.showinfo("Empty fields", "All your fields are empty !", icon="error")

        elif len(inputWebsite.get()) == 0 or len(inputPass.get()) == 0:
            messagebox.showinfo("Empty fields", "You must fill Website and Password fields !", icon="warning")

        else:
            MsgBox = messagebox.askquestion('Add new data','Are you sure you wanna create new record ?', icon = 'warning')

            if MsgBox == 'yes':

                websitesList = []
                iteration = 0

                try:

                    co, cur = create_connection()

                    # Check if the website account already exists
                    cur.execute("SELECT website FROM passwords")
                    rows = cur.fetchall()

                    for row in rows:
                        for cell in row:
                            decryptedData = decrypt_data(cell ,encoded_pvKey)
                            websitesList.append(decryptedData)

                    for i in range(len(websitesList)):
                        if inputWebsite.get() == websitesList[i]:
                            iteration = iteration + 1
                            break

                    if iteration > 0:
                        messagebox.showinfo("The website exists", "You already have an account for {} !".format(inputWebsite.get()), icon="warning")
                    else: # if doesn't exist, record is added

                        web = encrypt_data(inputWebsite.get(), encoded_pvKey)
                        user = encrypt_data(inputUsername.get(), encoded_pvKey)
                        email = encrypt_data(inputEmail.get(), encoded_pvKey)
                        passw = encrypt_data(inputPass.get(), encoded_pvKey)

                        cur.execute(""" INSERT INTO passwords(website, username, email, password) VALUES (?,?,?,?) """, (web, user, email, passw))
                        messagebox.showinfo("Success", "Your record was successfully added to the database.", icon="info")

                    close_connection(co)

                    # clear all inputs
                    inputWebsite.delete(0, 'end')
                    inputUsername.delete(0, 'end')
                    inputEmail.delete(0, 'end')
                    inputPass.delete(0, 'end')

                except Exception as e:
                    messagebox.showinfo("Something went wrong.", "Error is : {}".format(e), icon="error")
                    co.rollback()
                    close_connection(co)





    btnAdd = Button(frameBtns, text="Add new",font=("Verdana", 12), bg='#30336b', fg='white', command=addData)
    btnAdd.pack(side=RIGHT, padx=(2,0))


    window_create.mainloop()











# --------------------------------------------CHANGING-WINDOW------------------------------------------------

def backButtonRead():

    window_read.destroy()
    home_window()


def backButtonAdd():

    window_create.destroy()
    home_window()


# addNewPass()
login_window()
