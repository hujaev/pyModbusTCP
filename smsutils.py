#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Набор вспомогательных функций для работы с SMS
#
# большое спасибо:
#     http://www.varesano.net/blog/fabio/serial%20rs232%20connections%20python
#     http://www.dreamfabric.com/sms/

import serial, datetime, time, random


# Преобразование номера телефона в международном формате в формат SMS
#
# Исходная строка, содержащая телефон в международном формате 79130123456,
# дополняется справа символом F                                                            - 79130123456F,
# разбивается на пары символов                                                             - 79 13 01 23 45 6F,
# в каждой паре символы меняются местами                                                   - 97 31 10 32 54 F6,
# слева приписывается идентификатор международного формата (91)                            - 91 97 31 10 32 54 F6,
# слева приписывается количество цифр в телефоне, т.е. 11 в шестнадцатеричном формате (0B) - 0B 91 97 31 10 32 54 F6
#
# Возвращаемое значение - строка, содержащая закодированный номер телефона 0B919731103254F6
#
def PhoneNumberToSMS(number):
    number += 'F'
    result = '0B' + '91'
    i = 0
    while i < len(number):
        result += number[i+1] + number[i]
        i += 2
    return result


# Преобразование строки символов в формат SMS
#
# Каждый двухбайтовый юникодный символ в строке разбивается на пару байт,
# и формируется новая строка, состоящая из шестнадцатеричных представлений этих байтов
#
# Возвращаемое значение - строка, содержащая строку символов в формате SMS
#
def TextToSMS(text):
    b = text
    result = ''
    i = 0
    while i < len(b):
        o = ord(b[i])
        result += ("%0.2X" % (o/256)) + ("%0.2X" % (o%256))
        i += 1
    return result


# Восстановление номера телефона в международном формате в из формата SMS
#
# Исходная строка, содержащая закодированный телефон 9731103254F6
# разбивается на пары символов           - 97 31 10 32 54 F6,
# в каждой паре символы меняются местами - 79 13 01 23 46 6F,
# убирается символ F                     - 79130123456
#
# Возвращаемое значение - строка, содержащая номер телефона 79130123456
#
def SMSToPhoneNumber(data):
    result = ""
    i = 0
    while i < len(data):
        result += data[i+1] + data[i]
        i += 2
    return result[:-1]


# Восстановление строки символов в из формата SMS
#
# Исходная строка разбивается на четверки символов, которые преобразуются в целые числа
# и формируется строка, состоящая из соответствующих этим числам символов
#
# Возвращаемое значение - раскодированная строка
#
def SMSToText(text):
    result = u''
    i = 0
    while i+3 < len(text):
        result += unichr(int(text[i] + text[i+1] + text[i+2] + text[i+3],16))
        i += 4
    return result


# преобразование целого числа в строку из нулей и единиц, соответствующую его двоичной записи
# (использовалось для отладки)
def ByteToBitsString(byte, n):
    result = ''
    for i in range(0,n):
        if byte & (1 << i) != 0:
            result = '1' + result
        else:
            result = '0' + result
    return result


# Восстановление строки из её семибитного кода
#
# На вход подается закодированная строка  - 4DEA10
# эта строка разбивается на пары символов - 4D EA 10,
# каждая пара трактуется как шестнадцатиричное представление байта - 0x4D 0xEA 0x10 = 01001101 11101010 00010000
# из первого байта 01001101 берутся семь младших битов 1001101 и преобразуются в соответствующий символ ASCII - M
# оставшийся бит 0 дополняется слева шестью младшими битами второго байта 101010: 1010100 - T
# оставшиеся два бита 11 дополняются слева пятью младшими битами третьего байта 10000: 1000011 - С
# и т.д.
#
# Возвращаемое значение - раскодированная строка MTC
#
def Decode7bit(text):
    result = ''

    bytes = [int(text[i*2:i*2+2],16) for i in range(0,len(text)/2)]

    symbol = 0
    bits   = 0
    n      = 0

    while n < len(bytes):

        if bits == 7:
            result += chr(symbol)
            symbol = 0
            bits   = 0
        else:
            symbol += (bytes[n] & (0x7F >> bits)) << bits
            result += chr(symbol)
            symbol = (bytes[n] & (0x7F << (7-bits))) >> (7-bits)
            bits   = (8-7) + bits
            n += 1

    if bits > 0 and symbol != 0:
        result += chr(symbol)

    return result


# Класс для работы с часовыми поясами (см следующую функцию)
class smsTZ(datetime.tzinfo):
    hours = 0
    def __init__(self, h):
        self.hours = h
    def utcoffset(self, dt):
        return datetime.timedelta(hours=self.hours)
    def dst(self, dt):
        return datetime.timedelta(0)

