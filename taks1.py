from datetime import datetime


def get_days_from_today(date: str):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
    except:
        print("Input date param has wrong format or type. Please use string like \"YYYY-MM-DD\".")
        return None

    now_date = datetime.today()
    return (now_date - input_date).days
