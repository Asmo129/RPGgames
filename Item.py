class Weapon:
    def __init__(self, ID, Name, Type, Damage):
        self.ID = ID
        self.Name = Name
        self.Type = Type
        self.Damage = Damage

    def get_name(self):
        return self.Name

Baton = Weapon('STICK', 'Baton', 'SHORT', 1)