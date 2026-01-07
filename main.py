"""
Plan:
Data files:
1. cases (MySQL)
columns: case_id, lawyer_name, type, client_name, date_of_completion, description, status(completed or on going), payment_status(completed or not), notes
2. requests (MySQL)
columns: id, lawyer_name, type, client_name, details

3. login.csv (created)
columns: username, password, role(admin/lawyer/User/Intern)
4. interns.csv (created)
columns: id, name, email, phone, linkedin_profile/pdf, skills
5. lawyers.csv (created)
columns: id, name, email, specialization, experience_years, cases_solved, salary
6. payments.csv 
columns: case_id, amount, date_of_registeration, d/o completion, status(paid/unpaid), payment_opted

7. About.txt
Outline:

Functionalities:
1. Admin/Main Head - half programmer
    a. View all cases/lawyers/clients/interns
    b. View all successful/pending cases (graphs) (matplotlib)
    c. Add/remove lawyers/clients/interns/cases/requests
    d. Edit about page
    e. Exit
2. Lawyers
    a. View own cases/clients/requests
    b. Update case status/notes/payment status
    c. Accept/reject requests
    d. Assign interns work
    e. Exit
3. Clients
    a. View lawyers/cases
    b. Create new request
    c. Exit
4. Interns
    a. Apply for internship
    b. View status of application
    c. View assigned work
    d. Update work status/notes
    e. Exit
"""
#import statements
import csv,os,tabulate
import getpass
import pymysql
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

#functions
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def login_screen():
    clear_window()

    title = tk.Label(root, text="Login", font=("Arial", 24))
    title.pack(pady=10)

    tk.Label(root, text="Username:").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    def attempt_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        with open('login.csv', 'r') as f:
            r = csv.reader(f)
            for row in r:
                csv_username, csv_password, csv_role = row

                if csv_username == username and csv_password == password:
                    messagebox.showinfo("Login Successful", f"Welcome, {username}!")

                    # 🔑 Redirect based on role (same window)
                    if csv_role == "Admin":
                        admin_dashboard(username)
                    elif csv_role == "Lawyer":
                        lawyer_dashboard(username)
                    elif csv_role == "User":
                        client_dashboard(username)
                    elif csv_role == "Intern":
                        intern_dashboard(username)
                    return

        messagebox.showerror("Login Failed", "Invalid username or password!")

    tk.Button(root, text="Login", command=attempt_login).pack(pady=10)
    tk.Button(root, text="Back", command=main_screen).pack(pady=10)


"""def login_screen():
    clear_window()
    title=tk.Label(root, text="Login", font=("Arial", 24))
    title.pack(pady=10)
##
    '''role_label = tk.Label(root, text="Select Role:")
    role_label.pack(pady=10)

    role_var = tk.StringVar(value="User")
    user_radio = tk.Radiobutton(root, text="User", variable=role_var, value="User")
    user_radio.pack()

    intern_radio = tk.Radiobutton(root, text="Intern", variable=role_var, value="Intern")
    intern_radio.pack()

    lawyer_radio = tk.Radiobutton(root, text="Lawyer", variable=role_var, value="Lawyer")
    lawyer_radio.pack()

    admin_radio = tk.Radiobutton(root, text="Admin", variable=role_var, value="Admin")
    admin_radio.pack()'''

    username_label = tk.Label(root, text="Username:")
    username_label.pack(pady=5) 
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)
    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()
        role = role_var.get()
        f=open('login.csv','r')
        r=csv.reader(f)
        for i in r:
            if i[0]==username: # and i[2]==role:
                if i[1]==password:
                    tk.messagebox.showinfo("Login Successful", f"Welcome, {username}!")
                    # go to next window based on role
                    #define functions per role
                    f.close()
                    return True
                else:
                    tk.messagebox.showerror("Login Failed", "Invalid password!")
                    return False
        tk.messagebox.showerror("Login Failed", "Invalid username or role!")
        f.close()
    login_button = tk.Button(root, text="Login", command=attempt_login)
    login_button.pack(pady=10)

    back_btn = tk.Button(root, text="Back", command=main_screen)
    back_btn.pack(pady=10)"""

