import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pymysql
import webbrowser
from datetime import datetime
import pickle
import os
import csv

# Database connection configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'smh2sql',
    'database': 'LAWFIRM'
}

class DatabaseConnection:
    """Handle all database connections"""
    @staticmethod
    def connect():
        try:
            connection = pymysql.connect(**DB_CONFIG)
            return connection
        except pymysql.Error as err:
            messagebox.showerror("Database Error", f"Connection failed: {err}")
            return None

class LoginGUI:
    """User and Lawyer Login System"""
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title("Law Firm - Login")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        # Title
        title = ttk.Label(self.root, text="Justice League Law Firm", 
                         font=("Arial", 16, "bold"))
        title.pack(pady=20)
        
        # Login Type
        type_frame = ttk.LabelFrame(self.root, text="Select Login Type", padding=10)
        type_frame.pack(padx=20, pady=10, fill="x")
        
        self.login_type = tk.StringVar(value="user")
        ttk.Radiobutton(type_frame, text="User", variable=self.login_type, 
                       value="user").pack(anchor="w")
        ttk.Radiobutton(type_frame, text="Lawyer", variable=self.login_type, 
                       value="lawyer").pack(anchor="w")
        ttk.Radiobutton(type_frame, text="Admin", variable=self.login_type, 
                       value="admin").pack(anchor="w")
        
        # Login Form
        form_frame = ttk.LabelFrame(self.root, text="Login Credentials", padding=10)
        form_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        ttk.Label(form_frame, text="Username:").grid(row=0, column=0, sticky="w", pady=10)
        self.username_entry = ttk.Entry(form_frame, width=30)
        self.username_entry.grid(row=0, column=1, pady=10, padx=10)
        
        ttk.Label(form_frame, text="Password:").grid(row=1, column=0, sticky="w", pady=10)
        self.password_entry = ttk.Entry(form_frame, width=30, show="*")
        self.password_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(padx=20, pady=10, fill="x")
        
        ttk.Button(button_frame, text="Login", command=self.login).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Register", command=self.register).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side="left", padx=5)
    
    def login(self):
        """Handle login"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        login_type = self.login_type.get()
        
        if not username or not password:
            messagebox.showwarning("Warning", "Please enter username and password")
            return
        
        # Read credentials from CSV
        try:
            with open("usernames.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and row[0] == username and row[1] == password:
                        self.callback(username, login_type)
                        self.root.destroy()
                        return
            
            messagebox.showerror("Error", "Invalid credentials")
        except FileNotFoundError:
            messagebox.showerror("Error", "User database not found")
    
    def register(self):
        """Handle registration"""
        register_window = tk.Toplevel(self.root)
        register_window.title("Register")
        register_window.geometry("400x300")
        
        ttk.Label(register_window, text="Full Name:").grid(row=0, column=0, sticky="w", pady=10, padx=10)
        fullname_entry = ttk.Entry(register_window, width=30)
        fullname_entry.grid(row=0, column=1, pady=10, padx=10)
        
        ttk.Label(register_window, text="Username:").grid(row=1, column=0, sticky="w", pady=10, padx=10)
        username_entry = ttk.Entry(register_window, width=30)
        username_entry.grid(row=1, column=1, pady=10, padx=10)
        
        ttk.Label(register_window, text="Password:").grid(row=2, column=0, sticky="w", pady=10, padx=10)
        password_entry = ttk.Entry(register_window, width=30, show="*")
        password_entry.grid(row=2, column=1, pady=10, padx=10)
        
        ttk.Label(register_window, text="Confirm Password:").grid(row=3, column=0, sticky="w", pady=10, padx=10)
        confirm_entry = ttk.Entry(register_window, width=30, show="*")
        confirm_entry.grid(row=3, column=1, pady=10, padx=10)
        
        def save_user():
            fullname = fullname_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            confirm = confirm_entry.get()
            
            if not all([fullname, username, password, confirm]):
                messagebox.showwarning("Warning", "Please fill all fields")
                return
            
            if password != confirm:
                messagebox.showerror("Error", "Passwords do not match")
                return
            
            try:
                with open("usernames.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([username, password, "User"])
                messagebox.showinfo("Success", "Registration successful! Please login.")
                register_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Registration failed: {e}")
        
        ttk.Button(register_window, text="Register", command=save_user).grid(row=4, column=0, columnspan=2, pady=20)


class UserDashboard:
    """User Dashboard for requesting lawyers"""
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.connection = DatabaseConnection.connect()
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title(f"User Dashboard - {self.username}")
        self.root.geometry("700x600")
        
        # Title
        title = ttk.Label(self.root, text=f"Welcome, {self.username}!", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Menu
        menu_frame = ttk.Frame(self.root)
        menu_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Button(menu_frame, text="Request Lawyer", command=self.request_lawyer).pack(side="left", padx=5)
        ttk.Button(menu_frame, text="View Cases", command=self.view_cases).pack(side="left", padx=5)
        ttk.Button(menu_frame, text="Logout", command=self.root.destroy).pack(side="left", padx=5)
        
        # Content Frame
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    def request_lawyer(self):
        """Request a lawyer"""
        self.clear_content()
        
        request_frame = ttk.LabelFrame(self.content_frame, text="Request a Lawyer", padding=10)
        request_frame.pack(fill="both", expand=True)
        
        ttk.Label(request_frame, text="Select Case Type:").pack(anchor="w", pady=5)
        
        case_types = [
            "Immigration Law", "Criminal Law", "Real Estate Law",
            "Business Law", "Family Law", "Bankruptcy Law", "Tax Law"
        ]
        
        self.case_type = tk.StringVar(value=case_types[0])
        for case_type in case_types:
            ttk.Radiobutton(request_frame, text=case_type, variable=self.case_type,
                           value=case_type).pack(anchor="w", pady=3)
        
        ttk.Label(request_frame, text="Case Description:").pack(anchor="w", pady=(10, 5))
        self.case_desc = tk.Text(request_frame, height=5, width=50)
        self.case_desc.pack(fill="both", expand=True, pady=5)
        
        ttk.Label(request_frame, text="Urgency Level:").pack(anchor="w", pady=5)
        self.urgency = tk.StringVar(value="Normal")
        ttk.Radiobutton(request_frame, text="Normal Priority", variable=self.urgency,
                       value="2").pack(anchor="w")
        ttk.Radiobutton(request_frame, text="VIP Priority", variable=self.urgency,
                       value="1").pack(anchor="w")
        
        ttk.Button(request_frame, text="Submit Request", 
                  command=self.submit_request).pack(pady=10)
    
    def submit_request(self):
        """Submit lawyer request"""
        case_type = self.case_type.get()
        description = self.case_desc.get("1.0", tk.END)
        urgency = self.urgency.get()
        
        if not description.strip():
            messagebox.showwarning("Warning", "Please enter case description")
            return
        
        try:
            request_data = [
                None,  # Lawyer ID (to be filled)
                self.username,  # Client name
                datetime.now().strftime("%d/%m/%Y"),  # Date of request
                None, None,  # Lawyer name (to be filled)
                description.strip(),  # Description
                urgency  # Urgency code
            ]
            
            with open("request.dat", "ab") as f:
                pickle.dump(request_data, f)
            
            messagebox.showinfo("Success", "Request submitted successfully")
            self.request_lawyer()  # Refresh the form
        except Exception as e:
            messagebox.showerror("Error", f"Failed to submit request: {e}")
    
    def view_cases(self):
        """View user's cases"""
        self.clear_content()
        
        cases_frame = ttk.LabelFrame(self.content_frame, text="Your Cases", padding=10)
        cases_frame.pack(fill="both", expand=True)
        
        # Create treeview for cases
        tree = ttk.Treeview(cases_frame, columns=("Lawyer", "Date", "Type", "Status"),
                           height=15, show="headings")
        
        tree.column("Lawyer", width=150)
        tree.column("Date", width=100)
        tree.column("Type", width=150)
        tree.column("Status", width=100)
        
        tree.heading("Lawyer", text="Lawyer")
        tree.heading("Date", text="Date")
        tree.heading("Type", text="Case Type")
        tree.heading("Status", text="Status")
        
        # Load cases from file
        try:
            with open("request.dat", "rb") as f:
                while True:
                    try:
                        data = pickle.load(f)
                        if self.username in data[1]:
                            tree.insert("", "end", values=(
                                data[3] if len(data) > 3 else "Pending",
                                data[2],
                                "Case Type",
                                "Pending"
                            ))
                    except EOFError:
                        break
        except FileNotFoundError:
            ttk.Label(cases_frame, text="No cases found").pack()
        
        scrollbar = ttk.Scrollbar(cases_frame, orient="vertical", command=tree.yview)
        tree.config(yscroll=scrollbar.set)
        
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def clear_content(self):
        """Clear content frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()


class LawyerDashboard:
    """Lawyer Dashboard for viewing and approving cases"""
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.connection = DatabaseConnection.connect()
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title(f"Lawyer Dashboard - {self.username}")
        self.root.geometry("800x700")
        
        # Title
        title = ttk.Label(self.root, text=f"Welcome, {self.username}!", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Menu
        menu_frame = ttk.Frame(self.root)
        menu_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Button(menu_frame, text="View Requests", command=self.view_requests).pack(side="left", padx=5)
        ttk.Button(menu_frame, text="Manage Cases", command=self.manage_cases).pack(side="left", padx=5)
        ttk.Button(menu_frame, text="Logout", command=self.root.destroy).pack(side="left", padx=5)
        
        # Content Frame
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.view_requests()
    
    def view_requests(self):
        """View pending lawyer requests"""
        self.clear_content()
        
        requests_frame = ttk.LabelFrame(self.content_frame, text="Pending Requests", padding=10)
        requests_frame.pack(fill="both", expand=True)
        
        # Treeview for requests
        tree = ttk.Treeview(requests_frame, columns=("Client", "Date", "Description", "Urgency"),
                           height=15, show="headings")
        
        tree.column("Client", width=120)
        tree.column("Date", width=100)
        tree.column("Description", width=300)
        tree.column("Urgency", width=80)
        
        tree.heading("Client", text="Client Name")
        tree.heading("Date", text="Date")
        tree.heading("Description", text="Description")
        tree.heading("Urgency", text="Urgency")
        
        # Load requests
        try:
            with open("request.dat", "rb") as f:
                while True:
                    try:
                        data = pickle.load(f)
                        tree.insert("", "end", values=(
                            data[1],
                            data[2],
                            data[5][:50] if len(data) > 5 else "",
                            "VIP" if data[6] == "1" else "Normal" if len(data) > 6 else ""
                        ))
                    except EOFError:
                        break
        except FileNotFoundError:
            ttk.Label(requests_frame, text="No pending requests").pack()
        
        scrollbar = ttk.Scrollbar(requests_frame, orient="vertical", command=tree.yview)
        tree.config(yscroll=scrollbar.set)
        
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Approve button
        ttk.Button(self.content_frame, text="Approve Selected Case",
                  command=self.approve_case).pack(pady=10)
    
    def manage_cases(self):
        """Manage assigned cases"""
        self.clear_content()
        
        cases_frame = ttk.LabelFrame(self.content_frame, text="Your Cases", padding=10)
        cases_frame.pack(fill="both", expand=True)
        
        ttk.Label(cases_frame, text="Case management features coming soon").pack(pady=20)
    
    def approve_case(self):
        """Approve a case request"""
        messagebox.showinfo("Info", "Please select a case to approve")
    
    def clear_content(self):
        """Clear content frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()


