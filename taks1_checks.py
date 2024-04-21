from datetime import datetime
from taks1 import get_days_from_today
### Checks
# Wrong inputs
print(get_days_from_today(1)) # return None, print description
print(get_days_from_today("")) # return None, print description
print(get_days_from_today({})) # return None, print description
print(get_days_from_today(())) # return None, print description
print(get_days_from_today("12311-01-01")) # return None, print description

# Future date
print(get_days_from_today("2034-01-01")) # return < 0
# Past date
print(get_days_from_today("2024-01-01")) # return > 0
# Today date
print(get_days_from_today(datetime.today().strftime("%Y-%m-%d"))) #return 0
