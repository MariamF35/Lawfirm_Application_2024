# general statements and import statements 
import csv, getpass, pickle, os, random 
from tabulate import tabulate 
import matplotlib.pyplot as plt 
import mysql.connector 
import webbrowser 

obj = mysql.connector.connect(host="localhost", database="LAWFIRM", user="root", password="smh2sql") 
c = obj.cursor() 

def openlink(url): 
    webbrowser.open(url) 

def speciality(): 
    while True: 
        print("Choose speciality") 
        print("1.Immigration Lawyer\n2.Criminal Lawyer\n3.Real Estate Law Lawyer\n4.Business Lawyer\n5.Family Law\n6.Bankruptcy Law\n7.Tax Law\n8.Exit") 
        choice = eval(input("Please enter choice")) 
        if choice == 1: 
            q = "SELECT * FROM NEWLAWYER WHERE SPECIALITY IN ('IMMIGRATION LAW')" 
            c.execute(q) 
            l = c.fetchall() 
            if l != []: 
                table = tabulate(l, tablefmt="grid") 
                print(table) 
                choice1 = input("Enter name of lawyer whose CV you would like to look") 
                for i in l: 
                    if i[0] == choice1: 
                        link = i[2] 
                        openlink(link) 
                    else: 
                        print("No entry found") 
        
        if choice == 2: 
            q = "SELECT * FROM NEWLAWYER WHERE SPECIALITY IN ('CRIMINAL LAW')" 
            c.execute(q) 
            l = c.fetchall() 
            if l != []: 
                table = tabulate(l, tablefmt="grid") 
                print(table) 
                choice1 = input("Enter name of lawyer whose CV you would like to look") 
                for i in l: 
                    if i[0] == choice1: 
                        link = i[2] 
                        openlink(link) 
                    else: 
                        print("No entry found") 
                
        if choice == 3: 
            q = "SELECT * FROM NEWLAWYER WHERE SPECIALITY IN ('REAL ESTATE LAW')" 
            c.execute(q) 
            l = c.fetchall() 
            if l != []: 
                table = tabulate(l, tablefmt="grid") 
                print(table) 
                choice1 = input("Enter name of lawyer whose CV you would like to look") 
                for i in l: 
                    if i[0] == choice1: 
                        link = i[2] 
                        openlink(link) 
                    else: 
                        print("No entry found") 
                
        if choice == 4: 
            q = "SELECT * FROM NEWLAWYER WHERE SPECIALITY IN ('BUSINESS LAW')" 
            c.execute(q) 
            l = c.fetchall() 
            if l != []: 
                table = tabulate(l, tablefmt="grid") 
                print(table) 
                choice1 = input("Enter name of lawyer whose CV you would like to look") 
                for i in l: 
                    if i[0] == choice1: 
                        link = i[2] 
                        openlink(link) 
                    else: 
                        print("No entry found") 
                
        if choice == 5: 
            q = "SELECT * FROM NEWLAWYER WHERE SPECIALITY IN ('FAMILY LAW')" 
            c.execute(q) 
            l = c.fetchall() 
            if l != []: 
                table = tabulate(l, tablefmt="grid") 
                print(table) 
                choice1 = input("Enter name of lawyer whose CV you would like to look") 
                for i in l: 
                    if i[0] == choice1: 
                        link = i[2] 
                        openlink(link) 
                    else: 
                        print("No entry found") 
                
        if choice == 6: 
            q = "SELECT * FROM NEWLAWYER WHERE SPECIALITY IN ('BANKRUPTCY LAW')" 
            c.execute(q) 
            l = c.fetchall() 
            if l != []: 
                table = tabulate(l, tablefmt="grid") 
                print(table) 
                choice1 = input("Enter name of lawyer whose CV you would like to look") 
                for i in l: 
                    if i[0] == choice1: 
                        link = i[2] 
                        openlink(link) 
                    else: 
                        print("No entry found") 
                
        if choice == 7: 
            q = "SELECT * FROM NEWLAWYER WHERE SPECIALITY IN ('TAX LAW')" 
            c.execute(q) 
            l = c.fetchall() 
            if l != []: 
                table = tabulate(l, tablefmt="grid") 
                print(table) 
                choice1 = input("Enter name of lawyer whose CV you would like to look") 
                for i in l: 
                    if i[0] == choice1: 
                        link = i[2] 
                        openlink(link) 
                    else: 
                        print("No entry found") 
                
        if choice == 8: 
            break 

