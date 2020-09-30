import tkinter as tk
from tkinter import messagebox as tsmg
from tkinter import ttk
import sqlite3

if __name__ == '__main__':

# ADDING DATA TO DATABASE
    def addstudent():
        if ID.get() == "" or studentnameentry.get() == "" or branchentry.get() == "" or yearentry.get() == "" or courseentry.get() == "" or phoneentry.get() == "":
            tsmg.showinfo("Invalid", "Invalid Details")
        else:
            con = sqlite3.connect("management.db")
            cur = con.cursor()
            params = (ID.get(), studentnameentry.get(), branchentry.get(), yearentry.get(), courseentry.get(), phoneentry.get())
            cur.execute("INSERT INTO COACHING (ID, NAME, BRANCH, YEAR, COURSE, PHONE) VALUES(?,?,?,?,?,?)", params)
            con.commit()
            con.close()
            tsmg.showinfo("student added", "student data saved successfully")

# clear data
    def clear():
        IDvalue.set(0)
        studentnamevalue.set("")
        branchvalue.set("")
        yearvalue.set("")
        coursevalue.set("")
        phonevalue.set("")

# EXIT APP
    def Quit():
        op = tsmg.askyesno("EXIT", "Do you want to Exit ?")
        if op > 0 :
            window.destroy()

# DATA WINDOW
    def viewstudents():
        # DELETING DATA
        def deletestudent():
            con = sqlite3.connect("management.db")
            cur = con.cursor()
            for selected_item in tree.selection():
                print(selected_item)  # it prints the selected row id
                cur.execute("DELETE FROM COACHING WHERE id=?", (tree.set(selected_item, '#1'),))
                con.commit()
                tree.delete(selected_item)
            con.close()
            tsmg.showinfo("Deleted", "Data Deleted Successfully")

        def search():
            query = search_entry.get()
            selections = []
            for child in tree.get_children():
                if query in tree.item(child)['values']:  # compare strings in  lower cases.
                    print(tree.item(child)['values'])
                    selections.append(child)
            print('search completed')
            tree.selection_set(selections)

        win = tk.Toplevel()
        win.geometry("1200x420")
        win.minsize(1200, 400)
        win.maxsize(1200, 400)
        scrollx = tk.Scrollbar(win, orient="horizontal")
        scrolly = tk.Scrollbar(win, orient="vertical")
        tree = ttk.Treeview(win, columns=('ID', 'Name', 'Branch', 'Year', 'Course', 'Phone'), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side="bottom", fill="x")
        scrolly.pack(side="right", fill="y")
        scrollx.config(command=tree.xview)
        scrolly.config(command=tree.yview)

        f = tk.Frame(win)
        searchvalue = tk.StringVar()
        search_entry = tk.Entry(f, textvariable=searchvalue, font="lucida 10 bold")
        b = tk.Button(f, text="Search", command=search)
        b.pack(side='right', padx=15, pady=5)
        search_entry.pack(side='right', padx=10, pady=5)
        f.pack(anchor='ne')

        tree["columns"] = ("one", "two", "three", "four", "five","six")
        tree.column("one", stretch=tk.NO)
        tree.column("two", stretch=tk.NO)
        tree.column("three", stretch=tk.NO)
        tree.column("four", stretch=tk.NO)
        tree.column("five", stretch=tk.NO)
        tree.column("six", stretch=tk.NO)

        tree.heading("one", text="ID")
        tree.heading("two", text="name")
        tree.heading("three", text="branch")
        tree.heading("four", text="year")
        tree.heading("five", text="course")
        tree.heading("six", text="phone")
        tree['show'] = 'headings'
        tree.pack()

        b = tk.Button(win, text="delete", command=deletestudent)
        b.pack(padx=20, pady=10)

        con = sqlite3.connect("management.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM COACHING")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", tk.END, value=row)
        con.commit()
        con.close()

# MAIN WINDOW
    window = tk.Tk()
    window.title("student management system")
    window.minsize(500, 480)
    window.maxsize(500, 480)
    window.geometry("500x550")
    heading = tk.Label(window, text="Student Management System", font="lucida 20 bold")
    heading.pack()

# DATABASE
    con = sqlite3.connect("management.db")
    con.execute("CREATE TABLE IF NOT EXISTS COACHING(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, BRANCH TEXT NOT NULL, YEAR TEXT, COURSE TEXT, PHONE TEXT)")
    con.commit()
    con.close()

# LABELS AND ENTRIES

    IDvalue = tk.IntVar()
    studentnamevalue = tk.StringVar()
    branchvalue = tk.StringVar()
    yearvalue = tk.StringVar()
    coursevalue = tk.StringVar()
    phonevalue = tk.StringVar()

    f = tk.Frame(window)

    IDname = tk.Label(f, text="student's ID")
    IDname.pack(side=tk.LEFT, anchor="nw", padx="18", pady="10")
    ID = tk.Entry(f, textvariable=IDvalue)
    ID.pack(side=tk.RIGHT, anchor="ne", pady="11")
    f.pack()

    f = tk.Frame(window)
    studentname = tk.Label(f, text="student's name")
    studentname.pack(side=tk.LEFT, anchor="nw", padx="10", pady="10")
    studentnameentry = tk.Entry(f, textvariable=studentnamevalue)
    studentnameentry.pack(side=tk.RIGHT, anchor="ne", pady="11")
    f.pack()

    f = tk.Frame(window)
    branch = tk.Label(f, text="Branch")
    branch.pack(side=tk.LEFT, anchor="nw", padx="32", pady="10")
    branchentry = tk.Entry(f, textvariable=branchvalue)
    branchentry.pack(side=tk.RIGHT, anchor="ne", pady="11")
    f.pack()

    f = tk.Frame(window)
    year = tk.Label(f, text="year of college")
    year.pack(side=tk.LEFT, anchor="nw", padx="13", pady="10")
    yearentry = tk.Entry(f, textvariable=yearvalue)
    yearentry.pack(side=tk.RIGHT, anchor="ne", padx="5", pady="11")
    f.pack()

    f = tk.Frame(window)
    course = tk.Label(f, text="Course")
    course.pack(side=tk.LEFT, anchor="nw", padx="33", pady="10")
    courseentry = tk.Entry(f, textvariable=coursevalue)
    courseentry.pack(side=tk.RIGHT, anchor="ne", padx="10", pady="11")
    f.pack()

    f = tk.Frame(window)
    phone = tk.Label(f, text="Phone no.")
    phone.pack(side=tk.LEFT, anchor="nw", padx="25", pady="10")
    phoneentry = tk.Entry(f, textvariable=phonevalue)
    phoneentry.pack(side=tk.RIGHT, anchor="ne", padx="10", pady="11")
    f.pack()

# BUTTONS
    f1 = tk.Frame(window)
    Addstudent = tk.Button(f1, text="Add Student", command=addstudent,pady=5)
    Addstudent.pack(pady=20)
    clear = tk.Button(f1, text="Clear", command=clear, padx=10, pady=2)
    clear.pack()
    f1.pack(fill=tk.X, pady=2)

    f2 = tk.Frame(window)
    b1 = tk.Button(f2, text="View all Students", command=viewstudents, padx=5)
    b2 = tk.Button(f2, text="Exit",command=Quit)
    b1.pack(fill=tk.X)
    b2.pack(fill=tk.X)
    f2.pack(fill=tk.X, pady=20)

    window.mainloop()