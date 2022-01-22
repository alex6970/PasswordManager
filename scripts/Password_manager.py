from tkinter import * # (python GUI)
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import bcrypt

from encryption_decryption import encrypt_data, decrypt_data
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

    print("Trying to login... Please wait.")

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

    # msg = 'Hello how ya doin ?'

    global encoded_pvKey
    encoded_pvKey = pvKey.get().encode()

    window_sub.destroy()
    home_window()

    # crypt_msg = encrypt_data(msg, encoded_pvKey)
    # print(crypt_msg)
    #
    # decrypted_msg = decrypt_data(crypt_msg, encoded_pvKey)
    # print(decrypted_msg)






# --------------------------------------------HOME-WINDOW------------------------------------------------

def home_window():

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

    btnCreate = Button(frame2, text="Add new password",font=("Verdana", 12), height=2, width = 30, bg='#30336b', fg='white')
    btnCreate.pack(pady=5)

    btnUpdate = Button(frame2, text="Update password/account info",font=("Verdana", 12), height=2, width = 30,bg='#30336b', fg='white')
    btnUpdate.pack(pady=5)

    btnDelete = Button(frame2, text="Delete account/passwords",font=("Verdana", 12), height=2, width = 30,bg='#30336b', fg='white')
    btnDelete.pack(pady=5)



    window_home.mainloop()








# --------------------------------------------CRUD------------------------------------------------


# --------------------------------------------READ------------------------------------------------

def readPassLibrary():

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

    btnBack = Button(frame, text="Back",font=("Verdana", 12),bg='#30336b', fg='white')
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

    dataBox = ttk.Treeview(treeview_frame, yscrollcommand=tree_scroll.set, selectmode='extended', columns=['Website', 'Username', 'Password'])
    dataBox.pack()

    tree_scroll.config(command=dataBox.yview)

    dataBox.column('#0', width=0, stretch=NO)
    dataBox.column('Website', anchor=W, width=140)
    dataBox.column('Username', anchor=CENTER, width=140)
    dataBox.column('Password', anchor=CENTER, width=140)

    dataBox.heading('#0', text="", anchor=W)
    dataBox.heading('Website', text="Website", anchor=CENTER)
    dataBox.heading('Username', text="Username", anchor=CENTER)
    dataBox.heading('Password', text="Password", anchor=CENTER)

    fakeData = [
        ["Instagram", "Gandalf", "hbdhjs67DSHBds$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["Snapchat", "Alex", "sdbjk89$!$ù"],
        ["WhatsApp", "John", "cleks$ù"]
    ]

    dataBox.tag_configure('oddrow', background='white')
    dataBox.tag_configure('evenrow', background='lightblue')

    global count
    count = 0

    for record in fakeData:
        if count % 2 == 0:
            dataBox.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
            dataBox.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))

        count = count + 1





    window_read.mainloop()

    # co, cur = create_connection()
    #
    # cur.execute("""SELECT * FROM passwords """)
    #
    # # display query data
    # rows = cur.fetchall()
    # # for row in rows:
    # #     for cell in row:
    # #         print(cell)
    # print(rows)
    #
    # close_connection(co)




readPassLibrary()
