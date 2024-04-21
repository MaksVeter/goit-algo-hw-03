import re

def normalize_phone(phone_number: str):
    phone_number = re.sub(r"\D", "", phone_number)
    if (phone_number.startswith("380") and len(phone_number)==12):
        phone_number = "+"+phone_number
    else:
        phone_number = "+38"+phone_number
    print(phone_number)
    pass