# Восстановление даты и времени из их представления SMS
#
# На вход подается закодированная строка  - 11113131516461
# эта строка разбивается на пары символов - 11 11 31 31 51 64 61,
# в каждой паре символы меняются местами  - 11 11 13 13 15 46 16,
# получившиеся строки трактуются как шестнадцатиричные представления байтов - 0x11 0x11 0x13 0x13 0x15 0x46 0x16
# эти байты представляют собой соответственно год, месяц, день, часы, минуты, секунды, часовой пояс
# часовой пояс представляется как количество четвертей часа, т.е. 0x16 = GMT+4 (седьмой бит отвечает за знак)
#
# Возвращаемое значение - дата и время 2011-11-13 13:15:46+04:00
#
def SMSToTimeStamp(text):
    year   = int(text[1] + text[0]) + 2000
    month  = int(text[3] + text[2])
    day    = int(text[5] + text[4])
    hour   = int(text[7] + text[6])
    minute = int(text[9] + text[8])
    second = int(text[11] + text[10])
    tz     = int(text[13] + text[12])
    tz = ( (tz & 0x7F) if (tz & 0x80 == 0) else -(tz & 0x7F) ) / 4
    return datetime.datetime(year, month, day, hour, minute, second, 0, smsTZ(tz))


# Обмен с последовательным портом
def str_send (ser, textline):
    ser.write(textline)

    out = ''
    # let's wait one second before reading output (let's give device time to answer)
    N = 10
    while N > 0:
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if ('OK' in out) or ('ERROR' in out) or ('>' in out):
            N = 1

        N -= 1

    return out


# отправка пин-кода в открытый порт
def SendPINToPort(ser, pin):
    str_send(ser, 'AT+CPIN="%s"\r' % (pin))


# отправка пин-кода модему
def SendPIN(serial_name, pin):

    # подключаемся к порту
    ser = serial.Serial(serial_name, 115200, timeout=1)
    ser.open()

    # отправляем пин-код
    SendPINToPort(ser, pin)

    # закрываем порт
    ser.close()


# отправка SMS-сообщения
def SendSMS(msg, phone, serial_name, pin=None):

    # если нечего или некуда отправлять, выходим
    if msg == '' or len(phone) != 11:
        return

    # декодируем сообщение в utf-8
    message = msg.decode('utf-8')

    # разрезаем сообщение на кусочки по 66 символов
    chunks = []
    if len(message) > 70:
        while len(message) > 66:
            chunks.append(message[:66])
            message = message[66:]
    if len(message) > 0:
        chunks.append(message)

    # инициализируем служебную информацию
    SMS_SUBMIT_PDU = "11"
    CSMS_reference_number = ""

    # если сообщение требует конкатенации SMS, то подправляем служебную информацию
    # и генерируем четырехсимвольный номер сообщения
    if len(chunks) > 1:
        SMS_SUBMIT_PDU = "51"
        CSMS_reference_number = "%0.4X" % random.randrange(1,65536)

    # подключаемся к порту
    ser = serial.Serial(serial_name, 115200, timeout=1)
    ser.open()

    # устанавливаем формат передачи сообщения - PDU
    status = str_send(ser, 'AT+CMGF=0\r')

    # если в ответ пришел текст, содержащий SIM PIN REQUIRED, значит, модему нужен пин-код
    if 'SIM PIN' in status:
        SendPINToPort(ser, pin)
        str_send(ser, 'AT+CMGF=0\r')


    # отсылаем сообщение по кусочкам
    i = 1
    for chunk in chunks:

        # кодируем кусочек
        emessage = TextToSMS(chunk)

        # если сообщение состоит из нескольких кусочков, то в каждом кусочке надо указать
        # номер сообщения, количество кусочков и порядковый номер кусочка (1,2,3 и т.д.)
        if CSMS_reference_number != "":
            emessage = "06" + "08" + "04" + CSMS_reference_number + \
            ("%0.2X" % len(chunks)) + ("%0.2X" % i) + emessage

        # готовим строку для отправки в порт
        sms =                             \
            "00" +                        \
            SMS_SUBMIT_PDU +              \
            "00" +                        \
            PhoneNumberToSMS(phone) +     \
            "00" +                        \
            "08" +                        \
            "AA" +                        \
            "%0.2X" % (len(emessage)/2) + \
            emessage

        # подготавливаем модем - передаем ему длину отправляемой строки
        str_send(ser, 'AT+CMGS=' + str(len(sms)/2-1) + '\r')

        # отправляем строку
        str_send(ser, sms + '\x1A')

        i += 1

    # закрываем порт
    ser.close()