def newlawyer(): 
    while True: 
        print("1.New Entry\n2.Update Entry\n3.Delete Entry\n4.Exit") 
        choice = eval(input("Enter choice")) 
        if choice == 1: 
            q1 = "insert into NEWLAWYER VALUES (%s,%s,%s,%s,%s)" 
            a = input("NAME") 
            b = eval(input("AGE")) 
            d = input("ENTER CV LINK") 
            e = input("AREA OF SPECIALITY") 
            f = eval(input("NO. OF YEARS OF PRACTICE")) 
            c.execute(q1, (a, b, d, e, f)) 
            obj.commit() 
        if choice == 2: 
            while True: 
                name1 = input("Please enter your name") 
                q2 = "SELECT * FROM NEWLAWYER WHERE NAME=%s" 
                c.execute(q2, (name1,)) 
                l = c.fetchall() 
                if l == []: 
                    print("Please enter valid entry") 
                else: 
                    table = tabulate(l, tablefmt="grid") 
                    print(table) 
                    print("What changes would you like to make to above entry?") 
                    print("1:Name\n2:Age\n3:CV link\n4:Area of Speciality\n5:Years of Experience\n6:All") 
                    choice_changes = eval(input("Enter valid choice")) 
                    if choice_changes == 1: 
                        updated_name = input("Enter updated name") 
                        q3 = "UPDATE NEWLAWYER SET NAME=%s WHERE NAME=%s" 
                        c.execute(q3, (updated_name, name1)) 
                        q4 = "SELECT * FROM NEWLAWYER WHERE NAME=%s" 
                        c.execute(q4, (updated_name,)) 
                        l = c.fetchall() 
                        table = tabulate(l, tablefmt="grid") 
                        print(table) 
                        print("Name Updated") 
                        obj.commit() 
                        break 
                    if choice_changes == 2: 
                        og_age = eval(input("Enter original age")) 
                        updated_age = eval(input("Enter updated age")) 
                        q5 = "UPDATE NEWLAWYER SET AGE=%s WHERE AGE=%s" 
                        c.execute(q5, (updated_age, og_age)) 
                        q6 = "SELECT * FROM NEWLAWYER WHERE NAME=%s" 
                        c.execute(q6, (name1,)) 
                        l = c.fetchall() 
                        table = tabulate(l, tablefmt="grid") 
                        print(table) 
                        print("Age Updated") 
                        obj.commit() 
                        break 
                    if choice_changes == 3: 
                        og_CVlink = input("Enter original link") 
                        updated_CVlink = input("Enter updated link") 
                        q7 = "UPDATE NEWLAWYER SET CV_LINK=%s WHERE CV_LINK=%s" 
                        c.execute(q7, (updated_CVlink, og_CVlink)) 
                        q8 = "SELECT * FROM NEWLAWYER WHERE NAME=%s" 
                        c.execute(q8, (name1,)) 
                        l = c.fetchall() 
                        table = tabulate(l, tablefmt="grid") 
                        print(table) 
                        print("CV link Updated") 
                        obj.commit() 
                        break 
                    if choice_changes == 4: 
                        og_speciality = input("Enter original speciality") 
                        updated_speciality = input("Enter updated speciality") 
                        q9 = "UPDATE NEWLAWYER SET SPECIALITY=%s WHERE SPECIALITY=%s" 
                        c.execute(q9, (updated_speciality, og_speciality)) 
                        q10 = "SELECT * FROM NEWLAWYER WHERE NAME=%s" 
                        c.execute(q10, (name1,)) 
                        l = c.fetchall() 
                        table = tabulate(l, tablefmt="grid") 
                        print(table) 
                        print("Speciality Updated") 
                        obj.commit() 
                        break 
                    if choice_changes == 5: 
                        og_yoe = eval(input("Enter original years of experience")) 
                        updated_yoe = eval(input("Enter updated years of experience")) 
                        q11 = "UPDATE NEWLAWYER SET YEARS_OF_EXPERIENCE=%s WHERE YEARS_OF_EXPERIENCE=%s" 
                        c.execute(q11, (updated_yoe, og_yoe)) 
                        q12 = "SELECT * FROM NEWLAWYER WHERE NAME=%s" 
                        c.execute(q12, (name1,)) 
                        l = c.fetchall() 
                        table = tabulate(l, tablefmt="grid") 
                        print(table) 
                        print("Years of Experience Updated") 
                        obj.commit() 
                        break 
                    if choice_changes == 6: 
                        updated_name = input("Enter updated name") 
                        updated_age = eval(input("Enter updated age")) 
                        updated_CVlink = input("Enter updated link") 
                        updated_speciality = input("Enter updated speciality") 
                        updated_yoe = eval(input("Enter updated years of experience")) 
                        q13 = "UPDATE NEWLAWYER SET NAME=%s,AGE=%s,CV_LINK=%s,SPECIALITY=%s,YEARS_OF_EXPERIENCE=%s WHERE NAME=%s" 
                        c.execute(q13, (updated_name, updated_age, updated_CVlink, updated_speciality, updated_yoe, name1)) 
                        print("All Data Updated") 
                        q14 = "SELECT * FROM NEWLAWYER WHERE NAME=%s" 
                        c.execute(q14, (updated_name,)) 
                        l = c.fetchall() 
                        table = tabulate(l, tablefmt="grid") 
                        print(table) 
                        obj.commit() 
                        break 
        if choice == 3: 
            while True: 
                name1 = input("Please enter your name") 
                q = "SELECT * FROM NEWLAWYER WHERE NAME=%s" 
                c.execute(q, (name1,)) 
                l = c.fetchall() 
                if l != []: 
                    table = tabulate(l, tablefmt="grid") 
                    print(table) 
                    choice1 = input("Are you sure you would like to delete this entry") 
                    if choice1.lower() == "yes": 
                        q1 = "DELETE FROM NEWLAWYER WHERE NAME=%s" 
                        c.execute(q1, (name1,)) 
                        print("Entry deleted") 
                        obj.commit() 
                        break 
                    else: 
                        print() 
                else: 
                    print("Enter Valid Name") 
        if choice == 4: 
            break 

