# Application Flow & Architecture

## 🔄 Application Flow Diagrams

### Basic GUI Version Flow

```
┌─────────────────────────┐
│   Start Application     │
│  lawfirm_2024_gui.py    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   MainGUI Window        │
│  - Welcome Window       │
│  - 4 Menu Buttons       │
└────────────┬────────────┘
             │
    ┌────────┼────────┐
    │        │        │
    ▼        ▼        ▼
┌─────┐ ┌──────────┐ ┌────────┐
│ 1.  │ │ 2.       │ │ 3.     │
│Find │ │Manage    │ │Settings│
│Lawyer
──┐ │Lawyer      │ │        │
└──┬──┘ │Profiles  │ │        │
   │    └────┬─────┘ └───┬────┘
   │         │           │
   ▼         ▼           ▼
┌──────────────────────────────────┐
│  Separate Popup Windows          │
│  - Lawyer Finder                 │
│  - Profile Manager               │
│  - Configuration Display         │
└──────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────┐
│  Database Operations (PyMySQL)   │
│  - SELECT queries                │
│  - INSERT operations             │
│  - UPDATE operations             │
│  - DELETE operations             │
└──────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────┐
│  Error Handling                  │
│  - Connection errors             │
│  - Query errors                  │
│  - Display in dialogs            │
└──────────────────────────────────┘
```

### Enhanced GUI Version Flow

```
┌──────────────────────────────────┐
│   Start Application              │
│  lawfirm_2024_enhanced.py        │
└───────────────┬──────────────────┘
                │
                ▼
        ┌──────────────────┐
        │  LoginGUI Window │
        │  - Username field│
        │  - Password field│
        │  - Login buttons │
        └────────┬─────────┘
                 │
         ┌───────┴────────┐
         │                │
         ▼                ▼
    ┌────────┐      ┌──────────┐
    │ Register│     │  Login   │
    └────┬────┘     └────┬─────┘
         │               │
         │               ▼
         │        ┌────────────────────────────┐
         │        │ Select User Type:          │
         │        │ - User (Client)            │
         │        │ - Lawyer                   │
         │        │ - Admin                    │
         │        └──┬───────────────────────┬─┤
         │           │                       │ │
         └─────┬─────┘                       │ │
               │                             │ │
               ▼                             ▼ ▼
        ┌──────────────┐   ┌───────────────┐   ┌──────────────┐
        │User Register │   │User Dashboard │   │Lawyer        │
        │- Name        │   │- Request Test │   │Dashboard    │
        │- Username    │   │- View Cases   │   │- View Request│
        │- Password    │   │- Track Status │   │- Manage Case │
        └──────────────┘   └───────────────┘   │- Approve    │
                                                │  Requests    │
        ┌─────────────────────────────────────┤              │
        │                                     └──────────────┘
        │
        │                    ┌──────────────────┐
        │                    │Admin Dashboard   │
        │                    │- Manage Lawyers  │
        │                    │- View All Cases  │
        │                    │- View Reports    │
        │                    │- System Settings │
        │                    └──────────────────┘
        │
        └────────────┬────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────────┐
        │ Database Operations (PyMySQL)│
        │ - User authentication        │
        │ - Data CRUD operations       │
        │ - Case tracking              │
        │ - Lawyer management          │
        └──────────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────────┐
        │ File Operations              │
        │ - usernames.csv (auth)       │
        │ - request.dat (cases)        │
        │ - casefiles.csv (tracking)   │
        └──────────────────────────────┘
```

---

## 🎭 User Journey Maps

### Client User Flow
```
Start
  │
  ├─► Register New Account
  │   ├─► Enter name, username, password
  │   └─► Stored in CSV
  │
  ├─► Login
  │   ├─► Enter credentials
  │   └─► Verify in database
  │
  ├─► Request Lawyer
  │   ├─► Select speciality
  │   ├─► Describe case
  │   ├─► Choose urgency
  │   └─► Submit (stored in request.dat)
  │
  ├─► View Cases
  │   ├─► See pending requests
  │   ├─► See approved cases
  │   └─► Check status
  │
  └─► Logout/End
```

