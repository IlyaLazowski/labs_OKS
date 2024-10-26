



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
    # Разбиваем строку на куски по 8 бит
    chars = [bits[i:i + 8] for i in range(0, len(bits), 8)]
    # Преобразуем каждый кусок в символ
    return ''.join(chr(int(char, 2)) for char in chars)

print(bits_to_string(data3))