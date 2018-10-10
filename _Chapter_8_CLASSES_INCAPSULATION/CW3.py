class Critter():
    """virtual pet"""
    def __init__(self, name):
        print('Born new critter')
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print('Name critter not may empty string')
        else:
            self.__name = new_name
            print('Name change.')
    def talk(self):
        print('\nHello, my name', self.name)

crit = Critter('Bobik')
crit.talk()

print('client code', crit.name)
print('change name')
crit.name = 'Murzik'
crit.name = ''