def byte_stuffing(input_string):
    replacements = []
    result = ""
    length = len(input_string)

    start_index = 0

    while True:
        index = input_string.find('$u', start_index)
        if index == -1:
            break
        if index > 0:
            replacements.append(index)
            result += input_string[start_index:index] + 'r-'
        else:
            result += input_string[start_index:index + 2]

        start_index = index + 2

    result += input_string[start_index:]

    temp_result = ""

    for i in range(len(result)):
        if result[i] == 'r':
            if i + 1 < len(result) and result[i + 1] == '-':
                temp_result += 'r'  # Оставляем 'r' как есть
            else:
                temp_result += 'r+'
                replacements.append(len(temp_result) - 2)
        else:
            temp_result += result[i]

    print(result)

    return temp_result, replacements

def byte_on_stuffing(input_string):
    modified_string = input_string.replace('r-', '$u')
    modified_string = modified_string.replace('r+', 'r')
    return modified_string
