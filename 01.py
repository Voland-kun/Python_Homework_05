#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#user_text = 'Напишите программу програбвмму, удаляющую из текстабв текста все слова словабв, содержащие ""абв"".'

def read_file(file):
    with open(str(file), 'r', encoding='utf-8') as data:
        txt = data.read()
    return txt

def delete_words_a(s): #если "слово" это слово
    punctuation = '.,!?:;'
    for i in punctuation:
        s = s.replace(i, f' {i}')
    s = list(filter(lambda s: 'абв' not in s, s.split()))
    s = ' '.join(s)
    for i in punctuation:
        s = s.replace(f' {i}', i)
    return s

def delete_words_b(s): #если "слово" это часть строки отделённая пробелами
    s = list(filter(lambda s: 'абв' not in s, s.split()))
    s = ' '.join(s)
    return s    

def write_file(txt, file_name):
    with open(f'{file_name}', 'w', encoding='utf-8') as file:
        file.write(txt)

user_text = read_file('abv_in.txt')
print(user_text)

result_a = delete_words_a(user_text)
result_b = delete_words_b(user_text)
print(result_a)
print(result_b)
write_file(result_a, 'abv_result_a.txt')
write_file(result_a, 'abv_result_b.txt')