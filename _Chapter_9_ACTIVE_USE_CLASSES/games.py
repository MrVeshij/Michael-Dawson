class Player():
    """Player of game"""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ':\t' + str(self.score)
        return rep


def ask_yes_no(question):
    """Ask question with answer 'yes' or 'no' """
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Asks input number from certain range"""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print('You input not number.')
    return response

if __name__ == '__main__':
    print('You run that module, not import.')
    