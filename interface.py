import tkinter as tk
from tkinter import StringVar, OptionMenu
import com_func


def show_error(message):
    error_window = tk.Toplevel(root)
    error_window.title("Ошибка")
    error_window.geometry("400x200")  # Устанавливаем размер окна (ширина x высота)

    error_label = tk.Label(error_window, text=message, padx=10, pady=10)
    error_label.pack(pady=(20, 10))  # Добавляем отступы сверху и снизу

    close_button = tk.Button(error_window, text="Закрыть", command=error_window.destroy)
    close_button.pack(pady=(10, 20))  # Отступы для кнопки


def exception_handling():
    ports = [
        top_option_up_left.get(),
        top_option_up_right.get(),
        top_option_down_left.get(),
        top_option_down_right.get()
    ]

    if any("COM" not in port for port in ports):
        show_error("Не выбраны порты")
        return False

    if len(ports) != len(set(ports)):
        show_error("Выбраны одинаковые порты")
        return False

    if "Скорость" in speed_broadcast_two.get() or "Скорость" in speed_broadcast_one.get():
        show_error("Не выбраны скорости")
        return False

    return True


def on_submit_up():
    user_input = text_area_one.get("1.0", tk.END).strip()
    output_label_up_right.config(text=user_input)
    if exception_handling() == True:
        com_func.data_transfer(top_option_up_left.get(), top_option_up_right.get(), speed_broadcast_one.get(),
                               user_input)


def on_submit_down():
    user_input = text_area_two.get("1.0", tk.END).strip()
    output_label_bottom.config(text=user_input)
    if exception_handling() == True:
        com_func.data_transfer(top_option_down_right.get(), top_option_down_left.get(), speed_broadcast_one.get(),
                               user_input)


# Создание основного окна
root = tk.Tk()
root.title("lab one")

# Переменные для выпадающих меню
top_option_up_left = StringVar(root)
top_option_up_left.set("Выберите порт1")

top_option_up_right = StringVar(root)
top_option_up_right.set("Выберите порт2")

top_option_down_left = StringVar(root)
(top_option_down_left.set("Выберите порт3"))

top_option_down_right = StringVar(root)
top_option_down_right.set("Выберите порт4")

# Переменная для выбора скорости
speed_broadcast_one = StringVar(root)
speed_broadcast_one.set("Скорость1")

speed_broadcast_two = StringVar(root)
speed_broadcast_two.set("Скорость2")

# Создание верхнего выпадающего меню для ввода
top_option_menu = OptionMenu(root, top_option_up_left, *com_func.list_name_virtual_ports())
top_option_menu.grid(row=0, column=0, padx=5, pady=(10, 0))

speed_top_menu = OptionMenu(root, speed_broadcast_one, "4800", "9600", "14400", "19200")
speed_top_menu.grid(row=0, column=1, padx=10, pady=(10, 0))

# Создание верхнего текстового поля для ввода
text_area_one = tk.Text(root, width=40, height=10)
text_area_one.grid(row=1, column=0, padx=10, pady=10)

# Создание кнопки "Отправить" для верхнего поля9
submit_button_top = tk.Button(root, text="Отправить", command=on_submit_up)
submit_button_top.grid(row=1, column=1, padx=10)

# Создание выпадающего меню для поля вывода сверху
output_top_options = ["Результат 1", "Результат 2", "Результат 3"]
output_top_option_menu = OptionMenu(root, top_option_up_right, *com_func.list_name_virtual_ports())
output_top_option_menu.grid(row=0, column=2, padx=10, pady=(10, 0))

# Создание поля для вывода информации сверху
output_label_up_right = tk.Label(root, text="", width=40, height=10, anchor="nw", relief=tk.SUNKEN, justify="left",
                                 wraplength=275)
output_label_up_right.grid(row=1, column=2, padx=10, pady=10)

# Создание выпадающего меню для нижнего текстового поля
bottom_option_menu = OptionMenu(root, top_option_down_left, *com_func.list_name_virtual_ports())
bottom_option_menu.grid(row=2, column=0, padx=10, pady=(10, 0))

# Выпадающее меню для скорости снизу
speed_bottom_menu = OptionMenu(root, speed_broadcast_two, "4800", "9600", "14400", "19200")
speed_bottom_menu.grid(row=2, column=1, padx=10, pady=(10, 0))

# Создание поля для вывода информации снизу
output_label_bottom = tk.Label(root, text="", width=40, height=10, anchor="nw", relief=tk.SUNKEN, justify="left",
                               wraplength=275)
output_label_bottom.grid(row=3, column=0, padx=10, pady=10)

# Создание текстового поля для ввода снизу
text_area_two = tk.Text(root, width=40, height=10)
text_area_two.grid(row=3, column=2, padx=10, pady=10)

# Создание выпадающего меню для нижнего текстового поля
input_bottom_option_menu = OptionMenu(root, top_option_down_right, *com_func.list_name_virtual_ports())
input_bottom_option_menu.grid(row=2, column=2, padx=10, pady=(10, 0))

# Создание кнопки "Отправить" для нижнего поля
submit_button_bottom = tk.Button(root, text="Отправить", command=on_submit_down)
submit_button_bottom.grid(row=3, column=1, padx=10)



label_title = tk.Label(root, text="Состояние пакета:", font=("Arial", 12))
label_title.grid(row=3, column=1, padx=10, pady=(200, 0))

output_label_for_state_package = tk.Label(root, text="", width=40, height=10, anchor="nw", relief=tk.SUNKEN, justify="left",
                                 wraplength=275)
output_label_for_state_package.grid(row=4, column=1, padx=10, pady=10)


# Запуск основного цикла приложения

root.mainloop()
