def custom_write(file_name, strings):
    num_of_str = 1
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        string_positions[(num_of_str, file.tell())] = i
        file.write(f'\n{i}')
        num_of_str += 1
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

