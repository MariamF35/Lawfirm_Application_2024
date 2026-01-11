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
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        repassword = repassword_entry.get().strip()
        if password != repassword:
            tk.messagebox.showerror("Error", "Passwords do not match.")
            return
        if not username or not password:
            tk.messagebox.showerror("Error", "Username and password cannot be empty.")
            return
        signup(username, password, user_role)
        tk.messagebox.showinfo("Success", "Signup successful!")
        signup_win.destroy()
    signup_button = tk.Button(signup_win, text="Sign Up", command=attempt_signup)
    signup_button.pack(pady=10)

def signup(username, password, role):
    with open('login.csv', 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow([username, password, role])

def admin_dashboard(username):
    clear_window()
    title = tk.Label(root, text=f"Admin Dashboard - Welcome {username}", font=("Arial", 20))
    title.pack(pady=10)

    tk.Button(root, text="View All Cases", command=lambda: view_all_cases(username)).pack(pady=5)
    tk.Button(root, text="View All Lawyers", command=lambda: view_all_lawyers(username)).pack(pady=5)
    tk.Button(root, text="View All Clients", command=lambda: view_all_clients(username)).pack(pady=5)
    tk.Button(root, text="View All Interns", command=lambda: view_all_interns(username)).pack(pady=5)
    tk.Button(root, text="View Cases Statistics", command=lambda: view_cases_stats(username)).pack(pady=5)
    tk.Button(root, text="Add/Remove Entities", command=lambda: add_remove_entities(username)).pack(pady=5)
    tk.Button(root, text="Edit About Page", command=lambda: edit_about_page(username)).pack(pady=5)
    tk.Button(root, text="Logout", command=main_screen).pack(pady=10)

def lawyer_dashboard(username):
    clear_window()
    title = tk.Label(root, text=f"Lawyer Dashboard - Welcome {username}", font=("Arial", 20))
    title.pack(pady=10)

    tk.Button(root, text="View My Cases", command=lambda: view_my_cases(username)).pack(pady=5)
    tk.Button(root, text="View My Clients", command=lambda: view_my_clients(username)).pack(pady=5)
    tk.Button(root, text="View Requests", command=lambda: view_requests(username)).pack(pady=5)
    tk.Button(root, text="Update Case Status", command=lambda: update_case_status(username)).pack(pady=5)
    tk.Button(root, text="Accept/Reject Requests", command=lambda: accept_reject_requests(username)).pack(pady=5)
    tk.Button(root, text="Assign Intern Work", command=lambda: assign_intern_work(username)).pack(pady=5)
    tk.Button(root, text="Logout", command=main_screen).pack(pady=10)

def client_dashboard(username):
    clear_window()
    title = tk.Label(root, text=f"Client Dashboard - Welcome {username}", font=("Arial", 20))
    title.pack(pady=10)

    tk.Button(root, text="View Lawyers", command=lambda: view_lawyers(username)).pack(pady=5)
    tk.Button(root, text="View My Cases", command=lambda: view_my_cases_client(username)).pack(pady=5)
    tk.Button(root, text="Create New Request", command=lambda: create_new_request(username)).pack(pady=5)
    tk.Button(root, text="Logout", command=main_screen).pack(pady=10)

def intern_dashboard(username):
    clear_window()
    title = tk.Label(root, text=f"Intern Dashboard - Welcome {username}", font=("Arial", 20))
    title.pack(pady=10)

    tk.Button(root, text="Apply for Internship", command=lambda: apply_internship(username)).pack(pady=5)
    tk.Button(root, text="View Application Status", command=lambda: view_application_status(username)).pack(pady=5)
    tk.Button(root, text="View Assigned Work", command=lambda: view_assigned_work(username)).pack(pady=5)
    tk.Button(root, text="Update Work Status", command=lambda: update_work_status(username)).pack(pady=5)
    tk.Button(root, text="Logout", command=main_screen).pack(pady=10)

def add_lawyer(username):
    clear_window()
    title = tk.Label(root, text="Add Lawyer", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="ID:").pack(pady=5)
    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)
    
    tk.Label(root, text="Name:").pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)
    
    tk.Label(root, text="Email:").pack(pady=5)
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)
    
    tk.Label(root, text="Specialization:").pack(pady=5)
    spec_entry = tk.Entry(root)
    spec_entry.pack(pady=5)
    
    tk.Label(root, text="Experience Years:").pack(pady=5)
    exp_entry = tk.Entry(root)
    exp_entry.pack(pady=5)
    
    tk.Label(root, text="Cases Solved:").pack(pady=5)
    cases_entry = tk.Entry(root)
    cases_entry.pack(pady=5)
    
    tk.Label(root, text="Salary:").pack(pady=5)
    salary_entry = tk.Entry(root)
    salary_entry.pack(pady=5)
    
    def save_lawyer():
        row = [id_entry.get(), name_entry.get(), email_entry.get(), spec_entry.get(), exp_entry.get(), cases_entry.get(), salary_entry.get()]
        with open('lawyers.csv', 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(row)
        messagebox.showinfo("Success", "Lawyer added!")
        add_remove_entities(username)
    
    tk.Button(root, text="Save", command=save_lawyer).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: add_remove_entities(username)).pack(pady=10)
    clear_window()
    title = tk.Label(root, text="All Cases", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
        c = obj.cursor()
        c.execute("SELECT * FROM cases")
        rows = c.fetchall()
        if rows:
            headers = ["case_id", "lawyer_name", "type", "client_name", "date_of_completion", "description", "status", "payment_status", "notes"]
            text.insert(tk.END, '\t'.join(headers) + '\n\n')
            for row in rows:
                text.insert(tk.END, '\t'.join(str(x) for x in row) + '\n')
        else:
            text.insert(tk.END, "No cases found.")
        obj.close()
    except Exception as e:
        text.insert(tk.END, f"Error: {str(e)}")
    
    tk.Button(root, text="Back", command=lambda: admin_dashboard(username)).pack(pady=10)

def view_all_lawyers(username):
    clear_window()
    title = tk.Label(root, text="All Lawyers", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        with open('lawyers.csv', 'r') as f:
            r = csv.reader(f)
            headers = next(r, None)
            if headers:
                text.insert(tk.END, '\t'.join(headers) + '\n\n')
            for row in r:
                text.insert(tk.END, '\t'.join(row) + '\n')
    except FileNotFoundError:
        text.insert(tk.END, "Lawyers data not available.")
    
    tk.Button(root, text="Back", command=lambda: admin_dashboard(username)).pack(pady=10)

def view_all_clients(username):
    clear_window()
    title = tk.Label(root, text="All Clients", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
        c = obj.cursor()
        c.execute("SELECT DISTINCT client_name FROM cases")
        rows = c.fetchall()
        if rows:
            text.insert(tk.END, "Clients:\n\n")
            for row in rows:
                text.insert(tk.END, row[0] + '\n')
        else:
            text.insert(tk.END, "No clients found.")
        obj.close()
    except Exception as e:
        text.insert(tk.END, f"Error: {str(e)}")
    
    tk.Button(root, text="Back", command=lambda: admin_dashboard(username)).pack(pady=10)

def view_all_interns(username):
    clear_window()
    title = tk.Label(root, text="All Interns", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        with open('interns.csv', 'r') as f:
            r = csv.reader(f)
            headers = next(r, None)
            if headers:
                text.insert(tk.END, '\t'.join(headers) + '\n\n')
            for row in r:
                text.insert(tk.END, '\t'.join(row) + '\n')
    except FileNotFoundError:
        text.insert(tk.END, "Interns data not available.")
    
    tk.Button(root, text="Back", command=lambda: admin_dashboard(username)).pack(pady=10)

def view_cases_stats(username):
    clear_window()
    title = tk.Label(root, text="Cases Statistics", font=("Arial", 20))
    title.pack(pady=10)
    
    try:
        obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
        c = obj.cursor()
        c.execute("SELECT status, COUNT(*) FROM cases GROUP BY status")
        rows = c.fetchall()
        stats = {}
        for row in rows:
            stats[row[0]] = row[1]
        
        completed = stats.get('completed', 0)
        pending = stats.get('on going', 0)
        
        tk.Label(root, text=f"Completed Cases: {completed}").pack(pady=5)
        tk.Label(root, text=f"Pending Cases: {pending}").pack(pady=5)
        
        obj.close()
    except Exception as e:
        tk.Label(root, text=f"Error: {str(e)}").pack(pady=10)
    
    tk.Button(root, text="Back", command=lambda: admin_dashboard(username)).pack(pady=10)

def add_remove_entities(username):
    clear_window()
    title = tk.Label(root, text="Add/Remove Entities", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Button(root, text="Add Lawyer", command=lambda: add_lawyer(username)).pack(pady=5)
    tk.Button(root, text="Remove Lawyer", command=lambda: remove_lawyer(username)).pack(pady=5)
    tk.Button(root, text="Add Intern", command=lambda: add_intern(username)).pack(pady=5)
    tk.Button(root, text="Remove Intern", command=lambda: remove_intern(username)).pack(pady=5)
    tk.Button(root, text="Add Case", command=lambda: add_case(username)).pack(pady=5)
    tk.Button(root, text="Remove Case", command=lambda: remove_case(username)).pack(pady=5)
    
    tk.Button(root, text="Back", command=lambda: admin_dashboard(username)).pack(pady=10)

def edit_about_page(username):
    clear_window()
    title = tk.Label(root, text="Edit About Page", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        with open("About.txt", "r") as f:
            text.insert(tk.END, f.read())
    except FileNotFoundError:
        text.insert(tk.END, "")
    
    def save_about():
        with open("About.txt", "w") as f:
            f.write(text.get(1.0, tk.END))
        messagebox.showinfo("Success", "About page updated!")
    
    tk.Button(root, text="Save", command=save_about).pack(pady=5)
    tk.Button(root, text="Back", command=lambda: admin_dashboard(username)).pack(pady=10)

def add_lawyer(username):
    clear_window()
    title = tk.Label(root, text="Add Lawyer", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="ID:").pack(pady=5)
    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)
    
    tk.Label(root, text="Name:").pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)
    
    tk.Label(root, text="Email:").pack(pady=5)
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)
    
    tk.Label(root, text="Specialization:").pack(pady=5)
    spec_entry = tk.Entry(root)
    spec_entry.pack(pady=5)
    
    tk.Label(root, text="Experience Years:").pack(pady=5)
    exp_entry = tk.Entry(root)
    exp_entry.pack(pady=5)
    
    tk.Label(root, text="Cases Solved:").pack(pady=5)
    cases_entry = tk.Entry(root)
    cases_entry.pack(pady=5)
    
    tk.Label(root, text="Salary:").pack(pady=5)
    salary_entry = tk.Entry(root)
    salary_entry.pack(pady=5)
    
    def save_lawyer():
        row = [id_entry.get(), name_entry.get(), email_entry.get(), spec_entry.get(), exp_entry.get(), cases_entry.get(), salary_entry.get()]
        with open('lawyers.csv', 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(row)
        messagebox.showinfo("Success", "Lawyer added!")
        add_remove_entities(username)
    
    tk.Button(root, text="Save", command=save_lawyer).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: add_remove_entities(username)).pack(pady=10)

def remove_lawyer(username):
    clear_window()
    title = tk.Label(root, text="Remove Lawyer", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="Enter Lawyer ID to remove:").pack(pady=5)
    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)
    
    def remove():
        lid = id_entry.get()
        rows = []
        try:
            with open('lawyers.csv', 'r') as f:
                r = csv.reader(f)
                for row in r:
                    if row[0] != lid:
                        rows.append(row)
            with open('lawyers.csv', 'w', newline='') as f:
                w = csv.writer(f)
                w.writerows(rows)
            messagebox.showinfo("Success", "Lawyer removed!")
        except:
            messagebox.showerror("Error", "Failed to remove")
        add_remove_entities(username)
    
    tk.Button(root, text="Remove", command=remove).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: add_remove_entities(username)).pack(pady=10)

# Similarly for intern
def add_intern(username):
    clear_window()
    title = tk.Label(root, text="Add Intern", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="ID:").pack(pady=5)
    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)
    
    tk.Label(root, text="Name:").pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)
    
    tk.Label(root, text="Email:").pack(pady=5)
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)
    
    tk.Label(root, text="Phone:").pack(pady=5)
    phone_entry = tk.Entry(root)
    phone_entry.pack(pady=5)
    
    tk.Label(root, text="LinkedIn/Profile:").pack(pady=5)
    linkedin_entry = tk.Entry(root)
    linkedin_entry.pack(pady=5)
    
    tk.Label(root, text="Skills:").pack(pady=5)
    skills_entry = tk.Entry(root)
    skills_entry.pack(pady=5)
    
    def save_intern():
        row = [id_entry.get(), name_entry.get(), email_entry.get(), phone_entry.get(), linkedin_entry.get(), skills_entry.get()]
        with open('interns.csv', 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(row)
        messagebox.showinfo("Success", "Intern added!")
        add_remove_entities(username)
    
    tk.Button(root, text="Save", command=save_intern).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: add_remove_entities(username)).pack(pady=10)