### Lawyer User Flow
```
Start
  │
  ├─► Login
  │   ├─► Enter credentials
  │   └─► Access lawyer dashboard
  │
  ├─► View Requests
  │   ├─► See pending client cases
  │   ├─► See case details
  │   └─► View urgency level
  │
  ├─► Approve Cases
  │   ├─► Select case to approve
  │   ├─► Case moved to casefiles.csv
  │   └─► Removed from request.dat
  │
  ├─► Manage Cases
  │   ├─► View assigned cases
  │   ├─► Update status
  │   └─► Track progress
  │
  └─► Logout/End
```

### Admin User Flow
```
Start
  │
  ├─► Login (Admin Role)
  │
  ├─► Manage Lawyers
  │   ├─► View all lawyer profiles
  │   ├─► Add new lawyers
  │   ├─► Update profiles
  │   └─► Delete inactive lawyers
  │
  ├─► View All Cases
  │   ├─► See all cases in system
  │   ├─► Filter by speciality
  │   ├─► Track progress
  │   └─► Monitor revenue
  │
  ├─► View Reports
  │   ├─► Monthly revenue
  │   ├─► Case statistics
  │   ├─► Lawyer performance
  │   └─► Client satisfaction
  │
  ├─► System Settings
  │   ├─► Database configuration
  │   ├─► User access control
  │   ├─► System maintenance
  │   └─► Backup/Restore
  │
  └─► Logout/End
```

---

## 🏛️ System Architecture Layers

```
┌─────────────────────────────────────┐
│    Presentation Layer (Tkinter)      │
│  ├─ Windows and Dialogs             │
│  ├─ Form Fields and Buttons         │
│  ├─ Treeviews and Tables            │
│  └─ Message Boxes                   │
├─────────────────────────────────────┤
│    Business Logic Layer              │
│  ├─ Class: LoginGUI                 │
│  ├─ Class: UserDashboard            │
│  ├─ Class: LawyerDashboard           │
│  ├─ Class: AdminDashboard            │
│  └─ Validation & Processing         │
├─────────────────────────────────────┤
│    Data Access Layer (PyMySQL)       │
│  ├─ Class: DatabaseConnection       │
│  ├─ SQL Queries                     │
│  ├─ Connection Management           │
│  └─ Error Handling                  │
├─────────────────────────────────────┤
│    Data Storage Layer                │
│  ├─ MySQL Database                  │
│  │  └─ Table: NEWLAWYER             │
│  ├─ CSV Files                       │
│  │  ├─ usernames.csv                │
│  │  └─ casefiles.csv                │
│  └─ Pickle Files                    │
│     └─ request.dat                  │
└─────────────────────────────────────┘
```

---

## 📊 Database Entity Relationship

```
┌──────────────────────────┐
│      NEWLAWYER           │
├──────────────────────────┤
│ ID (PK)                  │
│ NAME                     │
│ AGE                      │
│ CV_LINK                  │◄─────┐
│ SPECIALITY               │      │
│ YEARS_OF_EXPERIENCE      │      │
└──────────────────────────┘      │
                                   │
                    Linked to      │
                    by URL         │
                                   │
┌──────────────────────────┐      │
│      CASE REQUEST        │      │
├──────────────────────────┤      │
│ Client Name              │      │
│ Lawyer ID (FK)           │──────┘
│ Date of Request          │
│ Description              │
│ Urgency Level            │
│ Status: Pending/Approved │
└──────────────────────────┘
        │
        │ Approved Cases Move To
        ▼
┌──────────────────────────┐
│      CASEFILES           │
├──────────────────────────┤
│ Lawyer ID (FK)           │
│ Case File No.            │
│ Client Name              │
│ Case Type                │
│ Status: Open/Closed      │
│ Payment Status           │
│ Case Description         │
└──────────────────────────┘
```

---

## 🔐 Security & Access Control

```
┌─────────────────────────┐
│  User Request           │
│  (Credentials)          │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Authentication Layer   │
│  ├─ Read usernames.csv  │
│  ├─ Verify credentials  │
│  └─ Check role/type     │
└────────────┬────────────┘
             │
    ┌────────┴──────────┐
    │                   │
    ▼                   ▼
┌──────────┐      ┌──────────┐
│ Invalid  │      │  Valid   │
│ → Deny   │      │ → Grant  │
└──────────┘      │ Access   │
                  └────┬─────┘
                       │
            ┌──────────┴──────────┐
            │                     │
            ▼                     ▼
      ┌──────────┐          ┌──────────┐
      │ Role:    │          │ Role:    │
      │ Client   │          │ Lawyer   │
      │ Admin    │          │ Admin    │
      └───┬──────┘          └────┬─────┘
          │                      │
          ▼                      ▼
    ┌─────────────┐        ┌─────────────┐
    │  Limited    │        │   Full      │
    │ Dashboard   │        │  Features   │
    └─────────────┘        └─────────────┘
```

