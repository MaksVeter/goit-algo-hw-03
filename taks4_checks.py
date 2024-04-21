from taks4 import get_upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith1", "birthday": "1990.04.26"},
    {"name": "Jane Smith2", "birthday": "1990.01.01"},
    {"name": "Jane Smith3", "birthday": "1990.12.30"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
