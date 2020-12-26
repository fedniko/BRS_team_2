class Group:
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year

    def __str__(self):
        template = 'Группа: {} Год: {}'
        return template.format(self.name, self.year)