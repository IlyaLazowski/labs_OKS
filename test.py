def replace_u(input_string):
    # Проверяем, содержит ли строка '$u' и не находится ли он в начале
    if '$u' in input_string and not input_string.startswith('$u'):
        input_string = input_string.replace('$u', 'r-')

    return input_string


input_str2 = "$u should stay the same"
result2 = replace_u(input_str2)
print(result2)  # Ожидаемый вывод: $u should stay the same


def replace_r(input_string):
    if '$u' in input_string and not input_string.startswith('$u'):
        input_string = input_string.replace('$u', 'r-')

    result = ""
    length = len(input_string)

    for i in range(length):
        # Если текущий символ 'r' и следующий не '-', заменяем на 'r+'
        if input_string[i] == 'r':
            if i + 1 < length and input_string[i + 1] == '-':
                result += 'r'  # Оставляем 'r' как есть
            else:
                result += 'r+'  # Заменяем 'r' на 'r+'
        else:
            result += input_string[i]  # Добавляем текущий символ как есть

    return result


# Пример использования
input_str = "---Hello$uworld and r test"
result = replace_r(input_str)
print(result)  # Ожидаемый вывод: Hello r+ world and r- test


def replace_r_symbols(input_string):
    replacements = []  # Список для хранения индексов замен
    result = ""
    length = len(input_string)

    # Заменяем '$u' на 'r-', если он не в начале строки
    start_index = 0  # Начальный индекс для поиска

    while True:
        index = input_string.find('$u', start_index)  # Находим индекс '$u'
        if index == -1:  # Если больше нет вхождений, выходим из цикла
            break
        if index > 0:  # Если '$u' не в начале строки
            replacements.append(index)
            result += input_string[start_index:index] + 'r-'  # Добавляем текст до и заменяем '$u' на 'r-'
        else:
            result += input_string[start_index:index + 2]  # Добавляем '$u' без изменений, если в начале

        start_index = index + 2  # Продолжаем поиск после текущего '$u'

    result += input_string[start_index:]  # Добавляем оставшуюся часть строки

    # Теперь заменяем 'r' на 'r+' в оставшейся части результата
    temp_result = ""

    for i in range(len(result)):
        if result[i] == 'r':
            if i + 1 < len(result) and result[i + 1] == '-':
                temp_result += 'r'  # Оставляем 'r' как есть
            else:
                temp_result += 'r+'  # Заменяем 'r' на 'r+'
                replacements.append(len(temp_result) - 1)  # Сохраняем индекс замены
        else:
            temp_result += result[i]  # Добавляем текущий символ как есть

    # Подсветка замен

    return temp_result, replacements  # Возвращаем результат и индексы замен


# Пример использования
input_str = "$ullo$uwrldand r te"
result, indices = replace_r_symbols(input_str)
print("Результат:", result)  # Ожидаемый вывод: Hello r+ world and r- test
print("Индексы замен:", indices)  # Вывод индексов замен
