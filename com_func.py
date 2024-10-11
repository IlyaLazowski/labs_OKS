import time
import serial
import serial.tools.list_ports
def data_transfer(com_port_sender, com_port_receiver, baudrate, message_to_send):
    print(com_port_sender)
    port_sender = com_port_sender
    port_receiver = com_port_receiver

    try:
        sender = serial.Serial(port_sender, baudrate, timeout=1)
        print(f'Порт {port_sender} открыт для отправки.')

        receiver = serial.Serial(port_receiver, baudrate, timeout=1)
        print(f'Порт {port_receiver} открыт для получения.')

        sender.write(message_to_send.encode('utf-8'))
        print(f'Отправлено: {message_to_send}')
        time.sleep(1)

        response = receiver.readline().decode('utf-8')
        if response:
            print(f'Ответ из {port_receiver}: {response}')
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


