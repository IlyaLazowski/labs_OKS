import tkinter as tk


def show_error(message , root):
    error_window = tk.Toplevel(root)
    error_window.title("Ошибка")
    error_window.geometry("400x200")  # Устанавливаем размер окна (ширина x высота)

    error_label = tk.Label(error_window, text=message, padx=10, pady=10)
    error_label.pack(pady=(20, 10))  # Добавляем отступы сверху и снизу

    close_button = tk.Button(error_window, text="Закрыть", command=error_window.destroy)
    close_button.pack(pady=(10, 20))  # Отступы для кнопки


def exception_handling(nameOfOptionMenuChoiseComPorts ,nameOfOptionMenuChoiseSpeed,root ):

    if "Выберите пару портов" == nameOfOptionMenuChoiseComPorts.get():
        show_error("Не выбраны порты",root)
        return False

    if "Выберите скорость" == nameOfOptionMenuChoiseSpeed.get():
        show_error("Не выбрана скорость",root)
        return False

    return True