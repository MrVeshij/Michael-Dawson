# 3)Реализуйте ту же самую функциональность, что и в предыдущей задаче, иным способом: на этот раз сохраните
# список рекордов в обычном текстовом файле.



import sys
def open_file(file_name, mode):
    """Open file"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print('Impossible open the file', file_name, 'Programm done\n', e)
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return in format view next lin game file"""
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line

def next_block(the_file):
    """Return next block data from game file"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    cost = next_line(the_file)

    return category, question, answers, correct, explanation, cost

def welcome(title):
    """welcomes player and tell him theme of game"""
    print('\t\tWelcome to the game "Trivia"!\n')
    print('\t\t', title, '\n')

def initiate():
    user = input('Input your name.\n')
    return user

def data_save(record):
    f = open('data.txt', 'a')
    f.writelines(record)
    f.close()

def data_read():
    f = open('data.txt', 'r')
    print(f.read())
    f.close()


def main():
    trivia_file = open_file('trivia.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    user = initiate()
    score = 0
    category,question,answers,correct,explanation, cost = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print('\t', i + 1, '-',answers[i])
        answer = input('Your answer: \n')
        if answer == correct:
            print('\nYes!', end=" ")
            score += int(cost)
        else:
            print('\nNo.', end=" ")
            cost = 0
        print(explanation)
        print('Points for the question: ', cost, '\n\n')
        category, question, answers, correct, explanation, cost = next_block(trivia_file)

    trivia_file.close()
    print('That last question')
    print('An your score', score, 'points.')
    record = [user,' ', str(score),'\n']
    data_save(record)
    print('\n\n\nAll records:\n')
    data_read()

main()
input('Press enter for exit')