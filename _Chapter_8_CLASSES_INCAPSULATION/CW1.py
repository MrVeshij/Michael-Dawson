class Critter():
    """Virtual pet"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        rep = "Object classes Critter\n"
        rep += 'name: ' + self.name + '\n'
        return rep
    def talk(self):
        print('Hello. My name ',self.name, '\n')

crit1 = Critter('Bobik')
crit2 = Critter('Pusik')

print(crit1)
print(crit2)

