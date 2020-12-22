class Subject:
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    def __str__(self):
        template = 'Код: {} Предмет: {}'
        return template.format(self.code, self.name)