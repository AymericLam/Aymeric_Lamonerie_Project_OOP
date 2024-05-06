class Reminder:
    def __init__(self, birthday):
        self.birthday = birthday

    def remind(self):
        raise NotImplementedError("Subclasses must implement this method.")

class PopupReminder(Reminder):
    def remind(self):
        print(f"Popup reminder: It's {self.birthday.name}'s birthday today!")

class EmailReminder(Reminder):
    def remind(self):
        print(f"Email reminder: Don't forget to wish {self.birthday.name} a happy birthday!")

class ReminderFactory:
    def create_reminder(self, birthday):
        return PopupReminder(birthday)