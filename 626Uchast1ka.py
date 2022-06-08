from tkinter import *
import mysql.connector
import time
import serial
import minimalmodbus
import datetime
import pyautogui
from setuptools import sic
from tkinter import ttk
import pyglet
import xlsxwriter
from tkcalendar import Calendar
from datetime import datetime
from datetime import timedelta


global sensr
sensr = 0
global onoff1,onoff2,onoff3, onoff4,onoff5,onoff6,onoff7,onoff8,res,\
    mtakror1,wtakror1,\
    mtakror2,wtakror2,\
    mtakror3,wtakror3,\
    mtakror4,wtakror4,\
    mtakror6,wtakror6,\
    mtakror7,wtakror7,\
    mtakror8,wtakror8,\
    mtakror5,wtakror5
res=300
mtakror1 = 1
mtakror2 = 1
mtakror3 = 1
mtakror4 = 1
mtakror5= 1
mtakror6 = 1
mtakror7 = 1
mtakror8 = 1
wtakror1 = 1
wtakror2 = 1
wtakror3 = 1
wtakror4 = 1
wtakror5= 1
wtakror6 = 1
wtakror7 = 1
wtakror8 = 1
wtakror9 = 1
wtakror10 = 1
#Mysql ulash
mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='water')
mycursor = mydb.cursor()
#programma qo'yilgan obekt
obekt="Select obekt from setup"
mycursor.execute(obekt)
obekt = mycursor.fetchone()[0]
#Comport o'zgartirish
mycursor.execute("SELECT comport FROM s_obekt where id=%s",[obekt])
exCom = mycursor.fetchone()[0]
comport = 'COM' + str(exCom)
#buyruqdagi suv hajmi
buyruqhajmi = "Select kub,sana from asos where obekt_id=%s order by id desc limit 1"
mycursor.execute(buyruqhajmi,[obekt])
# asos massiv oldingi buyruq1
asos = mycursor.fetchone()
#buyruq berilgan sana
sana=asos[1]




#me'yordan   kop suv o'tish chegarasi

mycursor.execute("Select ogoh,alarm,m_soni,s_soni from s_obekt where id=%s ",[obekt])
s_obekt = mycursor.fetchone()

m_soni=s_obekt[2]
s_soni=s_obekt[3]
ogoh=s_obekt[0]
alarm=s_obekt[1]
#me'yordan  juda kop suv o'tish chegarasi

#adress olish
mycursor.execute("Select m_address,s_address,min,max,m_id,activ from s_motor where  obekt_id=%s order by m_id ",[obekt])
s_motor = mycursor.fetchall()
#max7-motorniki
motor1=1
if(m_soni>0):
    if(s_motor[0][5]==1):
        max1 = s_motor[0][3]
        pastki_sath1 = s_motor[0][4]
        if(sensr==1):
            motorKalit1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
            motorKalit1.serial.baudrate = 9600
            motorKalit1.serial.bytesize = 8
            motorKalit1.serial.parity = serial.PARITY_NONE
            motorKalit1.serial.stopbits = 1
            motorKalit1.serial.timeout = 2  # seconds
            motorKalit1.address =1 # motor datchiklar 4, 3, 2   uchun Xiva

            motorsensor1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
            motorsensor1.serial.baudrate = 9600
            motorsensor1.serial.bytesize = 8
            motorsensor1.serial.parity = serial.PARITY_NONE
            motorsensor1.serial.stopbits = 1
            motorsensor1.serial.timeout = 2  # seconds
            motorsensor1.address = s_motor[0][1]
            motorsensor1.mode = minimalmodbus.MODE_RTU

    else:
        motor1=-1
else:
    motor1=0

motor2=1
if(m_soni>1):
    if(s_motor[1][5]==1):
        max2 = s_motor[1][3]
        pastki_sath2 = s_motor[1][4]

        if (sensr == 1):
            motorKalit2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
            motorKalit2.serial.baudrate = 9600
            motorKalit2.serial.bytesize = 8
            motorKalit2.serial.parity = serial.PARITY_NONE
            motorKalit2.serial.stopbits = 1
            motorKalit2.serial.timeout = 2  # seconds
            motorKalit2.address =1 # motor datchiklar 4, 3, 2   uchun Xiva

            motorsensor2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
            motorsensor2.serial.baudrate = 9600
            motorsensor2.serial.bytesize = 8
            motorsensor2.serial.parity = serial.PARITY_NONE
            motorsensor2.serial.stopbits = 1
            motorsensor2.serial.timeout = 2  # seconds
            motorsensor2.address = s_motor[0][1]
            motorsensor2.mode = minimalmodbus.MODE_RTU
    else:
        motor2=-1
else:
    motor2=0

motor3=1
if(m_soni>2):
    if(s_motor[2][5]==1):
        max3 = s_motor[2][3]
        pastki_sath3 = s_motor[2][4]
    else:
        motor3=-1
else:
    motor3=0

motor4=1
if(m_soni>3):
    if(s_motor[3][5]==1):
        max4 = s_motor[3][3]
        pastki_sath4 = s_motor[3][4]
    else:
        motor4=-1
else:
    motor4=0

motor5=1
if(m_soni>4):
    if(s_motor[4][5]==1):
        max5 = s_motor[4][3]
        pastki_sath5 = s_motor[4][4]
    else:
        motor5=-1
else:
    motor5=0

motor6=1
if(m_soni>5):
    if(s_motor[5][5]==1):
        max6 = s_motor[5][3]
        pastki_sath6 = s_motor[5][4]
    else:
        motor6=-1
else:
    motor6=0

motor7=1
if(m_soni>6):
    if(s_motor[6][5]==1):
        max7 = s_motor[6][3]
        pastki_sath7 = s_motor[6][4]
    else:
        motor7=-1
else:
    motor7=0


motor8 = 1
if (m_soni > 7):
    if (s_motor[7][5] == 1):
        max8 = s_motor[7][3]
        pastki_sath8 = s_motor[7][4]
    else:
        motor8 = -1
else:
    motor8 = 0

motor9 = 1
if (m_soni > 8):
    if (s_motor[8][5] == 1):
        max9 = s_motor[8][3]
        pastki_sath9 = s_motor[8][4]

    else:
        motor9 = -1
else:
    motor9 = 0

motor10=1
if(m_soni>9):
    if(s_motor[9][5]==1):
        max10 = s_motor[9][3]
        pastki_sath10 = s_motor[9][4]
    else:
        motor10=-1
else:
    motor10=0

max3 = s_motor[2][3]
max4 = s_motor[3][3]
max5 = s_motor[4][3]
max6 = s_motor[5][3]
max7 = s_motor[6][3]
max8 = s_motor[7][3]
max9 = s_motor[8][3]
max10 = s_motor[9][3]


if sensr == 1:
    onoff1 = 0
    onoff2 = 0
    onoff3 = 0
    onoff4 = 0
    onoff5 = 0
    onoff6 = 0
    onoff7 = 0
    onoff8 = 0
    onoff9 = 0
    onoff10 = 0

    # client2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    # client2.serial.baudrate = 9600
    # # baudrate
    # client2.serial.bytesize = 8
    # client2.serial.parity = serial.PARITY_NONE
    # client2.serial.stopbits = 1
    # client2.serial.timeout = 2  # seconds
    # client2.address = 4  # motor datchiklar 4, 3, 2   uchun Xiva
    #

    motorKalit2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorKalit2.serial.baudrate = 9600
    # baudrate
    motorKalit2.serial.bytesize = 8
    motorKalit2.serial.parity = serial.PARITY_NONE
    motorKalit2.serial.stopbits = 1
    motorKalit2.serial.timeout = 2  # seconds
    motorKalit2.address = 2  # motor datchiklar 4, 3, 2   uchun Xiva

    motorsensor2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorsensor2.serial.baudrate = 9600
    # baudrate
    motorsensor2.serial.bytesize = 8
    motorsensor2.serial.parity = serial.PARITY_NONE
    motorsensor2.serial.stopbits = 1
    motorsensor2.serial.timeout = 2  # seconds
    motorsensor2.address = 4  # input yozilgandan kelgani
    motorsensor2.mode = minimalmodbus.MODE_RTU

    motorsensor3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorKalit1.serial.baudrate = 9600
    # baudrate
    motorsensor3.serial.bytesize = 8
    motorsensor3.serial.parity = serial.PARITY_NONE
    motorsensor3.serial.stopbits = 1
    motorsensor3.serial.timeout = 2  # seconds
    motorsensor3.address = 5  # sensor 5, 6, 7  uchun Xiva
    motorsensor3.mode = minimalmodbus.MODE_RTU

    motorsensor4 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorKalit1.serial.baudrate = 9600
    # baudrate
    motorsensor4.serial.bytesize = 8
    motorsensor4.serial.parity = serial.PARITY_NONE
    motorsensor4.serial.stopbits = 1
    motorsensor4.serial.timeout = 2  # seconds
    motorsensor4.address = 6
    motorsensor4.mode = minimalmodbus.MODE_RTU

    motorsensor5 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorsensor5.serial.baudrate = 9600
    # baudrate
    motorsensor5.serial.bytesize = 8
    motorsensor5.serial.parity = serial.PARITY_NONE
    motorsensor5.serial.stopbits = 1
    motorsensor5.serial.timeout = 2
    motorsensor5.address = 7
    motorsensor5.mode = minimalmodbus.MODE_RTU

    motorsensor6 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorsensor6.serial.baudrate = 9600
    # baudrate
    motorsensor6.serial.bytesize = 8
    motorsensor6.serial.parity = serial.PARITY_NONE
    motorsensor6.serial.stopbits = 1
    motorsensor6.serial.timeout = 2
    motorsensor6.address = 8
    motorsensor6.mode = minimalmodbus.MODE_RTU

    motorsensor7 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorsensor7.serial.baudrate = 9600
    # baudrat8
    motorsensor7.serial.bytesize = 8
    motorsensor7.serial.parity = serial.PARITY_NONE
    motorsensor7.serial.stopbits = 1
    motorsensor7.serial.timeout = 2
    motorsensor7.address = 8
    motorsensor7.mode = minimalmodbus.MODE_RTU

    motorsensor8 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorsensor8.serial.baudrate = 9600
    # baudrat8
    motorsensor8.serial.bytesize = 8
    motorsensor8.serial.parity = serial.PARITY_NONE
    motorsensor8.serial.stopbits = 1
    motorsensor8.serial.timeout = 2
    motorsensor8.address = 8
    motorsensor8.mode = minimalmodbus.MODE_RTU

    watersensor1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor1.serial.baudrate = 9600
    # baudrate
    watersensor1.serial.bytesize = 8
    watersensor1.serial.parity = serial.PARITY_NONE
    watersensor1.serial.stopbits = 1
    watersensor1.serial.timeout = 2
    watersensor1.address = 9
    watersensor1.mode = minimalmodbus.MODE_RTU

    watersensor2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor2.serial.baudrate = 9600
    # baudrate
    watersensor2.serial.bytesize = 8
    watersensor2.serial.parity = serial.PARITY_NONE
    watersensor2.serial.stopbits = 1
    watersensor2.serial.timeout = 2
    watersensor2.address = 10
    watersensor2.mode = minimalmodbus.MODE_RTU



    watersensor3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor3.serial.baudrate = 9600
    # baudrate
    watersensor3.serial.bytesize = 8
    watersensor3.serial.parity = serial.PARITY_NONE
    watersensor3.serial.stopbits = 1
    watersensor3.serial.timeout = 2
    watersensor3.address = 11
    watersensor3.mode = minimalmodbus.MODE_RTU

    watersensor4 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor4.serial.baudrate = 9600
    # baudrat4
    watersensor4.serial.bytesize = 8
    watersensor4.serial.parity = serial.PARITY_NONE
    watersensor4.serial.stopbits = 1
    watersensor4.serial.timeout = 2
    watersensor4.address = 11
    watersensor4.mode = minimalmodbus.MODE_RTU4