def intro(): 
    f = open("intro.txt", 'r') 
    print(f.read()) 
    f.close() 

def money(var): 
    f = open('LawyerProfile.csv') 
    r = csv.reader(f) 
    for i in r: 
        if str(var) in i: 
            s = i[5] 
            f.close() 
            return s 

def name(x): 
    # x is the lawyer id
    f = open('LawyerProfile.csv') 
    r = csv.reader(f) 
    for i in r: 
        if x in i: 
            ln = i[1] + ' ' + i[2] 
            f.close() 
            return ln 

def ct(x): 
    f = open('LawyerProfile.csv') 
    r = csv.reader(f) 
    for i in r: 
        if i[0] == str(x): 
            c = i[4] 
            f.close() 
            return c 
    f.close() 

def change(l, name): 
    # l=lid name=name of client
    # purpose is to change status in casefiles.csv
    f = open('casefiles.csv', 'r') 
    f1 = open('kcasefiles.csv', 'w', newline='') 
    r = csv.reader(f) 
    w = csv.writer(f1) 
    for x in r: 
        if (str(l) in x) and ((x[6] == 'ND') or (x[4] == 'O')) and ((x[2] in name) or (name in x[2])): 
            k = [x[0], x[1], x[2], x[3], 'C', x[5], 'D', x[7], x[8]] 
            w.writerow(k) 
        else: 
            w.writerow(x) 
    f.close() 
    f1.close() 
    os.remove('casefiles.csv') 
    os.rename('kcasefiles.csv', 'casefiles.csv') 