def remove_intern(username):
    clear_window()
    title = tk.Label(root, text="Remove Intern", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="Enter Intern ID to remove:").pack(pady=5)
    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)
    
    def remove():
        iid = id_entry.get()
        rows = []
        try:
            with open('interns.csv', 'r') as f:
                r = csv.reader(f)
                for row in r:
                    if row[0] != iid:
                        rows.append(row)
            with open('interns.csv', 'w', newline='') as f:
                w = csv.writer(f)
                w.writerows(rows)
            messagebox.showinfo("Success", "Intern removed!")
        except:
            messagebox.showerror("Error", "Failed to remove")
        add_remove_entities(username)
    
    tk.Button(root, text="Remove", command=remove).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: add_remove_entities(username)).pack(pady=10)

def add_case(username):
    clear_window()
    title = tk.Label(root, text="Add Case", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="Case ID:").pack(pady=5)
    case_id_entry = tk.Entry(root)
    case_id_entry.pack(pady=5)
    
    tk.Label(root, text="Lawyer Name:").pack(pady=5)
    lawyer_entry = tk.Entry(root)
    lawyer_entry.pack(pady=5)
    
    tk.Label(root, text="Type:").pack(pady=5)
    type_entry = tk.Entry(root)
    type_entry.pack(pady=5)
    
    tk.Label(root, text="Client Name:").pack(pady=5)
    client_entry = tk.Entry(root)
    client_entry.pack(pady=5)
    
    tk.Label(root, text="Date of Completion:").pack(pady=5)
    date_entry = tk.Entry(root)
    date_entry.pack(pady=5)
    
    tk.Label(root, text="Description:").pack(pady=5)
    desc_entry = tk.Entry(root)
    desc_entry.pack(pady=5)
    
    tk.Label(root, text="Status:").pack(pady=5)
    status_entry = tk.Entry(root)
    status_entry.pack(pady=5)
    
    tk.Label(root, text="Payment Status:").pack(pady=5)
    pay_entry = tk.Entry(root)
    pay_entry.pack(pady=5)
    
    tk.Label(root, text="Notes:").pack(pady=5)
    notes_entry = tk.Entry(root)
    notes_entry.pack(pady=5)
    
    def save_case():
        try:
            obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
            c = obj.cursor()
            c.execute("INSERT INTO cases VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                      (case_id_entry.get(), lawyer_entry.get(), type_entry.get(), client_entry.get(), 
                       date_entry.get(), desc_entry.get(), status_entry.get(), pay_entry.get(), notes_entry.get()))
            obj.commit()
            obj.close()
            messagebox.showinfo("Success", "Case added!")
            add_remove_entities(username)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    tk.Button(root, text="Save", command=save_case).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: add_remove_entities(username)).pack(pady=10)

