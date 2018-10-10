#Realize 4 task with divide



human_number = int(input('Write number from 1 to 100'))
list_numb = [i for i in range(1,101)]


while True:
    guess_numb = len(list_numb) // 2
    if guess_numb == human_number:
        print('Victory!')
        break
    elif guess_numb > human_number:
        list_numb = list_numb[1: guess_numb]
    elif guess_numb < human_number:
        list_numb = list_numb[guess_numb:100]
        print('hey')
    print(guess_numb)