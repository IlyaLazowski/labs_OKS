import tkinter as tk
from tkinter import StringVar, OptionMenu, Text, scrolledtext
from work_func import com_func
from status_window import fill_values, highlight_character
from exeption.exeption_handling import exception_handling
from work_func.byte_stuffing import byte_stuffing
from work_func.hamming_code import hamming_encode, distort_data , hamming_decode ,bits_to_string
from work_func.com_func import Packet
from work_func.CSMA import receiving_the_package

def submission_processing():
    text_area2.delete("1.0", tk.END)
    user_input = text_area_one.get("1.0", tk.END).strip()
    if exception_handling(nameOfOptionMenuChoiseComPorts, nameOfOptionMenuChoiseSpeed, root):
        output_label_up_right.config(text=user_input)
        extracted_ports = nameOfOptionMenuChoiseComPorts.get().split(" и ")
        extracted_ports = [port.strip() for port in extracted_ports]

        baudrate = nameOfOptionMenuChoiseSpeed.get()  # Получаем скорость
        packet = Packet(20, extracted_ports[0], user_input)
        before_stuffing = packet.to_bytes()
        after_stuffing, replacements = byte_stuffing(before_stuffing)
        print(f"after = {after_stuffing}")

        bit_representation = ''.join(format(ord(c), '08b') for c in user_input)
        data = hamming_encode(bit_representation)
        data, presence_of_error, position = distort_data(data)
        data , error_position = hamming_decode(data)
        data = bits_to_string(data)

        response = com_func.data_transfer(extracted_ports[0], extracted_ports[1], baudrate, 20, data)

        bytes_write = len(response)

        fill_values(initial_data, text_area, baudrate, baudrate, bytes_write, before_stuffing, after_stuffing,
                    "", bit_representation, hamming_encode(bit_representation), presence_of_error, position)

        receiving_the_package(text_area2,tk)

        # Обновляем окно состояния
        fill_values(initial_data, text_area, baudrate, baudrate, bytes_write, before_stuffing, after_stuffing,
                    response, bit_representation, hamming_encode(bit_representation), presence_of_error, position)
        for i in range(len(replacements)):
            highlight_character(initial_data, text_area, 4, replacements[i])
            highlight_character(initial_data, text_area, 4, replacements[i] + 1)


initial_data = [
    "Write speed: ",
    "Read speed: ",
    "Bytes write: ",
    "Before byte-stuffing: ",
    "After byte-stuffing: ",
    "Bit representation: ",
    "Hamming code: ",
    "Presence of error: ",
    "Position error: ",
    "Result packet: "
]

root = tk.Tk()
status_window = tk.Toplevel(root)
status_window.title("Текстовое поле с параметрами")

text_window = tk.Toplevel(root)
text_window.title("Logger")

# Создаем текстовое поле с прокруткой
text_area2 = scrolledtext.ScrolledText(text_window, wrap=tk.WORD, width=40, height=10)
text_area2.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

text_area = Text(status_window, height=10, width=60, state='normal',wrap=tk.WORD)  # Включаем ввод
text_area.pack(padx=10, pady=10)

for item in initial_data:
    text_area.insert(tk.END, item + "\n")  # Вставляем изначальные данные

root.title("lab one")
root.geometry("1020x220")
text_area_one = tk.Text(root, width=40, height=10)
text_area_one.grid(row=1, column=0, padx=10, pady=10)

output_label_up_right = tk.Label(root, text="", width=40, height=10, anchor="nw", relief=tk.SUNKEN, justify="left",
                                 wraplength=275)
output_label_up_right.grid(row=1, column=2, padx=10, pady=10)

nameOfOptionMenuChoiseComPorts = StringVar(root)
nameOfOptionMenuChoiseComPorts.set("Выберите пару портов")
optionsOfChoiseComPorts = ["COM7 и COM10", "COM8 и COM9"]
optionMenuOfChoiseComPorts = OptionMenu(root, nameOfOptionMenuChoiseComPorts, *optionsOfChoiseComPorts)
optionMenuOfChoiseComPorts.grid(row=1, column=3, padx=10, pady=10, sticky="nw")

nameOfOptionMenuChoiseSpeed = StringVar(root)
nameOfOptionMenuChoiseSpeed.set("Выберите скорость")
optionsOfChoiseSpeed = ["4800", "9600", "14400", "19200"]
optionMenuOfChoiseSpeed = OptionMenu(root, nameOfOptionMenuChoiseSpeed, *optionsOfChoiseSpeed)
optionMenuOfChoiseSpeed.grid(row=1, column=4, padx=10, pady=10, sticky="nw")

submit_button = tk.Button(root, command=submission_processing, text="ОТПРАВИТЬ", width=15, height=3)
submit_button.grid(row=1, column=3, padx=20, pady=3, sticky="s", columnspan=2)

root.mainloop()
