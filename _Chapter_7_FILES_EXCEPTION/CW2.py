print('Create text file with method write()')
text_file = open('write_it.txt', 'w')

test_object = 'hello\nchicken, 1,2,3,4,5'
text_file.write(test_object)#'String 1\n')
text_file.write('That string 2\n')
text_file.write('Another string have number 3\n')
text_file.close()

print('\nRead new create file')
text_file = open('write_it.txt', 'r')
print(text_file.read())
text_file.close()

print('\nCreate text file with method writelines()')
text_file = open('write_it.txt', 'w')
lines = ['String 1', 'That string 2', 'Another string with number 3\n']
text_file.writelines(lines)
text_file.close()

print('\nRead again create file')
text_file = open('write_it.txt', 'r')
print(text_file.read())
text_file.close()

