import tkinter as tk
from tkinter import StringVar, OptionMenu , Text , Button
import com_func
import status_window
from status_window import fill_values , highlight_character , highlight_line # Импортируем функцию
from exception_handling import exception_handling

def submission_processing():
    user_input = text_area_one.get("1.0", tk.END).strip()
    if exception_handling(nameOfOptionMenuChoiseComPorts ,nameOfOptionMenuChoiseSpeed,root ) == True:
        extracted_ports = nameOfOptionMenuChoiseComPorts.get().split(" и ")
        extracted_ports = [port.strip() for port in extracted_ports]
        response = com_func.data_transfer(extracted_ports[0], extracted_ports[1],
                                          nameOfOptionMenuChoiseSpeed.get(),
                                          user_input)
        output_label_up_right.config(text=response)

initial_data = [
    "state: ",
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

text_area = Text(status_window, height=10, width=50, state='normal')  # Включаем ввод
text_area.pack(padx=10, pady=10)

for item in initial_data:
    text_area.insert(tk.END, item + "\n")  # Вставляем изначальные данные

text_area.config(state='disabled')
fill_button = Button(status_window, text="Заполнить параметры", command=lambda: fill_values(initial_data,text_area))
fill_button.pack(pady=10)

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

submit_button = tk.Button(root, command=submission_processing, text="ОТПРАВИТЬ",width=15, height=3)
submit_button.grid(row=1, column=3, padx=20, pady=3,sticky="s",columnspan=2)

root.mainloop()