def remove_case(username):
    clear_window()
    title = tk.Label(root, text="Remove Case", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="Enter Case ID to remove:").pack(pady=5)
    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)
    
    def remove():
        cid = id_entry.get()
        try:
            obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
            c = obj.cursor()
            c.execute("DELETE FROM cases WHERE case_id = %s", (cid,))
            obj.commit()
            obj.close()
            messagebox.showinfo("Success", "Case removed!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        add_remove_entities(username)
    
    tk.Button(root, text="Remove", command=remove).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: add_remove_entities(username)).pack(pady=10)

# Lawyer functions
def view_my_cases(username):
    clear_window()
    title = tk.Label(root, text="My Cases", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
        c = obj.cursor()
        c.execute("SELECT * FROM cases WHERE lawyer_name = %s", (username,))
        rows = c.fetchall()
        if rows:
            headers = ["case_id", "lawyer_name", "type", "client_name", "date_of_completion", "description", "status", "payment_status", "notes"]
            text.insert(tk.END, '\t'.join(headers) + '\n\n')
            for row in rows:
                text.insert(tk.END, '\t'.join(str(x) for x in row) + '\n')
        else:
            text.insert(tk.END, "No cases found.")
        obj.close()
    except Exception as e:
        text.insert(tk.END, f"Error: {str(e)}")
    
    tk.Button(root, text="Back", command=lambda: lawyer_dashboard(username)).pack(pady=10)

def view_my_clients(username):
    clear_window()
    title = tk.Label(root, text="My Clients", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
        c = obj.cursor()
        c.execute("SELECT DISTINCT client_name FROM cases WHERE lawyer_name = %s", (username,))
        rows = c.fetchall()
        if rows:
            text.insert(tk.END, "Clients:\n\n")
            for row in rows:
                text.insert(tk.END, row[0] + '\n')
        else:
            text.insert(tk.END, "No clients found.")
        obj.close()
    except Exception as e:
        text.insert(tk.END, f"Error: {str(e)}")
    
    tk.Button(root, text="Back", command=lambda: lawyer_dashboard(username)).pack(pady=10)

def view_requests(username):
    clear_window()
    title = tk.Label(root, text="Requests", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
        c = obj.cursor()
        c.execute("SELECT * FROM requests WHERE lawyer_name = %s", (username,))
        rows = c.fetchall()
        if rows:
            headers = ["id", "lawyer_name", "type", "client_name", "details"]
            text.insert(tk.END, '\t'.join(headers) + '\n\n')
            for row in rows:
                text.insert(tk.END, '\t'.join(str(x) for x in row) + '\n')
        else:
            text.insert(tk.END, "No requests found.")
        obj.close()
    except Exception as e:
        text.insert(tk.END, f"Error: {str(e)}")
    
    tk.Button(root, text="Back", command=lambda: lawyer_dashboard(username)).pack(pady=10)

def update_case_status(username):
    clear_window()
    title = tk.Label(root, text="Update Case Status", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="Case ID:").pack(pady=5)
    case_id_entry = tk.Entry(root)
    case_id_entry.pack(pady=5)
    
    tk.Label(root, text="New Status:").pack(pady=5)
    status_entry = tk.Entry(root)
    status_entry.pack(pady=5)
    
    tk.Label(root, text="Notes:").pack(pady=5)
    notes_entry = tk.Entry(root)
    notes_entry.pack(pady=5)
    
    def update():
        try:
            obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
            c = obj.cursor()
            c.execute("UPDATE cases SET status = %s, notes = %s WHERE case_id = %s AND lawyer_name = %s", 
                      (status_entry.get(), notes_entry.get(), case_id_entry.get(), username))
            obj.commit()
            obj.close()
            messagebox.showinfo("Success", "Case updated!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        lawyer_dashboard(username)
    
    tk.Button(root, text="Update", command=update).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: lawyer_dashboard(username)).pack(pady=10)

def accept_reject_requests(username):
    clear_window()
    title = tk.Label(root, text="Accept/Reject Requests", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="Request ID:").pack(pady=5)
    req_id_entry = tk.Entry(root)
    req_id_entry.pack(pady=5)
    
    tk.Label(root, text="Action (accept/reject):").pack(pady=5)
    action_entry = tk.Entry(root)
    action_entry.pack(pady=5)
    
    def process():
        action = action_entry.get().lower()
        if action == 'accept':
            # Create case from request
            try:
                obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
                c = obj.cursor()
                c.execute("SELECT * FROM requests WHERE id = %s", (req_id_entry.get(),))
                req = c.fetchone()
                if req:
                    c.execute("INSERT INTO cases (case_id, lawyer_name, type, client_name, description, status) VALUES (%s, %s, %s, %s, %s, 'on going')", 
                              (req[0], req[1], req[2], req[3], req[4]))
                    c.execute("DELETE FROM requests WHERE id = %s", (req_id_entry.get(),))
                    obj.commit()
                    messagebox.showinfo("Success", "Request accepted!")
                obj.close()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif action == 'reject':
            try:
                obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
                c = obj.cursor()
                c.execute("DELETE FROM requests WHERE id = %s", (req_id_entry.get(),))
                obj.commit()
                obj.close()
                messagebox.showinfo("Success", "Request rejected!")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        lawyer_dashboard(username)
    
    tk.Button(root, text="Process", command=process).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: lawyer_dashboard(username)).pack(pady=10)

def assign_intern_work(username):
    # Placeholder
    clear_window()
    title = tk.Label(root, text="Assign Intern Work", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="Feature not implemented yet").pack(pady=10)
    
    tk.Button(root, text="Back", command=lambda: lawyer_dashboard(username)).pack(pady=10)

def view_lawyers():
    clear_window()
    title = tk.Label(root, text="Lawyers", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        with open('lawyers.csv', 'r') as f:
            r = csv.reader(f)
            headers = next(r, None)
            if headers:
                text.insert(tk.END, '\t'.join(headers) + '\n\n')
            for row in r:
                text.insert(tk.END, '\t'.join(row) + '\n')
    except FileNotFoundError:
        text.insert(tk.END, "Lawyers data not available.")
    
    tk.Button(root, text="Back", command=lambda: client_dashboard("client")).pack(pady=10)  # Need to pass username, but since it's global, perhaps change

# Actually, to fix, make view_lawyers take username
def view_lawyers(username):
    clear_window()
    title = tk.Label(root, text="Lawyers", font=("Arial", 20))
    title.pack(pady=10)
    
    frame = tk.Frame(root)
    frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    text = tk.Text(frame, wrap=tk.WORD, font=("Courier", 10), yscrollcommand=scrollbar.set)
    text.pack(expand=True, fill=tk.BOTH)
    
    scrollbar.config(command=text.yview)
    
    try:
        with open('lawyers.csv', 'r') as f:
            r = csv.reader(f)
            data = list(r)
            if data:
                table = tabulate.tabulate(data, headers="firstrow", tablefmt="grid")
                text.insert(tk.END, table)
            else:
                text.insert(tk.END, "No lawyers data available.")
    except FileNotFoundError:
        text.insert(tk.END, "Lawyers data not available.")
    
    tk.Button(root, text="Back", command=lambda: client_dashboard(username)).pack(pady=10)

def view_my_cases_client(username):
    clear_window()
    title = tk.Label(root, text="My Cases", font=("Arial", 20))
    title.pack(pady=10)
    
    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
    
    try:
        obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
        c = obj.cursor()
        c.execute("SELECT * FROM cases WHERE client_name = %s", (username,))
        rows = c.fetchall()
        if rows:
            headers = ["case_id", "lawyer_name", "type", "client_name", "date_of_completion", "description", "status", "payment_status", "notes"]
            text.insert(tk.END, '\t'.join(headers) + '\n\n')
            for row in rows:
                text.insert(tk.END, '\t'.join(str(x) for x in row) + '\n')
        else:
            text.insert(tk.END, "No cases found.")
        obj.close()
    except Exception as e:
        text.insert(tk.END, f"Error: {str(e)}")
    
    tk.Button(root, text="Back", command=lambda: client_dashboard(username)).pack(pady=10)

def create_new_request(username):
    clear_window()
    title = tk.Label(root, text="Create New Request", font=("Arial", 20))
    title.pack(pady=10)
    
    # Display lawyers table
    lawyers_label = tk.Label(root, text="Available Lawyers:", font=("Arial", 14))
    lawyers_label.pack(pady=5)
    
    lawyers_frame = tk.Frame(root)
    lawyers_frame.pack(expand=False, fill=tk.X, padx=20, pady=5)
    
    lawyers_scrollbar = tk.Scrollbar(lawyers_frame)
    lawyers_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    lawyers_text = tk.Text(lawyers_frame, wrap=tk.WORD, font=("Courier", 10), height=10, yscrollcommand=lawyers_scrollbar.set)
    lawyers_text.pack(expand=True, fill=tk.X)
    
    lawyers_scrollbar.config(command=lawyers_text.yview)
    
    try:
        with open('lawyers.csv', 'r') as f:
            r = csv.reader(f)
            data = list(r)
            if data:
                table = tabulate.tabulate(data, headers="firstrow", tablefmt="grid")
                lawyers_text.insert(tk.END, table)
                
            else:
                lawyers_text.insert(tk.END, "No lawyers available.")
    except FileNotFoundError:
        lawyers_text.insert(tk.END, "Lawyers data not available.")
    
    lawyers_text.config(state=tk.DISABLED)  # Make it read-only
    
    # Form
    tk.Label(root, text="Request ID:").pack(pady=5)
    req_id_entry = tk.Entry(root)
    req_id_entry.pack(pady=5)
    
    tk.Label(root, text="Lawyer Name:").pack(pady=5)
    lawyer_entry = tk.Entry(root)
    lawyer_entry.pack(pady=5)
    
    tk.Label(root, text="Type:").pack(pady=5)
    type_entry = tk.Entry(root)
    type_entry.pack(pady=5)
    
    tk.Label(root, text="Details:").pack(pady=5)
    details_entry = tk.Entry(root)
    details_entry.pack(pady=5)
    
    def save_request():
        try:
            obj = pymysql.connect(host="127.0.0.1", user="root", password="smh2MySQL!", database="trial", port=3306)
            c = obj.cursor()
            c.execute("INSERT INTO requests VALUES (%s, %s, %s, %s, %s)", 
                      (req_id_entry.get(), lawyer_entry.get(), type_entry.get(), username, details_entry.get()))
            obj.commit()
            obj.close()
            messagebox.showinfo("Success", "Request created!")
            client_dashboard(username)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    tk.Button(root, text="Save", command=save_request).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: client_dashboard(username)).pack(pady=10)

# Intern functions
def apply_internship(username):
    # Assume username is the intern's name or something, but since signup adds to login, perhaps add to interns.csv
    clear_window()
    title = tk.Label(root, text="Apply for Internship", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="Name:").pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)
    
    tk.Label(root, text="Email:").pack(pady=5)
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)
    
    tk.Label(root, text="Phone:").pack(pady=5)
    phone_entry = tk.Entry(root)
    phone_entry.pack(pady=5)
    
    tk.Label(root, text="LinkedIn/Profile:").pack(pady=5)
    linkedin_entry = tk.Entry(root)
    linkedin_entry.pack(pady=5)
    
    tk.Label(root, text="Skills:").pack(pady=5)
    skills_entry = tk.Entry(root)
    skills_entry.pack(pady=5)
    
    def apply():
        row = [username, name_entry.get(), email_entry.get(), phone_entry.get(), linkedin_entry.get(), skills_entry.get()]
        with open('interns.csv', 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(row)
        messagebox.showinfo("Success", "Application submitted!")
        intern_dashboard(username)
    
    tk.Button(root, text="Apply", command=apply).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: intern_dashboard(username)).pack(pady=10)

