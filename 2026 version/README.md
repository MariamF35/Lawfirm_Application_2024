# Law Firm Management System - GUI Version

## Overview
This is a modernized version of the law firm management system using **PyMySQL** for database connectivity and **Tkinter** for graphical user interface (GUI).

## Key Changes from Original Version

### 1. Database Connection
- **Old:** `mysql.connector`
- **New:** `pymysql` (lightweight, pure Python implementation)

### 2. User Interface
- **Old:** Console-based with `input()` and `print()`
- **New:** Modern GUI with Tkinter featuring:
  - Clean windows and dialog boxes
  - Button-based navigation
  - Table views with scrollbars
  - Input validation
  - Error handling with message dialogs

### 3. Code Structure
- Object-oriented design with separate classes for different functionalities
- Better separation of concerns
- More maintainable and scalable code
- Improved error handling with try-except blocks

## Features

### 1. Find Lawyer by Speciality
- Search lawyers by their speciality (Immigration, Criminal, Real Estate, etc.)
- View lawyer details in a table format
- Open CV links in browser directly from the application

### 2. Manage Lawyer Profiles
- Add new lawyer entries
- Update existing lawyer information
- Delete lawyer profiles
- Form-based input with validation

### 3. Settings
- View current database configuration
- Easy-to-read configuration display

## Installation

1. **Install Python 3.7+**

2. **Install Required Packages**
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pymysql==1.1.0
pip install tabulate==0.9.0
pip install matplotlib==3.8.0
```

3. **Database Configuration**
Update the `DB_CONFIG` dictionary in `lawfirm_2024_gui.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'smh2sql',
    'database': 'LAWFIRM'
}
```

## Running the Application

```bash
python lawfirm_2024_gui.py
```

## Database Schema

The application expects the following table structure:

```sql
CREATE TABLE NEWLAWYER (
    NAME VARCHAR(100),
    AGE INT,
    CV_LINK VARCHAR(255),
    SPECIALITY VARCHAR(100),
    YEARS_OF_EXPERIENCE INT
);
```

## Advantages of This Version

✅ **Better UX:** Graphical interface vs command-line
✅ **Easier Input:** Form fields with validation
✅ **Cleaner Code:** Object-oriented and modular design
✅ **Lightweight DB:** PyMySQL is pure Python (no C dependencies)
✅ **Cross-Platform:** Works on Windows, Mac, and Linux
✅ **Better Error Messages:** Dialog boxes instead of console errors
✅ **Scalable:** Easy to add new features and windows

## Future Enhancements

- Add user authentication/login screen
- Implement client management module
- Add case tracking system
- Create reports and analytics
- Add search and filter capabilities
- Implement data export to CSV/PDF
- Add multi-threaded database operations

## Notes

- This version focuses on core lawyer management features
- The console-based features (case management, user registration) can be added to the GUI
- Database credentials should be stored in configuration files in production
- Consider implementing connection pooling for better performance

## Troubleshooting

**Connection Error:** Check if MySQL is running and credentials are correct
**PyMySQL not found:** Run `pip install pymysql`
**Tkinter not found:** On Linux, run `sudo apt-get install python3-tk`

---
For more information or support, contact justiceleaguelawfirm11@outlook.com
