class Birthday:
    def __init__(self, name, date):
        self.name = name
        self.date = date

class BirthdayManager:
    def __init__(self):
        self.birthdays = []

    def add_birthday(self, name, date):
        self.birthdays.append(Birthday(name, date))

    def edit_birthday(self, index, name, date):
        self.birthdays[index].name = name
        self.birthdays[index].date = date

    def delete_birthday(self, index):
        del self.birthdays[index]