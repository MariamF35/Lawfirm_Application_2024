import csv
import os
import pickle
import random
import tkinter as tk
import webbrowser
from datetime import datetime
from tkinter import messagebox, scrolledtext, ttk

import matplotlib.pyplot as plt
import pymysql

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "smh2sql",
    "database": "LAWFIRM",
}

USERNAMES_FILE = "usernames.csv"
LAWYER_PROFILE_FILE = "LawyerProfile.csv"
REQUEST_FILE = "request.dat"
CASEFILES_FILE = "casefiles.csv"
ABOUT_FILE = "about.txt"

CASE_TYPES = [
    "Immigration",
    "Criminal",
    "Real Estate",
    "Business",
    "Family",
    "Bankruptcy",
    "Tax",
    "Defense",
]


def ensure_files():
    if not os.path.exists(USERNAMES_FILE):
        with open(USERNAMES_FILE, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["username", "password", "role", "full_name"])
            w.writerow(["managing_partner", "partner123", "Managing Partner", "Managing Partner"])
            w.writerow(["lawyer_demo", "law123", "Lawyer", "Lawyer Demo"])
            w.writerow(["user_demo", "user123", "User", "User Demo"])

    if not os.path.exists(LAWYER_PROFILE_FILE):
        with open(LAWYER_PROFILE_FILE, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow([
                "lawyer_id",
                "name",
                "specialization",
                "hourly_rate",
                "cases_handled",
                "cv_link",
                "experience",
            ])
            w.writerow(["L101", "Ayesha Khan", "Immigration", "175", "112", "https://example.com/cv/ayesha", "8"])
            w.writerow(["L102", "Rohan Das", "Criminal", "220", "140", "https://example.com/cv/rohan", "11"])
            w.writerow(["L103", "Faria Noor", "Family", "160", "93", "https://example.com/cv/faria", "7"])

    if not os.path.exists(REQUEST_FILE):
        with open(REQUEST_FILE, "wb") as f:
            pickle.dump([], f)

    if not os.path.exists(CASEFILES_FILE):
        with open(CASEFILES_FILE, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow([
                "lawyer_id",
                "file_no",
                "client_name",
                "priority",
                "status",
                "case_type",
                "payment",
                "date",
                "description",
            ])

    if not os.path.exists(ABOUT_FILE):
        with open(ABOUT_FILE, "w", encoding="utf-8") as f:
            f.write(
                "Justice League Law Firm\n"
                "Services: Immigration, Criminal, Real Estate, Business, Family, Bankruptcy, Tax, Defense\n"
                "Vision: Accessible and trusted legal services for every client.\n"
                "Contact Email: contact@justiceleaguefirm.com\n"
            )


def mysql_connect():
    try:
        return pymysql.connect(**DB_CONFIG)
    except Exception as err:
        messagebox.showwarning("Database", f"MySQL connection failed: {err}")
        return None


class LawFirmGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Justice League Law Firm")
        self.root.geometry("920x700")
        self.current_user = None
        self.current_role = None
        self.current_full_name = ""
        ensure_files()
        self.show_main_menu()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def title_block(self, text):
        ttk.Label(self.root, text=text, font=("Arial", 18, "bold")).pack(pady=12)

    def show_main_menu(self):
        self.clear()
        self.title_block("Main Menu")
        box = ttk.Frame(self.root, padding=20)
        box.pack(fill="x")
        ttk.Button(box, text="Login", command=self.show_login, width=35).pack(pady=8)
        ttk.Button(box, text="Signup", command=self.show_signup_menu, width=35).pack(pady=8)
        ttk.Button(box, text="About Us", command=self.show_about, width=35).pack(pady=8)
        ttk.Button(box, text="Exit", command=self.exit_app, width=35).pack(pady=8)

    # ---------------- Login / Signup ----------------
    def show_login(self):
        self.clear()
        self.title_block("Login")

        frm = ttk.Frame(self.root, padding=15)
        frm.pack()
        ttk.Label(frm, text="Username").grid(row=0, column=0, sticky="w", pady=6)
        ttk.Label(frm, text="Password").grid(row=1, column=0, sticky="w", pady=6)

        username = ttk.Entry(frm, width=35)
        password = ttk.Entry(frm, show="*", width=35)
        username.grid(row=0, column=1, pady=6)
        password.grid(row=1, column=1, pady=6)

        def do_login():
            u, p = username.get().strip(), password.get().strip()
            with open(USERNAMES_FILE, newline="", encoding="utf-8") as f:
                r = csv.DictReader(f)
                for row in r:
                    if row["username"] == u and row["password"] == p:
                        self.current_user = row["username"]
                        self.current_role = row["role"]
                        self.current_full_name = row.get("full_name", row["username"])
                        messagebox.showinfo("Welcome", f"Welcome {self.current_full_name}!")
                        if self.current_role == "User":
                            self.user_dashboard()
                        elif self.current_role == "Lawyer":
                            self.lawyer_dashboard()
                        elif self.current_role == "Managing Partner":
                            self.partner_dashboard()
                        else:
                            messagebox.showwarning("Role", f"Unknown role: {self.current_role}")
                        return
            messagebox.showerror("Login Failed", "Invalid username/password")

        ttk.Button(self.root, text="Verify Login", command=do_login).pack(pady=10)
        ttk.Button(self.root, text="Back", command=self.show_main_menu).pack()

    def show_signup_menu(self):
        self.clear()
        self.title_block("Signup")
        box = ttk.Frame(self.root, padding=20)
        box.pack(fill="x")
        ttk.Button(box, text="New User", command=self.signup_user, width=35).pack(pady=10)
        ttk.Button(box, text="New Lawyer", command=self.signup_lawyer_menu, width=35).pack(pady=10)
        ttk.Button(box, text="Back", command=self.show_main_menu, width=35).pack(pady=10)

    def signup_user(self):
        self.clear()
        self.title_block("Signup → New User")
        frm = ttk.Frame(self.root, padding=15)
        frm.pack()

        labels = ["Full Name", "Password", "Confirm Password"]
        entries = []
        for i, lbl in enumerate(labels):
            ttk.Label(frm, text=lbl).grid(row=i, column=0, sticky="w", pady=6)
            e = ttk.Entry(frm, width=36, show="*" if "Password" in lbl else "")
            e.grid(row=i, column=1, pady=6)
            entries.append(e)

        def generate_username(full_name):
            base = "".join(full_name.lower().split())[:8] or "user"
            with open(USERNAMES_FILE, newline="", encoding="utf-8") as f:
                taken = {row["username"] for row in csv.DictReader(f)}
            while True:
                candidate = f"{base}{random.randint(100,999)}"
                if candidate not in taken:
                    return candidate

        def save_user():
            full_name, pwd, conf = [e.get().strip() for e in entries]
            if not full_name or not pwd:
                messagebox.showwarning("Validation", "Name and password are required")
                return
            if pwd != conf:
                messagebox.showerror("Validation", "Passwords do not match")
                return
            uname = generate_username(full_name)
            with open(USERNAMES_FILE, "a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow([uname, pwd, "User", full_name])
            messagebox.showinfo("Signup Complete", f"Welcome {full_name}!\nYour username: {uname}")
            self.show_main_menu()

        ttk.Button(self.root, text="Create Account", command=save_user).pack(pady=10)
        ttk.Button(self.root, text="Back", command=self.show_signup_menu).pack()

    def signup_lawyer_menu(self):
        self.clear()
        self.title_block("Signup → New Lawyer")
        box = ttk.Frame(self.root, padding=20)
        box.pack(fill="x")
        ttk.Button(box, text="New Entry", command=self.lawyer_new_entry, width=35).pack(pady=8)
        ttk.Button(box, text="Update Entry", command=self.lawyer_update_entry, width=35).pack(pady=8)
        ttk.Button(box, text="Delete Entry", command=self.lawyer_delete_entry, width=35).pack(pady=8)
        ttk.Button(box, text="Back", command=self.show_signup_menu, width=35).pack(pady=8)

    def lawyer_new_entry(self):
        self.lawyer_db_form("New Entry", "insert")

    def lawyer_update_entry(self):
        self.lawyer_db_form("Update Entry", "update")

    def lawyer_delete_entry(self):
        self.lawyer_db_form("Delete Entry", "delete")

    def lawyer_db_form(self, heading, mode):
        self.clear()
        self.title_block(f"New Lawyer → {heading}")
        frm = ttk.Frame(self.root, padding=15)
        frm.pack()

        fields = ["Name", "Age", "CV Link", "Speciality", "Experience"]
        ents = {}
        for i, field in enumerate(fields):
            ttk.Label(frm, text=field).grid(row=i, column=0, sticky="w", pady=5)
            ent = ttk.Entry(frm, width=40)
            ent.grid(row=i, column=1, pady=5)
            ents[field] = ent

        def submit():
            conn = mysql_connect()
            if not conn:
                return
            c = conn.cursor()
            name = ents["Name"].get().strip()
            try:
                if mode == "insert":
                    c.execute(
                        "INSERT INTO NEWLAWYER (NAME, AGE, CV_LINK, SPECIALITY, YEARS_OF_EXPERIENCE) VALUES (%s,%s,%s,%s,%s)",
                        (
                            name,
                            int(ents["Age"].get().strip()),
                            ents["CV Link"].get().strip(),
                            ents["Speciality"].get().strip(),
                            int(ents["Experience"].get().strip()),
                        ),
                    )
                    messagebox.showinfo("Done", "Lawyer inserted")
                elif mode == "update":
                    c.execute(
                        "UPDATE NEWLAWYER SET AGE=%s, CV_LINK=%s, SPECIALITY=%s, YEARS_OF_EXPERIENCE=%s WHERE NAME=%s",
                        (
                            int(ents["Age"].get().strip()),
                            ents["CV Link"].get().strip(),
                            ents["Speciality"].get().strip(),
                            int(ents["Experience"].get().strip()),
                            name,
                        ),
                    )
                    messagebox.showinfo("Done", "Lawyer updated")
                else:
                    if not messagebox.askyesno("Confirm", f"Delete lawyer {name}?"):
                        return
                    c.execute("DELETE FROM NEWLAWYER WHERE NAME=%s", (name,))
                    messagebox.showinfo("Done", "Lawyer deleted")
                conn.commit()
            except Exception as err:
                messagebox.showerror("Database Error", str(err))
            finally:
                c.close()
                conn.close()

        ttk.Button(self.root, text="Submit", command=submit).pack(pady=8)
        ttk.Button(self.root, text="Back", command=self.signup_lawyer_menu).pack(pady=4)

    # ---------------- User Dashboard ----------------
    def user_dashboard(self):
        self.clear()
        self.title_block("User Dashboard")
        box = ttk.Frame(self.root, padding=20)
        box.pack(fill="x")
        ttk.Button(box, text="Request Lawyer", command=self.user_request_lawyer, width=36).pack(pady=8)
        ttk.Button(box, text="View Case Status", command=self.user_view_case_status, width=36).pack(pady=8)
        ttk.Button(box, text="Payment", command=self.user_payment, width=36).pack(pady=8)
        ttk.Button(box, text="Logout", command=self.show_main_menu, width=36).pack(pady=8)

    def _load_lawyer_profiles(self):
        with open(LAWYER_PROFILE_FILE, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def user_request_lawyer(self):
        self.clear()
        self.title_block("User → Request Lawyer")

        top = ttk.Frame(self.root, padding=10)
        top.pack(fill="x")
        ttk.Label(top, text="Case Type").pack(side="left", padx=6)
        selected_case = tk.StringVar(value=CASE_TYPES[0])
        ttk.Combobox(top, values=CASE_TYPES, textvariable=selected_case, state="readonly", width=20).pack(side="left")

        cols = ("ID", "Name", "Specialization", "Hourly Rate", "Cases Handled")
        tree = ttk.Treeview(self.root, columns=cols, show="headings", height=10)
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=160 if c in ("Name", "Specialization") else 120)
        tree.pack(fill="both", expand=True, padx=14, pady=8)

        detail = tk.StringVar(value="Select a lawyer and click Explore Details")
        ttk.Label(self.root, textvariable=detail, foreground="blue").pack(pady=4)

        form = ttk.Frame(self.root, padding=10)
        form.pack(fill="x")
        lawyer_id_entry = ttk.Entry(form, width=15)
        hours_entry = ttk.Entry(form, width=10)
        ttk.Label(form, text="Lawyer ID").grid(row=0, column=0, padx=5, pady=4)
        lawyer_id_entry.grid(row=0, column=1, padx=5, pady=4)
        ttk.Label(form, text="Estimated Hours").grid(row=0, column=2, padx=5, pady=4)
        hours_entry.grid(row=0, column=3, padx=5, pady=4)
        estimate_lbl = tk.StringVar(value="Estimated Amount: --")
        ttk.Label(form, textvariable=estimate_lbl).grid(row=0, column=4, padx=8)

        req = ttk.Frame(self.root, padding=10)
        req.pack(fill="x")
        client_name = ttk.Entry(req, width=25)
        req_date = ttk.Entry(req, width=14)
        req_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        description = ttk.Entry(req, width=35)
        urgency = ttk.Combobox(req, values=["Low", "Medium", "High"], state="readonly", width=10)
        urgency.set("Medium")
        ttk.Label(req, text="Client Name").grid(row=0, column=0, padx=4)
        client_name.grid(row=0, column=1, padx=4)
        ttk.Label(req, text="Date").grid(row=0, column=2, padx=4)
        req_date.grid(row=0, column=3, padx=4)
        ttk.Label(req, text="Description").grid(row=1, column=0, padx=4, pady=6)
        description.grid(row=1, column=1, columnspan=3, sticky="we", padx=4)
        ttk.Label(req, text="Urgency").grid(row=1, column=4, padx=4)
        urgency.grid(row=1, column=5, padx=4)

        profiles = self._load_lawyer_profiles()

        def refresh_lawyers():
            for i in tree.get_children():
                tree.delete(i)
            case_type = selected_case.get().lower()
            matches = [p for p in profiles if case_type in p["specialization"].lower()]
            for p in matches:
                tree.insert("", "end", values=(p["lawyer_id"], p["name"], p["specialization"], p["hourly_rate"], p["cases_handled"]))
            if not matches:
                messagebox.showinfo("Info", "No matching lawyers found")

        def selected_profile(lawyer_id):
            for p in profiles:
                if p["lawyer_id"] == lawyer_id:
                    return p
            return None

        def explore_details():
            p = selected_profile(lawyer_id_entry.get().strip())
            if not p:
                messagebox.showwarning("Validation", "Invalid Lawyer ID")
                return
            detail.set(
                f"{p['name']} | Experience: {p.get('experience','N/A')} yrs | CV: {p.get('cv_link','N/A')}"
            )

        def calc_amount():
            p = selected_profile(lawyer_id_entry.get().strip())
            if not p:
                messagebox.showwarning("Validation", "Enter valid Lawyer ID")
                return
            try:
                hrs = float(hours_entry.get().strip())
                amt = hrs * float(p["hourly_rate"])
                estimate_lbl.set(f"Estimated Amount: {amt:.2f}")
            except ValueError:
                messagebox.showwarning("Validation", "Hours must be numeric")

        def store_request():
            p = selected_profile(lawyer_id_entry.get().strip())
            if not p:
                messagebox.showwarning("Validation", "Enter valid Lawyer ID")
                return
            try:
                hrs = float(hours_entry.get().strip())
            except ValueError:
                messagebox.showwarning("Validation", "Hours must be numeric")
                return
            if not messagebox.askyesno("Confirm", "Confirm lawyer request?"):
                return
            with open(REQUEST_FILE, "rb") as f:
                data = pickle.load(f)
            data.append(
                {
                    "status": "PENDING",
                    "username": self.current_user,
                    "lawyer_id": p["lawyer_id"],
                    "case_type": selected_case.get(),
                    "client_name": client_name.get().strip() or self.current_full_name,
                    "date": req_date.get().strip(),
                    "description": description.get().strip(),
                    "urgency": urgency.get(),
                    "estimated_hours": hrs,
                    "estimated_amount": round(hrs * float(p["hourly_rate"]), 2),
                }
            )
            with open(REQUEST_FILE, "wb") as f:
                pickle.dump(data, f)
            messagebox.showinfo("Saved", "Request stored in request.dat as PENDING")

        btns = ttk.Frame(self.root)
        btns.pack(pady=8)
        ttk.Button(btns, text="Show Matching Lawyers", command=refresh_lawyers).pack(side="left", padx=5)
        ttk.Button(btns, text="Explore Details", command=explore_details).pack(side="left", padx=5)
        ttk.Button(btns, text="Calculate Amount", command=calc_amount).pack(side="left", padx=5)
        ttk.Button(btns, text="Confirm Request", command=store_request).pack(side="left", padx=5)
        ttk.Button(btns, text="Back", command=self.user_dashboard).pack(side="left", padx=5)

        refresh_lawyers()

    def user_view_case_status(self):
        self.clear()
        self.title_block("User → View Case Status")
        out = scrolledtext.ScrolledText(self.root, width=110, height=30)
        out.pack(padx=12, pady=8)

        out.insert(tk.END, "PENDING REQUESTS (request.dat)\n")
        out.insert(tk.END, "=" * 70 + "\n")
        with open(REQUEST_FILE, "rb") as f:
            reqs = pickle.load(f)
        shown = 0
        for r in reqs:
            if r.get("username") == self.current_user and r.get("status") == "PENDING":
                out.insert(
                    tk.END,
                    f"Client: {r['client_name']} | Case: {r['case_type']} | Lawyer: {r['lawyer_id']} | Urgency: {r['urgency']}\n",
                )
                shown += 1
        if shown == 0:
            out.insert(tk.END, "No pending requests found.\n")

        out.insert(tk.END, "\nAPPROVED CASES (casefiles.csv)\n")
        out.insert(tk.END, "=" * 70 + "\n")
        with open(CASEFILES_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                if row["client_name"].lower() == self.current_full_name.lower() or row["client_name"].lower() == self.current_user.lower():
                    out.insert(
                        tk.END,
                        f"File: {row['file_no']} | Lawyer: {row['lawyer_id']} | Status: {row['status']} | Payment: {row['payment']}\n",
                    )
                    count += 1
            if count == 0:
                out.insert(tk.END, "No approved cases found.\n")

        ttk.Button(self.root, text="Back", command=self.user_dashboard).pack(pady=6)

    def user_payment(self):
        self.clear()
        self.title_block("User → Payment")

        approved = []
        with open(CASEFILES_FILE, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
            for i, row in enumerate(rows):
                if (
                    row["status"].upper() == "APPROVED"
                    and row["client_name"].lower() in {self.current_user.lower(), self.current_full_name.lower()}
                ):
                    approved.append((i, row))

        frm = ttk.Frame(self.root, padding=10)
        frm.pack(fill="x")
        case_var = tk.StringVar()
        payment_var = tk.StringVar(value="Full Payment")
        hours_entry = ttk.Entry(frm, width=10)
        ttk.Label(frm, text="Approved Case (file no)").grid(row=0, column=0, padx=5, pady=5)
        combo_vals = [r[1]["file_no"] for r in approved]
        box = ttk.Combobox(frm, values=combo_vals, textvariable=case_var, state="readonly", width=20)
        box.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(frm, text="Hours").grid(row=0, column=2, padx=5)
        hours_entry.grid(row=0, column=3, padx=5)
        ttk.Radiobutton(frm, text="Full Payment", variable=payment_var, value="Full Payment").grid(row=1, column=0, columnspan=2, sticky="w")
        ttk.Radiobutton(frm, text="4 Installments", variable=payment_var, value="4 Installments").grid(row=1, column=2, columnspan=2, sticky="w")
        amt_lbl = tk.StringVar(value="Total: --")
        ttk.Label(frm, textvariable=amt_lbl, foreground="blue").grid(row=2, column=0, columnspan=4, pady=8)

        def pay():
            if not approved:
                messagebox.showinfo("Payment", "No approved case available")
                return
            file_no = case_var.get().strip()
            if not file_no:
                messagebox.showwarning("Validation", "Select an approved case")
                return
            try:
                hrs = float(hours_entry.get().strip())
            except ValueError:
                messagebox.showwarning("Validation", "Hours must be numeric")
                return
            row_idx = None
            selected = None
            for i, row in approved:
                if row["file_no"] == file_no:
                    row_idx, selected = i, row
                    break
            if selected is None:
                return
            rate = 0.0
            for p in self._load_lawyer_profiles():
                if p["lawyer_id"] == selected["lawyer_id"]:
                    rate = float(p["hourly_rate"])
                    break
            total = round(hrs * rate, 2)
            amt_lbl.set(f"Total: {total:.2f}")

            rows[row_idx]["payment"] = payment_var.get()
            rows[row_idx]["status"] = "CLOSED"
            with open(CASEFILES_FILE, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=rows[0].keys())
                w.writeheader()
                w.writerows(rows)
            messagebox.showinfo("Payment", f"Payment recorded ({payment_var.get()}). Case closed.")

        ttk.Button(self.root, text="Process Payment", command=pay).pack(pady=8)
        ttk.Button(self.root, text="Back", command=self.user_dashboard).pack()

    # ---------------- Lawyer Dashboard ----------------
    def lawyer_dashboard(self):
        self.clear()
        self.title_block("Lawyer Dashboard")
        box = ttk.Frame(self.root, padding=20)
        box.pack(fill="x")
        ttk.Button(box, text="View Requests", command=self.lawyer_view_requests, width=36).pack(pady=8)
        ttk.Button(box, text="Approve Case", command=self.lawyer_approve_case, width=36).pack(pady=8)
        ttk.Button(box, text="View Clients", command=self.lawyer_view_clients, width=36).pack(pady=8)
        ttk.Button(box, text="Logout", command=self.show_main_menu, width=36).pack(pady=8)

    def lawyer_view_requests(self):
        self.clear()
        self.title_block("Lawyer → View Requests")
        frm = ttk.Frame(self.root, padding=10)
        frm.pack()
        lid = ttk.Entry(frm, width=18)
        ttk.Label(frm, text="Lawyer ID").grid(row=0, column=0, padx=5)
        lid.grid(row=0, column=1, padx=5)
        out = scrolledtext.ScrolledText(self.root, width=110, height=25)
        out.pack(padx=10, pady=8)

        def load_req():
            out.delete("1.0", tk.END)
            with open(REQUEST_FILE, "rb") as f:
                data = pickle.load(f)
            for r in data:
                if r.get("lawyer_id") == lid.get().strip() and r.get("status") == "PENDING":
                    out.insert(
                        tk.END,
                        f"Client: {r['client_name']} | Date: {r['date']} | Urgency: {r['urgency']}\nDescription: {r['description']}\n\n",
                    )

        ttk.Button(self.root, text="Show Matching Requests", command=load_req).pack(pady=6)
        ttk.Button(self.root, text="Back", command=self.lawyer_dashboard).pack()

    def lawyer_approve_case(self):
        self.clear()
        self.title_block("Lawyer → Approve Case")
        frm = ttk.Frame(self.root, padding=10)
        frm.pack()
        lid = ttk.Entry(frm, width=18)
        client = ttk.Entry(frm, width=25)
        ttk.Label(frm, text="Lawyer ID").grid(row=0, column=0, padx=5, pady=4)
        lid.grid(row=0, column=1, padx=5)
        ttk.Label(frm, text="Client Name").grid(row=1, column=0, padx=5, pady=4)
        client.grid(row=1, column=1, padx=5)

        def approve():
            lawyer_id = lid.get().strip()
            client_name = client.get().strip()
            with open(REQUEST_FILE, "rb") as f:
                reqs = pickle.load(f)
            idx = None
            selected = None
            for i, r in enumerate(reqs):
                if r.get("client_name").lower() == client_name.lower() and r.get("lawyer_id") == lawyer_id:
                    idx = i
                    selected = r
                    break
            if selected is None:
                messagebox.showwarning("Approve", "Matching request not found")
                return

            file_no = f"F{random.randint(10000, 99999)}"
            with open(CASEFILES_FILE, "a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(
                    [
                        lawyer_id,
                        file_no,
                        selected["client_name"],
                        selected.get("urgency", "Medium"),
                        "APPROVED",
                        selected.get("case_type", "General"),
                        "PENDING",
                        datetime.now().strftime("%Y-%m-%d"),
                        selected.get("description", ""),
                    ]
                )

            reqs.pop(idx)
            with open(REQUEST_FILE, "wb") as f:
                pickle.dump(reqs, f)
            messagebox.showinfo("Case Approved 👍", f"Case approved. File Number: {file_no}")

        ttk.Button(self.root, text="Approve Case", command=approve).pack(pady=8)
        ttk.Button(self.root, text="Back", command=self.lawyer_dashboard).pack()

    def lawyer_view_clients(self):
        self.clear()
        self.title_block("Lawyer → View Clients")
        frm = ttk.Frame(self.root, padding=10)
        frm.pack()
        letter = ttk.Entry(frm, width=6)
        ttk.Label(frm, text="First Letter of Law (F/R/C/B/I/T)").grid(row=0, column=0, padx=5)
        letter.grid(row=0, column=1, padx=5)
        out = scrolledtext.ScrolledText(self.root, width=110, height=26)
        out.pack(padx=10, pady=8)

        def show_clients():
            out.delete("1.0", tk.END)
            ch = letter.get().strip().upper()[:1]
            with open(CASEFILES_FILE, newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if row["case_type"].upper().startswith(ch):
                        out.insert(tk.END, f"{row['client_name']} | {row['case_type']} | File: {row['file_no']}\n")

        ttk.Button(self.root, text="Show Clients", command=show_clients).pack(pady=6)
        ttk.Button(self.root, text="Back", command=self.lawyer_dashboard).pack()

    # ---------------- Managing Partner ----------------
    def partner_dashboard(self):
        self.clear()
        self.title_block("Managing Partner Dashboard")
        box = ttk.Frame(self.root, padding=20)
        box.pack(fill="x")
        ttk.Button(box, text="View Clients", command=self.partner_view_clients, width=36).pack(pady=8)
        ttk.Button(box, text="View Lawyer Profiles", command=self.partner_view_lawyers, width=36).pack(pady=8)
        ttk.Button(box, text="Track Revenue", command=self.partner_track_revenue, width=36).pack(pady=8)
        ttk.Button(box, text="Add/Delete Case", command=self.partner_add_delete_case, width=36).pack(pady=8)
        ttk.Button(box, text="Logout", command=self.show_main_menu, width=36).pack(pady=8)

    def partner_view_clients(self):
        self.clear()
        self.title_block("Managing Partner → View Clients")
        out = scrolledtext.ScrolledText(self.root, width=120, height=30)
        out.pack(padx=12, pady=8)
        with open(CASEFILES_FILE, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        if not rows:
            out.insert(tk.END, "No case records found.\n")
        else:
            out.insert(tk.END, "Lawyer ID | File No | Client | Status | Payment | Description\n")
            out.insert(tk.END, "=" * 90 + "\n")
            for r in rows:
                out.insert(
                    tk.END,
                    f"{r['lawyer_id']} | {r['file_no']} | {r['client_name']} | {r['status']} | {r['payment']} | {r['description']}\n",
                )
        ttk.Button(self.root, text="Back", command=self.partner_dashboard).pack(pady=6)

    def partner_view_lawyers(self):
        self.clear()
        self.title_block("Managing Partner → View Lawyer Profiles (MySQL)")
        frm = ttk.Frame(self.root, padding=10)
        frm.pack(fill="x")
        spec = tk.StringVar(value="Immigration Law")
        specs = [
            "Immigration Law",
            "Criminal Law",
            "Real Estate Law",
            "Business Law",
            "Family Law",
            "Bankruptcy Law",
            "Tax Law",
            "Defense Law",
        ]
        ttk.Label(frm, text="Select Speciality").pack(side="left", padx=6)
        ttk.Combobox(frm, values=specs, textvariable=spec, state="readonly", width=24).pack(side="left", padx=6)

        cols = ("Name", "Age", "CV Link", "Speciality", "Experience")
        tree = ttk.Treeview(self.root, columns=cols, show="headings", height=16)
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=180 if c in ("Name", "CV Link") else 110)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        def load_data():
            conn = mysql_connect()
            if not conn:
                return
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT NAME, AGE, CV_LINK, SPECIALITY, YEARS_OF_EXPERIENCE FROM NEWLAWYER WHERE SPECIALITY=%s",
                    (spec.get(),),
                )
                rows = cur.fetchall()
                for i in tree.get_children():
                    tree.delete(i)
                for r in rows:
                    tree.insert("", "end", values=r)
                cur.close()
            except Exception as err:
                messagebox.showerror("MySQL Error", str(err))
            finally:
                conn.close()

        def open_cv():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("CV", "Select one lawyer first")
                return
            link = tree.item(sel[0])["values"][2]
            if link:
                webbrowser.open(link)

        b = ttk.Frame(self.root)
        b.pack(pady=5)
        ttk.Button(b, text="Show Profiles", command=load_data).pack(side="left", padx=5)
        ttk.Button(b, text="Open CV", command=open_cv).pack(side="left", padx=5)
        ttk.Button(b, text="Back", command=self.partner_dashboard).pack(side="left", padx=5)

    def partner_track_revenue(self):
        self.clear()
        self.title_block("Managing Partner → Track Revenue")
        frm = ttk.Frame(self.root, padding=10)
        frm.pack()
        month = ttk.Entry(frm, width=15)
        values = ttk.Entry(frm, width=50)
        ttk.Label(frm, text="End Month (e.g. Jun)").grid(row=0, column=0, padx=5, pady=6)
        month.grid(row=0, column=1, padx=5)
        ttk.Label(frm, text="Revenue Values (comma separated)").grid(row=1, column=0, padx=5, pady=6)
        values.grid(row=1, column=1, padx=5)

        def plot_graph():
            raw = [x.strip() for x in values.get().split(",") if x.strip()]
            try:
                y = [float(x) for x in raw]
            except ValueError:
                messagebox.showwarning("Validation", "Revenue values must be numeric")
                return
            x = [f"M{i+1}" for i in range(len(y))]
            plt.figure(figsize=(8, 4))
            plt.plot(x, y, marker="o")
            plt.title(f"Monthly Revenue Trend up to {month.get().strip()}")
            plt.xlabel("Month")
            plt.ylabel("Revenue")
            plt.tight_layout()
            plt.show()

        ttk.Button(self.root, text="Generate Graph", command=plot_graph).pack(pady=8)
        ttk.Button(self.root, text="Back", command=self.partner_dashboard).pack()

    def partner_add_delete_case(self):
        self.clear()
        self.title_block("Managing Partner → Add/Delete Case")

        frm = ttk.Frame(self.root, padding=10)
        frm.pack()
        fields = [
            "Lawyer ID",
            "File No",
            "Client Name",
            "Priority",
            "Status",
            "Case Type",
            "Payment Status",
            "Date",
            "Description",
        ]
        entries = {}
        for i, fld in enumerate(fields):
            ttk.Label(frm, text=fld).grid(row=i, column=0, sticky="w", padx=5, pady=3)
            e = ttk.Entry(frm, width=35)
            e.grid(row=i, column=1, padx=5, pady=3)
            entries[fld] = e

        del_row = ttk.Entry(frm, width=10)
        ttk.Label(frm, text="Delete row #").grid(row=len(fields), column=0, sticky="w", padx=5, pady=8)
        del_row.grid(row=len(fields), column=1, sticky="w", padx=5)

        def add_case():
            vals = [entries[f].get().strip() for f in fields]
            if not all(vals):
                messagebox.showwarning("Validation", "Fill all fields to add case")
                return
            with open(CASEFILES_FILE, "a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(
                    [
                        vals[0],
                        vals[1],
                        vals[2],
                        vals[3],
                        vals[4],
                        vals[5],
                        vals[6],
                        vals[7],
                        vals[8],
                    ]
                )
            messagebox.showinfo("Add Case", "Case added")

        def delete_case():
            try:
                idx = int(del_row.get().strip())
            except ValueError:
                messagebox.showwarning("Validation", "Enter a valid row number")
                return
            with open(CASEFILES_FILE, newline="", encoding="utf-8") as f:
                rows = list(csv.reader(f))
            if idx <= 0 or idx >= len(rows):
                messagebox.showwarning("Delete", "Row out of range")
                return
            rows.pop(idx)
            with open(CASEFILES_FILE, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows(rows)
            messagebox.showinfo("Delete", "Case removed")

        b = ttk.Frame(self.root)
        b.pack(pady=8)
        ttk.Button(b, text="Add Case", command=add_case).pack(side="left", padx=6)
        ttk.Button(b, text="Delete Case", command=delete_case).pack(side="left", padx=6)
        ttk.Button(b, text="Back", command=self.partner_dashboard).pack(side="left", padx=6)

    # ---------------- About / Exit ----------------
    def show_about(self):
        self.clear()
        self.title_block("About Us")
        text = scrolledtext.ScrolledText(self.root, width=100, height=30)
        text.pack(padx=12, pady=8)
        with open(ABOUT_FILE, encoding="utf-8") as f:
            text.insert(tk.END, f.read())
        text.config(state="disabled")
        ttk.Button(self.root, text="Back", command=self.show_main_menu).pack(pady=6)

    def exit_app(self):
        messagebox.showinfo("Exit", "Thank You for Visiting Justice League Law Firm")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LawFirmGUI(root)
    root.mainloop()