def remove(l): 
    # l=lid
    # purpose is to make changes to request.dat
    f = open('request.dat', 'rb') 
    f1 = open('krequest.dat', 'wb') 
    while True: 
        try: 
            x = pickle.load(f) 
            if l in x: 
                pass 
            else: 
                pickle.dump(x, f1) 
        except EOFError: 
            break 
    f.close() 
    f1.close() 
    os.remove('request.dat') 
    os.rename('krequest.dat', 'request.dat') 

def type(t): 
    if t == 1: 
        spec = 'Immigration Law' 
    elif t == 2: 
        spec = 'Criminal Law' 
    elif t == 3: 
        spec = 'Real Estate Law' 
    elif t == 4: 
        spec = 'Business Law' 
    elif t == 5: 
        spec = 'Family Law' 
    elif t == 6: 
        spec = "Bankruptcy Law" 
    elif t == 7: 
        spec = 'Tax Law' 
    elif t == 8: 
        spec = 'Defense Law' 
    print("List Of Lawyers:") 
    f = open("LawyerProfile.csv") 
    r = csv.reader(f) 
    data = f.readlines() 
    nl = [] 
    for jk in range(len(data)): 
        tt = data[jk] 
        tempjk = tt.rstrip('\n') 
        splittedone = tempjk.split(',') 
        a = splittedone.pop(6)  # popping target contribution
        a = splittedone.pop(7)  # popping monthly salary
        if jk == 0: 
            nl.append(splittedone) 
        elif spec in tt: 
            nl.append(splittedone) 
    print(tabulate(nl, headers='firstrow', tablefmt='grid')) 
    print() 

def login1(): 
    f = open("usernames.csv") 
    username = input('Enter Your Username: ') 
    password = getpass.getpass('Enter Your Password: ') 
    print() 
    l = f.readlines() 
    for i in range(len(l)): 
        vv = l[i] 
        templ = vv.strip().split(',') 
        if username == templ[0]: 
            pwd = templ[1] 
            if pwd == password: 
                # Successful login
                formatted_username = username[0:].capitalize() 
                u1 = '' 
                for j in formatted_username: 
                    if j.isupper(): 
                        u1 = u1 + j 
                    elif j.islower(): 
                        u1 = u1 + j 
                    elif j.isspace(): 
                        u1 += ' ' 
                print("Welcome", u1, '\n') 
                return (True, u1) 
            else: 
                print("Incorrect Password Entered!\n") 
                return (False, None) 
        else: 
            # Username not found in the file
            print("Wrong Username Entered!\n") 
            return (False, None) 

def delete(yy):  # yy=row index to delete
    lines = [] 
    f = open("casefiles.csv", "r") 
    r = csv.reader(f) 
    for i, row in enumerate(r): 
        if i != yy: 
            lines.append(row) 
    f.close() 
    f1 = open("casefiles.csv", "w", newline="") 
    w = csv.writer(f1) 
    w.writerows(lines) 
    f1.close() 

