#  1)Напишите проrрамму, которая бы считала по просьбе пользователя. Надо позволить пользователю ввести
# начапо и конец счета, а также интервал между называемыми целыми числами.

# Псевдокод:
# Юзер вводит начало счета, конец и интервал
# Вроде бы циклом можно сделать, да в цикле

start = int(input('Input number for start'))
end = int(input('Input number for end'))
step = int(input('Input number for step'))
numb = 0

while numb != end:
    numb = numb + step
    print(numb)