---

## 🔄 Data Flow During Case Request

```
Client Input
    │
    ├─ Case Type
    ├─ Description
    ├─ Urgency Level
    └─ Client Name
         │
         ▼
   Validation
    │
    ├─ Check required fields
    ├─ Validate urgency level
    └─ Verify client name
         │
         ▼
   Create Request Object
    │
    └─ [Lawyer ID, Client Name, Date, Description, Urgency]
         │
         ▼
   Serialize to Pickle
    │
    └─ Store in request.dat binary file
         │
         ▼
   Display Confirmation
    │
    └─ "Request submitted successfully"
         │
         ▼
   Lawyer Views Request
    │
    ├─ Read request.dat
    ├─ Deserialize pickled data
    └─ Display in dashboard
         │
         ▼
   Lawyer Approves
    │
    ├─ Create case record
    ├─ Insert into casefiles.csv
    ├─ Remove from request.dat
    └─ Assign case parameters
         │
         ▼
   Client Views Case
    │
    └─ Case appears in "Your Cases"
```

---

## 📈 Database Query Flow

```
User Action
    │
    ▼
┌────────────────────────┐
│ Python Application     │
│ Calls Database Method  │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ DatabaseConnection     │
│ pymysql.connect()      │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ Create Cursor          │
│ connection.cursor()    │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ Execute Query          │
│ cursor.execute(query)  │
│ with parameters        │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ MySQL Server           │
│ Process Query          │
│ Return Results         │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ Fetch Results          │
│ fetchall() / fetchone()│
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ Process Results        │
│ Format for Display     │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ Display in GUI         │
│ Treeview / Dialog      │
└────────────────────────┘
```

---

## 🚀 Feature Request Priority Matrix

```
HIGH IMPACT / HIGH EFFORT
├─ Multi-threading for long queries
├─ Email notification system
└─ Advanced reporting

HIGH IMPACT / LOW EFFORT
├─ Password hashing
├─ Search/Filter capabilities
├─ Pagination for large results
└─ User activity logging

LOW IMPACT / HIGH EFFORT
├─ Mobile app version
├─ Advanced analytics
└─ AI-powered recommendations

LOW IMPACT / LOW EFFORT  
├─ Dark mode theme
├─ Font size adjustments
├─ Export to PDF
└─ Print functionality
```

---

## 🔧 Deployment Architecture

```
DEVELOPMENT
├─ Local MySQL (credentials in code)
├─ Test data in CSV files
└─ Debug mode enabled

                    │
                    │ (Code Review & Testing)
                    ▼

STAGING
├─ Staging MySQL server
├─ Environment variables for credentials
├─ Logging enabled
└─ Performance testing

                    │
                    │ (Final Verification)
                    ▼

PRODUCTION
├─ Production MySQL server
├─ Secure credential management
├─ Error logging system
├─ Connection pooling
└─ Backup strategy

                    │
                    │ (Monitoring)
                    ▼

MONITORING
├─ Error tracking
├─ Performance metrics
├─ User activity logs
└─ Database health checks
```

---

## 📊 Class Dependency Diagram

```
MainApplication
    │
    ├─► DatabaseConnection
    │   └─ Used by all GUI classes
    │
    ├─► LoginGUI
    │   ├─ Creates UserDashboard
    │   ├─ Creates LawyerDashboard
    │   └─ Creates AdminDashboard
    │
    ├─► UserDashboard
    │   ├─ Uses DatabaseConnection
    │   └─ File operations (request.dat)
    │
    ├─► LawyerDashboard
    │   ├─ Uses DatabaseConnection
    │   └─ File operations (casefiles.csv)
    │
    └─► AdminDashboard
        └─ Uses DatabaseConnection
```

---

**Version:** 2024.1  
**Status:** Complete  
**Last Updated:** February 18, 2026