def view_application_status(username):
    clear_window()
    title = tk.Label(root, text="Application Status", font=("Arial", 20))
    title.pack(pady=10)
    
    try:
        with open('interns.csv', 'r') as f:
            r = csv.reader(f)
            for row in r:
                if row[0] == username:
                    tk.Label(root, text="Application found. Status: Approved").pack(pady=10)
                    break
            else:
                tk.Label(root, text="No application found.").pack(pady=10)
    except FileNotFoundError:
        tk.Label(root, text="No applications.").pack(pady=10)
    
    tk.Button(root, text="Back", command=lambda: intern_dashboard(username)).pack(pady=10)

def view_assigned_work(username):
    # Placeholder
    clear_window()
    title = tk.Label(root, text="Assigned Work", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="No work assigned yet.").pack(pady=10)
    
    tk.Button(root, text="Back", command=lambda: intern_dashboard(username)).pack(pady=10)

def update_work_status(username):
    # Placeholder
    clear_window()
    title = tk.Label(root, text="Update Work Status", font=("Arial", 20))
    title.pack(pady=10)
    
    tk.Label(root, text="Feature not implemented yet.").pack(pady=10)
    
    tk.Button(root, text="Back", command=lambda: intern_dashboard(username)).pack(pady=10)


def about_us():
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


#Main Program
root = tk.Tk()
root.title("Law Firm Management System")
root.geometry("800x600")
def main_screen():
    clear_window()
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
