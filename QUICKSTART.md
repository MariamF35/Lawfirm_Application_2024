# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Python 3.7 or higher installed
- MySQL/MariaDB running with LAWFIRM database
- Administrator access

---

## Step 1: Install Dependencies (1 minute)

Open PowerShell/Command Prompt in the 164 folder:

```powershell
pip install -r requirements.txt
```

Or manually install:
```powershell
pip install pymysql
pip install tabulate
pip install matplotlib
```

---

## Step 2: Verify Installation (1 minute)

```powershell
python -c "import pymysql; import tkinter; print('✓ All packages installed')"
```

---

## Step 3: Update Database Configuration (1 minute)

Edit the `DB_CONFIG` in either Python file you want to use:

**Line 8-13** in `lawfirm_2024_gui.py` or `lawfirm_2024_enhanced.py`:

```python
DB_CONFIG = {
    'host': 'localhost',      # Change if your MySQL is on different host
    'user': 'root',           # Your MySQL username
    'password': 'smh2sql',    # Your MySQL password ← UPDATE THIS
    'database': 'LAWFIRM'     # Your database name
}
```

---

## Step 4: Run the Application (1 minute)

### Option A: Basic GUI Version (Recommended for beginners)
```powershell
python lawfirm_2024_gui.py
```
Features:
- Find lawyers by speciality
- Manage lawyer profiles
- Simple and clean interface

### Option B: Enhanced GUI Version (Full features)
```powershell
python lawfirm_2024_enhanced.py
```
Features:
- User login system
- Client dashboard
- Lawyer dashboard
- Admin panel
- Case management

---

## Step 5: Test the Application (1 minute)

### For Basic Version:
1. Click "Search Lawyers"
2. Select a speciality (e.g., "Immigration Law")
3. Click "Search Lawyers" button
4. Results should display in the table

### For Enhanced Version:
1. **First Time:**
   - Click "Register" button
   - Create an account
   - Choose login type: User

2. **Login:**
   - Use your registered credentials
   - Explore your dashboard

---

## Troubleshooting

### ❌ "pymysql not found"
```powershell
pip install pymysql --upgrade
```

### ❌ "Connection refused" Error
- Check MySQL is running: `mysql -u root -p`
- Verify credentials in DB_CONFIG match your MySQL setup
- Check database exists: `SHOW DATABASES;`

### ❌ Tkinter not working
**Windows:** Usually built-in. Try reinstalling Python with Tkinter option checked.

**Linux:**
```bash
sudo apt-get install python3-tk
```

**Mac:**
```bash
brew install python3
```

### ❌ "LAWFIRM database not found"
Create the database:
```sql
CREATE DATABASE LAWFIRM;
USE LAWFIRM;

CREATE TABLE NEWLAWYER (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100),
    AGE INT,
    CV_LINK VARCHAR(255),
    SPECIALITY VARCHAR(100),
    YEARS_OF_EXPERIENCE INT
);
```

---

## File Structure

```
164/
├── lawfirm_2024.py                 (Original console version)
├── lawfirm_2024_gui.py             ← Use this (Basic)
├── lawfirm_2024_enhanced.py        ← Use this (Advanced)
├── requirements.txt                 ← Install dependencies
├── README.md                         ← Full documentation
├── MIGRATION_GUIDE.md               ← Detailed migration info
├── usernames.csv                    (Auto-created for user accounts)
├── request.dat                      (Auto-created for case requests)
└── casefiles.csv                    (Auto-created for cases)
```

---

## Key Differences from Original

| Aspect | Original | New GUI |
|--------|----------|---------|
| Interface | Console/Terminal | Graphical Window |
| Database | mysql.connector | PyMySQL |
| Input Method | eval() + input() | Form fields (safer) |
| Error Handling | Console errors | dialog boxes |
| User Experience | Command-line style | Modern GUI |

---

## Next Steps

1. ✅ Install requirements
2. ✅ Configure database
3. ✅ Run application
4. ✅ Create test account (Enhanced version)
5. ✅ Add lawyers to database
6. 📚 Read README.md for advanced features

---

## Support Resources

- **README.md** - Full feature documentation
- **MIGRATION_GUIDE.md** - Detailed comparison with original
- **Code Comments** - Each function is well-documented

---

## Common Use Cases

### Just want to see it work?
```powershell
python lawfirm_2024_gui.py
```

### Want full system with login?
```powershell
python lawfirm_2024_enhanced.py
```

### Want to add custom features?
Edit `lawfirm_2024_gui.py` starting at line 150 (ManageLawyerGUI class)

---

## Performance Tips

- Keep MySQL running in background
- Use Basic version for simple operations
- Use Enhanced version for complete system
- Ensure stable internet for CV links to work

---

**You're ready! Run the application now:** 🎉

```powershell
python lawfirm_2024_gui.py
```

Questions? Check README.md or MIGRATION_GUIDE.md
