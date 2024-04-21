from datetime import datetime, timedelta


def check_potential_congrats_date(date, now):
    congratulation_date = None
    # check if date is weekend and move it to next monday
    if date.weekday() > 4:
        date = date + timedelta(days=(7-date.weekday()))

    # check if date is in 7 days range from today
    if (0 <= (date-now).days < 7):
        congratulation_date = date

    return congratulation_date


def get_upcoming_birthdays(users: list):
    now_date = datetime.today().date()
    format = "%Y.%m.%d"
    res = []
    for user in users:
        name = user["name"]
        congratulation_date = None
        user_birth_date = datetime.strptime(
            user["birthday"], format).date()
        # use current and next years to check to cover cases when today is the end of the year
        for case in range(0,1):
            user_potential_congrat_date = user_birth_date.replace(
                year=(now_date.year+case))
            congratulation_date = check_potential_congrats_date(
                user_potential_congrat_date, now_date)
            if (congratulation_date):
                break

        if congratulation_date:
            res.append(
                {"name": name, 'congratulation_date': congratulation_date.strftime(format)})

    return res
