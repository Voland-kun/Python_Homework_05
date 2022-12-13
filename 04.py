# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('input.txt', 'r') as data:
#     user_text = data.read()

def read_file(file):
    with open(str(file), 'r') as data:
        txt = data.read()
    return txt

#initial_test_txt = 'aaaaaFfffhhUUUUipdAAAAffffff'

def encodeRLE(txt):
    result_txt = ''
    sample = ''
    count = 1
    for i in txt:
        if i != sample:
            if sample:
                result_txt += f'{count}{sample}'
            sample = i
            count = 1
        else: count += 1
    result_txt += str(count) + sample
    return result_txt

# если в исходных данных были цифры работать не будет

def decodeRLE(txt):
    result_txt = ''
    k = ''
    for i in txt:
        if i.isdigit():
            k += i
        else:
            result_txt += i*int(k)
            k = ''
    return result_txt

def write_file(txt, file_name):
    with open(f'{file_name}', 'w') as file:
        file.write(txt)

encode_result = encodeRLE(read_file('initial_line.txt'))
write_file(encode_result, 'encode_result.txt')

decode_result = decodeRLE(read_file('encode_result.txt'))
write_file(decode_result, 'decode_result.txt')

if read_file('initial_line.txt') == read_file('decode_result.txt'):
    print('Повезло')
else: print('Не повезло')