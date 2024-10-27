import random
def hamming_encode(data):
    # Ensure the data contains only '0' and '1' characters
    if not all(bit in '01' for bit in data):
        raise ValueError("Data must be a binary string (only '0' and '1' characters are allowed).")

    m = len(data)
    r = 0
    # Calculate the number of parity bits required
    while 2 ** r < m + r + 1:
        r += 1

    # Create an array for encoded data
    encoded = ['0'] * (m + r)
    j = 0
    for i in range(1, m + r + 1):
        if not (i & (i - 1)) == 0:  # Check if i is a power of 2
            encoded[i - 1] = data[j]
            j += 1

    # Clear the calculation text box before adding new data
    # parity_calc_text.delete(1.0, tk.END)

    # Fill in parity bits and display calculation steps
    print(encoded)
    for i in range(r):
        parity_index = 2 ** i - 1
        parity_value = 0
        involved_bits = []  # Bits involved in the check
        parity_formula = f"P{i + 1}({parity_index}, "

        for j in range(parity_index + 1, m + r + 1):
            if j & (parity_index + 1) == parity_index + 1:
                involved_bits.append(f"{encoded[j - 1]}(бит {j})")
                parity_value ^= int(encoded[j - 1])  # Convert to int safely
                parity_formula += f"{j}, "

        encoded[parity_index] = str(parity_value)
        parity_formula = parity_formula[:-2] + f") = {' + '.join([bit.split('(бит')[0] for bit in involved_bits])} = {parity_value}\n"

        # Display calculation steps for each parity bit

        print(parity_formula)
    print(encoded)
    return ''.join(encoded)


def hamming_decode(data):
    # Определяем длину данных и количество контрольных битов
    m = len(data)
    r = 0
    while 2 ** r < m:
        r += 1

    # Инициализируем массив для синдромов
    parity_bits = [0] * r
    for i in range(r):
        parity_index = 2 ** i - 1
        for j in range(parity_index + 1, m + 1):
            if j & (parity_index + 1) == parity_index + 1:
                parity_bits[i] ^= int(data[j - 1])

    # Вычисляем индекс ошибки на основе синдромов
    error_index = sum([bit * (2 ** i) for i, bit in enumerate(parity_bits)]) - 1

    if error_index >= 0:
        # Исправляем одиночную ошибку
        data = list(data)
        data[error_index] = '1' if data[error_index] == '0' else '0'
        data = ''.join(data)

    # Удаляем контрольные биты и возвращаем только данные
    result_data = ''.join(data[i] for i in range(m) if not (i + 1 & i == 0))  # Убираем контрольные биты

    return result_data, error_index



import random

def distort_data(data):
    # Преобразуем строку в список для изменения
    data = list(data)
    presence_of_error = "no error"
    position = "no"

    # Генерация случайного числа для определения типа ошибки
    error_chance = random.random()

    # Искажение одного бита с вероятностью 60%
    if error_chance < 0.6:
        bit_to_flip = random.randint(0, len(data) - 1)
        data[bit_to_flip] = '1' if data[bit_to_flip] == '0' else '0'
        presence_of_error = "single error"
        position = str(bit_to_flip)

    # Искажение двух бит с вероятностью 25%
    elif error_chance < 0.85:  # 0.6 + 0.25 = 0.85
        if len(data) >= 2:
            bits_to_flip = random.sample(range(len(data)), 2)
            for bit in bits_to_flip:
                data[bit] = '1' if data[bit] == '0' else '0'
            presence_of_error = "double fault"
            position = str(bits_to_flip)

    # Возвращаем обратно в строку
    return ''.join(data), presence_of_error, position




data2 = "100010010001"


data = "A"
if not all(c in '01' for c in data):
    data = ''.join(format(ord(c), '08b') for c in data)  # Convert characters to binary

print(data)
hamming_encode(data)

data3, error_i = hamming_decode(data2)
print(error_i)
print(data3)

def bits_to_string(bits):
    # Проверка на корректность входных данных
    if len(bits) % 8 != 0:
        raise ValueError("The length of the bit string must be a multiple of 8.")

    # Преобразование битов в символы
    characters = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]  # Получаем 8-битный байт
        character = chr(int(byte, 2))  # Преобразуем в символ
        characters.append(character)

    return ''.join(characters)

print(bits_to_string(data3))