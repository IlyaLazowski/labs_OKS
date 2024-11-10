import random
def hamming_encode(data):

    if not all(bit in '01' for bit in data):
        raise ValueError("Data must be a binary string (only '0' and '1' characters are allowed).")

    m = len(data)
    r = 0

    while 2 ** r < m + r + 1:
        r += 1


    encoded = ['0'] * (m + r)
    j = 0
    for i in range(1, m + r + 1):
        if not (i & (i - 1)) == 0:
            encoded[i - 1] = data[j]
            j += 1



    print(encoded)
    for i in range(r):
        parity_index = 2 ** i - 1
        parity_value = 0
        involved_bits = []
        parity_formula = f"P{i + 1}({parity_index}, "

        for j in range(parity_index + 1, m + r + 1):
            if j & (parity_index + 1) == parity_index + 1:
                involved_bits.append(f"{encoded[j - 1]}(бит {j})")
                parity_value ^= int(encoded[j - 1])
                parity_formula += f"{j}, "

        encoded[parity_index] = str(parity_value)
        parity_formula = parity_formula[:-2] + f") = {' + '.join([bit.split('(бит')[0] for bit in involved_bits])} = {parity_value}\n"



        print(parity_formula)
    print(encoded)
    return ''.join(encoded)


def hamming_decode(data):

    m = len(data)
    r = 0
    while 2 ** r < m:
        r += 1


    parity_bits = [0] * r
    for i in range(r):
        parity_index = 2 ** i - 1
        for j in range(parity_index + 1, m + 1):
            if j & (parity_index + 1) == parity_index + 1:
                parity_bits[i] ^= int(data[j - 1])


    error_index = sum([bit * (2 ** i) for i, bit in enumerate(parity_bits)]) - 1

    if error_index >= 0:

        data = list(data)
        data[error_index] = '1' if data[error_index] == '0' else '0'
        data = ''.join(data)


    result_data = ''.join(data[i] for i in range(m) if not (i + 1 & i == 0))

    return result_data, error_index



import random

def distort_data(data):

    data = list(data)
    presence_of_error = "no error"
    position = "no"


    error_chance = random.random()


    if error_chance < 0.6:
        bit_to_flip = random.randint(0, len(data) - 1)
        data[bit_to_flip] = '1' if data[bit_to_flip] == '0' else '0'
        presence_of_error = "single error"
        position = str(bit_to_flip)


    elif error_chance < 0.85:  # 0.6 + 0.25 = 0.85
        if len(data) >= 2:
            bits_to_flip = random.sample(range(len(data)), 2)
            for bit in bits_to_flip:
                data[bit] = '1' if data[bit] == '0' else '0'
            presence_of_error = "double fault"
            position = str(bits_to_flip)


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

    if len(bits) % 8 != 0:
        raise ValueError("The length of the bit string must be a multiple of 8.")

    characters = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        character = chr(int(byte, 2))
        characters.append(character)

    return ''.join(characters)

print(bits_to_string(data3))