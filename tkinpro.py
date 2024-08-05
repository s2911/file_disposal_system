import mysql.connector as a
from datetime import datetime
import tkinter as tk
from tkinter import messagebox


con = a.connect(host="localhost",
                user="root",
                passwd="S@hil2911",
                database="fds")


def calculate_pending_days(incoming, outgoing):
    incoming_date = datetime.strptime(incoming, "%Y-%m-%d")
    outgoing_date = datetime.strptime(outgoing, "%Y-%m-%d")
    pending_days = (outgoing_date - incoming_date).days
    return pending_days


def submit_data():
    try:
        c = con.cursor()
        sql_insert = "INSERT INTO fdss (fileNo, subject, deptIn, deptOut, incoming, outgoing, pendingDays) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        fileNo = int(fileNo_entry.get())
        subject = subject_entry.get()
        deptIn = deptIn_entry.get()
        deptOut = deptOut_entry.get()
        incoming = incoming_entry.get()
        outgoing = outgoing_entry.get()
        pendingDays = calculate_pending_days(incoming, outgoing)
        c.execute(sql_insert, (fileNo, subject, deptIn, deptOut, incoming, outgoing, pendingDays))
        con.commit()
        messagebox.showinfo("Success", "Data entered successfully")
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        c.close()


def clear_entries():
    fileNo_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    deptIn_entry.delete(0, tk.END)
    deptOut_entry.delete(0, tk.END)
    incoming_entry.delete(0, tk.END)
    outgoing_entry.delete(0, tk.END)


def new_entry():
    clear_entries()


root = tk.Tk()
root.title("File Disposal System")


frame = tk.Frame(root)
frame.pack(padx=20, pady=20)


heading = tk.Label(frame, text="File Disposal System", font=("Helvetica", 18))
heading.grid(row=0, columnspan=2)


tk.Label(frame, text="File Number:").grid(row=1, column=0, sticky="e")
tk.Label(frame, text="Subject:").grid(row=2, column=0, sticky="e")
tk.Label(frame, text="Department In:").grid(row=3, column=0, sticky="e")
tk.Label(frame, text="Department Out:").grid(row=4, column=0, sticky="e")
tk.Label(frame, text="Incoming Date (YYYY-MM-DD):").grid(row=5, column=0, sticky="e")
tk.Label(frame, text="Outgoing Date (YYYY-MM-DD):").grid(row=6, column=0, sticky="e")

fileNo_entry = tk.Entry(frame)
subject_entry = tk.Entry(frame)
deptIn_entry = tk.Entry(frame)
deptOut_entry = tk.Entry(frame)
incoming_entry = tk.Entry(frame)
outgoing_entry = tk.Entry(frame)

fileNo_entry.grid(row=1, column=1)
subject_entry.grid(row=2, column=1)
deptIn_entry.grid(row=3, column=1)
deptOut_entry.grid(row=4, column=1)
incoming_entry.grid(row=5, column=1)
outgoing_entry.grid(row=6, column=1)


submit_button = tk.Button(frame, text="Submit", command=submit_data)
submit_button.grid(row=7, column=0, padx=(0, 5))


new_entry_button = tk.Button(frame, text="New Entry", command=new_entry)
new_entry_button.grid(row=7, column=1, padx=(5, 0))


root.mainloop()

con.close()
