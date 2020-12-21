from datetime import date


class Student:
    def __init__(self, code: int, fio: str, birthdate: date, email: str, phone: str):
        self.code = code
        self.fio = fio
        self.birthdate = birthdate
        self.email = email
        self.phone = phone

    def __str__(self):
        template = 'Код: {} ФИО: {} Дата: {} Почта: {} Телефон: {}'
        return template.format(self.code, self.fio, self.birthdate, self.email, self.phone)
