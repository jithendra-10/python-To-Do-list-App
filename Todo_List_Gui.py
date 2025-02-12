import tkinter as tk
from tkinter import messagebox
def add_task():
    task = task_entry.get()
    if task.strip():
        tasks_listbox.insert(tk.END, task)
        save_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def remove_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        tasks_listbox.delete(selected_task)
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "No task selected!")
        
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                tasks_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = tasks_listbox.get(0, tk.END)
        file.writelines(task + "\n" for task in tasks)
root = tk.Tk()
root.title("To-Do List")
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=2, padx=10, pady=10)
tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
load_tasks()
root.mainloop()
