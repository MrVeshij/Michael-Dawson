#  2)Напишите проrрамму, которая принимала бы текст из попьзовательского ввода и печатала этот текст на экране
# наоборот.

# Псевдокод:
# Введенный юзером код пересобирается в новый список и выводится на экран
# В итоге решил задачу посредством срезов

text_user = input('Write something\n')
length_text = len(text_user)
reverse_text = text_user[length_text::-1]

print('Wow! Your text changed: {}'.format(reverse_text))