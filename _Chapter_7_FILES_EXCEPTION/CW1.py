print('open and close file')
text_file = open('read_it.txt','r',encoding='utf-8')
text_file.close()

print('\nRead file by symbole')
text_file = open('read_it.txt','r')
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print('\nRead file wholly')
text_file = open('read_it.txt','r')
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print('\nRead one string by symbole')
text_file = open('read_it.txt','r')
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print('\nRead one string wholly')
text_file = open('read_it.txt', 'r')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print('\nRead wholly file in list')
text_file = open('read_it.txt', 'r')
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print('\nCombined file line by line')
text_file = open('C:/users/veshi/desktop/read_it.txt', 'r')
for line in text_file:
    print(line)
text_file.close()


