import random
import time


def channel_check(text_area,tk):
    while True:
        if random.random() < 0.5:
            text_area.insert(tk.END, "Канал свободен\n")
            break
        else:
            text_area.insert(tk.END, "Канал занят\n")
        # Генерируем случайную задержку от 0 до 500 мс
            sleep_time = random.uniform(0, 0.5)  # 0.5 секунд = 500 мс
            text_area.insert(tk.END, f"Задержка: {sleep_time:.3f} ms\n")
            time.sleep(sleep_time)  # Пауза


def sending_package(text_area,tk):
    channel_check(text_area,tk)
    text_area.insert(tk.END, "Отправка пакета\n")
    if random.random() < 0.4:
        text_area.insert(tk.END, "Коллизий не произошло, принимаем пакет\n")
        return True
    else:
        text_area.insert(tk.END, "Возникла коллизия!\n")
        return False


def receiving_the_package(text_area , tk):
    for i in range(10):
        if sending_package(text_area ,tk) == True:
            text_area.insert(tk.END, "Успешно получен\n")
            return True
        else:
            text_area.insert(tk.END, "Отправка jam-сигнала\n")
            text_area.insert(tk.END, f"{i+1} попытка повторной отправки кадра\n")
            sleep_time = random.uniform(0, 0.5)  # 0.5 секунд = 500 мс
            text_area.insert(tk.END, f"Задержка: {sleep_time:.3f} ms\n") # Ограничиваем до 3 знаков после запятой
            time.sleep(sleep_time)  # Пауза
    return False