# PROGRAM
# intro()
print() 
while True: 
    ch = eval(input("Main menu:\n1. User\n2. Managing Partner\n3. Lawyer\n4. New Registration\nTO END PROGRAM, ENTER 90\nEnter choice: ")) 
    if ch == 1:  # User
        t = login1() 
        x = t[0] 
        while x == True: 
            ch1 = eval(input("1. Request a Lawyer\n2. Veiw Status of Cases\n3. More About Law Firm\n4. Return to Previous Menu\nEnter choice: ")) 
            if ch1 == 1: 
                choice = eval(input("\nWhat is your case regarding?\n1. Immigration Law\n2. Criminal Law\n3. Real Estate Law\n4. Business Law\n5. Family Law\n6. Bankruptancy\n7. Tax Law\n8. Defense Law\nEnter choice: ")) 
                type(choice) 
                explore = input("Would you like to explore more about our lawyers?")  # Input = Yes/ No
                if explore.upper() == "YES": 
                    while True: 
                        reqlawyer = eval(input("Enter Lawyer ID="))  # user will enter the id of the lawyer and info
                        ol = [] 
                        reqid = str(reqlawyer) 
                        f2 = open("LawyerProfile.csv") 
                        r2 = csv.reader(f2) 
                        ll = f2.readlines() 
                        for jj in range(1, len(ll)): 
                            if reqid in ll[jj]: 
                                splitone = ll[jj].split(',') 
                                ol.extend([['ID= ', reqlawyer], ['Name - ', splitone[1], splitone[2]], ['Specialisation - ', splitone[4]], ['Hourly rate - ', splitone[5]], ['Number of cases handled - ', splitone[7]]]) 
                                fg = True 
                                break 
                        if ol == []: 
                            print("Wrong ID Entered") 
                            fg = False 
                        if fg == True: 
                            for i in ol: 
                                print(i[0], i[1]) 
                            eh = eval(input("Enter estimated number of hours you require: ")) 
                            mm = int(ol[3][1]) 
                            amt = eh * mm 
                            print("Estimated value to pay = ", amt) 
                            confirm = input("Do you want to proceed with this lawyer? ") 
                            if confirm.upper() == 'YES': 
                                print() 
                                clientname = input("Enter client name: ") 
                                doreg = input("Enter today's date seperated with '/': ") 
                                des = input("Enter short description of your case: ") 
                                uc = eval(input("Enter how urgent your case must be solved --> 1 = VIP Prioritiy, 2 = Normal Priority: ")) 
                                rl = [] 
                                rl.append(ol[0][1]) 
                                rl.extend([clientname, doreg]) 
                                rl.extend([ol[1][1], ol[1][2]]) 
                                rl.extend([des, uc]) 
                                f3 = open("request.dat", "ab") 
                                pickle.dump(rl, f3) 
                                f3.close() 
                                f2.close() 
                                break 
                            else: 
                                print() 
                                break 
                else: 
                    print("Returning To Previous Menu") 
                    break 
            elif explore.upper() == 'NO': 
                print("Returning to previous menu") 
                print() 
            elif ch1 == 2:  # Veiw cases status
                reqf = open("request.dat", 'rb') 
                fl = []  # original list to be tabulated
                h = ['Lawyer ID', 'Lawyer Name', 'D/o Requesting', 'Case', 'Description', 'Urgency Code', 'Status'] 
                fl.append(h) 
                af = None  # actual flag
                print() 
                flag1 = False 
                while True: 
                    try: 
                        row = pickle.load(reqf) 
                        # row=['lawyerid','clientname','doreg','lfn','lln','desc','uc'....]
                        if t[1] in row[1] or row[1] in t[1]: 
                            tempsl = [] 
                            ln = row[3] + ' ' + row[4] 
                            casetype = ct(row[0]) 
                            tempsl.extend([row[0], ln, row[2], casetype, row[5], row[6], 'PENDING']) 
                            fl.append(tempsl) 
                            af = False 
                            flag1 = True 
                        else: 
                            if flag1 == True: 
                                flag1 = True 
                            else: 
                                flag1 = False 
                    except EOFError: 
                        if flag1 == False: 
                            print("You don't have any pending cases\n") 
                        cf = open('casefiles.csv') 
                        rf = csv.reader(cf) 
                        for i in rf: 
                            if (t[1] in i or i[2] in t[1]) and (i[6] == 'ND'): 
                                ln = name(i[0]) 
                                fl.extend([[i[0], ln, i[7], i[5], i[8], i[3], 'APPROVED']]) 
                                af = True 
                        if fl != []: 
                            print(tabulate(fl, headers='firstrow', tablefmt='grid')) 
                        else: 
                            print("You have no approved requests also!") 
                            af = None 
                        cf.close() 
                        reqf.close() 
                        break 
                if af == True: 
                    ppay = input("Proceed with payment?\nEnter Yes or No: ") 
                    if ppay.upper() == 'YES': 
                        lid = eval(input("Enter your lawyer's ID: ")) 
                        menu = eval(input("How would you like to pay?\n1. Pay full amount at once\n2. Pay 4 installments\nEnter choice:")) 
                    else: 
                        print("Please make sure to pay your dues by the earliest\n") 
                        menu = 0 
                    if menu == 1: 
                        eh = eval(input("Enter estimated number of hours you require: ")) 
                        mm = money(lid) 
                        amt = eh * int(mm) 
                        print("Amount to be paid = ", amt) 
                        print("Preference Noted") 
                        change(lid, t[1])  # lawyerid, t[1]
                        remove(lid) 
                        print() 
                    elif menu == 2: 
                        eh = eval(input("Enter estimated number of hours you require: ")) 
                        mm = money(lid) 
                        print(mm) 
                        amt = eh * int(mm) 
                        print('Amount to be paid per month for 4 months = ', amt / 4) 
                        print("Preference Noted") 
                        change(lid, t[1])  # change status
                        remove(lid) 
                        print() 
                    elif menu == 0: 
                        pass 
                elif af == None: 
                    print("You have no cases") 
                    print() 
                elif af == False: 
                    print("Please wait for the concerned lawyer to veiw your case request.\n") 
                    print() 
            elif ch1 == 3:  # More abt law firm
                print() 
                f = open("about.txt") 
                print(f.read()) 
                f.close() 
                print() 
            elif ch1 == 4:  # Exit
                print("Logging out") 
                print("Returning to previous menu") 
                print() 
                break 
    # EXECUTIVE-Managing Partner
    elif ch == 2: 
        cond = login1() 
        while cond[0] == True: 
            print("1. View Client Details\n2. View New Lawyer Profiles\n3. Track Monthly Revenue\n4. To Add/Delete Cases\nTO RETURN TO MAIN MENU, ENTER 21\n") 
            ch2 = eval(input("Enter Choice=")) 
            if ch2 == 1: 
                f1 = open("casefiles.csv") 
                r = csv.reader(f1) 
                data = f1.readlines() 
                nl = [] 
                for jk in data: 
                    tempjk = jk.rstrip('\n') 
                    splittedone = tempjk.split(',') 
                    nl.append(splittedone) 
                print(tabulate(nl, headers='firstrow', tablefmt='grid')) 
                print("*For status\n1 = Open Case\n0 = Closed Case") 
                print() 
            elif ch2 == 2: 
                speciality() 
            elif ch2 == 3: 
                while True: 
                    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"] 
                    revenue_rate = [] 
                    end_month = input("Enter the end month: ") 
                    end_month_index = months.index(end_month) 
                    for month in months[:end_month_index + 1]: 
                        rate = float(input(f"Enter Revenue Rate for {month}: ")) 
                        revenue_rate.append(rate) 
                    plt.plot(months[:end_month_index + 1], revenue_rate, color='red', marker='o') 
                    plt.title('Monthly Revenue Statistics of 2023', fontsize=14) 
                    plt.xlabel('Month', fontsize=14) 
                    plt.ylabel('Revenue', fontsize=14) 
                    plt.grid(True) 
                    plt.show() 
                    print() 
                    break 
            elif ch2 == 4: 
                print("1.To Add\n2.To Delete") 
                cc = eval(input("Enter choice=")) 
                if cc == 1: 
                    def appending(): 
                        f = open("casefiles.csv", "a", newline="") 
                        w = csv.writer(f) 
                        n = eval(input("Enter the no. of cases to be added=")) 
                        for i in range(n): 
                            a = eval(input("Lawyer ID= ")) 
                            b = eval(input("Enter File No.= ")) 
                            c = input("Enter Client Name= ") 
                            d = input("Enter Priority= ") 
                            e = input("Enter Status= ") 
                            f_input = input("Enter Type Of Case= ") 
                            g = input("Enter Payment Status= ") 
                            h = input("Date Of Registeration ") 
                            i = input("Enter Description=") 
                            l = [a, b, c, d, e, f_input, g, h, i] 
                            w.writerow(l) 
                        f.close() 
                    appending() 
                    print() 
                    print("CASE ADDED TO THE FILE!") 
                    print() 
                elif cc == 2: 
                    def delete(yy): 
                        lines = [] 
                        f = open("casefiles.csv", "r") 
                        r = csv.reader(f) 
                        for i, row in enumerate(r): 
                            if i != yy: 
                                lines.append(row) 
                        f.close() 
                        f1 = open("casefiles.csv", "w", newline="") 
                        w = csv.writer(f1) 
                        w.writerows(lines) 
                        f1.close() 
                    yy = eval(input("Input Row To Delete=")) 
                    delete(yy) 
                    print() 
                    print("CASE DELETED FROM THE FILE!") 
                    print() 
                else: 
                    print() 
                    print("WRONG INPUT PLEASE TRY AGAIN!") 
                    print() 
            elif ch2 == 21: 
                print() 
                print("RETURNING TO PREVIOUS MENU!") 
                print() 
                break 
            else: 
                print() 
                print("INVALID CHOICE! PLEASE TRY AGAIN.") 
                print() 
    elif ch == 3:  # LAWYER
        condi = login1() 
        while condi[0] == True: 
            ch3 = eval(input("1. View requests\n2. View client information\n3.To return to main menu, enter 23: ")) 
            print() 
            if ch3 == 1: 
                f = open("request.dat", "rb") 
                l = [] 
                try: 
                    while True: 
                        x = pickle.load(f) 
                        l.append(x) 
                except EOFError: 
                    f.close() 
                if len(l) <= 1: 
                    print("no pending requests") 
                else: 
                    l1 = [] 
                    xx = 0 
                    lawyer = eval(input("Enter your Lawyer ID")) 
                    for i in l: 
                        if i[0] == lawyer: 
                            l1.append(i) 
                            xx += 1 
                    print(tabulate(l1)) 
                    choice = input("Would you like approve cases?") 
                    if choice == "YES": 
                        while True: 
                            choice2 = input("Enter client name of the case you want to approve") 
                            f1 = open("casefiles.csv", "a") 
                            w = csv.writer(f1) 
                            c = 0 
                            approved = False 
                            for list in l: 
                                if list[1] == choice2: 
                                    c += 1 
                                    r_no = random.randint(100, 999) 
                                    law = input("Please enter which law should this case be segregated in") 
                                    first_name = list[3].lower() 
                                    last_name = list[4][:2].lower() 
                                    mail = first_name + last_name + "@gmail.com" 
                                    l1 = [list[0], r_no, list[3], list[4], mail, list[1], list[6], "O", law, "NA", list[2], list[5]] 
                                    w.writerow(l1) 
                                    approved = True 
                            f1.close() 
                            if approved: 
                                f2 = open("request1.dat", "wb") 
                                for list in l: 
                                    if list[1] != choice2: 
                                        pickle.dump(list, f2) 
                                f2.close() 
                                os.remove("request.dat") 
                                os.rename("request1.dat", "request.dat") 
                                thumbs_up_emoji = "👍" 
                                print(f"Case approved {thumbs_up_emoji}") 
                                break 
                            if c == 0: 
                                print() 
                                print("enter valid client") 
                                print() 
                    if choice == "NO": 
                        print() 
                    if xx == 0: 
                        print("Wrong ID") 
                        print() 
            if ch3 == 2: 
                f5 = open("casefiles.csv") 
                r = csv.reader(f5) 
                data = f5.readline() 
                choice = input("Enter clients of which law? Input should be first letter of Law, for eg: for Family Law input should be F") 
                if choice == "F": 
                    l1 = [] 
                    while data: 
                        tempm = data.rstrip('\n') 
                        splittedone = tempm.split(',') 
                        if "Family Law" in splittedone: 
                            l1.append(splittedone) 
                        data = f5.readline() 
                    print(tabulate(l1)) 
                    if l1 == []: 
                        print("No Family Law cases") 
                elif choice == "R": 
                    l1 = [] 
                    while data: 
                        tempm = data.rstrip('\n') 
                        splittedone = tempm.split(',') 
                        if "Real Estate Law" in splittedone: 
                            l1.append(splittedone) 
                        data = f5.readline() 
                    print(tabulate(l1)) 
                    if l1 == []: 
                        print("No Real Estate cases") 
                elif choice == "C": 
                    l1 = [] 
                    while data: 
                        tempm = data.rstrip('\n') 
                        splittedone = tempm.split(',') 
                        if "Criminal Law" in splittedone: 
                            l1.append(splittedone) 
                        data = f5.readline() 
                    print(tabulate(l1)) 
                    if l1 == []: 
                        print("No Criminal cases") 
                elif choice == "B": 
                    l1 = [] 
                    while data: 
                        tempm = data.rstrip('\n') 
                        splittedone = tempm.split(',') 
                        if "Bankruptcy Law" in splittedone: 
                            l1.append(splittedone) 
                        data = f5.readline() 
                    print(tabulate(l1)) 
                    if l1 == []: 
                        print("No Bankruptcy Law cases") 
                elif choice == "I": 
                    l1 = [] 
                    while data: 
                        tempm = data.rstrip('\n') 
                        splittedone = tempm.split(',') 
                        if "Immigration Law" in splittedone: 
                            l1.append(splittedone) 
                        data = f5.readline() 
                    print(tabulate(l1)) 
                    if l1 == []: 
                        print("No Immigration Law cases") 
                elif choice == "T": 
                    l1 = [] 
                    while data: 
                        tempm = data.rstrip('\n') 
                        splittedone = tempm.split(',') 
                        if "Tax Law" in splittedone: 
                            l1.append(splittedone) 
                        data = f5.readline() 
                    print(tabulate(l1)) 
                    if l1 == []: 
                        print("No Tax Law cases") 
                f5.close() 
            elif ch3 == 23: 
                print("Returning to previous menu") 
                break 
            print() 
    elif ch == 4: 
        x = True 
        while x == True: 
            print("Register as a: \n1. New User\n2. New Lawyer/Intern\nTO RETURN TO MAIN MENU, ENTER 3") 
            ch4_1 = eval(input("Enter choice:")) 
            if ch4_1 == 1: 
                fullname = input("Enter full name: ") 
                l = fullname.split(' ') 
                t = tuple(l) 
                username = ''.join(t) 
                pwd = input("Enter password: ") 
                rpwd = input("Re-enter password: ") 
                if rpwd == pwd: 
                    print(l[0], "Welcome to Justice League Law Firm!") 
                    print("Your username is ", username, 'and your password is ', pwd) 
                    f = open("usernames.csv", "a") 
                    l = [username, pwd, "User"] 
                    w = csv.writer(f) 
                    w.writerow(l) 
                    f.close() 
                    break 
                else: 
                    print("Second entry doesn't match the first entry, please try again") 
                    break 
            elif ch4_1 == 2: 
                newlawyer() 
                pass 
            elif ch4_1 == 3:  # Exit
                print("Returning to main menu") 
                print() 
                break 
    elif ch == 90: 
        print() 
        print("ENDING THE PROGRAM!") 
        print() 
        print("THANK YOU FOR VISITING!") 
        print() 
        print("For more information, contact us at justiceleaguelawfirm11@outlook.com") 
        print() 
        break 
