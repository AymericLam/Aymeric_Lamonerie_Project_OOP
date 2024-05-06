import tkinter as tk
from tkinter import simpledialog, messagebox
from birthday_manager import BirthdayManager
from reminder import ReminderFactory
from file_handler import FileHandler
from datetime import datetime

class BirthdayReminderApp:
    def __init__(self, root, filename):
        self.root = root
        self.root.title("Birthday Reminder")
        self.filename = filename
        self.birthday_manager = BirthdayManager()
        self.reminder_factory = ReminderFactory()
        self.file_handler = FileHandler()

        # Load birthdays from file
        self.load_birthdays()

        self.display_birthdays()
        self.create_widgets()

    def load_birthdays(self):
        data = self.file_handler.read_from_file(self.filename)
        for line in data:
            name, date = line.strip().split('-')
            self.birthday_manager.add_birthday(name.strip(), date.strip())

    def save_birthdays(self):
        data = [f"{birthday.name} - {birthday.date}" for birthday in self.birthday_manager.birthdays]
        self.file_handler.write_to_file(data, self.filename)

    def display_birthdays(self):
        # Affichage des anniversaires dans l'interface graphique
        self.birthday_listbox = tk.Listbox(self.root)
        self.birthday_listbox.pack()

        for birthday in self.birthday_manager.birthdays:
            self.birthday_listbox.insert(tk.END, f"{birthday.name} - {birthday.date}")

    def create_widgets(self):
        # Création des widgets pour l'ajout, l'édition et la suppression des anniversaires
        add_button = tk.Button(self.root, text="Add Birthday", command=self.add_birthday)
        add_button.pack(side=tk.LEFT)

        edit_button = tk.Button(self.root, text="Edit Birthday", command=self.edit_birthday)
        edit_button.pack(side=tk.LEFT)

        delete_button = tk.Button(self.root, text="Delete Birthday", command=self.delete_birthday)
        delete_button.pack(side=tk.LEFT)

        remind_button = tk.Button(self.root, text="Remind Birthdays", command=self.remind_birthdays)
        remind_button.pack(side=tk.LEFT)

        # Création du widget Listbox pour afficher les rappels d'anniversaire
        self.reminder_listbox = tk.Listbox(self.root)
        self.reminder_listbox.pack()

    def add_birthday(self):
        # Ajouter un anniversaire à la liste
        name = simpledialog.askstring("Add Birthday", "Enter name:")
        date = simpledialog.askstring("Add Birthday", "Enter date (MM/DD):")
        if name and date:
            self.birthday_manager.add_birthday(name, date)
            self.update_birthday_listbox()
            self.save_birthdays()

    def edit_birthday(self):
        # Modifier un anniversaire existant
        selected_index = self.birthday_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            birthday = self.birthday_manager.birthdays[selected_index]

            new_name = simpledialog.askstring("Edit Birthday", "Enter new name:", initialvalue=birthday.name)
            new_date = simpledialog.askstring("Edit Birthday", "Enter new date (MM/DD):", initialvalue=birthday.date)
            if new_name and new_date:
                self.birthday_manager.edit_birthday(selected_index, new_name, new_date)
                self.update_birthday_listbox()
                self.save_birthdays()

    def delete_birthday(self):
        # Supprimer un anniversaire de la liste
        selected_index = self.birthday_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            confirmed = messagebox.askokcancel("Delete Birthday", "Are you sure you want to delete this birthday?")
            if confirmed:
                self.birthday_manager.delete_birthday(selected_index)
                self.update_birthday_listbox()
                self.save_birthdays()

    def remind_birthdays(self):
        # Effacer d'abord toute ancienne liste de rappels d'anniversaire
        self.clear_reminder_list()

        # Get current date
        today = datetime.today()

        # Display reminders for birthdays happening today
        for birthday in self.birthday_manager.birthdays:
            b_date = datetime.strptime(birthday.date, "%m/%d")
            if b_date.month == today.month and b_date.day == today.day:
                reminder_text = f"Today is {birthday.name}'s birthday!"
                self.add_to_reminder_list(reminder_text)

    def clear_reminder_list(self):
        # Effacer la liste des rappels d'anniversaire précédents
        self.reminder_listbox.delete(0, tk.END)

    def add_to_reminder_list(self, reminder_text):
        # Ajouter un rappel d'anniversaire à la liste des rappels dans l'interface graphique
        self.reminder_listbox.insert(tk.END, reminder_text)

    def update_birthday_listbox(self):
        # Mettre à jour l'affichage de la liste des anniversaires
        self.birthday_listbox.delete(0, tk.END)
        for birthday in self.birthday_manager.birthdays:
            self.birthday_listbox.insert(tk.END, f"{birthday.name} - {birthday.date}")


if __name__ == "__main__":
    filename = "birthdays.txt"
    root = tk.Tk()
    app = BirthdayReminderApp(root, filename)
    root.mainloop()

