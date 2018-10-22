def test(number):
    guess_numb = number
    list_numb = [i for i in range(1, 102)]
    numb = max(list_numb) // 2
    count = 1

    while True:
        if guess_numb == numb:
            break
        elif guess_numb > numb:
            list_numb = list_numb[list_numb.index(numb):]
        elif guess_numb < numb:
            list_numb = list_numb[:list_numb.index(numb) + 1]
        numb = max(list_numb) - len(list_numb) // 2
        count += 1
    print('\nAttempts are {}. \nNumber guessed - {}'.format(count, guess_numb), '\n',numb == guess_numb)
    return count


result = []
for number in range(1,101):
    result.append(test(number))
    print('Number compare - {}'.format(number))
print(result, '\n', max(result))