# чтение SMS сообщений с сим-карты
#
# возвращаемое значение: список, состоящий из кортежей, каждый из которых содержит
# номер слота на сим-карте, в котором находится сообщение (0-19),
# номер телефона отправителя,
# дату отправления сообщения,
# текст сообщения
#
def GetSMS(serial_name, pin=None):

    result = []

    # подключаемся к порту
    ser = serial.Serial(serial_name, 115200, timeout=1)
    ser.open()

    # устанавливаем формат передачи сообщения - PDU
    status = str_send(ser, 'AT+CMGF=0\r')

    # если в ответ пришел текст, содержащий SIM PIN REQUIRED, значит, модему нужен пин-код
    if 'SIM PIN' in status:
        SendPINToPort(ser, pin)
        str_send(ser, 'AT+CMGF=0\r')

    # запрашиваем список сообщений (4 - все сообщения)
    messages = str_send(ser, 'AT+CMGL=4\r')

    if 'ERROR' not in messages:

        strings = messages.split('\n')

        i = 0

        while i < len(strings):

            if '+CMGL: ' in strings[i]:

                message_header = strings[i][7:]
                message_body = strings[i+1]

                offset = 0

                SMSC_length = int(message_body[offset:offset+2],16)
                offset += 2

                SMSC_address = message_body[offset:offset+2*SMSC_length]
                SMSC_typeOfAddress = SMSC_address[:2]
                SMSC_serviceCenterNumber = SMSToPhoneNumber( SMSC_address[2:] )
                offset += 2*SMSC_length

                SMS_deliverBits = int(message_body[offset:offset+2],16)
                offset += 2

                SMS_senderNumberLength = int(message_body[offset:offset+2],16)
                offset += 2

                SMS_senderNumberType = message_body[offset:offset+2]
                offset += 2

                SMS_senderNumber = message_body[offset:offset+SMS_senderNumberLength+(1 if SMS_senderNumberLength & 1 != 0 else 0) ]
                if SMS_senderNumberType == '91':
                    SMS_senderNumber = SMSToPhoneNumber(SMS_senderNumber)
                if int(SMS_senderNumberType[0],16) & 5 == 5:
                    SMS_senderNumber = Decode7bit(SMS_senderNumber)
                offset += SMS_senderNumberLength+(1 if SMS_senderNumberLength & 1 != 0 else 0)

                TP_protocolIdentifier = message_body[offset:offset+2]
                offset += 2

                TP_dataCodingScheme = int(message_body[offset:offset+2],16)
                offset += 2

                TP_serviceCenterTimeStamp = SMSToTimeStamp(message_body[offset:offset+14])
                offset += 14

                TP_userDataLength = int(message_body[offset:offset+2],16)
                offset += 2

                if SMS_deliverBits & 64 != 0:
                    SMS_userDataHeaderLength = int(message_body[offset:offset+2],16)
                    offset += 2
                    SMS_userDataHeader = message_body[offset:offset+2*SMS_userDataHeaderLength]
                    offset += 2*SMS_userDataHeaderLength

                message_text = None
                if (TP_dataCodingScheme == 0):
                    message_text = Decode7bit(message_body[offset:])
                if (TP_dataCodingScheme & 8 != 0):
                    message_text = SMSToText(message_body[offset:])
                if message_text is None:
                    message_text = message_body[offset:]

                # добавляем в результирующий список кортеж, содержащий
                # номер слота на сим-карте, в котором находится сообщение (0-19),
                # номер телефона отправителя,
                # дату отправления сообщения,
                # текст сообщения
                result.append((message_header.split(',')[0], SMS_senderNumber, TP_serviceCenterTimeStamp, message_text))

                i += 2

            else:

                i += 1

    # закрываем порт
    ser.close()

    return result



# удаление SMS сообщения в слоте с номером slot с сим-карты
def DeleteSMS(serial_name, slot, pin=None):

    # подключаемся к порту
    ser = serial.Serial(serial_name, 115200, timeout=1)
    ser.open()

    # удаляем сообщение
    status = str_send(ser, 'AT+CMGD=%s\r' % (slot))

    # если в ответ пришел текст, содержащий SIM PIN REQUIRED, значит, модему нужен пин-код
    if 'SIM PIN' in status:
        SendPINToPort(ser, pin)
        str_send(ser, 'AT+CMGD=%s\r' % (slot))

    # закрываем порт
    ser.close()