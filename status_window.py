import tkinter as tk
from tkinter import Text, Button
import time

def fill_values(initial_data,text_area ,state=0, write_speed=0, read_speed=0, bytes_write=0, before_byte_stuffing="", after_byte_staffinf="", result_packet=""):
    text_area.config(state='normal')
    text_area.delete('1.0', tk.END)

    filled_values = [
        "Running",
        "1000 MB/s",
        "800 MB/s",
        "2048 Bytes",
        "1500 Bytes",
        "1450 Bytes",
        "Success"
    ]

    # Обновляем значения в текстовом поле
    for i, value in enumerate(filled_values):
        line = initial_data[i].strip() + value + "\n"
        text_area.insert(tk.END, line)  # Вставляем новую строку

    # Отключаем текстовое поле снова
    text_area.config(state='disabled')  # Отключаем ввод


def highlight_character(initial_data,text_area , line_index, char_index):
    # Включаем текстовое поле для редактирования
    text_area.config(state='normal')  # Включаем ввод

    # Вычисляем позицию: добавляем 1 к line_index (строки начинаются с 1) и 10 к char_index (смещение после двоеточия)
    position = f"{line_index + 1}.{len(initial_data[line_index].strip()) + char_index}"

    # Добавляем тег для раскрашивания
    text_area.tag_add("highlight", position, f"{position} + 1c")  # +1c - один символ вправо
    text_area.tag_config("highlight", foreground="red")  # Настраиваем цвет

    # Отключаем текстовое поле снова
    text_area.config(state='disabled')  # Отключаем ввод


def highlight_line(initial_data,text_area, line_index):
    # Включаем текстовое поле для редактирования
    text_area.config(state='normal')  # Включаем ввод

    # Вычисляем позицию: добавляем 1 к line_index (строки начинаются с 1)
    position = f"{line_index + 1}.0"

    # Получаем длину строки
    lineLen = len(text_area.get(f"{line_index + 1}.0", f"{line_index + 1}.0 lineend"))

    # Добавляем тег для раскрашивания
    text_area.tag_add("highlight", position, f"{position} + {lineLen}c")  # Указываем длину линии
    text_area.tag_config("highlight", foreground="red")  # Настраиваем цвет

    # Отключаем текстовое поле снова
    text_area.config(state='disabled')  # Отключаем ввод


