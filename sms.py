import smsutils

# отправляем SMS
smsutils.SendSMS('Привет, мир!', '+998935602290', '/dev/ttyUSB0')

# читаем SMS с карты
result = smsutils.GetSMS('/dev/ttyUSB0')

#for r in result:
#    print r[0], ' ', r[1], ' ', r[2], '\n', r[3]