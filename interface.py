import tkinter as tk
from tkinter import StringVar, OptionMenu, Text, Button
import com_func
import status_window
from status_window import fill_values, highlight_character
from exeption_handling import exception_handling

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



def submission_processing():
    user_input = text_area_one.get("1.0", tk.END).strip()
    if exception_handling(nameOfOptionMenuChoiseComPorts, nameOfOptionMenuChoiseSpeed, root):
        output_label_up_right.config(text=user_input)
        extracted_ports = nameOfOptionMenuChoiseComPorts.get().split(" и ")
        extracted_ports = [port.strip() for port in extracted_ports]

        baudrate = nameOfOptionMenuChoiseSpeed.get()  # Получаем скорость
        response = com_func.data_transfer(extracted_ports[0], extracted_ports[1], baudrate, 20, user_input)

        before_stuffing = response
        after_stuffing , replacements = byte_stuffing(before_stuffing)

        bytes_write = len(response)

        # Обновляем окно состояния
        fill_values(initial_data, text_area,  baudrate, baudrate, bytes_write, before_stuffing, after_stuffing,
                    response)
        for i in range(len(replacements)):
            highlight_character(initial_data, text_area, 4, replacements[i])
            highlight_character(initial_data, text_area, 4, replacements[i] + 1)


initial_data = [
    "Write speed: ",
    "Read speed: ",
    "Bytes write: ",
    "Before byte-stuffing: ",
    "After byte-stuffing: ",
    "Result packet: "
]

root = tk.Tk()
status_window = tk.Toplevel(root)
status_window.title("Текстовое поле с параметрами")

text_area = Text(status_window, height=10, width=60, state='normal')  # Включаем ввод
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