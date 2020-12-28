from datetime import date
from Group import *

class Student:
    def __init__(self, code: int, fio: str, birthdate: date, email: str, phone: str, group: Group):
        self.code = code
        self.fio = fio
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.group = group

    def __str__(self):
        template = 'Код: {} ФИО: {} Дата: {} Почта: {} Телефон: {} Группа: {}'
        return template.format(self.code, self.fio, self.birthdate, self.email, self.phone, self.group.name)