def signup_screen():
    signup_win = tk.Toplevel(root)
    signup_win.title("Sign Up")
    signup_win.geometry("400x350")
    role_label = tk.Label(signup_win, text="Are you an intern?")
    role_label.pack(pady=10)
    role_var = tk.StringVar(value="no")
    yes_radio = tk.Radiobutton(signup_win, text="Yes", variable=role_var, value="yes")
    yes_radio.pack()
    no_radio = tk.Radiobutton(signup_win, text="No", variable=role_var, value="no")
    no_radio.pack()
    username_label = tk.Label(signup_win, text="Username:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(signup_win)
    username_entry.pack(pady=5)
    password_label = tk.Label(signup_win, text="Password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(signup_win, show="*")
    password_entry.pack(pady=5)
    repassword_label = tk.Label(signup_win, text="Re-enter Password:")
    repassword_label.pack(pady=5)
    repassword_entry = tk.Entry(signup_win, show="*")
    repassword_entry.pack(pady=5)
    def attempt_signup():
        role = role_var.get()
        if role == "yes":
            user_role = "Intern"
        else:
            user_role = "User"
        username = username_entry.get()
        password = password_entry.get()
        repassword = repassword_entry.get()
        if password != repassword:
            tk.messagebox.showerror("Error", "Passwords do not match.")
            return
        signup()
        tk.messagebox.showinfo("Success", "Signup successful!")
        signup_win.destroy()
    signup_button = tk.Button(signup_win, text="Sign Up", command=attempt_signup)
    signup_button.pack(pady=10)

def about_us():
    clear_window()
    title = tk.Label(root, text="About Us", font=("Arial", 24))
    title.pack(pady=10)
    about_text = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
    about_text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    try:
        with open("About.txt", "r") as f:
            about_text.insert(tk.END, f.read())
    except FileNotFoundError:
        about_text.insert(tk.END, "About Us information is not available.")

    back_btn = tk.Button(root, text="Back", command=main_screen)
    back_btn.pack(pady=10)


'''def about_us():
    about_win = tk.Toplevel(root)
    about_win.title("About Us")
    about_win.geometry("500x400")
    about_text = tk.Text(about_win, wrap=tk.WORD)
    about_text.pack(expand=True, fill=tk.BOTH)
    try:
        with open("About.txt", "r") as f:
            content = f.read()
            about_text.insert(tk.END, content)
    except FileNotFoundError:
        about_text.insert(tk.END, "About Us information is not available.")
'''

#Main Program
root = tk.Tk()
root.title("Law Firm Management System")
root.geometry("800x600")
def main_screen():
    clear_window()
    obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
    c = obj.cursor()
    label = tk.Label(root, text="WELCOME TO JUSTICE LAW FIRM MANAGEMENT SYSTEM", font=("Arial", 24))
    label.pack(pady=20)

    tk.Button(root, text="Login", font=("Arial", 16), command=login_screen).pack(pady=10)

    tk.Button(root, text="Sign Up", font=("Arial", 16), command=signup_screen).pack(pady=10)

    tk.Button(root, text="About Us", font=("Arial", 16), command=about_us).pack(pady=10)
    tk.Button(root, text="Exit", font=("Arial", 16), command=root.quit).pack(pady=10)


'''obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
c = obj.cursor()
root = tk.Tk()
root.title("Law Firm Management System")
root.geometry("800x600")
#window 1
label = tk.Label(root, text="WELCOME TO JUSTICE LAW FIRM MANAGEMENT SYSTEM", font=("Arial", 24))
label.pack(pady=20)
login_button = tk.Button(root, text="Login", font=("Arial", 16), command=lambda: login_screen())
login_button.pack(pady=10)
signup_button = tk.Button(root, text="Sign Up", font=("Arial", 16), command=lambda: signup_screen())
signup_button.pack(pady=10)
about = tk.Button(root, text="About Us", font=("Arial", 16), command=lambda: about_us())
about.pack(pady=10)

c.close()
obj.close()'''
main_screen()
#c.close()
#obj.close()
root.mainloop()
'''def getinfo():
    cur.execute("SELECT * FROM trialtable")
    data=cur.fetchall()
    for row in data:
        print(row)
#getinfo()
def insertinfo():
    name=input("Enter name:")
    age=int(input("Enter age:"))
    addr=input("Enter address:")
    cur.execute("INSERT INTO trialtable (name,age,address) VALUES (%s,%s,%s)",(name,age,addr))
    c.commit()
    print("Data inserted successfully")
print("hello world")'''

#  MAIN PROGRAM

#functions
def login(role): #returns True/False
    f=open('login.csv','r')
    r=csv.reader(f)
    #r=username,pwd,role
    username=input("Enter username: ")
    pwd=input("Enter password: ") #add getpass
    for i in r:
        if i[0]==username:
            #username is correct
            if i[1]==pwd:
                #password is correct
                if i[2]==role:
                    print("Login successful")
                    f.close()
                    return True
                else:
                    print("You are not registered as",role)
                    f.close()
                    return False
            else:
                print("Incorrect password")
                f.close()
                return False
    print("Username not found")
    f.close()
    return False

def signup():
    role=input("Are you an intern?\nEnter yes/no: ")
    if role.lower()=='yes':
        role='Intern'
    else:
        role='User'
    f=open('login.csv','a')
    w=csv.writer(f)
    username=input("Enter username: ")
    pwd=input("Enter password: ")
    repwd =input("Re-enter password: ")
    while pwd!=repwd:
        print("Passwords do not match. Try again.")
        pwd=input("Enter password: ")
        repwd =input("Re-enter password: ")
    w.writerow([username,pwd,role])
    f.close()
    print("Signup successful")

def viewlawyers():
    f=open('cases.csv','r')
    r=csv.reader(f)
    lawyers=set()
    for i in r:
        lawyers.add(i)
    print("Lawyers:")
    print(tabulate.tabulate(lawyers,tablefmt="grid"))
    f.close()

def viewinterns():
    f=open('interns.csv','r')
    r=csv.reader(f)
    interns=[]
    for i in r:
        interns.append(i)
    print("Interns:")
    print(tabulate.tabulate(interns,tablefmt="grid"))
    f.close()