else:
    onoff1 = 10 # simulyator
    onoff2 = 10
    onoff3 = 10
    onoff4 = 10 # simulyator
    onoff5 = 10
    onoff6 = 10
    onoff7 = 10
    onoff8 = 10

# this is the slave address number
# client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
global motorSensor7a,motorSensor8a
motorSensor1a = '110'
motorSensor2a = '150'
motorSensor3a = '200'
motorSensor4a = '110'
motorSensor5a = '150'
motorSensor6a = '200'

motorSensor7a = '150'
motorSensor8a = '200'



def ogoh():
    labelin=labelINCub.cget('text')
    if(float(asos[0])+ogoh<float(labelin)  and float(labelin)<float(asos[0])+alarm):
        player = pyglet.media.Player()
        song = 'ogoh.mp3'
        src = pyglet.media.load(song)
        player.queue(src)
        def play():
            player.play()
        play()
    elif(float(float(asos[0])+alarm)<float(labelin)):
        player = pyglet.media.Player()
        song = 'alarm.mp3'
        src = pyglet.media.load(song)
        player.queue(src)

        def play():
            player.play()
        play()
    labelINCub.after(15000, ogoh)

def on1():
    global onoff1
    if onoff1 != 11:


        res = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res == None:
            return
        if sensr != 0:
            try:

                motorKalit1.write_register(2, 0x0200)
                motorKalit1.write_register(1, 0x0100)
                onoff1=1


            except:
                pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
                onoff1=0

        else:
            onoff1 = 11

    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return
    motorSensorSql = "INSERT INTO asos_motor(asos_id,suvSathi,updown,bsana,amal,user_id)VALUES (%s,%s,%s,%s,%s,%s)"
    valmotorSensor = (1, 20, onoff1, datetime.datetime.now(), 1, 1)
    mycursor.execute(motorSensorSql, valmotorSensor)
    mydb.commit()

    labOldmotorSensor1 = float(labelmotorSensor1.cget("text"))
    labelOldmotorSensor1 = Label(secondWindow,text=str(labOldmotorSensor1), bg="grey",fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor1.grid(row=3, column=4)
    sath1.configure(text=str(res))
def on2():
    global onoff1
    if onoff1 != 12:
        res2 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res2 == None:
            return
        if sensr != 0:
            try:
                onoff1 = 1
                motorKalit1.write_register(1, 0x0200)
                motorKalit1.write_register(2, 0x0100)
            except:
                pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff1 = 12


    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return
    motorSensorSql = "INSERT INTO asos_motor(asos_id,suvSathi,updown,bsana,amal,user_id)VALUES (%s,%s,%s,%s,%s,%s)"
    valmotorSensor = (1, 20, onoff1, datetime.datetime.now(), 1, 1)
    mycursor.execute(motorSensorSql, valmotorSensor)
    mydb.commit()
    labOldmotorSensor1 = float(labelmotorSensor1.cget("text"))
    labelOldmotorSensor1 = Label(secondWindow, text=str(labOldmotorSensor1), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor1.grid(row=3, column=4)
    sath1.configure(text=str(res2))
def on3():
    global onoff2
    if onoff2 != 11:

        res21 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 21 == None:
            return
        if sensr != 0:
            try:
                onoff2 = 1
                motorKalit1.write_register(4, 0x0200)
                motorKalit1.write_register(3, 0x0100)
            except:
             pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff2 = 11


    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return

    onoff2=11
    labOldmotorSensor2 = float(labelmotorSensor2.cget("text"))
    labelOldmotorSensor2 = Label(secondWindow, text=str(labOldmotorSensor2),bg="grey",fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor2.grid(row=4, column=4)
    sath2.configure(text=str(res21))
def on4():
    global onoff2
    if onoff2 != 12:

        res22 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 22 == None:
            return
        if sensr != 0:
            try:

                onoff2 = 1
                motorKalit1.write_register(3, 0x0200)
                motorKalit1.write_register(4, 0x0100)
            except:
                pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff2 = 12

        onoff2 = 12
    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return

    labOldmotorSensor2 = float(labelmotorSensor2.cget("text"))
    labelOldmotorSensor2 = Label(secondWindow, text=str(labOldmotorSensor2), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor2.grid(row=4, column=4)
    sath2.configure(text=str(res22))
def on5():
    global onoff3
    if onoff3 != 11:

        res31 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 31 == None:
            return
        if sensr != 0:
            try:
                onoff3 = 1
                motorKalit1.write_register(6, 0x0200)
                motorKalit1.write_register(5, 0x0100)
            except:
                  pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff3 = 11


    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return

    labOldmotorSensor3 = float(labelmotorSensor3.cget("text"))
    labelOldmotorSensor3 = Label(secondWindow, text=str(labOldmotorSensor3), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor3.grid(row=5, column=4)
    sath3.configure(text=str(res31))
def on6():
    global onoff3
    if onoff3 != 12:

        res32 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 32 == None:
            return
        if sensr != 0:

            try:
                onoff3 = 2
                motorKalit1.write_register(6, 0x0200)
                motorKalit1.write_register(5, 0x0100)
            except:
                pyautogui.alert(text="Signal bo'lmadi qayta urinib ko'ring",title='ogohlantirish',bg='yellow')

        else:
            onoff3 = 12


    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting",title='ogohlantirish')
        return

    labOldmotorSensor3 = float(labelmotorSensor3.cget("text"))
    labelOldmotorSensor3 = Label(secondWindow, text=str(labOldmotorSensor3), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor3.grid(row=5, column=4)
    sath3.configure(text=str(res32))


def on7():
    global onoff4
    if onoff4 != 11:


        res41 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res41 == None:
            return
        if sensr != 0:
            try:
                onoff4 = 1
                motorKalit1.write_register(2, 0x0200)
                motorKalit1.write_register(1, 0x0100)
            except:
                pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff4 = 11



    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return
    motorSensorSql = "INSERT INTO asos_motor(asos_id,suvSathi,updown,bsana,amal,user_id)VALUES (%s,%s,%s,%s,%s,%s)"
    valmotorSensor = (1, 20, onoff4, datetime.datetime.now(), 1, 1)
    mycursor.execute(motorSensorSql, valmotorSensor)
    mydb.commit()



    labOldmotorSensor4 = float(labelmotorSensor1.cget("text"))
    labelOldmotorSensor4 = Label(secondWindow,text=str(labOldmotorSensor4), bg="grey",fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor4.grid(row=6, column=4)
    sath4.configure(text=str(res41))
def on8():
    global onoff4
    if onoff4 != 12:

        res42 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res42 == None:
            return
        if sensr != 0:
            try:
                onoff4 = 1
                motorKalit1.write_register(7, 0x0200)
                motorKalit1.write_register(8, 0x0100)
            except:
                pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff4 = 12


    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return
    motorSensorSql = "INSERT INTO asos_motor(asos_id,suvSathi,updown,bsana,amal,user_id)VALUES (%s,%s,%s,%s,%s,%s)"
    valmotorSensor = (1, 20, onoff4, datetime.datetime.now(), 1, 1)
    mycursor.execute(motorSensorSql, valmotorSensor)
    mydb.commit()
    labOldmotorSensor4 = float(labelmotorSensor4.cget("text"))
    labelOldmotorSensor4 = Label(secondWindow, text=str(labOldmotorSensor4), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor4.grid(row=6, column=4)
    sath4.configure(text=str(res42))
def on9():
    global onoff5
    if onoff5 != 11:

        res51 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 51 == None:
            return
        if sensr != 0:
            try:
                onoff5 = 1
                motorKalit2.write_register(2, 0x0200)
                motorKalit2.write_register(1, 0x0100)
            except:
             pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff5 = 11


    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return

    onoff5=11
    labOldmotorSensor5 = float(labelmotorSensor5.cget("text"))
    labelOldmotorSensor5 = Label(secondWindow, text=str(labOldmotorSensor5),bg="grey",fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor5.grid(row=7, column=4)
    sath5.configure(text=str(res51))
def on10():
    global onoff5
    if onoff5 != 12:

        res52 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 52 == None:
            return
        if sensr != 0:
            try:

                onoff5 = 1
                motorKalit2.write_register(1, 0x0200)
                motorKalit2.write_register(2, 0x0100)
            except:
                pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff5 = 12


    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return

    labOldmotorSensor5 = float(labelmotorSensor5.cget("text"))
    labelOldmotorSensor5 = Label(secondWindow, text=str(labOldmotorSensor5), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor5.grid(row=7, column=4)
    sath5.configure(text=str(res52))
def on11():
    global onoff6
    if onoff6 != 11:

        res61 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 61 == None:
            return
        if sensr != 0:
            try:
                onoff6 = 1
                motorKalit2.write_register(4, 0x0200)
                motorKalit2.write_register(3, 0x0100)
            except:
                  pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff6 = 11

        onoff6 = 11
    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return
    onoff6=11
    labOldmotorSensor6 = float(labelmotorSensor6.cget("text"))
    labelOldmotorSensor6 = Label(secondWindow, text=str(labOldmotorSensor6), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor6.grid(row=8, column=4)
    sath6.configure(text=str(res61))
def on12():
    global onoff6
    if onoff6 != 12:

        res62 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 62 == None:
            return
        if sensr != 0:

            try:
                onoff6 = 2
                motorKalit2.write_register(3, 0x0200)
                motorKalit2.write_register(4, 0x0100)
            except:
                pyautogui.alert(text="Signal bo'lmadi qayta urinib ko'ring",title='ogohlantirish',bg='yellow')

        else:
            onoff6 = 12

        onoff6 = 12
    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting",title='ogohlantirish')
        return

    labOldmotorSensor6 = float(labelmotorSensor6.cget("text"))
    labelOldmotorSensor6 = Label(secondWindow, text=str(labOldmotorSensor6), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor6.grid(row=8, column=4)
    sath6.configure(text=str(res62))
def on13():
    global onoff7
    if onoff7 != 11:

        res71 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res71 == None:
            return
        if sensr != 0:

            try:
                onoff7 = 2
                motorKalit2.write_register(3, 0x0200)
                motorKalit2.write_register(4, 0x0100)
            except:
                pyautogui.alert(text="Signal bo'lmadi qayta urinib ko'ring",title='ogohlantirish',bg='yellow')

        else:
            onoff7 = 11

        onoff7 = 11
    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting",title='ogohlantirish')
        return

    labOldmotorSensor7 = float(labelmotorSensor6.cget("text"))
    labelOldmotorSensor7 = Label(secondWindow, text=str(labOldmotorSensor7), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor7.grid(row=9, column=4)
    sath7.configure(text=str(res71))
def on14():
    global onoff7
    if onoff7 != 12:

        res72 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 72 == None:
            return
        if sensr != 0:

            try:
                onoff7 = 2
                motorKalit2.write_register(3, 0x0200)
                motorKalit2.write_register(4, 0x0100)
            except:
                pyautogui.alert(text="Signal bo'lmadi qayta urinib ko'ring",title='ogohlantirish',bg='yellow')

        else:
            onoff7 = 12

        onoff7 = 12
    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting",title='ogohlantirish')
        return

    labOldmotorSensor7 = float(labelmotorSensor6.cget("text"))
    labelOldmotorSensor7 = Label(secondWindow, text=str(labOldmotorSensor7), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor7.grid(row=9, column=4)
    sath7.configure(text=str(res72))
def on15():
    global onoff8
    if onoff8 != 11:

        res81 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res81 == None:
            return
        if sensr != 0:

            try:
                onoff8 = 1
                motorKalit2.write_register(3, 0x0200)
                motorKalit2.write_register(4, 0x0100)
            except:
                pyautogui.alert(text="Signal bo'lmadi qayta urinib ko'ring",title='ogohlantirish',bg='yellow')

        else:
            onoff8 = 11

        onoff8 = 11
    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting",title='ogohlantirish')
        return

    labOldmotorSensor8 = float(labelmotorSensor6.cget("text"))
    labelOldmotorSensor8 = Label(secondWindow, text=str(labOldmotorSensor8), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor8.grid(row=10, column=4)
    sath8.configure(text=str(res81))
def on16():
    global onoff8
    if onoff8 != 12:

        res82 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res82 == None:
            return
        if sensr != 0:

            try:
                onoff8 = 2
                motorKalit2.write_register(3, 0x0200)
                motorKalit2.write_register(4, 0x0100)
            except:
                pyautogui.alert(text="Signal bo'lmadi qayta urinib ko'ring",title='ogohlantirish',bg='yellow')

        else:
            onoff8 = 12

        onoff8 = 12
    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting",title='ogohlantirish')
        return

    labOldmotorSensor8 = float(labelmotorSensor8.cget("text"))
    labelOldmotorSensor8 = Label(secondWindow, text=str(labOldmotorSensor8), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldmotorSensor8.grid(row=10, column=4)
    sath8.configure(text=str(res82))

def modalRegistr():
    modalRegistr=Tk()
    modalRegistr.geometry("600x400")
    labRegistr=Label(modalRegistr,text='Registr adress',width=13,font=('italic', 14, 'bold'))
    labRegistr.grid(row=1,column=1,padx=3,pady=3)
    entryRegistr=Entry(modalRegistr,width=7,font=('italic', 16, 'bold'))
    labRegistr.grid(row=1,column=2,padx=3,pady=3)


motorSensorSql = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
wmotorSensor1 = (1, 1, 1, 0, 4)
mycursor.execute(motorSensorSql, wmotorSensor1)
motorMax="Select id from motor_sensor where obekt_id=%s order by id desc limit 1"
mycursor.execute(motorMax,[obekt])
Maxvalue=mycursor.fetchone()[0]



def motorSensor():
    SensorSql="INSERT INTO water_sensor(asos_id,sensor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
    motorSensorSql="INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
    wmotorSensor1 = (1, 1, 1, 0, 4)
    wmotorSensor2 = (1, 2, 1, 0, 4)
    wmotorSensor3 = (1, 3, 1, 0, 4)
    wmotorSensor4 = (1, 4, 1, 0, 4)
    wmotorSensor5 = (1, 5, 1, 0, 4)
    wmotorSensor6 = (1, 6, 1, 0, 4)
    wmotorSensor7 = (1, 7, 1, 0, 4)
    wmotorSensor8 = (1, 8, 1, 0, 4)
   #valmotorSensor7 = (1, 7, 1, 0, obekt)
   #valmotorSensor8 = (1, 8, 1, 0, obekt)
    # mycursor.execute(SensorSql,wmotorSensor1)
    # mycursor.execute(SensorSql,wmotorSensor2)
    # mycursor.execute(SensorSql,wmotorSensor3)
    # mycursor.execute(SensorSql,wmotorSensor4)
    # mycursor.execute(SensorSql,wmotorSensor5)
    # mycursor.execute(SensorSql,wmotorSensor6)
    # mycursor.execute(SensorSql,wmotorSensor7)
    # mycursor.execute(SensorSql,wmotorSensor8)

    mycursor.execute(motorSensorSql,wmotorSensor1)
    mycursor.execute(motorSensorSql,wmotorSensor2)
    mycursor.execute(motorSensorSql,wmotorSensor3)
    mycursor.execute(motorSensorSql,wmotorSensor4)
    mycursor.execute(motorSensorSql,wmotorSensor5)
    mycursor.execute(motorSensorSql,wmotorSensor6)
    mycursor.execute(motorSensorSql,wmotorSensor7)
    mycursor.execute(motorSensorSql,wmotorSensor8)

if(Maxvalue<10):
  motorSensor()




def motor_sensor():
    global motorSensor1a,motorSensor2a,motorSensor3a,mtakror1,mtakror2,mtakror3,mtakror4,mtakror5,mtakror6,mtakror7,mtakror8,\
        motorSensor4a,motorSensor5a,motorSensor6a,motorSensor7a,motorSensor8a,\
        onoff1,onoff2,onoff3,onoff4,\
        onoff5,onoff6,onoff7,onoff8,res
    if sensr == 1:
        try:
         motorSensor1a = str(motorsensor1.read_register(1, 0, 3))
         labelmotorSensor1.configure(bg='white', fg="black")
        except:
            motorSensorXatoSql = "INSERT INTO xato_motorSensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato = (1, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql, valmotorSensorxato)
            motorSensor1a=labelmotorSensor1.cget('text')
            labelmotorSensor1.configure(bg='black',fg="white")

     #motorSensor2
        try:
            motorSensor2a = str(motorsensor2.read_register(1, 0, 3))
            labelmotorSensor2.configure(bg='white', fg="black")
        except:
            print('d')
            motorSensorXatoSql2 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato2 = (2, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql2, valmotorSensorxato2)
            motorSensor2a = labelmotorSensor2.cget('text')
            labelmotorSensor2.configure(bg='black', fg="white")
    #senso
        try:
            motorSensor3a = str(motorsensor3.read_register(1, 0, 3))
            labelmotorSensor3.configure(bg='white', fg="black")
        except:
            motorSensorXatoSql3 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato3 = (3, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql3, valmotorSensorxato3)
            motorSensor3a = labelmotorSensor3.cget('text')
            labelmotorSensor3.configure(bg='black', fg="white")
    #senso
        try:
           motorSensor4a = str(motorsensor4.read_register(1, 0, 3))
           labelmotorSensor4.configure(bg='white', fg="black")
        except:
            motorSensorXatoSql4 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato4 = (4, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql4, valmotorSensorxato4)
            motorSensor4a = labelmotorSensor4.cget('text')
            labelmotorSensor4.configure(bg='black', fg="white")

     #Sens5
        try:
            motorSensor5a = str(motorsensor5.read_register(1, 0, 3))
            labelmotorSensor5.configure(bg='white', fg="black")
        except:
            motorSensorXatoSql5 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato5 = (5, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql5, valmotorSensorxato5)
            motorSensor5a = labelmotorSensor5.cget('text')
            labelmotorSensor5.configure(bg='black', fg="white")
    #senso
        try:
            motorSensor6a = str(motorsensor6.read_register(1, 0, 3))
            labelmotorSensor6.configure(bg='white', fg="black")
        except:
            motorSensorXatoSql6 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato6 = (6, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql6, valmotorSensorxato6)
            motorSensor6a = labelmotorSensor6.cget('text')
            labelmotorSensor6.configure(bg='black', fg="white")

         #motorSensor7
        try:
            motorSensor7a = str(motorsensor7.read_register(1, 0, 3))
            labelmotorSensor7.configure(bg='white', fg="black")
        except:
            motorSensorXatoSql6 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato6 = (6, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql6, valmotorSensorxato6)
            motorSensor7a = labelmotorSensor7.cget('text')
            labelmotorSensor7.configure(bg='black', fg="white")

        #ssor8
        try:
            motorSensor8a = str(motorsensor8.read_register(1, 0, 3))
            labelmotorSensor8.configure(bg='white', fg="black")
        except:
            valmotorSensorxato7 = (6, 'motorSensor ishlamadi')
            motorSensorXatoSql7= "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            mycursor.execute(motorSensorXatoSql7, valmotorSensorxato7)
            motorSensor8a = labelmotorSensor8.cget('text')
            labelmotorSensor8.configure(bg='black', fg="white")
    else:
        if onoff1 == 11:
            motorSensor1a = str(float(motorSensor1a) - 50)

            if (float(motorSensor1a) < 0):
                motorSensor1a = '0'
                onoff1 = 10
        if onoff1 == 12:
            motorSensor1a = str(float(motorSensor1a) + 50)
           #motorSensor2
        if onoff2 == 11:
            motorSensor2a = str(float(motorSensor2a) - 50)

            if (float(motorSensor2a) < 0):
                motorSensor2a = '0'
                onoff2 = 10
        if onoff2 == 12:
            motorSensor2a = str(float(motorSensor2a) + 50)
                  #motorSensor3
        if onoff3 == 11:
            motorSensor3a = str(float(motorSensor3a) - 50)

            if (float(motorSensor3a) < 0):
                motorSensor3a = '0'
                onoff3 = 10
        if onoff3 == 12:
            motorSensor3a = str(float(motorSensor3a) + 50)
             #motorSensor4
        if onoff4 == 11:
            motorSensor4a = str(float(motorSensor4a) - 50)

            if (float(motorSensor4a) < 0):
                motorSensor4a = '0'
                onoff4 = 10
        if onoff4 == 12:
            motorSensor4a = str(float(motorSensor4a) + 50)
             #motorSensor5
        if onoff5 == 11:
            motorSensor5a = str(float(motorSensor5a) - 50)

            if (float(motorSensor5a) < 0):
                motorSensor5a = '0'
                onoff5 = 10
        if onoff5 == 12:
            motorSensor5a = str(float(motorSensor5a) + 50)
             #motorSensor6
        if onoff6 == 11:
            motorSensor6a = str(float(motorSensor6a) - 50)

            if (float(motorSensor6a) < 0):
                motorSensor6a = '0'
                onoff6 = 10
        if onoff6 == 12:
            motorSensor6a = str(float(motorSensor6a) + 50)
             #motorSensor7
        if onoff7 == 11:
            motorSensor7a = str(float(motorSensor7a) - 50)

            if (float(motorSensor7a) < 0):
                motorSensor7a = '0'
                onoff7 = 10
        if onoff7 == 12:
            motorSensor7a = str(float(motorSensor7a) + 50)
             #motorSensor8
        if onoff8 == 11:
            motorSensor8a = str(float(motorSensor8a) - 50)

            if (float(motorSensor8a) < 0):
                motorSensor8a = '0'
                onoff8 = 10
        if onoff8 == 12:
            motorSensor8a = str(float(motorSensor8a) + 50)



    motorSensor1 = round(pastki_sath1 - (float(float(motorSensor1a) / 100)), 2)
    motorSensor2 = round(pastki_sath2 - (float(float(motorSensor2a) / 100)), 2)
    motorSensor3 = round(pastki_sath3 - (float(float(motorSensor3a) / 100)), 2)
    motorSensor4 = round(pastki_sath4 - (float(float(motorSensor4a) / 100)), 2)
    motorSensor5 = round(pastki_sath5 - (float(float(motorSensor5a) / 100)), 2)
    motorSensor6 = round(pastki_sath6 - (float(float(motorSensor6a) / 100)), 2)
    motorSensor7 = round(pastki_sath7 - (float(float(motorSensor7a) / 100)), 2)
    motorSensor8 = round(pastki_sath8 - (float(float(motorSensor8a) / 100)), 2)

    #tekshirish motorSensor1
    if motorSensor1 > float(pastki_sath1 - 0.2):
        if sensr != 0:
            try:
                onoff1 = 0
                motorKalit1.write_register(1, 0x0200)
            except:
                print(" aaa")
                # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
        else:
            onoff1 = 10
            motorSensor1 = pastki_sath1

        if motorSensor1 < 0.1:
         if sensr != 0:
             try:
                motorKalit1.write_register(2, 0x0200)
                onoff1 = 0
             except:
                 print(" aaa"  )#pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

         else:
            onoff1 = 10
    if (float(motorSensor1a)>pastki_sath1*1000):
        onoff1=10
        motorSensor1="0"
    #motorSensor2
    if motorSensor2 > float(pastki_sath2 - 0.2):
        if sensr != 0:
            try:
                onoff2 = 0
                motorKalit1.write_register(3, 0x0200)
            except:
               print(" aaa"  )# pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
        else:
            onoff2 = 10
            motorSensor2 = pastki_sath2
        if motorSensor2 < 0.1:
            if sensr != 0:
                try:
                    motorKalit1.write_register(4, 0x0200)
                    onoff2 = 0
                except:
                    # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
                    print(" aaa")
            else:
                onoff2 = 10
    if (float(motorSensor2a) > pastki_sath2 * 1000):
        onoff2= 10
        motorSensor2 = "0"

    #motorSensor3
    if motorSensor3 > float(pastki_sath3 - 0.2) :
        if sensr != 0:
            onoff3 = 0
            try:
                motorKalit1.write_register(5, 0x0200)
            except:
                # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
              print(" aaa"  )
        else:
            onoff3 = 10
            motorSensor3 = pastki_sath3

    if (float(motorSensor3a) > pastki_sath3 * 1000):
        if sensr != 0:
            try:

                motorKalit1.write_register(6, 0x0200)
                onoff3 = 0
            except:
                #pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
                print(" aaa")
        else:
            onoff3 = 10
            motorSensor3 = "0"

            #tekshirish motorSensor4
    if motorSensor4 > float(pastki_sath4 - 0.2):
        if sensr != 0:
            try:
                onoff4 = 0
                motorKalit1.write_register(7, 0x0200)
            except:
                # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
                print(" aaa")
        else:
            onoff4 = 10
            motorSensor4 = pastki_sath4

        if motorSensor4 < 0.1:
         if sensr != 0:
             try:
                motorKalit1.write_register(8, 0x0200)
                onoff4 = 0
             except:
                 # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
                 print(" aaa")
         else:
            onoff4 = 10
    if (float(motorSensor4a)>pastki_sath4*1000):
        onoff4=10
        motorSensor4="0"
    #motorSensor5
    if motorSensor5 > float(pastki_sath5 - 0.2):
        if sensr != 0:
            try:
                onoff5 = 0
                motorKalit2.write_register(1, 0x0200)
            except:
                print(" aaa") # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
        else:
            onoff5 = 10
            motorSensor5 = pastki_sath5
        if motorSensor5 < 0.1:
            if sensr != 0:
                try:
                    motorKalit2.write_register(2, 0x0200)
                    onoff5 = 0
                except:

                    print(" aaa")
                    # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
            else:
                onoff5= 10
        # motorSensor7
        if motorSensor7 > float(pastki_sath5 - 0.2):
            if sensr != 0:
                try:
                    onoff7 = 0
                    motorKalit2.write_register(1, 0x0200)
                except:
                    print(" aaa")  # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
            else:
                onoff7 = 10
                motorSensor7 = pastki_sath5
            if motorSensor7 < 0.1:
                if sensr != 0:
                    try:
                        motorKalit2.write_register(2, 0x0200)
                        onoff7 = 0
                    except:

                        print(" aaa")
                        # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
                else:
                    onoff7 = 10

        # motorSensor8
        if motorSensor8 > float(pastki_sath5 - 0.2):
            if sensr != 0:
                try:
                    onoff8 = 0
                    motorKalit2.write_register(1, 0x0200)
                except:
                    print(" aaa")  # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
            else:
                onoff8 = 10
                motorSensor8 = pastki_sath5
            if motorSensor8 < 0.1:
                if sensr != 0:
                    try:
                        motorKalit2.write_register(2, 0x0200)
                        onoff8 = 0
                    except:

                        print(" aaa")
                        # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
                else:
                    onoff8 = 10
    if (float(motorSensor8a) > pastki_sath5 * 1000):
        onoff8 = 10
        motorSensor8 = "0"

    #motorSensor6
    if motorSensor6> float(pastki_sath6 - 0.2) :
        if sensr != 0:
            onoff6 = 0
            try:
                motorKalit2.write_register(3, 0x0200)
            except:
                print(" aaa"  )# pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
        else:
            onoff6 = 10
            motorSensor6= pastki_sath6

    if (float(motorSensor6a) > pastki_sath6 * 1000):
        if sensr != 0:
            try:

                motorKalit2.write_register(4, 0x0200)
                onoff6 = 0
            except:
                print(" aaa")
                # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
        else:
            onoff6 = 10
            motorSensor6 = "0"


    labelmotorSensor1.configure(text=motorSensor1)
    labelmotorSensor2.configure(text=motorSensor2)
    labelmotorSensor3.configure(text=motorSensor3)
    labelmotorSensor4.configure(text=motorSensor4)
    labelmotorSensor5.configure(text=motorSensor5)
    labelmotorSensor6.configure(text=motorSensor6)

    labelmotorSensor7.configure(text=motorSensor7)
    labelmotorSensor8.configure(text=motorSensor8)

    #
    #
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=1 order by id desc limit 1",[obekt])
    lastmotorSensor1 = mycursor.fetchone()[0]
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=2 order by id desc limit 1",[obekt])
    lastmotorSensor2 = mycursor.fetchone()[0]
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=3 order by id desc limit 1",[obekt])
    lastmotorSensor3 = mycursor.fetchone()[0]
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=4 order by id desc limit 1",[obekt])
    lastmotorSensor4 = mycursor.fetchone()[0]
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=5 order by id desc limit 1",[obekt])
    lastmotorSensor5 = mycursor.fetchone()[0]
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=6 order by id desc limit 1",[obekt])
    lastmotorSensor6 = mycursor.fetchone()[0]
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=7 order by id desc limit 1",[obekt])
    lastmotorSensor7 = mycursor.fetchone()[0]
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=8 order by id desc limit 1",[obekt])
    lastmotorSensor8 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=1 order by id desc limit 1",[obekt])
    id1 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=2 order by id desc limit 1",[obekt])
    id2 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=3 order by id desc limit 1",[obekt])
    id3 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=4 order by id desc limit 1",[obekt])
    id4 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=5 order by id desc limit 1",[obekt])
    id5 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=6 order by id desc limit 1",[obekt])
    id6 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=7 order by id desc limit 1",[obekt])
    id7 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=8 order by id desc limit 1",[obekt])
    id8 = mycursor.fetchone()[0]


    #motorSensor1
    if (float(motorSensor1) == float(lastmotorSensor1)):
        mtakror1 = mtakror1 + 1
        mycursor.execute("UPDATE motor_sensor SET takror=%s where id=%s  ", [mtakror1, id1])

    else:
        motorSensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
        valmotorSensor1 = (1, 1, 1, motorSensor1, obekt)
        mycursor.execute(motorSensorSql1, valmotorSensor1)
        lastmotorSensor1 = motorSensor1
        mtakror = 1

    # motorSensor2
    if (float(motorSensor2) == float(lastmotorSensor2)):
        mtakror2 = mtakror2 + 1
        mycursor.execute("UPDATE motor_sensor SET takror=%s where id=%s  ", [mtakror2, id2])

    else:
        motorSensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
        valmotorSensor2 = (1, 2, 1, motorSensor2, obekt)
        mycursor.execute(motorSensorSql1, valmotorSensor2)
        lastmotorSensor2 = motorSensor2
        mtakror2 = 1

    # motorSensor3
    if (float(motorSensor3) == float(lastmotorSensor3)):
        mtakror3 = mtakror3 + 1
        mycursor.execute("UPDATE motor_sensor SET takror=%s where id=%s  ", [mtakror3, id3])

    else:
        motorSensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
        valmotorSensor3 = (1, 3, 1, motorSensor3, obekt)
        mycursor.execute(motorSensorSql1, valmotorSensor3)
        lastmotorSensor3 = motorSensor3
        mtakror3 = 1

    # motorSensor4
    if (float(motorSensor4) == float(lastmotorSensor4)):
        mtakror4 = mtakror4 + 1
        mycursor.execute("UPDATE motor_sensor SET takror=%s where id=%s  ", [mtakror4, id4])

    else:
        motorSensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
        valmotorSensor4 = (1, 4, 1, motorSensor4, obekt)
        mycursor.execute(motorSensorSql1, valmotorSensor4)
        lastmotorSensor4 = motorSensor4
        mtakror4 = 1

    # motorSensor5
    if (float(motorSensor5) == float(lastmotorSensor5)):
        mtakror5 = mtakror5 + 1
        mycursor.execute("UPDATE motor_sensor SET takror=%s where id=%s  ", [mtakror5, id5])

    else:
        motorSensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
        valmotorSensor5 = (1, 5, 1, motorSensor5, obekt)
        mycursor.execute(motorSensorSql1, valmotorSensor5)
        lastmotorSensor5 = motorSensor5
        mtakror5 = 1

    # motorSensor6
    if (float(motorSensor6) == float(lastmotorSensor6)):
        mtakror6 = mtakror6 + 1
        mycursor.execute("UPDATE motor_sensor SET takror=%s where id=%s  ", [mtakror6, id6])

    else:
        motorSensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
        valmotorSensor6 = (1, 6, 1, motorSensor6, obekt)
        mycursor.execute(motorSensorSql1, valmotorSensor6)
        lastmotorSensor6 = motorSensor6
        mtakror6 = 1
    # motorSensor7
    if (float(motorSensor7) == float(lastmotorSensor7)):
        mtakror7 = mtakror7 + 1
        mycursor.execute("UPDATE motor_sensor SET takror=%s where id=%s  ", [mtakror7, id7])

    else:
        motorSensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
        valmotorSensor7 = (1, 7, 1, motorSensor7, obekt)
        mycursor.execute(motorSensorSql1, valmotorSensor7)
        lastmotorSensor7 = motorSensor7
        mtakror7 = 1

    # motorSensor8
    if (float(motorSensor8) == float(lastmotorSensor8)):
        mtakror8 = mtakror8 + 1
        mycursor.execute("UPDATE motor_sensor SET takror=%s where id=%s  ", [mtakror8, id8])

    else:
        motorSensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
        valmotorSensor8 = (1, 8, 1, motorSensor8, obekt)
        mycursor.execute(motorSensorSql1, valmotorSensor8)
        lastmotorSensor8 = motorSensor8
        mtakror8 = 1

    mydb.commit()
    labelmotorSensor1.after(3000,motor_sensor)

def off1():


    res = pyautogui.confirm(text='', title='1 - motor harakatini to`xtasizmi() ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    global onoff1
    if sensr != 0:
        try:
            motorKalit1.write_register(1, 0x0200)
            motorKalit1.write_register(2, 0x0200)
            onoff1 = 0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        onoff1 = 10
def off2():
    global onoff2
    res = pyautogui.confirm(text='', title='2 - motor harakatini to`xtotasizmi() ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return

    if sensr != 0:
        try:
            motorKalit1.write_register(3, 0x0200)
            motorKalit1.write_register(4, 0x0200)
            onoff2=0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
     onoff2 = 10

def off3():
    global onoff3
    res = pyautogui.confirm(text='STOP', title='3 - motor harakatini to`xtotasizmi ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return

    if sensr != 0:
        try:
            motorKalit1.write_register(5, 0x0200)
            motorKalit1.write_register(6, 0x0200)
            onoff3=0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        onoff3 = 10
def off4():
    global onoff4
    res = pyautogui.confirm(text='', title='4 - motor harakatini to`xtasizmi() ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    global onoff4
    if sensr != 0:
        try:
            motorKalit1.write_register(7, 0x0200)
            motorKalit1.write_register(8, 0x0200)
            onoff4 = 0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        onoff4 = 10
def off5():
    global onoff5
    res = pyautogui.confirm(text='', title='5 - motor harakatini to`xtotasizmi() ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    if sensr != 0:
        try:
            motorKalit2.write_register(1, 0x0200)
            motorKalit2.write_register(2, 0x0200)
            onoff5=0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
     onoff5 = 10

def off6():
    global onoff6
    res = pyautogui.confirm(text='STOP', title='6 - motor harakatini to`xtotasizmi ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    if sensr != 0:
        try:
            motorKalit2.write_register(3, 0x0200)
            motorKalit2.write_register(4, 0x0200)
            onoff6=0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        onoff6 = 10

def off7():
    global onoff7
    res = pyautogui.confirm(text='STOP', title='6 - motor harakatini to`xtotasizmi ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    if sensr != 0:
        try:
            motorKalit2.write_register(3, 0x0200)
            motorKalit2.write_register(4, 0x0200)
            onoff7=0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        onoff7 = 10

def off8():
    global onoff8
    res = pyautogui.confirm(text='STOP', title='6 - motor harakatini to`xtotasizmi ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    if sensr != 0:
        try:
            motorKalit2.write_register(3, 0x0200)
            motorKalit2.write_register(4, 0x0200)
            onoff8=0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        onoff8 = 10

def water_sensor():

    global wtakror1,  wtakror2, wtakror3, wtakror4,  wtakror6, wtakror7, wtakror8, wtakror5
    farq= "Select farq_sm from s_farq where sensor_id=1 and obekt_id=%s order by id desc limit 1"
    mycursor.execute(farq,[obekt])
    farqSath1 = mycursor.fetchone()[0]

    farq= "Select farq_sm from s_farq where sensor_id=2 and obekt_id=%s order by id desc limit 1"
    mycursor.execute(farq,[obekt])
    farqSath2=mycursor.fetchone()[0]

    farq = "Select farq_sm from s_farq where sensor_id=3  and obekt_id=%s order by id desc limit 1"
    mycursor.execute(farq,[obekt])
    farqSath3 = mycursor.fetchone()[0]

    farq = "Select farq_sm from s_farq where sensor_id=4  and obekt_id=%s order by id desc limit 1"
    mycursor.execute(farq,[obekt])
    farqSath4=mycursor.fetchone()[0]

    mycursor.execute("SELECT reykasathi FROM s_sensor where sensor_id=1 and obekt_id=%s  ",[obekt])
    reyka_height = mycursor.fetchone()[0]

    mycursor.execute("SELECT sensorsathi FROM s_sensor where sensor_id=1 and obekt_id=%s   ",[obekt])
    water_height = mycursor.fetchone()[0]

    totalHeight = float(reyka_height + water_height)

    #
    # mycursor.execute("SELECT suvSathi from water_sensor where obekt_id=%s and sensor_id=1 order by id desc limit 1",[obekt])
    # lastSensor1 = mycursor.fetchone()[0]
    #
    # mycursor.execute("SELECT suvSathi from water_sensor where obekt_id=%s and sensor_id=2 order by id desc limit 1",[obekt])
    # lastSensor2 = mycursor.fetchone()[0]
    #
    # mycursor.execute("SELECT suvSathi from water_sensor where obekt_id=%s and sensor_id=3 order by id desc limit 1",[obekt])
    # lastSensor3 = mycursor.fetchone()[0]
    #
    # mycursor.execute("SELECT suvSathi from water_sensor where obekt_id=%s and sensor_id=4 order by id desc limit 1",[obekt])
    # lastSensor4 = mycursor.fetchone()[0]
    #
    # mycursor.execute("SELECT id from water_sensor where obekt_id=%s and sensor_id=1 order by id desc limit 1", [obekt])
    # wid1 = mycursor.fetchone()[0]
    #
    # mycursor.execute("SELECT id from water_sensor where obekt_id=%s and sensor_id=2 order by id desc limit 1", [obekt])
    # wid2 = mycursor.fetchone()[0]
    #
    # mycursor.execute("SELECT id from water_sensor where obekt_id=%s and sensor_id=3 order by id desc limit 1", [obekt])
    # wid3 = mycursor.fetchone()[0]
    #
    # mycursor.execute("SELECT id from water_sensor where obekt_id=%s and sensor_id=4 order by id desc limit 1", [obekt])
    # wid4 = mycursor.fetchone()[0]

    if sensr != 0:
        try:
         sensor11b = str(watersensor1.read_register(1, 0, 3))
        except:



            sensorXatoSql5 = "INSERT INTO xato_sensor(sensor_id,status,obekt_id)VALUES (%s,%s,%s)"
            valSensorxato5 = (7, 'Sensor ishlamadi',obekt)
            mycursor.execute(sensorXatoSql5, valSensorxato5)
            sensor11b=labelIN.cget('text')
            sath1.configure(bg='black',fg="white")

    else:
        sensor11b = '2000'
    sensor11 = round(float(totalHeight) - float(int(sensor11b) / 1000), 2)
    labelIN.configure(text=sensor11)
    # kirish qismidagi jadval bo'yicha
    cub = " Select kub from suvhajmi where sensor_id=41 and obekt_id=%s  "   ###
    mycursor.execute(cub,[obekt])
    massiv = mycursor.fetchall()


    sensor11CM = int(sensor11 * 100)+farqSath1
    if sensor11CM < 240:
        kub1 = massiv[sensor11CM][0]

        labelINCub.configure(text=kub1)
    else:
        labelINCub.configure(text="not found")
    labelINCub.configure(text=kub1)



    # sensor12 uchun
    mycursor.execute("SELECT reykasathi FROM s_sensor where sensor_id=2 and obekt_id=%s ",[obekt])
    reyka_height = mycursor.fetchone()[0]

    mycursor.execute("SELECT sensorsathi FROM s_sensor where sensor_id=2 and obekt_id=%s ",[obekt])
    water_height = mycursor.fetchone()[0]
    totalHeight = float(reyka_height + water_height)

    if sensr != 0:
        try:
         sensor12b = str(watersensor2.read_register(1, 0, 3))
        except:
            sensorXatoSql6 = "INSERT INTO xato_sensor(sensor_id,status,obekt_id)VALUES (%s,%s,%s)"
            valSensorxato6 = (8, 'Sensor ishlamadi',obekt)
            mycursor.execute(sensorXatoSql6, valSensorxato6)
            sensor12b=labelOut1.cget('text')
            labelOut1.configure(bg='black',fg="white")

    else:
        sensor12b = '2000'

    sensor12 = round(totalHeight - float(int(sensor12b) / 1000), 2)
    # #Cubini hisoblash
    cub = " Select kub from suvhajmi where sensor_id=41  and obekt_id=%s  "    # jadval berilishi kerak  sensor_id=2
    mycursor.execute(cub,[obekt])
    massiv = mycursor.fetchall()


    sensor12CM = int(sensor12 * 100)+farqSath2
    if sensor12CM < 240:
        kub2 = massiv[sensor12CM][0]
        labelOut1Cub.configure(text=kub2)
    else:
        labelOut1Cub.configure(text="not found")

    labelOut1.configure(text=sensor12)



    # sensor13 uchun
    mycursor.execute("SELECT reykasathi FROM s_sensor where s_address=3 and obekt_id=%s  ",[obekt])
    reyka_height = mycursor.fetchone()[0]

    mycursor.execute("SELECT sensorsathi FROM s_sensor where s_address=3 and obekt_id=%s  ",[obekt])
    water_height = mycursor.fetchone()[0]
    totalHeight = float(reyka_height + water_height)
    if sensr != 0:
        try:
         sensor13b = str(watersensor3.read_register(1, 0, 3))
        except:
            sensorXatoSql = "INSERT INTO xato_sensor(sensor_id,status,obekt_id)VALUES (%s,%s,%s)"
            valSensorxato = (7, 'Sensor ishlamadi',obekt)
            mycursor.execute(sensorXatoSql, valSensorxato)
            sensor13b=labelOut2.cget('text')
            labelOut2.configure(bg='black',fg="white")
    else:
        sensor13b = '2000'
    sensor13 = round(totalHeight - float(int(sensor13b) / 1000), 2)
    cub = " Select kub from suvhajmi where sensor_id=41  and obekt_id=%s "  # jadval berilishi kerak  sensor_id=3


    mycursor.execute(cub,[obekt])
    massiv = mycursor.fetchall()
    sensor13CM = int(sensor13 * 100)+farqSath3
    if sensor13CM < 240:
        kub3 = massiv[sensor13CM][0]
        labelOut2Cub.configure(text=kub3)
    else:
        labelOut2Cub.configure(text="not found")
    labelOut2.configure(text=sensor13)



    # sensor14 uchun
    mycursor.execute("SELECT reykasathi FROM s_sensor where s_address=4 and obekt_id=%s ",[obekt])
    reyka_height = mycursor.fetchone()[0]

    mycursor.execute("SELECT sensorsathi FROM s_sensor where s_address=4 and obekt_id=%s ",[obekt])
    water_height = mycursor.fetchone()[0]
    totalHeight = float(reyka_height + water_height)

    if sensr != 0:
        try:
         sensor14b = str(watersensor4.read_register(1, 0, 3))
        except:
            sensorXatoSql8 = "INSERT INTO xato_sensor(sensor_id,status,obekt_id)VALUES (%s,%s,%s)"
            valSensorxato8 = (14, 'Sensor ishlamadi',obekt)
            mycursor.execute(sensorXatoSql8, valSensorxato8)
            sensor14b=labelOut3.cget('text')
            labelOut3.configure(bg='black',fg="white")

    else:
        sensor14b = '2000'

    sensor14 = round(totalHeight - float(int(sensor14b )/ 1000), 2)
    # #Cubini hisoblash
    cub = " Select kub from suvhajmi where sensor_id=41  and obekt_id=%s  "    # jadval berilishi kerak  sensor_id=2
    mycursor.execute(cub,[obekt])
    massiv = mycursor.fetchall()

    sensor14CM = int(sensor14 * 100)+farqSath4
    if sensor14CM < 240:
        kub4 = massiv[sensor14CM][0]
        labelOut3Cub.configure(text=kub4)
    else:
        labelOut3Cub.configure(text="not found")

    labelOut3.configure(text=sensor14)

    current_time = datetime.now()

# tekshirish
    if(current_time.minute==10 or current_time.minute==20 or current_time.minute==30 or current_time.minute==40  or current_time.minute==50 or current_time.minute==60 ):
  # Bazaga yozish
    # waterSensor1

          motorSensorSql1 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,suvSathi,obekt_id,sarfi)VALUES (%s,%s,%s,%s,%s,%s)"
          valmotorSensor1 = (1, 1, 1, sensor11, obekt, kub1)
          mycursor.execute(motorSensorSql1, valmotorSensor1)
          # Watersensor2
          waterSensorSql2 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,suvSathi,obekt_id,sarfi)VALUES (%s,%s,%s,%s,%s,%s)"
          valwaterSensor2 = (1, 2, 1, sensor12, obekt, kub2)
          mycursor.execute(waterSensorSql2, valwaterSensor2)


              # waterSensor3

          waterSensorSql3 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,suvSathi,obekt_id,sarfi)VALUES (%s,%s,%s,%s,%s,%s)"
          valwaterSensor3 = (1, 3, 1, sensor13, obekt, kub3)
          mycursor.execute(waterSensorSql3, valwaterSensor3)


           # waterSensor4


          waterSensorSql4 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,suvSathi,obekt_id,sarfi)VALUES (%s,%s,%s,%s,%s,%s)"
          valwaterSensor4 = (1, 4, 1, sensor14, obekt, kub4)
          mycursor.execute(waterSensorSql4, valwaterSensor4)



    mydb.commit()
    labelmotorSensor1.after(60000, water_sensor)

window = Tk()
newWindow=ttk.Notebook(window)
firstWindow=Frame(newWindow,bg="Khaki")
secondWindow=Frame(newWindow)
thirdWindow=Frame(newWindow)
newWindow.add(thirdWindow,text="hisobot")
newWindow.add(secondWindow,text="user")

newWindow.add(firstWindow,text="Settings")


newWindow.pack(expand=True,fill="both")
window.title('SUV INSHOATI NAZORATI')
window.geometry('1200x700')
window.configure(bg="#0099cc")

label = Label(secondWindow,text='Buyruq ', fg='white', bg='black', width=7, font=('italic', 12, 'bold'))

label2b = Label(secondWindow, text= str(asos[0]) , fg='black', bg='white', width=4,
               font=('italic', 16, 'bold'))
label2b.grid(row=1, column=1,columnspan=2 )

label3 = Label(secondWindow, text= str(sana) , fg='black', bg='white', width=16,
               font=('italic', 16, 'bold'))
label3.grid(row=1, column=3 )

label2k = Label(secondWindow, text=' kub ', fg='orange', bg='blue', width=3,
               font=('italic', 14, 'bold'))
label2k.grid(row=1, column=2)
label.grid(row=1,column=1,padx=4)
Label(secondWindow,text='surjina sathi /m').grid(row=2,column=2,padx=1,pady=8)
Label(secondWindow,text='bosilgandagi sathi /m').grid(row=2,column=3,padx=1,pady=8)
Label(secondWindow,text='qanchaga kutarilishi /m').grid(row=2,column=4,padx=1,pady=8)

label1 = Label(secondWindow,text='1', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold'))
label1.grid(row=3, column=1, padx=3,pady=6)

labelmotorSensor1 = Label(secondWindow,font=('Arial', 20), bg='white', fg='blue', width=5, bd=2,relief=SUNKEN)
labelmotorSensor1.grid(row=3, column=2)

sath1 = Label(secondWindow,font=('Arial', 20),text='', bg='white', fg='blue', width=5, bd=2, relief=SUNKEN)
sath1.grid(row=3, column=3,padx=0)
button11 = Button(secondWindow, width=5, command=on1, text='tepaga', fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=3, column=5, padx=1, pady=6)
button12 = Button(secondWindow, width=5, command=off1, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=3, column=6, padx=3, pady=6)
button13 = Button(secondWindow, width=5, command=on2, text='pastga', fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=3, column=7, padx=1, pady=6)

label2 = Label(secondWindow,text='2', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=4, column=1, padx=1,
                                                                                             pady=6)
labelmotorSensor2 = Label(secondWindow,font=('Arial', 20), bg='white', fg='black', width=5, bd=2,
                     relief=SUNKEN)
labelmotorSensor2.grid(row=4, column=2)
sath2 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
              relief=SUNKEN)
sath2.grid(row=4, column=3)
button21 = Button(secondWindow, width=5, command=on3, text='tepaga', fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=4, column=5, padx=1, pady=3)
button22 = Button(secondWindow,width=5, command=off2, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=4, column=6, padx=3, pady=6)
button23 = Button(secondWindow, width=5, command=on4, text='pastga', fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=4, column=7, padx=1, pady=6)

label3 = Label(secondWindow,text='3', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=5, column=1, padx=1,
                                                                                             pady=6)
labelmotorSensor3 = Label(secondWindow,font=('Arial', 20), text=' ', bg='white', fg='blue', width=5, bd=2,
                     relief=SUNKEN)
labelmotorSensor3.grid(row=5, column=2)
sath3 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
              relief=SUNKEN)
sath3.grid(row=5, column=3)
button31 = Button(secondWindow, width=5, text='tepaga', command=on5, fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=5, column=5, padx=1, pady=6)
button32 = Button(secondWindow, width=5, text='stop', command=off3, fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=5, column=6, padx=1, pady=6)
button33 = Button(secondWindow, width=5, text='pastga', command=on6, fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=5, column=7, padx=1, pady=6)


label4 = Label(secondWindow,text='4', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold'))
label4.grid(row=6, column=1, padx=3,pady=6)

labelmotorSensor4 = Label(secondWindow,font=('Arial', 20), bg='white', fg='blue', width=5, bd=2,relief=SUNKEN)
labelmotorSensor4.grid(row=6, column=2)

sath4 = Label(secondWindow,font=('Arial', 20),text='', bg='white', fg='blue', width=5, bd=2, relief=SUNKEN)
sath4.grid(row=6, column=3,padx=0)
button41 = Button(secondWindow, width=5, command=on7, text='tepaga', fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=6, column=5, padx=1, pady=6)
button42 = Button(secondWindow, width=5, command=off4, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=6, column=6, padx=3, pady=6)
button43 = Button(secondWindow, width=5, command=on8, text='pastga', fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=6, column=7, padx=1, pady=6)

label5 = Label(secondWindow,text='5', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=7, column=1, padx=1,
                                                                                             pady=6)
labelmotorSensor5 = Label(secondWindow,font=('Arial', 20), bg='white', fg='black', width=5, bd=2,
                     relief=SUNKEN)
labelmotorSensor5.grid(row=7, column=2)
sath5 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
              relief=SUNKEN)
sath5.grid(row=7, column=3)
button51 = Button(secondWindow, width=5, command=on9, text='tepaga', fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=7, column=5, padx=1, pady=3)
button52 = Button(secondWindow,width=5, command=off5, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=7, column=6, padx=3, pady=6)
button53 = Button(secondWindow, width=5, command=on10, text='pastga', fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=7, column=7, padx=1, pady=6)

label6 = Label(secondWindow,text='6', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=8, column=1, padx=1,
                                                                                             pady=6)
labelmotorSensor6 = Label(secondWindow,font=('Arial', 20), text=' ', bg='white', fg='blue', width=5, bd=2,
                     relief=SUNKEN)
labelmotorSensor6.grid(row=8, column=2)
sath6 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
              relief=SUNKEN)
sath6.grid(row=8, column=3)
button61 = Button(secondWindow, width=5, text='tepaga', command=on11, fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=8, column=5, padx=1, pady=6)
button62 = Button(secondWindow, width=5, text='stop', command=off6, fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=8, column=6, padx=1, pady=6)
button63 = Button(secondWindow, width=5, text='pastga', command=on12, fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=8, column=7, padx=1, pady=6)


label7 = Label(secondWindow,text='7', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=9, column=1, padx=1,  pady=6)
labelmotorSensor7 = Label(secondWindow,font=('Arial', 20), text=' ', bg='white', fg='blue', width=5, bd=2,relief=SUNKEN)
labelmotorSensor7.grid(row=9, column=2)
sath7 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
              relief=SUNKEN)
sath7.grid(row=9, column=3)
button71 = Button(secondWindow, width=5, text='tepaga', command=on13, fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=9, column=5, padx=1, pady=6)
button72 = Button(secondWindow, width=5, text='stop', command=off7, fg='white', bg='red', font=('italic', 14, 'bold')).grid(row=9, column=6, padx=1, pady=6)
button73 = Button(secondWindow, width=5, text='pastga', command=on14, fg='black', bg='yellow', font=('italic', 14, 'bold')).grid(row=9, column=7, padx=1, pady=6)


label8 = Label(secondWindow,text='8', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=10, column=1, padx=1,                                                                                    pady=6)
labelmotorSensor8 = Label(secondWindow,font=('Arial', 20), text=' ', bg='white', fg='blue', width=5, bd=2,  relief=SUNKEN)
labelmotorSensor8.grid(row=10, column=2)
sath8 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,  relief=SUNKEN)
sath8.grid(row=10, column=3)
button81 = Button(secondWindow, width=5, text='tepaga', command=on15, fg='white', bg='green',    font=('italic', 14, 'bold')).grid(row=10, column=5, padx=1, pady=6)
button82 = Button(secondWindow, width=5, text='stop', command=off8, fg='white', bg='red', font=('italic', 14, 'bold')).grid(row=10, column=6, padx=1, pady=6)
button83 = Button(secondWindow, width=5, text='pastga', command=on16, fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=10, column=7, padx=1, pady=6)



inWater=Label(secondWindow,font=('Arial', 16), text='suv sathi', bg='white', fg='blue', width=8, bd=2,
                     relief=SUNKEN)
inWater.grid(row=12, column=2, padx=1, pady=6)
inWaterCub=Label(secondWindow,font=('Arial', 16), text='suv hajmi', bg='white', fg='blue', width=8, bd=2,
                     relief=SUNKEN)
inWaterCub.grid(row=12, column=3, padx=2, pady=6)
labelInZey = Label(secondWindow,text='IN', fg='white', bg='blue', width=7, font=('italic', 16, 'bold')).grid(row=13, column=1, padx=1, pady=6)
labelOutPlovon = Label(secondWindow,text='Out1', fg='white', bg='blue', width=7, font=('italic', 16, 'bold')).grid(row=14, column=1, padx=1, pady=6)
labelOutPut2 = Label(secondWindow,text='Out2  ', fg='white', bg='blue', width=10, font=('italic', 12, 'bold')).grid(row=15,column=1, padx=3,                                                                                                               pady=6)
labelOutPut3 = Label(secondWindow,text='Out3  ', fg='white', bg='blue', width=10, font=('italic', 12, 'bold')).grid(row=16,column=1, padx=3,                                                                                                               pady=6)

labelIN = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelIN.grid(row=13, column=2)
labelOut1 = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut1.grid(row=14, column=2)
labelOut1Cub = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut1Cub.grid(row=15, column=3)

labelINCub = Label(secondWindow,text='2', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelINCub.grid(row=13, column=3)
labelOut2Cub = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut2Cub.grid(row=14, column=3)
labelOut3Cub = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut3Cub.grid(row=16, column=3)

labelOut2 = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut2.grid(row=15, column=2)

labelOut3 = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut3.grid(row=16, column=2)

firstButton=Button(firstWindow,text='registr',bg='#00ffff',command=modalRegistr,width='12',font=('italic', 14, 'bold'))
firstButton.grid(row=1,column=1,padx=55,pady=160)
firstButton2=Button(firstWindow,text='farq',bg='yellow',width='12',font=('italic', 14, 'bold'))
firstButton2.grid(row=1,column=2,padx=35,pady=160)
firstButton3=Button(firstWindow,text='lavozim',bg='#00ffff',width='12',font=('italic', 14, 'bold'))
firstButton3.grid(row=1,column=3,padx=35,pady=160)

firstButton4=Button(firstWindow,text='user',bg='yellow',width='12',font=('italic', 14, 'bold'))
firstButton4.grid(row=1,column=4,padx=35,pady=160)
firstButton5=Button(firstWindow,text='otdel',bg='#00ffff',width='12',font=('italic', 14, 'bold'))
firstButton5.grid(row=1,column=5,padx=35,pady=160)

# Add Calendar
fromcal = Calendar(thirdWindow, selectmode='day', year=2022, month=3, day=26)
fromcal.grid(row=1,column=1,padx=20,pady=20)# Add Calendar
tocal = Calendar(thirdWindow, selectmode='day',year=2022, month=4,day=15)
tocal.grid(row=1,column=2,padx=20,pady=20)


def grad_date():
    fromDate=datetime.strptime((fromcal.get_date()+' 00:00:00'),"%m/%d/%y %H:%M:%S")
    # fromDate2=datetime.strptime(fromcal.get_date(),"%b/%d/%Y")
    toDate= datetime.strptime((tocal.get_date()+' 23:59:59'),"%m/%d/%y %H:%M:%S")
    time_interval=toDate-fromDate
    date.config(text="Selected Date is: " + fromcal.get_date())
    date2.config(text="Selected Date is: " + tocal.get_date())
    sql1="Select id, sarfi,sana from water_sensor where obekt_id=%s and sensor_id=1 and sana  between %s and %s"
    sql2="Select id, sarfi,sana from water_sensor where obekt_id=%s and sensor_id=2 and sana  between %s and %s"
    sql3="Select id, sarfi,sana from water_sensor where obekt_id=%s and sensor_id=3 and sana  between %s and %s"
    sql4="Select id, sarfi,sana from water_sensor where obekt_id=%s and sensor_id=4 and sana  between %s and %s"

    mycursor.execute(sql1,[obekt,fromDate,toDate])
    massivsensor1=mycursor.fetchall()

    mycursor.execute(sql2,[obekt,fromDate,toDate])
    massivsensor2=mycursor.fetchall()

    mycursor.execute(sql3,[obekt,fromDate,toDate])
    massivsensor3=mycursor.fetchall()

    mycursor.execute(sql4,[obekt,fromDate,toDate])
    massivsensor4=mycursor.fetchall()
    mydb.commit()
    workbook = xlsxwriter.Workbook('D:/data.xlsx')
    worksheet = workbook.add_worksheet()
    # Widen column A for extra visibility.

    # print( massivsensor1[1][2])
    # print(massivsensor1[1][0])
    # print( massivsensor1[0][2])
    # print(massivsensor1[0][0])
    # o=massivsensor1[1][2]-massivsensor1[0][2]
    # print(o.total_seconds())

    writeSensorinDatabase=300
    worksheet.set_column('A:A', 14)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('D:D', 16)
# A number to convert to a date.
    format5 = workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})
    format2 = workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})
    uzunlik1 =len(massivsensor1)
    uzunlik2 =len(massivsensor2)
    uzunlik3 =len(massivsensor3)
    uzunlik4 =len(massivsensor4)

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#ADD8E6'})
    merge_format2 = workbook.add_format({
            'bold': 1,
            'border': 1,
            'valign': 'vcenter',
            'fg_color': '#ADD8E6'})
    merge_format4 = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#90EE90'})
    merge_format3 = workbook.add_format({
            'bold': 1,
            'border': 1,
            'valign': 'vcenter',
            'fg_color': 'yellow'})

    worksheet.merge_range('A1:G1', 'Uchtom suv omboridagi suv sarfi haqida', merge_format)
    worksheet.merge_range('A2:G2', fromcal.get_date()+" dan "+tocal.get_date()+"gacha bo'lgan davrda" , merge_format)
    worksheet.merge_range('A3:G3', "suv sarfini hisoblash" , merge_format)
    worksheet.merge_range('A4:G4', "1-datchik" , merge_format3)
    worksheet.write("A5","№ ",merge_format2)
    worksheet.write("B5","Boshlanish ",merge_format2)
    worksheet.write("C5","sarf ",merge_format2)
    worksheet.write("D5","Jami  ",merge_format2)

    total1=0
    for x in range(1,uzunlik1):
          total1=total1+massivsensor1[x][1]*writeSensorinDatabase

          worksheet.write('A'+str(x+5), x)       # 28/02/13 12:00
          worksheet.write('B'+str(x+5), massivsensor1[x][2],format5)
          #datetime.strptime('4/22/16 10:00:00',"%m/%d/%y %H:%M:%S") 28/02/13 12:00
         # worksheet.write('C'+str(x), totals)    # 28/02/13 12:00
          worksheet.write('C'+str(x+5), massivsensor1[x][1])       # 28/02/13 12:00
          worksheet.write('D'+str(x+5), massivsensor1[x][1]*writeSensorinDatabase)       # 28/02/13 12:00

    worksheet.merge_range('B' + str(uzunlik1 + 5)+':'+'C' + str(uzunlik1 + 5), "Umumiy 1-datchikdagi rasxod", merge_format)
    worksheet.write('D' + str(uzunlik1 + 5), total1)

    worksheet.write('A'+ str(uzunlik1 + 7),"2-datchikdagi  ",merge_format3)
    worksheet.write('A'+ str(uzunlik1 + 8),"№",merge_format2)
    worksheet.write('B'+ str(uzunlik1 + 8),"Boshlanish ",merge_format2)
    worksheet.write('C'+ str(uzunlik1 + 8)," Sarfi",merge_format2)
    worksheet.write('D'+ str(uzunlik1 + 8),"Jami ",merge_format2)

    total2=0
    for x in range(1,uzunlik2):
          total2=total2+massivsensor2[x][1]*writeSensorinDatabase

          worksheet.write('A' + str(x+uzunlik1 + 8), x)  # 28/02/13 12:00
          worksheet.write('B' + str(x + uzunlik1 + 8), massivsensor2[x][2], format5)
          # datetime.strptime('4/22/16 10:00:00',"%m/%d/%y %H:%M:%S") 28/02/13 12:00
          # worksheet.write('C'+str(x), totals)    # 28/02/13 12:00
          worksheet.write('C' + str(x + uzunlik1 + 8), massivsensor2[x][1])  # 28/02/13 12:00
          worksheet.write('D' + str(x + uzunlik1 + 8), massivsensor2[x][1] * writeSensorinDatabase)  #delta time qo'yish kerak

    worksheet.merge_range('A' + str(uzunlik1+uzunlik2 + 9)+':'+'C' + str(uzunlik1 + uzunlik2+9), "Umumiy 2-datchikdagi rasxod", merge_format)
    worksheet.write('D' + str(uzunlik1 + uzunlik2+9), total2)


    worksheet.write('A'+ str(uzunlik1+uzunlik2 + 10),"3-datchikdagi  ",merge_format3)
    worksheet.write('A'+ str(uzunlik1 +uzunlik2+ 11),"№",merge_format2)
    worksheet.write('B'+ str(uzunlik1 +uzunlik2+ 11),"Boshlanish ",merge_format2)
    worksheet.write('C'+ str(uzunlik1 +uzunlik2+ 11)," Sarfi",merge_format2)
    worksheet.write('D'+ str(uzunlik1+uzunlik2 + 11),"Jami ",merge_format2)

    total3=0
    for x in range(1,uzunlik3):
          total3=total3+massivsensor3[x][1]*writeSensorinDatabase

          worksheet.write('A' + str(x  +uzunlik1+uzunlik2 + 11), x)  # 28/02/13 12:00
          worksheet.write('B' + str(x + uzunlik1+uzunlik2 + 11), massivsensor3[x][2], format5)
          worksheet.write('C' + str(x + uzunlik1+uzunlik2 + 11), massivsensor3[x][1])  # 28/02/13 12:00
          worksheet.write('D' + str(x + uzunlik1 +uzunlik2+ 11), massivsensor3[x][1] * writeSensorinDatabase)  #delta time qo'yish kerak

    worksheet.merge_range('A' + str(uzunlik1+uzunlik2+uzunlik3+ 12)+':'+'C' + str(uzunlik1 +uzunlik3+ uzunlik2+12), "Umumiy 3-datchikdagi rasxod", merge_format)
    worksheet.write('D' + str(uzunlik1 + uzunlik2+uzunlik3+12), total2)


    worksheet.write('A'+ str(uzunlik1+ uzunlik2+uzunlik3 + 13),"4-datchikdagi  ",merge_format3)
    worksheet.write('A'+ str(uzunlik1 + uzunlik2+uzunlik3+ 14),"№",merge_format2)
    worksheet.write('B'+ str(uzunlik1 + uzunlik2+uzunlik3+ 14),"Boshlanish ",merge_format2)
    worksheet.write('C'+ str(uzunlik1 + uzunlik2+uzunlik3+ 14)," Sarfi",merge_format2)
    worksheet.write('D'+ str(uzunlik1 + uzunlik2+uzunlik3+ 14),"Jami ",merge_format2)

    total4=0
    for x in range(1,uzunlik4):
          total4=total4+massivsensor4[x][1]*writeSensorinDatabase

          worksheet.write('A' + str(x  +uzunlik1 + uzunlik2+uzunlik3+14), x)  # 28/02/13 12:00
          worksheet.write('B' + str(x + uzunlik1 + uzunlik2+uzunlik3+14), massivsensor4[x][2], format5)
          worksheet.write('C' + str(x + uzunlik1+ uzunlik2+uzunlik3 +14), massivsensor4[x][1])  # 28/02/13 12:00
          worksheet.write('D' + str(x + uzunlik1+ uzunlik2+uzunlik3 +14), massivsensor4[x][1] * writeSensorinDatabase)  #delta time qo'yish kerak

    worksheet.merge_range('A' + str(uzunlik1+uzunlik2 +uzunlik3+uzunlik4+ 15)+':'+'C' + str(uzunlik1 +uzunlik3+uzunlik4+ uzunlik2+15), "Umumiy 4-datchikdagi rasxod", merge_format)
    worksheet.write('D' + str(uzunlik1 + uzunlik2+uzunlik3+uzunlik4+15), total2)
    worksheet.merge_range('A' + str(uzunlik1+uzunlik2+uzunlik3+uzunlik4 + 16)+':'+'C' + str(uzunlik1 +uzunlik3+uzunlik4+ uzunlik2+16), "Umumiy  rasxod", merge_format4)
    worksheet.write('D' + str(uzunlik1 + uzunlik2+uzunlik3+uzunlik4+16), total2+total1+total3+total4)

    workbook.close()
# Add Button and Label
Button(thirdWindow, text="Hisobot",
       command=grad_date,bg='#00ffff',width='12',font=('italic', 14, 'bold')).grid(row=2,column=2,columnspan=2,padx=320,pady=20)

date = Label(thirdWindow, text="")
date.grid(row=3,column=1,padx=20,pady=20)

date2 = Label(thirdWindow, text="")
date2.grid(row=3,column=2,padx=20,pady=20)


motor_sensor()

water_sensor()
ogoh()
window.mainloop()

