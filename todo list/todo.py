import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.tasks = []

        # Title
        title_label = tk.Label(
            root, text="My To-Do List", font=("Helvetica", 18, "bold"),
            bg="#f0f0f0", pady=10
        )
        title_label.pack()

        # Entry frame
        entry_frame = tk.Frame(root, bg="#f0f0f0")
        entry_frame.pack(pady=10, padx=10, fill="x")

        self.task_entry = tk.Entry(entry_frame, font=("Helvetica", 12))
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=5)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        add_btn = tk.Button(
            entry_frame, text="Add", command=self.add_task,
            bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold")
        )
        add_btn.pack(side="left", padx=(5, 0))

        # Listbox frame
        list_frame = tk.Frame(root)
        list_frame.pack(pady=10, padx=10, fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox = tk.Listbox(
            list_frame, font=("Helvetica", 12), yscrollcommand=scrollbar.set,
            selectbackground="#a6a6a6", activestyle="none"
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.task_listbox.yview)

        self.task_listbox.bind("<Double-Button-1>", self.toggle_complete)

        # Buttons frame
        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        delete_btn = tk.Button(
            btn_frame, text="Delete Selected", command=self.delete_task,
            bg="#f44336", fg="white", font=("Helvetica", 10, "bold")
        )
        delete_btn.grid(row=0, column=0, padx=5)

        clear_btn = tk.Button(
            btn_frame, text="Clear All", command=self.clear_all,
            bg="#ff9800", fg="white", font=("Helvetica", 10, "bold")
        )
        clear_btn.grid(row=0, column=1, padx=5)

        # Hint label
        hint_label = tk.Label(
            root, text="Double-click a task to mark it complete/incomplete",
            font=("Helvetica", 9), bg="#f0f0f0", fg="gray"
        )
        hint_label.pack(pady=(0, 10))

        self.load_tasks()

        # Save tasks on close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Warning", "Please enter a task.")
            return
        self.tasks.append({"text": task_text, "done": False})
        self.task_entry.delete(0, tk.END)
        self.refresh_listbox()

    def toggle_complete(self, event):
        selection = self.task_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        self.refresh_listbox()

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showinfo("Info", "Select a task to delete.")
            return
        index = selection[0]
        del self.tasks[index]
        self.refresh_listbox()

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Delete all tasks?"):
            self.tasks = []
            self.refresh_listbox()

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["text"]
            if task["done"]:
                display_text = "✔ " + display_text
            self.task_listbox.insert(tk.END, display_text)
            if task["done"]:
                self.task_listbox.itemconfig(tk.END, fg="gray")

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            try:
                with open(FILE_NAME, "r") as f:
                    self.tasks = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.tasks = []
        self.refresh_listbox()

    def save_tasks(self):
        with open(FILE_NAME, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def on_close(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