class AdminDashboard:
    """Admin Dashboard for system management"""
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.connection = DatabaseConnection.connect()
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title(f"Admin Dashboard - {self.username}")
        self.root.geometry("700x600")
        
        # Title
        title = ttk.Label(self.root, text=f"Admin Panel - {self.username}", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Menu
        menu_frame = ttk.LabelFrame(self.root, text="Administrative Functions", padding=10)
        menu_frame.pack(padx=10, pady=10, fill="both")
        
        ttk.Button(menu_frame, text="Manage Lawyers", width=30,
                  command=self.manage_lawyers).pack(pady=5)
        ttk.Button(menu_frame, text="View All Cases", width=30,
                  command=self.view_all_cases).pack(pady=5)
        ttk.Button(menu_frame, text="View Reports", width=30,
                  command=self.view_reports).pack(pady=5)
        ttk.Button(menu_frame, text="System Settings", width=30,
                  command=self.system_settings).pack(pady=5)
        ttk.Button(menu_frame, text="Logout", width=30,
                  command=self.root.destroy).pack(pady=5)
    
    def manage_lawyers(self):
        """Manage lawyer profiles"""
        messagebox.showinfo("Info", "Lawyer management interface opening...")
    
    def view_all_cases(self):
        """View all cases in the system"""
        messagebox.showinfo("Info", "Case overview interface opening...")
    
    def view_reports(self):
        """View system reports"""
        messagebox.showinfo("Info", "Reports interface opening...")
    
    def system_settings(self):
        """System configuration"""
        messagebox.showinfo("Info", "System settings interface opening...")


class MainApplication:
    """Main Application Entry Point"""
    def __init__(self, root):
        self.root = root
        self.root.withdraw()  # Hide main window
        self.show_login()
    
    def show_login(self):
        """Show login window"""
        login_window = tk.Toplevel(self.root)
        LoginGUI(login_window, self.on_login_success)
    
    def on_login_success(self, username, login_type):
        """Handle successful login"""
        self.root.deiconify()
        self.root.title("Law Firm Management System")
        self.root.geometry("800x700")
        
        if login_type == "user":
            UserDashboard(self.root, username)
        elif login_type == "lawyer":
            LawyerDashboard(self.root, username)
        elif login_type == "admin":
            AdminDashboard(self.root, username)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
