# 🏛️ Law Firm Management System

A **Python-based Law Firm Management System** built using **Tkinter**, **MySQL**, **CSV files**, and **Matplotlib**.
This project manages **cases, lawyers, clients, interns, and requests** with role-based access control.

---

## 📌 Features Overview

The system supports **four roles**:

### 👨‍💼 Admin (Main Head)

* View all:

  * Cases
  * Lawyers
  * Clients
  * Interns
* Add / Remove:

  * Lawyers
  * Interns
  * Cases
* Edit *About Us* page
* View case statistics (Completed vs Ongoing)
* Logout

---

### ⚖️ Lawyer

* View:

  * Own cases
  * Own clients
  * Client requests
* Accept or reject client requests
* Update:

  * Case status
  * Case notes
* Assign work to interns *(placeholder)*
* Logout

---

### 👤 Client

* View:

  * Available lawyers
  * Own cases
* Create new case requests
* Logout

---

### 🎓 Intern

* Apply for internship
* View application status
* View assigned work *(placeholder)*
* Update work status *(placeholder)*
* Logout

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI
* **MySQL** – Case & Request storage
* **CSV Files** – Login, Lawyers, Interns, Payments
* **Matplotlib** – Case statistics graph
* **Tabulate** – Table formatting
* **PyMySQL** – MySQL connectivity

---

## 📂 Project Structure

```
Law-Firm-Management-System/
│
├── main.py                  # Main application file
├── login.csv                # User login credentials
├── lawyers.csv              # Lawyer details
├── interns.csv              # Intern details
├── payments.csv             # Payment records
├── About.txt                # About Us content
├── README.md                # Project documentation
│
└── requirements.txt         # (Optional)
```

---

## 🗄️ Database Schema (MySQL)

### 📁 cases

| Column             | Type                 |
| ------------------ | -------------------- |
| case_id            | INT (PK)             |
| lawyer_name        | VARCHAR              |
| type               | VARCHAR              |
| client_name        | VARCHAR              |
| date_of_completion | DATE                 |
| description        | TEXT                 |
| status             | completed / on going |
| payment_status     | completed / not      |
| notes              | TEXT                 |

### 📁 requests

| Column      | Type     |
| ----------- | -------- |
| id          | INT (PK) |
| lawyer_name | VARCHAR  |
| type        | VARCHAR  |
| client_name | VARCHAR  |
| details     | TEXT     |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/law-firm-management-system.git
cd law-firm-management-system
```

### 2️⃣ Install dependencies

```bash
pip install pymysql matplotlib tabulate
```

### 3️⃣ Setup MySQL

* Create a database named `trial`
* Create required tables using the schema above
* Update MySQL credentials in `main.py`:

```python
pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="YOUR_PASSWORD",
    database="trial"
)
```

### 4️⃣ Run the application

```bash
python main.py
```

---

## 🔐 Default Roles (login.csv)

| Role   | Access                  |
| ------ | ----------------------- |
| Admin  | Full access             |
| Lawyer | Case & request handling |
| User   | Client                  |
| Intern | Internship features     |

> **Note:** Passwords are stored in plain text (for academic/demo purposes only).

---

## 📊 Case Statistics

Admin can view:

* Number of **Completed cases**
* Number of **Ongoing cases**

Displayed using **Matplotlib bar chart**.

---

## 🚧 Known Limitations

* Passwords are not encrypted
* Intern work assignment is a placeholder
* Payment module not fully integrated
* No role-based data validation

---

## 🚀 Future Enhancements

* Password hashing (bcrypt)
* Full payment gateway integration
* Intern task assignment system
* Search & filter options
* Report generation
* Role-based permission enforcement

---

## 👨‍💻 Author

Developed as an **academic project** using Python and MySQL by Mariam Fatima, Shresti Subahar and Grehna Geo Marian.
Feel free to fork, improve, and contribute.

---

## 📜 License

This project is for **educational purposes**.
---
