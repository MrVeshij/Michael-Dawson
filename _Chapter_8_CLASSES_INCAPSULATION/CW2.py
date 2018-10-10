class Critter():
    """virtual pen"""
    total = 0
    @staticmethod
    def status():
        print('\nTotal pets now: ', Critter.total)
    def __init__(self, name):
        print('Born new pet!')
        self.name = name
        Critter.total += 1

print(Critter.total)
crit1 = Critter('pet1')
crit2 = Critter('pet2')
crit3 = Critter('pet3')
Critter.status()
print(crit1.total)

