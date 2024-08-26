import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Contacts dictionary to store contact information
        self.contacts = []

        # Labels and entry widgets for contact details
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Phone Number:").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(root, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for adding, updating, deleting, and searching contacts
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.grid(row=7, column=0, padx=10, pady=5)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=7, column=1, padx=10, pady=5)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(root, width=50, height=10)
        self.contact_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        # Populate initial contact list
        self.update_contact_list()

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone:
            contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contacts.append(contact)
            self.update_contact_list()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showwarning("Warning", "Name and Phone Number are required fields.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            name = self.name_entry.get().strip()
            phone = self.phone_entry.get().strip()
            email = self.email_entry.get().strip()
            address = self.address_entry.get().strip()

            if name and phone:
                self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
                self.update_contact_list()
                self.clear_entries()
                messagebox.showinfo("Success", "Contact updated successfully.")
            else:
                messagebox.showwarning("Warning", "Name and Phone Number are required fields.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.update_contact_list()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def search_contact(self):
        query = self.search_entry.get().strip().lower()
        if query:
            search_results = [contact for contact in self.contacts
                              if query in contact["name"].lower() or query in contact["phone"]]
            self.display_contacts(search_results)
        else:
            self.update_contact_list()

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def display_contacts(self, contacts):
        self.contact_listbox.delete(0, tk.END)
        for contact in contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
