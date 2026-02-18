# 🚀 Quick Reference Card

## Installation (Copy-Paste)

```powershell
# Navigate to project folder
cd c:\Users\B-101\Desktop\164

# Install all dependencies at once
pip install -r requirements.txt

# Verify installation
python -c "import pymysql; print('✓ Ready')"
```

---

## Run Application

```powershell
# Start Basic GUI Version (Recommended for beginners)
python lawfirm_2024_gui.py

# OR Start Full-Featured Version (Complete system)
python lawfirm_2024_enhanced.py
```

---

## Database Configuration

**File:** Any Python application (line 8-13)

```python
DB_CONFIG = {
    'host': 'localhost',      # Your MySQL host
    'user': 'root',           # Your MySQL username  
    'password': 'smh2sql',    # Your MySQL password ← UPDATE THIS
    'database': 'LAWFIRM'     # Your database name
}
```

---

## Basic GUI Version Features

| Feature | How to Use |
|---------|-----------|
| **Find Lawyers** | Click menu → Select speciality → Click search button |
| **Add Lawyer** | Click "Manage Lawyer Profiles" → Fill form → Click "New Entry" |
| **Update Lawyer** | Fill name field → Fill new info → Click "Update Entry" |
| **Delete Lawyer** | Fill name field → Click "Delete Entry" |
| **View CV** | Select lawyer from results → Click "View CV" |

---

## Enhanced Version Features

| Feature | Step |
|---------|------|
| **Register** | Click Register → Enter details → Create account |
| **Login** | Enter username/password → Select role → Click Login |
| **Request Lawyer** | Dashboard → "Request Lawyer" → Fill form → Submit |
| **View Cases** | Dashboard → "View Cases" → See your case status |
| **Admin Panel** | Login as Admin → Access all management functions |

---

## Troubleshooting Quick Fixes

### Issue: pymysql not found
```powershell
pip install --upgrade pymysql
```

### Issue: Can't connect to MySQL
```powershell
# Check if MySQL is running
mysql -u root -p

# Verify credentials in DB_CONFIG match
```

### Issue: Tkinter not found (Linux)
```bash
sudo apt-get install python3-tk
```

### Issue: Application won't start
```powershell
# Check Python version (need 3.7+)
python --version

# Check all imports work
python -c "import pymysql, tkinter; print('OK')"
```

---

## Key Classes & Methods

### DatabaseConnection
```python
connection = DatabaseConnection.connect()
cursor = connection.cursor()
cursor.execute(query)
connection.commit()
```

### Main Windows
```python
LawyerFinderGUI          # Find lawyers by speciality
ManageLawyerGUI          # CRUD operations for lawyers
LoginGUI                 # User login system
UserDashboard            # Client interface
LawyerDashboard          # Lawyer interface
AdminDashboard           # Admin interface
```

---

## File Structure

```
folder/
├── lawfirm_2024_gui.py         ← Use this (Basic)
├── lawfirm_2024_enhanced.py    ← Use this (Advanced)
├── requirements.txt             ← Run: pip install -r requirements.txt
├── QUICKSTART.md                ← Read this first (5 min)
├── README.md                    ← Features guide
├── ARCHITECTURE.md              ← Visual diagrams
└── Other docs
```

---

## Command Reference

### PowerShell/Command Prompt

```powershell
# Navigate to folder
cd c:\Users\B-101\Desktop\164

# Install dependencies
pip install -r requirements.txt

# Run application
python lawfirm_2024_gui.py

# Check Python version
python --version

# Test imports
python -c "import pymysql; print('OK')"

# List installed packages
pip list

# Upgrade pip
pip install --upgrade pip
```

---

## Documentation Map

```
START HERE
    │
    ├─► QUICKSTART.md (5 min) ← Fast setup
    │
    ├─► README.md (10 min) ← Feature details
    │
    ├─► ARCHITECTURE.md (10 min) ← Visual diagrams
    │
    └─► MIGRATION_GUIDE.md (15 min) ← Detailed comparison
```

---

## Database Query Examples

### Find Lawyers
```python
cursor.execute("SELECT * FROM NEWLAWYER WHERE SPECIALITY = %s", ("Immigration Law",))
results = cursor.fetchall()
```

