import time
import serial
import serial.tools.list_ports


class Packet:
    def __init__(self, group_number, com_port, message):
        self.group_number = group_number
        self.com_port = com_port
        n = self.group_number
        self.flag = f"${chr(97 + n)}"  # '$' + 'a' + n (где 'a' - это 97 в ASCII)
        self.destination_address = 0
        self.source_address = str(self.com_port)
        if len(message) > n:
            self.data = message[:n]  # Обрезаем сообщение до длины group_number
        else:
            self.data = message
        self.fcs = 0

    def to_bytes(self):
        return (self.flag +
                str(self.destination_address) +
                self.source_address +
                self.data +
                str(self.fcs))


def data_transfer(com_port_sender, com_port_receiver, baudrate, group_number, message_to_send):
    print(com_port_sender)
    port_sender = com_port_sender
    port_receiver = com_port_receiver

    try:
        sender = serial.Serial(port_sender, baudrate, timeout=1)
        print(f'Порт {port_sender} открыт для отправки.')

        receiver = serial.Serial(port_receiver, baudrate, timeout=1)
        print(f'Порт {port_receiver} открыт для получения.')

        # Создаем пакет
        packet = Packet(group_number, com_port_sender, message_to_send)
        message_bytes = packet.to_bytes().encode('utf-8')  # Получаем байтовое представление пакета

        # Отправляем сообщение
        sender.write(message_bytes)
        print(f'Отправлено: {message_bytes}')
        time.sleep(1)

        response = receiver.readline()  # Читаем ответ
        if response:
            response_decoded = response.decode('utf-8')
            print(f'Ответ из {port_receiver}: {response_decoded}')
            response = response_decoded
        else:
            print('Ответ не получен.')

    except serial.SerialException as e:
        print(f'Ошибка: {e}')
        response = None  # Обработка случая, когда возникла ошибка
    finally:
        sender.close()
        print(f'Порт {port_sender} закрыт.')
        receiver.close()
        print(f'Порт {port_receiver} закрыт.')

    return response


def list_virtual_ports():
    ports = serial.tools.list_ports.comports()
    virtual_ports = []
    for port in ports:
        if "Software" in port.description:
            virtual_ports.append(port.device)
    return virtual_ports


def list_name_virtual_ports():
    virtual_ports2 = []
    virtual_ports = list_virtual_ports()
    if virtual_ports:
        virtual_ports2.extend(virtual_ports)
    return virtual_ports2