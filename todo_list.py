import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []

        # Create a frame for better organization
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for listbox
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Entry for adding new tasks
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Buttons for actions
        self.create_button = tk.Button(root, text="Create Task", width=48, command=self.create_task)
        self.create_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", width=48, command=self.update_task)
        self.update_button.pack(pady=5)

        self.track_button = tk.Button(root, text="Track Task", width=48, command=self.track_task)
        self.track_button.pack(pady=5)

    def create_task(self):
        task = self.entry.get().strip()  # Get task description from entry
        if task:
            self.tasks.append({"description": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)  # Clear entry after adding task
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_description = self.entry.get().strip()
            if new_description:
                self.tasks[selected_task_index]['description'] = new_description
                self.update_task_list()
                self.entry.delete(0, tk.END)  # Clear entry after updating task
            else:
                messagebox.showwarning("Warning", "You must enter a new description.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def track_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]['completed'] = True
            self.update_task_list()
            messagebox.showinfo("Task Tracked", "Task has been successfully tracked.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to track.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Clear current tasks in listbox
        for task in self.tasks:
            status = "Tracked" if task['completed'] else "Not Tracked"
            self.task_listbox.insert(tk.END, f"{task['description']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