### Add New Lawyer
```python
cursor.execute(
    "INSERT INTO NEWLAWYER (NAME, AGE, CV_LINK, SPECIALITY, YEARS_OF_EXPERIENCE) VALUES (%s, %s, %s, %s, %s)",
    ("John Doe", 35, "http://cv.com", "Immigration Law", 10)
)
connection.commit()
```

### Update Lawyer
```python
cursor.execute(
    "UPDATE NEWLAWYER SET AGE=%s WHERE NAME=%s",
    (36, "John Doe")
)
connection.commit()
```

### Delete Lawyer
```python
cursor.execute("DELETE FROM NEWLAWYER WHERE NAME=%s", ("John Doe",))
connection.commit()
```

---

## Key Technologies

| Tech | Version | Purpose |
|------|---------|---------|
| Python | 3.7+ | Language |
| PyMySQL | 1.1.0 | Database |
| Tkinter | Built-in | GUI |
| Tabulate | 0.9.0 | Tables |
| Matplotlib | 3.8.0 | Charts |

---

## Performance Tips

✅ Keep MySQL running in background  
✅ Use Basic version for simple operations  
✅ Close windows properly to free resources  
✅ Ensure stable database connection  
✅ Test with small dataset first  

---

## Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: pymysql` | Package not installed | `pip install pymysql` |
| `(2003) Can't connect` | MySQL not running | Start MySQL service |
| `ModuleNotFoundError: tkinter` | TK not installed | Linux: `apt-get install python3-tk` |
| `EOF Error` | File corruption | Delete `.dat` files and restart |
| `SQL syntax error` | Query error | Check SQL in code |

---

## Security Checklist

- [x] No eval() in new version (Safe ✅)
- [x] Parameterized SQL queries (Prevents injection ✅)
- [ ] TODO: Add password hashing
- [ ] TODO: Use environment variables for credentials

---

## Next Actions

### Now (< 5 minutes)
1. Read QUICKSTART.md
2. Install dependencies
3. Run application

### Today
1. Explore both versions
2. Test all features
3. Add test data

### This Week
1. Customize colors/fonts
2. Add more features
3. Deploy to environment

---

## Support Docs (Included)

1. **QUICKSTART.md** - Getting started
2. **README.md** - Features & troubleshooting
3. **MIGRATION_GUIDE.md** - Old vs new comparison
4. **ARCHITECTURE.md** - Technical details
5. **IMPLEMENTATION_CHECKLIST.md** - Verification checklist
6. **SUMMARY.md** - Project overview
7. **This file** - Quick reference

---

## Code Locations (Important Lines)

| What | File | Line |
|------|------|------|
| Database config | Both apps | 8-13 |
| Main GUI class | lawfirm_2024_gui.py | 120 |
| Login class | lawfirm_2024_enhanced.py | 250 |
| User dashboard | lawfirm_2024_enhanced.py | 310 |
| Run application | Both apps | Last line |

---

## Frequently Used Commands

```powershell
# Start here
python lawfirm_2024_gui.py

# Make a database backup
mysqldump -u root -p LAWFIRM > backup.sql

# List all users
SELECT * FROM usernames (in MySQL)

# View all lawyers
SELECT * FROM NEWLAWYER (in MySQL)

# Clear test data
DELETE FROM NEWLAWYER WHERE NAME LIKE '%test%'
```

---

## Success Indicators ✅

- Application window opens
- No Python errors
- Database connection works
- Can search for lawyers
- Can add new lawyers
- Can see results in table
- CV links open in browser

---

## Version Info

**Project:** Law Firm Management System  
**Version:** 2024.1 Beta  
**Status:** Ready for use  
**Python:** 3.7+  
**Database:** MySQL/MariaDB  

---

## Emergency Quick Start

If running out of time:

```powershell
# 1. Open PowerShell in the 164 folder
# 2. Run these commands:

pip install pymysql tabulate matplotlib
python lawfirm_2024_gui.py

# Done! App should start
```

---

**Bookmark this file - comes in handy!**

For detailed information, see the other documentation files.

**Version:** Quick Reference v1  
**Last Updated:** Feb 18, 2026
