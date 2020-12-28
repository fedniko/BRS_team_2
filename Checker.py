import re


def check_email(email):
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-z.]{2,6}$)", email):
        return True
    else:
        return False


def check_phone(phone):
    if re.match(r"(^(\+7)|8)\d{10}$", phone):
        return True
    else:
        return False
