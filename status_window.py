import tkinter as tk
from tkinter import Text, Button

def fill_values(initial_data, text_area, write_speed=0, read_speed=0, bytes_write=0, before_byte_stuffing="", after_byte_stuffing="", result_packet=""):
    text_area.config(state='normal')
    text_area.delete('1.0', tk.END)

    filled_values = [
        f"{write_speed} Baud",
        f"{read_speed} Baud",
        f"{bytes_write} Bytes",
        str(before_byte_stuffing),
        str(after_byte_stuffing),
        str(result_packet)
    ]

    # Обновляем значения в текстовом поле
    for i, value in enumerate(filled_values):
        line = initial_data[i].strip() + value + "\n"
        text_area.insert(tk.END, line)

    # Отключаем текстовое поле снова
    text_area.config(state='disabled')


def highlight_character(initial_data, text_area, line_index, char_index):
    text_area.config(state='normal')
    position = f"{line_index + 1}.{len(initial_data[line_index].strip()) + char_index}"
    text_area.tag_add("highlight", position, f"{position} + 1c")
    text_area.tag_config("highlight", foreground="red")
    text_area.config(state='disabled')

def highlight_line(initial_data, text_area, line_index):
    text_area.config(state='normal')
    position = f"{line_index + 1}.0"
    lineLen = len(text_area.get(f"{line_index + 1}.0", f"{line_index + 1}.0 lineend"))
    text_area.tag_add("highlight", position, f"{position} + {lineLen}c")
    text_area.tag_config("highlight", foreground="red")
    text_area.config(state='disabled')