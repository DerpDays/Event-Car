from datetime import date
import re

def check_email(email) -> bool:
    return bool(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))

def check_password(password) -> bool:
    return bool(re.fullmatch(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$', password))

def check_birthday(age) -> bool:
    yrs = date.today().years - age.years