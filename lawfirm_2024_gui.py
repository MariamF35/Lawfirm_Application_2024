import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pymysql
import webbrowser
import csv
import pickle
import os
import random
from tkinter import filedialog

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

class LawyerFinderGUI:
    """Main GUI for searching lawyers by speciality"""
    def __init__(self, root, parent_window):
        self.root = root
        self.parent_window = parent_window
        self.connection = DatabaseConnection.connect()
        
        if not self.connection:
            return
            
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title("Find Lawyer by Speciality")
        self.root.geometry("700x600")
        
        # Title
        title = ttk.Label(self.root, text="Search Lawyers by Speciality", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Speciality Frame
        spec_frame = ttk.LabelFrame(self.root, text="Select Speciality", padding=10)
        spec_frame.pack(padx=10, pady=10, fill="both")
        
        specialities = [
            "Immigration Law", "Criminal Law", "Real Estate Law",
            "Business Law", "Family Law", "Bankruptcy Law", "Tax Law"
        ]
        
        self.speciality_var = tk.StringVar(value=specialities[0])
        
        for spec in specialities:
            ttk.Radiobutton(spec_frame, text=spec, variable=self.speciality_var,
                           value=spec).pack(anchor="w", pady=5)
        
        # Search Button
        ttk.Button(spec_frame, text="Search Lawyers", 
                  command=self.search_lawyers).pack(pady=10)
        
        # Results Frame
        results_frame = ttk.LabelFrame(self.root, text="Results", padding=10)
        results_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Treeview for results
        self.tree = ttk.Treeview(results_frame, columns=("Name", "Age", "Speciality", "Experience"),
                                 height=12, show="headings")
        self.tree.column("Name", width=150)
        self.tree.column("Age", width=80)
        self.tree.column("Speciality", width=150)
        self.tree.column("Experience", width=100)
        
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Speciality", text="Speciality")
        self.tree.heading("Experience", text="Years Experience")
        
        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.tree.yview)
        self.tree.config(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # View CV Button
        button_frame = ttk.Frame(self.root)
        button_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Button(button_frame, text="View CV", command=self.view_cv).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.root.destroy).pack(side="left", padx=5)
    
    def search_lawyers(self):
        """Search lawyers by speciality"""
        speciality = self.speciality_var.get()
        query = "SELECT NAME, AGE, SPECIALITY, YEARS_OF_EXPERIENCE FROM NEWLAWYER WHERE SPECIALITY = %s"
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (speciality,))
            results = cursor.fetchall()
            
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            if results:
                for row in results:
                    self.tree.insert("", "end", values=row)
                messagebox.showinfo("Success", f"Found {len(results)} lawyer(s)")
            else:
                messagebox.showwarning("No Results", "No lawyers found for this speciality")
            
            cursor.close()
        except pymysql.Error as err:
            messagebox.showerror("Error", f"Query failed: {err}")
    
    def view_cv(self):
        """View selected lawyer's CV"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a lawyer first")
            return
        
        item = self.tree.item(selected[0])
        lawyer_name = item['values'][0]
        
        query = "SELECT CV_LINK FROM NEWLAWYER WHERE NAME = %s"
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (lawyer_name,))
            result = cursor.fetchone()
            
            if result and result[0]:
                webbrowser.open(result[0])
                messagebox.showinfo("Success", "CV opened in browser")
            else:
                messagebox.showwarning("Error", "No CV link available for this lawyer")
            
            cursor.close()
        except pymysql.Error as err:
            messagebox.showerror("Error", f"Query failed: {err}")


class ManageLawyerGUI:
    """GUI for managing lawyer profiles"""
    def __init__(self, root):
        self.root = root
        self.connection = DatabaseConnection.connect()
        
        if not self.connection:
            return
        
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title("Manage Lawyer Profiles")
        self.root.geometry("800x700")
        
        # Title
        title = ttk.Label(self.root, text="Lawyer Profile Management", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Menu Buttons
        menu_frame = ttk.Frame(self.root)
        menu_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Button(menu_frame, text="New Entry", command=self.new_entry).pack(side="left", padx=5)
        ttk.Button(menu_frame, text="Update Entry", command=self.update_entry).pack(side="left", padx=5)
        ttk.Button(menu_frame, text="Delete Entry", command=self.delete_entry).pack(side="left", padx=5)
        ttk.Button(menu_frame, text="Back", command=self.root.destroy).pack(side="left", padx=5)
        
        # Info Frame
        info_frame = ttk.LabelFrame(self.root, text="Lawyer Information", padding=10)
        info_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Name
        ttk.Label(info_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = ttk.Entry(info_frame, width=40)
        self.name_entry.grid(row=0, column=1, pady=5, padx=5)
        
        # Age
        ttk.Label(info_frame, text="Age:").grid(row=1, column=0, sticky="w", pady=5)
        self.age_entry = ttk.Entry(info_frame, width=40)
        self.age_entry.grid(row=1, column=1, pady=5, padx=5)
        
        # CV Link
        ttk.Label(info_frame, text="CV Link:").grid(row=2, column=0, sticky="w", pady=5)
        self.cv_entry = ttk.Entry(info_frame, width=40)
        self.cv_entry.grid(row=2, column=1, pady=5, padx=5)
        
        # Speciality
        ttk.Label(info_frame, text="Speciality:").grid(row=3, column=0, sticky="w", pady=5)
        self.spec_var = tk.StringVar()
        spec_combo = ttk.Combobox(info_frame, textvariable=self.spec_var, width=38,
                                 values=["Immigration Law", "Criminal Law", "Real Estate Law",
                                        "Business Law", "Family Law", "Bankruptcy Law", "Tax Law"])
        spec_combo.grid(row=3, column=1, pady=5, padx=5)
        
        # Years of Experience
        ttk.Label(info_frame, text="Years of Experience:").grid(row=4, column=0, sticky="w", pady=5)
        self.exp_entry = ttk.Entry(info_frame, width=40)
        self.exp_entry.grid(row=4, column=1, pady=5, padx=5)
        
        # Status
        self.status_label = ttk.Label(self.root, text="", foreground="green")
        self.status_label.pack(pady=5)
    
    def new_entry(self):
        """Add new lawyer entry"""
        name = self.name_entry.get()
        age = self.age_entry.get()
        cv_link = self.cv_entry.get()
        speciality = self.spec_var.get()
        experience = self.exp_entry.get()
        
        if not all([name, age, cv_link, speciality, experience]):
            messagebox.showwarning("Warning", "Please fill all fields")
            return
        
        query = "INSERT INTO NEWLAWYER (NAME, AGE, CV_LINK, SPECIALITY, YEARS_OF_EXPERIENCE) VALUES (%s, %s, %s, %s, %s)"
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (name, int(age), cv_link, speciality, int(experience)))
            self.connection.commit()
            messagebox.showinfo("Success", "Lawyer profile added successfully")
            self.clear_fields()
            cursor.close()
        except pymysql.Error as err:
            messagebox.showerror("Error", f"Failed to add entry: {err}")
    
    def update_entry(self):
        """Update lawyer entry"""
        name = self.name_entry.get()
        if not name:
            messagebox.showwarning("Warning", "Please enter lawyer name to update")
            return
        
        age = self.age_entry.get()
        cv_link = self.cv_entry.get()
        speciality = self.spec_var.get()
        experience = self.exp_entry.get()
        
        query = "UPDATE NEWLAWYER SET AGE=%s, CV_LINK=%s, SPECIALITY=%s, YEARS_OF_EXPERIENCE=%s WHERE NAME=%s"
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (int(age) if age else None, cv_link, speciality, 
                                 int(experience) if experience else None, name))
            self.connection.commit()
            messagebox.showinfo("Success", "Lawyer profile updated successfully")
            self.clear_fields()
            cursor.close()
        except pymysql.Error as err:
            messagebox.showerror("Error", f"Failed to update entry: {err}")
    
    def delete_entry(self):
        """Delete lawyer entry"""
        name = self.name_entry.get()
        if not name:
            messagebox.showwarning("Warning", "Please enter lawyer name to delete")
            return
        
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?"):
            query = "DELETE FROM NEWLAWYER WHERE NAME=%s"
            
            try:
                cursor = self.connection.cursor()
                cursor.execute(query, (name,))
                self.connection.commit()
                messagebox.showinfo("Success", "Lawyer profile deleted successfully")
                self.clear_fields()
                cursor.close()
            except pymysql.Error as err:
                messagebox.showerror("Error", f"Failed to delete entry: {err}")
    
    def clear_fields(self):
        """Clear all input fields"""
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.cv_entry.delete(0, tk.END)
        self.spec_var.set("")
        self.exp_entry.delete(0, tk.END)


class MainGUI:
    """Main application window"""
    def __init__(self, root):
        self.root = root
        self.root.title("Law Firm Management System")
        self.root.geometry("500x400")
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = ttk.Label(self.root, text="Justice League Law Firm", 
                         font=("Arial", 16, "bold"))
        title.pack(pady=20)
        
        # Subtitle
        subtitle = ttk.Label(self.root, text="Management System", 
                            font=("Arial", 12))
        subtitle.pack(pady=5)
        
        # Menu Frame
        menu_frame = ttk.LabelFrame(self.root, text="Select Option", padding=20)
        menu_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        buttons = [
            ("1. Find Lawyer by Speciality", self.open_lawyer_finder),
            ("2. Manage Lawyer Profiles", self.open_manage_lawyer),
            ("3. Settings", self.open_settings),
            ("4. Exit", self.exit_app)
        ]
        
        for text, command in buttons:
            ttk.Button(menu_frame, text=text, command=command, width=40).pack(pady=10)
    
    def open_lawyer_finder(self):
        """Open lawyer finder window"""
        finder_window = tk.Toplevel(self.root)
        LawyerFinderGUI(finder_window, self.root)
    
    def open_manage_lawyer(self):
        """Open manage lawyer window"""
        manage_window = tk.Toplevel(self.root)
        ManageLawyerGUI(manage_window)
    
    def open_settings(self):
        """Open settings window"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("400x300")
        
        info_frame = ttk.LabelFrame(settings_window, text="Database Configuration", padding=20)
        info_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        for key, value in DB_CONFIG.items():
            ttk.Label(info_frame, text=f"{key.capitalize()}:").pack(anchor="w", pady=5)
            ttk.Label(info_frame, text=str(value), foreground="blue").pack(anchor="w", pady=2, padx=20)
        
        ttk.Button(settings_window, text="Close", command=settings_window.destroy).pack(pady=10)
    
    def exit_app(self):
        """Exit application"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()
