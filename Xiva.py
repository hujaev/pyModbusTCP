from tkinter import *
from tkinter.ttk import Progressbar

import mysql.connector
import time
import serial
import progressbar
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
sensr = 1
global onoff1, onoff2, onoff3, onoff4, onoff5, onoff6, onoff7, onoff8, res, \
    mtakror1, wtakror1, \
    mtakror2, wtakror2, \
    mtakror3, wtakror3

mtakror1 = 1
mtakror2 = 1
mtakror3 = 1

wtakror1 = 1
wtakror2 = 1
wtakror3 = 1
global motorSensor1,mfoiz2,mfoiz3,mfoiz1 ,oraliq1, oraliq2, oraliq3, labOldmotorSensor1, \
    labOldmotorSensor2, labOldmotorSensor3, motorSensor2, motorSensor3, \
    motorSensor2a, motorSensor1a, motorSensor3a
motorSensor1a = '1110'
motorSensor2a = '1150'
motorSensor3a = '1100'
oraliq1 = 0.0
oraliq2 = 0.0
oraliq3 = 0.0
mfoiz2=0
mfoiz3=0
mfoiz1=0
labOldmotorSensor1 = 110.0
labOldmotorSensor2 = 150
labOldmotorSensor3 = 200

motorSensor1 = 0
motorSensor2 = 0
motorSensor3 = 0

# Mysql ulash
mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='water')
mycursor = mydb.cursor()
# programma qo'yilgan obekt
obekt = "Select obekt from setup"
mycursor.execute(obekt)
obekt = mycursor.fetchone()[0]
# Comport o'zgartirish
mycursor.execute("SELECT comport FROM s_obekt where id=%s", [obekt])
exCom = mycursor.fetchone()[0]
comport = 'COM' + str(exCom)
# buyruqdagi suv hajmi
buyruqhajmi = "Select kub,sana from asos where obekt_id=%s order by id desc limit 1"
mycursor.execute(buyruqhajmi, [obekt])
# asos massiv oldingi buyruq1
asos = mycursor.fetchone()
# buyruq berilgan sana
sana = asos[1]

# adress olish
mycursor.execute("Select m_address,s_address,min,max,m_id,activ from s_motor where  obekt_id=%s order by m_id ",
                 [obekt])
s_motor = mycursor.fetchall()

mycursor.execute("Select r_id,address from s_rele where obekt_id=%s ", [obekt])
s_rele = mycursor.fetchall()
# me'yordan   kop suv o'tish chegarasi

mycursor.execute("Select ogoh,alarm,m_soni,s_soni,rele_soni  from s_obekt where id=%s ", [obekt])
s_obekt = mycursor.fetchone()

rele_soni = s_obekt[4]
m_soni = s_obekt[2]
s_soni = s_obekt[3]
ogoh1 = s_obekt[0]
alarm1 = s_obekt[1]
# me'yordan  juda kop suv o'tish chegarasi
if (rele_soni > 0):
    if (sensr == 0):
        motorKalit1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
        motorKalit1.serial.baudrate = 9600
        motorKalit1.serial.bytesize = 8
        motorKalit1.serial.parity = serial.PARITY_NONE
        motorKalit1.serial.stopbits = 1
        motorKalit1.serial.timeout = 2  # seconds
        motorKalit1.address = s_rele[0][1]  # motor datchiklar 4, 3, 2   uchun Xiva

if (rele_soni > 1):
    if (sensr == 1):
        motorKalit2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
        motorKalit2.serial.baudrate = 9600
        motorKalit2.serial.bytesize = 8
        motorKalit2.serial.parity = serial.PARITY_NONE
        motorKalit2.serial.stopbits = 1
        motorKalit2.serial.timeout = 2  # seconds
        motorKalit2.address = s_rele[1][1]  # motor datchiklar 4, 3, 2   uchun Xiva

if (rele_soni > 2):
    if (sensr == 1):
        motorKalit3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
        motorKalit3.serial.baudrate = 9600
        motorKalit3.serial.bytesize = 8
        motorKalit3.serial.parity = serial.PARITY_NONE
        motorKalit3.serial.stopbits = 1
        motorKalit3.serial.timeout = 2  # seconds
        motorKalit3.address = s_rele[2][1]  # motor datchiklar 4, 3, 2   uchun Xiva

motor1 = 1
if (m_soni > 0):
    if (s_motor[0][5] == 1):
        max1 = s_motor[0][3]
        pastki_sath1 = s_motor[0][2]
        if (sensr == 0):
            motorsensor1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
            motorsensor1.serial.baudrate = 9600
            motorsensor1.serial.bytesize = 8
            motorsensor1.serial.parity = serial.PARITY_NONE
            motorsensor1.serial.stopbits = 1
            motorsensor1.serial.timeout = 2  # seconds
            motorsensor1.address = s_motor[0][1]
            motorsensor1.mode = minimalmodbus.MODE_RTU

    else:
        motor1 = -1
else:
    motor1 = 0

motor2 = 1
if (m_soni > 1):
    if (s_motor[1][5] == 1):
        max2 = s_motor[1][3]
        pastki_sath2 = s_motor[1][2]

        if (sensr == 0):
            motorsensor2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
            motorsensor2.serial.baudrate = 9600
            motorsensor2.serial.bytesize = 8
            motorsensor2.serial.parity = serial.PARITY_NONE
            motorsensor2.serial.stopbits = 1
            motorsensor2.serial.timeout = 2  # seconds
            motorsensor2.address = s_motor[1][1]
            motorsensor2.mode = minimalmodbus.MODE_RTU
    else:
        motor2 = -1
else:
    motor2 = 0

motor3 = 1
if (m_soni > 2):
    if (s_motor[2][5] == 1):
        max3 = s_motor[2][3]
        pastki_sath3 = s_motor[2][2]
        if (sensr == 0):
            motorsensor3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
            motorsensor3.serial.baudrate = 9600
            motorsensor3.serial.bytesize = 8
            motorsensor3.serial.parity = serial.PARITY_NONE
            motorsensor3.serial.stopbits = 1
            motorsensor3.serial.timeout = 2  # seconds
            motorsensor3.address = s_motor[2][1]
            motorsensor3.mode = minimalmodbus.MODE_RTU

    else:
        motor3 = -1
else:
    motor3 = 0

if sensr == 0:
    onoff1 = 0
    onoff2 = 0
    onoff3 = 0


    watersensor1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor1.serial.baudrate = 9600
    # baudrate
    watersensor1.serial.bytesize = 8
    watersensor1.serial.parity = serial.PARITY_NONE
    watersensor1.serial.stopbits = 1
    watersensor1.serial.timeout = 2
    watersensor1.address = 5
    watersensor1.mode = minimalmodbus.MODE_RTU

    watersensor2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor2.serial.baudrate = 9600
    # baudrate
    watersensor2.serial.bytesize = 8
    watersensor2.serial.parity = serial.PARITY_NONE
    watersensor2.serial.stopbits = 1
    watersensor2.serial.timeout = 2
    watersensor2.address = 6
    watersensor2.mode = minimalmodbus.MODE_RTU

    watersensor3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor3.serial.baudrate = 9600
    # baudrate
    watersensor3.serial.bytesize = 8
    watersensor3.serial.parity = serial.PARITY_NONE
    watersensor3.serial.stopbits = 1
    watersensor3.serial.timeout = 2
    watersensor3.address = 7
    watersensor3.mode = minimalmodbus.MODE_RTU


else:
    onoff1 = 10  # simulyator
    onoff2 = 10
    onoff3 = 10





def ogoh():
    labelin = w_lbl_in_cub.cget('text')
    if (float(asos[0]) + ogoh1 < float(labelin) and float(labelin) < float(asos[0]) + alarm1):
        player = pyglet.media.Player()
        song = 'ogoh.mp3'
        src = pyglet.media.load(song)
        player.queue(src)

        def play():
            player.play()

        play()
    elif (float(float(asos[0]) + alarm1) < float(labelin)):
        player = pyglet.media.Player()
        song = 'alarm.mp3'
        src = pyglet.media.load(song)
        player.queue(src)

        def play():
            player.play()

        play()
    w_lbl_in_cub.after(15000, ogoh)



def on1():
    global onoff1, labOldmotorSensor1, oraliq1
    labOldmotorSensor1 = float(m_sensor_lbl_input_1.cget("text"))
    if onoff1 != 11:
        res11 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        try:
            oraliq1 = float(int(res11) / 100)
            # pastki_sath1 - max1=1.45
            print(onoff1)
            if(sensr==0):
              onoff1=11
            elif(sensr==1):
              onoff1=1
            if(oraliq1+labOldmotorSensor1>pastki_sath1 - max1):
                pyautogui.alert(text="Siz kiritgan son meyordan ortiqcha ")
                if (sensr == 0):
                    onoff1 = 10
                elif (sensr == 1):
                    onoff1 = 0


            else:
                labOldmotorSensor1 = float(m_sensor_lbl_input_1.cget("text"))
                labelOldmotorSensor1 = Label(secondWindow, text=str(labOldmotorSensor1), bg="grey", fg="white", width=7,
                                             font=('italic', 16, 'bold'))
                labelOldmotorSensor1.grid(row=3, column=5)
                m_up_input1.configure(text=str(res11))
        except:
            res = pyautogui.alert(text="Siz maydonni bo'sh qoldirdingiz yoki simvol kiritdiz qayta urinib ko'ring", title='Oraliq masofa', )
        if sensr != 0:
            if (onoff1 == 1):
                try:

                    motorKalit1.write_register(2, 0x0200)
                    motorKalit1.write_register(1, 0x0100)
                except:
                    pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return




def on3():
    global onoff2, labOldmotorSensor2, oraliq2
    labOldmotorSensor2 = float(m_sensor_lbl_input_2.cget("text"))
    if onoff2 != 11:
        res21 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        try:
            oraliq2 = float(int(res21) / 100)
            if (sensr == 0):
                onoff2 = 11
            elif (sensr == 1):
                onoff2 = 1
            if (oraliq2 + labOldmotorSensor2 > pastki_sath2 - max2):
                pyautogui.alert(text="Siz kiritgan son meyordan ortiqcha ")
                print(onoff2)
                if (sensr == 0):
                    onoff2 = 10
                elif (sensr == 1):
                    onoff2 = 0
            else:
                labOldmotorSensor2 = float(m_sensor_lbl_input_2.cget("text"))
                labelOldmotorSensor2 = Label(secondWindow, text=str(labOldmotorSensor2), bg="grey", fg="white", width=7,
                                             font=('italic', 16, 'bold'))
                labelOldmotorSensor2.grid(row=4, column=5)
                m_up_input2.configure(text=str(res21))
        except:
            res = pyautogui.alert(text="Siz maydonni bo'sh qoldirdingiz yoki simvol kiritdiz qayta urinib ko'ring", title='Oraliq masofa', )
        if sensr != 0:
            if (onoff2 != 1):
                try:
                    onoff2 = 1
                    motorKalit1.write_register(4, 0x0200)
                    motorKalit1.write_register(3, 0x0100)
                except:
                    pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return


def on5():
    global onoff3, labOldmotorSensor3, oraliq3
    labOldmotorSensor3 = float(m_sensor_lbl_input_3.cget("text"))
    if onoff3 != 11:

        res31 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res31 == None:
            return
        try:
            oraliq3 = float(int(res31) / 100)
            if (sensr == 0):
                onoff3 = 11
            elif (sensr == 1):
                onoff3 = 1
            if (oraliq3 + labOldmotorSensor3 > pastki_sath3 - max3):
                pyautogui.alert(text="Siz kiritgan son meyordan ortiqcha ")
                print(onoff3)
                if (sensr == 0):
                    onoff3 = 10
                elif (sensr == 1):
                    onoff3 = 0

            else:
                labOldmotorSensor3 = float(m_sensor_lbl_input_3.cget("text"))
                labelOldmotorSensor3 = Label(secondWindow, text=str(labOldmotorSensor3), bg="grey", fg="white", width=7,
                                             font=('italic', 16, 'bold'))
                labelOldmotorSensor3.grid(row=5, column=5)
                m_up_input3.configure(text=str(res31))
        except:
            res = pyautogui.alert(
                text="Siz maydonni bo'sh qoldirdingiz yoki simvol kiritdiz qayta urinib ko'ring",
                title='Oraliq masofa', )

        if sensr != 0:
            if (onoff3 != 1):
                try:
                    onoff3 = 1
                    motorKalit1.write_register(6, 0x0200)
                    motorKalit1.write_register(5, 0x0100)
                except:
                    pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return
def on2():
    global onoff1, labOldmotorSensor1, oraliq1

    labOldmotorSensor1 = float(m_sensor_lbl_input_1.cget("text"))
    if onoff1 != 12:

        res12 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        try:
            oraliq1 = float(int(res12) / 100)
            if (sensr == 0):
                onoff1 = 12
            elif (sensr == 1):
                onoff1 = 2
            if (-oraliq1 + labOldmotorSensor1 < 0):
                pyautogui.alert(text="Siz kiritgan son meyordan ortiqcha ")
                print(onoff1)
                if (sensr == 0):
                    onoff1 = 10
                elif (sensr == 1):
                    onoff1 = 0
            else:
                labOldmotorSensor1 = float(m_sensor_lbl_input_1.cget("text"))
                labelOldmotorSensor1 = Label(secondWindow, text=str(labOldmotorSensor1), bg="grey", fg="white", width=7,
                                             font=('italic', 16, 'bold'))
                labelOldmotorSensor1.grid(row=3, column=5)
                m_up_input1.configure(text="-"+str(res12))
        except:
            res = pyautogui.alert(text="Siz maydonni bo'sh qoldirdingiz yoki simvol kiritdiz qayta urinib ko'ring",
                                  title='Oraliq masofa', )
        if sensr != 0:
            if (onoff1!= 2):
                try:
                    onoff1 = 2
                    motorKalit1.write_register(1, 0x0200)
                    motorKalit1.write_register(2, 0x0100)
                except:
                    pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return
def on4():
    global onoff2, labOldmotorSensor2, oraliq2
    labOldmotorSensor2 = float(m_sensor_lbl_input_2.cget("text"))
    if onoff2 != 12:

        res22 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        try:

            oraliq2 = float(int(res22) / 100)
            if (sensr == 0):
                onoff2 = 12
            elif (sensr == 1):
                onoff2 = 2
            if (-oraliq2 + labOldmotorSensor2 < 0):
                pyautogui.alert(text="Siz kiritgan son meyordan ortiqcha ")
                print(onoff2)
                if (sensr == 0):
                    onoff2 = 10
                elif (sensr == 1):
                    onoff2 = 0
            else:
                labOldmotorSensor2 = float(m_sensor_lbl_input_2.cget("text"))
                labelOldmotorSensor2 = Label(secondWindow, text=str(labOldmotorSensor2), bg="grey", fg="white", width=7,
                                             font=('italic', 16, 'bold'))
                labelOldmotorSensor2.grid(row=4, column=5)
                m_up_input2.configure(text="-"+str(res22))
        except:
            res = pyautogui.alert(text="Siz maydonni bo'sh qoldirdingiz yoki simvol kiritdiz qayta urinib ko'ring",
                                  title='Oraliq masofa', )

        if sensr != 0:

            if (onoff2 != 2):
                try:

                    onoff2 = 2
                    motorKalit1.write_register(3, 0x0200)
                    motorKalit1.write_register(4, 0x0100)

                except:
                    pyautogui.alert(text="signal yo'q qayta urinib ko'ring")



    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return



def on6():
    global onoff3, labOldmotorSensor3, oraliq3
    labOldmotorSensor3 = float(m_sensor_lbl_input_3.cget("text"))
    if onoff3 != 12:

        res32 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        try:

            oraliq3 = float(int(res32) / 100)
            if (sensr == 0):
                onoff3 = 12
            elif (sensr == 1):
                onoff3 = 2
            if (-oraliq3 + labOldmotorSensor3 < 0):
                pyautogui.alert(text="Siz kiritgan son meyordan ortiqcha ")
                print(onoff3)
                if (sensr == 0):
                    onoff3 = 10
                elif (sensr == 1):
                    onoff3 = 0

            else:
                labOldmotorSensor3 = float(m_sensor_lbl_input_3.cget("text"))
                labelOldmotorSensor3 = Label(secondWindow, text=str(labOldmotorSensor3), bg="grey", fg="white", width=7,
                                             font=('italic', 16, 'bold'))
                labelOldmotorSensor3.grid(row=5, column=5)
                m_up_input3.configure(text="-"+str(res32))
        except:
            res = pyautogui.alert(text="Siz maydonni bo'sh qoldirdingiz yoki simvol kiritdiz qayta urinib ko'ring",
                                  title='Oraliq masofa', )

        if sensr != 0:

            if (onoff3 != 2):
                try:

                    onoff3 = 2
                    motorKalit1.write_register(5, 0x0200)
                    motorKalit1.write_register(6, 0x0100)

                except:
                    pyautogui.alert(text="signal yo'q qayta urinib ko'ring")



    else:
        pyautogui.alert(text="motor ishlayapti to'xtashini kuting")
        return




def modalRegistr():
    modalRegistr = Tk()
    modalRegistr.geometry("600x400")
    labRegistr = Label(modalRegistr, text='Registr adress', width=13, font=('italic', 14, 'bold'))
    labRegistr.grid(row=1, column=1, padx=3, pady=3)
    entryRegistr = Entry(modalRegistr, width=7, font=('italic', 16, 'bold'))
    labRegistr.grid(row=1, column=2, padx=3, pady=3)


motorSensorSql = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
wmotorSensor1 = (1, 1, 1, 0, 4)
mycursor.execute(motorSensorSql, wmotorSensor1)


def motorSensor():
    SensorSql = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
    motorSensorSql = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,suvSathi,obekt_id)VALUES (%s,%s,%s,%s,%s)"
    wmotorSensor1 = (1, 1, 1, 0, 1)
    wmotorSensor2 = (1, 2, 1, 0, 1)
    wmotorSensor3 = (1, 3, 1, 0, 1)

    # valmotorSensor7 = (1, 7, 1, 0, obekt)
    # valmotorSensor8 = (1, 8, 1, 0, obekt)
    mycursor.execute(SensorSql, wmotorSensor1)
    mycursor.execute(SensorSql, wmotorSensor2)
    mycursor.execute(SensorSql, wmotorSensor3)


    mycursor.execute(motorSensorSql, wmotorSensor1)
    mycursor.execute(motorSensorSql, wmotorSensor2)
    mycursor.execute(motorSensorSql, wmotorSensor3)

motorSensor()

print(motorSensor2)
def motor_sensor():
    global motorSensor1a, motorSensor2a, motorSensor3a, mtakror1, mtakror2, mtakror3, \
        motorSensor1, motorSensor2, motorSensor2, motorSensor2, motorSensor3, \
        onoff1, onoff2, onoff3, onoff4, oraliq1, oraliq2, oraliq3,

    if sensr == 1:
        try:
            motorSensor1a = str(motorsensor1.read_register(1, 0, 3))
            m_sensor_lbl_input_1.configure(bg='white', fg="black")
            labelSensor1a = int(m_sensor_lbl_input_1.cget('text'))
        except:
            motorSensorXatoSql = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato = (1, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql, valmotorSensorxato)
            #motorSensor1a = labelSensor1a
            m_sensor_lbl_input_1.configure(bg='black', fg="white")

        # motorSensor2
        try:
            motorSensor2a = str(motorsensor2.read_register(1, 0, 3))
            m_sensor_lbl_input_2.configure(bg='white', fg="black")
            labelSensor2a = m_sensor_lbl_input_2.cget('text')
        except:
            print('d')
            motorSensorXatoSql2 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato2 = (2, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql2, valmotorSensorxato2)
            #motorSensor2a = labelSensor2a
            m_sensor_lbl_input_2.configure(bg='black', fg="white")
        # sensor
        try:
            motorSensor3a = str(motorsensor3.read_register(1, 0, 3))
            m_sensor_lbl_input_3.configure(bg='white', fg="black")
            labelSensor3a = str(m_sensor_lbl_input_3.cget('text'))
        except:
            motorSensorXatoSql3 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valmotorSensorxato3 = (3, 'motorSensor ishlamadi')
            mycursor.execute(motorSensorXatoSql3, valmotorSensorxato3)
            #motorSensor3a =str(labelSensor3a)
            m_sensor_lbl_input_3.configure(bg='black', fg="white")
    motorSensor1 = round(pastki_sath1 - (float(motorSensor1a) / 1000), 2)

    motorSensor2 = round(pastki_sath2 - (float(motorSensor2a) / 1000), 2)

    motorSensor3 = round(pastki_sath3 - (float(motorSensor3a) / 1000), 2)





    mfoiz2 = round(100*motorSensor2 / (pastki_sath2 - max2),1)
    mfoiz3 = round((100 * motorSensor3) / (pastki_sath3 - max3), 1)
    mfoiz1 = round(100 * motorSensor1 / (pastki_sath1 - max1), 1)
    #         Motorning ekranda kursatiladigan qiymatlari

    Label(secondWindow, text=str(mfoiz1)+"%", font=('Arial', 18), bg='white', fg='blue', width=5, bd=2, relief=SUNKEN).grid(
        row=3, column=3, padx=1, pady=8)
    Label(secondWindow, text="motor foizi", font=('Arial', 10),  fg='black', width=10).grid(
        row=2, column=3, padx=1, pady=8)
    # foizini hisoblash

    Label(secondWindow, text=str(mfoiz2) + '%', font=('Arial', 18), bg='white', fg='blue', width=5, bd=2,
          relief=SUNKEN).grid(row=4, column=3, padx=1, pady=8)
    # foizini hisoblash

    Label(secondWindow, text=str(mfoiz3) + '%', font=('Arial', 18), bg='white', fg='blue', width=5, bd=2,
          relief=SUNKEN).grid(row=5, column=3, padx=1, pady=8)

    print(motorSensor1)
    # 1-motor yuqoriga kutarilish
    if ( motorSensor1 >= oraliq1 + labOldmotorSensor1):
        if (onoff1 == 1 and sensr == 1):
            onoff1 = 0
            motorKalit1.write_register(1, 0x0200)
        if (onoff1 == 11 and sensr == 0):
            onoff1 = 10
    if (motorSensor1 >= pastki_sath1 - max1):
        if (onoff1 == 1  and sensr == 1):
            onoff1 = 0
            motorKalit1.write_register(1, 0x0200)
        if (onoff1 == 11  and sensr == 0):
            onoff1 = 10

    # 1-motor pastga tushishi
    if (motorSensor1 <= labOldmotorSensor1 - oraliq1):
        if ( onoff1 == 2 and sensr == 1):
            onoff1 = 0
            motorKalit1.write_register(2, 0x0200)
        if ( onoff1 == 12 and sensr == 0):
            onoff1=10
    if (motorSensor1 < 0.18):
        if (onoff1 == 2 and sensr == 1):
            onoff1 = 0
            motorKalit1.write_register(2, 0x0200)
        if (onoff1 == 12 and sensr == 0):
            onoff1 = 10
    # 2-motor yuqoriga kutarilish
    if (motorSensor2 >= oraliq2 + labOldmotorSensor2):
        if (onoff2 == 1 and sensr == 1):
            onoff2 = 0
            motorKalit1.write_register(3, 0x0200)
        if (onoff2 == 11 and sensr == 0):
            onoff2 = 10
    if ( motorSensor2 >= pastki_sath2 - max2):
        if (onoff2 == 1 and sensr == 1):
            onoff2 = 0
            motorKalit1.write_register(3, 0x0200)
        if (onoff2 == 11 and sensr == 0):
            onoff2 = 10
    # 2-motor pastga tushishi
    if (motorSensor2 <= labOldmotorSensor2 - oraliq2):
        if (onoff2 == 2 and sensr == 1):
            onoff2 = 0
            motorKalit1.write_register(4, 0x0200)
        if (onoff2 == 12 and sensr == 0):
            onoff2 = 10

    if ( motorSensor2 < 0.18):
        if ( onoff2 == 2 and sensr == 1):
            onoff2 = 0
            motorKalit1.write_register(4, 0x0200)
        if ( onoff2 == 12 and sensr == 0):
            onoff2 = 10
    # 3-motor yuqoriga kutarilish
    if (motorSensor3 >= oraliq3 + labOldmotorSensor3):
        if (onoff3== 1 and sensr == 1):
            onoff3 = 0
            motorKalit1.write_register(5, 0x0200)
        if (onoff3== 11 and sensr == 0):
            onoff3 = 10
    if (motorSensor3 >= pastki_sath3 - max3):
        if (onoff3 == 1 and sensr == 1):
            onoff3 = 0
            motorKalit1.write_register(5, 0x0200)
        if (onoff3 == 11 and sensr == 0):
            onoff3 = 10

    # 3-motor pastga tushishi
    if (  motorSensor3 <= labOldmotorSensor3 - oraliq3 ):
        if (onoff3 == 2 and sensr == 1):
            onoff3 = 0
            motorKalit1.write_register(6, 0x0200)
        if (onoff3 == 12 and sensr == 0):
            onoff3 = 10
    if ( motorSensor3 <= 0.18 ):
        if( onoff3 == 2 and sensr==1):
          onoff3 = 0
          motorKalit1.write_register(6, 0x0200)
        if( onoff3 == 12 and sensr==0):
            onoff3=10

    if (sensr == 0):
        if onoff1 == 11:
            motorSensor1a = str(float(motorSensor1a) - 50)
            def step():
                for i in range(5):
                    secondWindow.update_idletasks()
                    bar['value'] += 20
                    time.sleep(1)
            bar=Progressbar(secondWindow,orient=HORIZONTAL ,length=200)
            bar.grid(row=3, column=8)


        if onoff1 == 12:
            motorSensor1a = str(float(motorSensor1a) + 50)

        # motorSensor2
        if onoff2 == 11:
            motorSensor2a = str(float(motorSensor2a) - 50)
        if onoff2 == 12:
            motorSensor2a = str(float(motorSensor2a) + 50)
        # motorSensor3
        if onoff3 == 11:
            motorSensor3a = str(float(motorSensor3a) - 50)
        if onoff3 == 12:
            motorSensor3a = str(float(motorSensor3a) + 50)

    m_sensor_lbl_input_1.configure(text=motorSensor1)
    m_sensor_lbl_input_2.configure(text=motorSensor2)
    m_sensor_lbl_input_3.configure(text=motorSensor3)


    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=1 order by id desc limit 1",
                     [obekt])
    lastmotorSensor1 = mycursor.fetchone()[0]
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=2 order by id desc limit 1",
                     [obekt])
    lastmotorSensor2 = mycursor.fetchone()[0]
    mycursor.execute("SELECT suvSathi from motor_sensor where obekt_id=%s and motor_id=3 order by id desc limit 1",
                     [obekt])
    lastmotorSensor3 = mycursor.fetchone()[0]

    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=1 order by id desc limit 1", [obekt])
    id1 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=2 order by id desc limit 1", [obekt])
    id2 = mycursor.fetchone()[0]
    mycursor.execute("SELECT id from motor_sensor where obekt_id=%s and motor_id=3 order by id desc limit 1", [obekt])
    id3 = mycursor.fetchone()[0]

    # motorSensor1
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


    m_sensor_lbl_input_1.after(1000, motor_sensor)


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
            onoff2 = 0
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
            onoff3 = 0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        onoff3 = 10


mycursor.execute("SELECT reykasathi,sensorsathi,name FROM s_sensor where s_type=1 and obekt_id=%s  ", [obekt])
mas_s_sensor = mycursor.fetchone()
reyka_height = mas_s_sensor[0]
water_height = mas_s_sensor[1]
s_sensor_name = mas_s_sensor[2]

totalHeight = float(reyka_height + water_height)

mycursor.execute("SELECT reykasathi,sensorsathi,name FROM s_sensor where s_type=3 and obekt_id=%s  ", [obekt])

mas_s_sensor3 = mycursor.fetchone()
reyka_height3 = mas_s_sensor3[0]
water_height3 = mas_s_sensor3[1]
s_sensor_name3 = mas_s_sensor3[2]

totalHeight3 = float(reyka_height3 + water_height3)

mycursor.execute("SELECT reykasathi,sensorsathi,name FROM s_sensor where s_type=2 and obekt_id=%s  ", [obekt])
mas_s_sensor2 = mycursor.fetchone()
reyka_height2 = mas_s_sensor2[0]
water_height2 = mas_s_sensor2[1]
s_sensor_name2 = mas_s_sensor2[2]

totalHeight2 = float(reyka_height2 + water_height2)


def water_sensor():
    global wtakror1, wtakror2, wtakror3, wtakror4, wtakror6, wtakror7, wtakror8, wtakror5
    farq = "Select farq_sm from s_farq where sensor_id=1 and obekt_id=%s order by id desc limit 1"
    mycursor.execute(farq, [obekt])
    farqSath1 = mycursor.fetchone()[0]

    farq = "Select farq_sm from s_farq where sensor_id=2 and obekt_id=%s order by id desc limit 1"
    mycursor.execute(farq, [obekt])
    farqSath2 = mycursor.fetchone()[0]

    farq = "Select farq_sm from s_farq where sensor_id=3  and obekt_id=%s order by id desc limit 1"
    mycursor.execute(farq, [obekt])
    farqSath3 = mycursor.fetchone()[0]


    if sensr != 0:
        try:
            sensor11b = str(watersensor1.read_register(1, 0, 3))
        except:

            sensorXatoSql5 = "INSERT INTO xato_sensor(s_sensor,status,obekt_id)VALUES (%s,%s,%s)"
            valSensorxato5 = (7, 'Sensor ishlamadi', obekt)
            mycursor.execute(sensorXatoSql5, valSensorxato5)
            sensor11b = w_lbl_in.cget('text')
            # sath1.configure(bg='black', fg="white")

    else:
        sensor11b = '2001'
    sensor11 = round(float(totalHeight) - float(int(sensor11b) / 1000), 2)
    w_lbl_in.configure(text=sensor11)
    # kirish qismidagi jadval bo'yicha
    cub = " Select kub from suvhajmi where sensor_id=1 and obekt_id=%s  "  ###
    mycursor.execute(cub, [obekt])
    massiv = mycursor.fetchall()

    sensor11CM = int(sensor11 * 100) + farqSath1
    if sensor11CM < 240:
        kub1 = massiv[sensor11CM][0]

        w_lbl_in_cub.configure(text=kub1)
    else:
        w_lbl_in_cub.configure(text="not found")
    w_lbl_in_cub.configure(text=kub1)
    # sensor12 uchun

    if sensr != 0:
        try:
            sensor12b = str(watersensor2.read_register(1, 0, 3))
        except:
            sensorXatoSql6 = "INSERT INTO xato_sensor(sensor_id,status,obekt_id)VALUES (%s,%s,%s)"
            valSensorxato6 = (8, 'Sensor ishlamadi', obekt)
            mycursor.execute(sensorXatoSql6, valSensorxato6)
            sensor12b = w_lbl_out1 .cget('text')
            w_lbl_out1 .configure(bg='black', fg="white")

    else:
        sensor12b = '2001'

    sensor12 = round(totalHeight2 - float(int(sensor12b) / 1000), 2)
    # #Cubini hisoblash
    cub = " Select kub from suvhajmi where sensor_id=1  and obekt_id=%s  "  # jadval berilishi kerak  sensor_id=2
    mycursor.execute(cub, [obekt])
    massiv = mycursor.fetchall()

    sensor12CM = int(sensor12 * 100) + farqSath2
    if sensor12CM < 240:
        kub2 = massiv[sensor12CM][0]
        w_lbl_cub_out1.configure(text=kub2)
    else:
        w_lbl_cub_out1.configure(text="not found")

    w_lbl_out1.configure(text=sensor12)

    # sensor13 uchun

    if sensr != 0:
        try:
            sensor13b = str(watersensor3.read_register(1, 0, 3))
        except:
            sensorXatoSql = "INSERT INTO xato_sensor(sensor_id,status,obekt_id)VALUES (%s,%s,%s)"
            valSensorxato = (7, 'Sensor ishlamadi', obekt)
            mycursor.execute(sensorXatoSql, valSensorxato)
            sensor13b = w_lbl_out2.cget('text')
            w_lbl_out2.configure(bg='black', fg="white")
    else:
        sensor13b = '2001'
    sensor13 = round(totalHeight3 - float(int(sensor13b) / 1000), 2)
    cub = " Select kub from suvhajmi where sensor_id=1  and obekt_id=%s "  # jadval berilishi kerak  sensor_id=3

    mycursor.execute(cub, [obekt])
    massiv = mycursor.fetchall()
    sensor13CM = int(sensor13 * 100) + farqSath3
    if sensor13CM < 240:
        kub3 = massiv[sensor13CM][0]
        w_lbl_cub_out2.configure(text=kub3)
    else:
        w_lbl_cub_out2.configure(text="not found")
    w_lbl_out2.configure(text=sensor13)

    current_time = datetime.now()

    # tekshirish
    if (
            current_time.minute == 10 or current_time.minute == 20 or current_time.minute == 30 or current_time.minute == 40 or current_time.minute == 50 or current_time.minute == 60):
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

    mydb.commit()
    m_sensor_lbl_input_1.after(60000, water_sensor)


window = Tk()
newWindow = ttk.Notebook(window)
firstWindow = Frame(newWindow, bg="Khaki")
secondWindow = Frame(newWindow)
thirdWindow = Frame(newWindow)
newWindow.add(secondWindow, text="user")
newWindow.add(thirdWindow, text="hisobot")
newWindow.add(firstWindow, text="Settings")

newWindow.pack(expand=True, fill="both")
window.title('SUV INSHOATI NAZORATI 1.1')
window.geometry('1200x700')
window.configure(bg="#0099cc")
# buyruq text
lbl_buyruq_text = Label(secondWindow, text='Buyruq ', fg='white', bg='black', width=7, font=('italic', 12, 'bold'))
lbl_buyruq_text.grid(row=1, column=1, padx=2)
# buyruqdagi berilgan malumot suv hajmi
lbl_buyruq_hajm= Label(secondWindow, text=str(asos[0]), fg='black', bg='white', width=4,font=('italic', 16, 'bold'))
lbl_buyruq_hajm.grid(row=1, column=1, columnspan=2)
# buyruqdagi berilgan sana malumoti
lbl_buyruq_sana = Label(secondWindow, text=str(sana), fg='black', bg='white', width=16,font=('italic', 16, 'bold'))
lbl_buyruq_sana.grid(row=1, column=3)
# buyruqga tegishli oddiy kub text
lbl_buyruq_kub_text = Label(secondWindow, text=' kub ', fg='orange', bg='blue', width=3,font=('italic', 14, 'bold'))
lbl_buyruq_kub_text .grid(row=1, column=2)
#yerdan qancha balandlikda turishi surjinaning caption
Label(secondWindow, text='surjina sathi /m').grid(row=2, column=2, padx=1, pady=8)
#surjina  qancha balandlikda kutarish kerakligi caption
Label(secondWindow, text=' kutarilishi /sm',width=12).grid(row=2, column=4, padx=1, pady=8)
#foizini hisoblash

print(mfoiz2)

#bosilgandagi sathi caption
Label(secondWindow, text='bosilgandagi sathi /m').grid(row=2, column=5, padx=1, pady=8)
#motorning nechanchiligini bildirish  text 1
mlbl_text_1 = Label(secondWindow, text='1', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold'))
mlbl_text_1.grid(row=3, column=1, padx=2, pady=6)
#yerdan qancha balandlikda turishi surjinaning input 1
m_sensor_lbl_input_1 = Label(secondWindow, text=" ", font=('Arial', 20), bg='white', fg='blue', width=5, bd=2,relief=SUNKEN)
m_sensor_lbl_input_1.grid(row=3, column=2)
#kutarish kerak bo'lgan chegara 1
m_up_input1 = Label(secondWindow, font=('Arial', 20), text='', bg='white', fg='blue', width=5, bd=2, relief=SUNKEN)
m_up_input1.grid(row=3, column=4, padx=0)
#Button ko'tarish to'xtatish, tushirish 1-motorniki
mbtn_up1_text  = Button(secondWindow, width=5, command=on1, text='tepaga', fg='white', bg='green',font=('italic', 14, 'bold')).grid(row=3,  column=9, padx=1, pady=6)
mbtn_stop1_text = Button(secondWindow, width=5, command=off1, text='stop', fg='white', bg='red',font=('italic', 14, 'bold')).grid(row=3,    column=10, padx=3, pady=6)
mbtn_down1_text  = Button(secondWindow, width=5, command=on2, text='pastga', fg='black', bg='yellow',font=('italic', 14, 'bold')).grid(row=3,column=11, padx=1, pady=6)
#motorning nechanchiligini bildirish  text 2
mlbl_text_2 = Label(secondWindow, text='2', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=4,column=1,padx=1,pady=6)
#yerdan qancha balandlikda turishi surjinaning input 2
m_sensor_lbl_input_2 = Label(secondWindow, font=('Arial', 20), bg='white', fg='black', width=5, bd=2, relief=SUNKEN)
m_sensor_lbl_input_2.grid(row=4, column=2)

#kutarish kerak bo'lgan chegara 2
m_up_input2 = Label(secondWindow, font=('Arial', 20), text='', bg='white', fg='blue', width=5, bd=2, relief=SUNKEN)
m_up_input2.grid(row=4, column=4)
#Button ko'tarish to'xtatish, tushirish 2-motorniki
mbtn_up_text2   = Button(secondWindow, width=5, command=on3, text='tepaga', fg='white', bg='green',font=('italic', 14, 'bold')).grid(row=4, column=9, padx=1, pady=3)
mbtn_stop_text2 = Button(secondWindow, width=5, command=off2, text='stop', fg='white', bg='red',font=('italic', 14, 'bold')).grid(row=4, column=10, padx=3, pady=6)
mbtn_down_text2 = Button(secondWindow, width=5, command=on4, text='pastga', fg='black', bg='yellow',font=('italic', 14, 'bold')).grid(row=4, column=11, padx=1, pady=6)
#motorning nechanchiligini bildirish  text 3
mlbl_text_3  = Label(secondWindow, text='3', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=5,column=1,padx=1,pady=6)
#yerdan qancha balandlikda turishi surjinaning input 3

m_sensor_lbl_input_3 = Label(secondWindow, font=('Arial', 20), text=' ', bg='white', fg='blue', width=5, bd=2,relief=SUNKEN)
m_sensor_lbl_input_3.grid(row=5, column=2)
#kutarish kerak bo'lgan chegara 3
m_up_input3= Label(secondWindow, font=('Arial', 20), text='', bg='white', fg='blue', width=5, bd=2,relief=SUNKEN)
m_up_input3.grid(row=5, column=4)
#Button ko'tarish to'xtatish, tushirish 2-motorniki
mbtn_up_text3   = Button(secondWindow, width=5, text='tepaga', command=on5, fg='white', bg='green', font=('italic', 14, 'bold')).grid(row=5, column=9, padx=1, pady=6)
mbtn_stop_text3 = Button(secondWindow, width=5, text='stop', command=off3, fg='white', bg='red',font=('italic', 14, 'bold')).grid(row=5, column=10, padx=1, pady=6)
mbtn_down_text3 = Button(secondWindow, width=5, text='pastga', command=on6, fg='black', bg='yellow',font=('italic', 14, 'bold')).grid(row=5, column=11, padx=1, pady=6)
#suv sathini kursatuvchi label caption
w_lbl_in_caption = Label(secondWindow, font=('Arial', 16), text='suv sathi', bg='white', fg='blue', width=8, bd=2, relief=SUNKEN)
w_lbl_in_caption.grid(row=12, column=2, padx=1, pady=26)

#suv sathini kursatuvchi label caption
w_lbl_cub_caption = Label(secondWindow, font=('Arial', 16), text='suv hajmi', bg='white', fg='blue', width=8, bd=2, relief=SUNKEN)
w_lbl_cub_caption.grid(row=12, column=3, padx=2, pady=26)

#kanal nomlari kursatuvchi label text
k_lbl_in1 = Label(secondWindow, text=s_sensor_name, fg='white', bg='blue', width=14, font=('italic', 16, 'bold')).grid(row=13, column=1, padx=1, pady=6)
k_lbl_out1 = Label(secondWindow, text=s_sensor_name2, fg='white', bg='blue', width=14, font=('italic', 16, 'bold')).grid(row=14, column=1, padx=1, pady=6)
k_lbl_out2 = Label(secondWindow, text=s_sensor_name3, fg='white', bg='blue', width=14, font=('italic', 16, 'bold')).grid(row=15, column=1, padx=3, pady=6)
# labelOutPut3 = Label(secondWindow,text='Out3  ', fg='white', bg='blue', width=10, font=('italic', 12, 'bold')).grid(row=16,column=1, padx=3,                                                                                                               pady=6)

#suv sathini kursatuvchi label
w_lbl_in = Label(secondWindow, text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
w_lbl_in.grid(row=13, column=2)
w_lbl_out1 = Label(secondWindow, text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
w_lbl_out1 .grid(row=14, column=2)


w_lbl_out2 = Label(secondWindow, text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
w_lbl_out2.grid(row=15, column=2)
#suv oqimini kub/s kursatuvchi label
w_lbl_in_cub= Label(secondWindow, text='2', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
w_lbl_in_cub.grid(row=13, column=3)

w_lbl_cub_out1 = Label(secondWindow, text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
w_lbl_cub_out1.grid(row=15, column=3)


w_lbl_cub_out2 = Label(secondWindow, text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
w_lbl_cub_out2.grid(row=14, column=3)
# labelOut3Cub = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
# labelOut3Cub.grid(row=16, column=3)



# labelOut3 = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
# labelOut3.grid(row=16, column=2)

firstButton = Button(firstWindow, text='registr', bg='#00ffff', command=modalRegistr, width='12', font=('italic', 14, 'bold'))
firstButton.grid(row=1, column=1, padx=55, pady=160)
firstButton2 = Button(firstWindow, text='farq', bg='yellow', width='12', font=('italic', 14, 'bold'))
firstButton2.grid(row=1, column=2, padx=35, pady=160)
firstButton3 = Button(firstWindow, text='lavozim', bg='#00ffff', width='12', font=('italic', 14, 'bold'))
firstButton3.grid(row=1, column=3, padx=35, pady=160)

firstButton4 = Button(firstWindow, text='user', bg='yellow', width='12', font=('italic', 14, 'bold'))
firstButton4.grid(row=1, column=4, padx=35, pady=160)
firstButton5 = Button(firstWindow, text='otdel', bg='#00ffff', width='12', font=('italic', 14, 'bold'))
firstButton5.grid(row=1, column=5, padx=35, pady=160)

# Add Calendar
from_cal = Calendar(thirdWindow, selectmode='day', year=2022, month=3, day=26)
from_cal.grid(row=1, column=1, padx=20, pady=20)  # Add Calendar
to_cal = Calendar(thirdWindow, selectmode='day', year=2022, month=4, day=15)
to_cal.grid(row=1, column=2, padx=20, pady=20)


def grad_date():
    fromDate = datetime.strptime((from_cal.get_date() + ' 00:00:00'), "%m/%d/%y %H:%M:%S")
    # fromDate2=datetime.strptime(from_cal.get_date(),"%b/%d/%Y")
    toDate = datetime.strptime((to_cal.get_date() + ' 23:59:59'), "%m/%d/%y %H:%M:%S")
    time_interval = toDate - fromDate
    date.config(text="Selected Date is: " + from_cal.get_date())
    date2.config(text="Selected Date is: " + to_cal.get_date())
    sql1 = "Select id, sarfi,sana from water_sensor where obekt_id=%s and sensor_id=1 and sana  between %s and %s"
    sql2 = "Select id, sarfi,sana from water_sensor where obekt_id=%s and sensor_id=2 and sana  between %s and %s"
    sql3 = "Select id, sarfi,sana from water_sensor where obekt_id=%s and sensor_id=3 and sana  between %s and %s"
    # sql4="Select id, sarfi,sana from water_sensor where obekt_id=%s and sensor_id=4 and sana  between %s and %s"

    mycursor.execute(sql1, [obekt, fromDate, toDate])
    massivsensor1 = mycursor.fetchall()

    mycursor.execute(sql2, [obekt, fromDate, toDate])
    massivsensor2 = mycursor.fetchall()

    mycursor.execute(sql3, [obekt, fromDate, toDate])
    massivsensor3 = mycursor.fetchall()

    # mycursor.execute(sql4,[obekt,fromDate,toDate])
    # massivsensor4=mycursor.fetchall()
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

    writeSensorinDatabase = 300
    worksheet.set_column('A:A', 14)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('D:D', 16)
    # A number to convert to a date.
    format5 = workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})
    format2 = workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})
    uzunlik1 = len(massivsensor1)
    uzunlik2 = len(massivsensor2)
    uzunlik3 = len(massivsensor3)
    # uzunlik4 =len(massivsensor4)

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

    worksheet.merge_range('A1:G1', 'Toshsaqa obektidagi suv sarfi haqida', merge_format)
    worksheet.merge_range('A2:G2', from_cal.get_date() + " dan " + to_cal.get_date() + "gacha bo'lgan davrda",
                          merge_format)
    worksheet.merge_range('A3:G3', "suv sarfini hisoblash", merge_format)
    worksheet.merge_range('A4:G4', "1-datchik", merge_format3)
    worksheet.write("A5", "№ ", merge_format2)
    worksheet.write("B5", "Boshlanish ", merge_format2)
    worksheet.write("C5", "sarf ", merge_format2)
    worksheet.write("D5", "Jami  ", merge_format2)

    total1 = 0
    for x in range(0, uzunlik1):
        total1 = total1 + massivsensor1[x][1] * writeSensorinDatabase

        worksheet.write('A' + str(x + 5), x + 1)  # 28/02/13 12:00
        worksheet.write('B' + str(x + 5), massivsensor1[x][2], format5)
        # datetime.strptime('4/22/16 10:00:00',"%m/%d/%y %H:%M:%S") 28/02/13 12:00
        # worksheet.write('C'+str(x), totals)    # 28/02/13 12:00
        worksheet.write('C' + str(x + 5), massivsensor1[x][1])  # 28/02/13 12:00
        worksheet.write('D' + str(x + 5), massivsensor1[x][1] * writeSensorinDatabase)  # 28/02/13 12:00

    worksheet.merge_range('B' + str(uzunlik1 + 5) + ':' + 'C' + str(uzunlik1 + 5), "Umumiy 1-datchikdagi rasxod",
                          merge_format)
    worksheet.write('D' + str(uzunlik1 + 5), total1)

    worksheet.write('A' + str(uzunlik1 + 7), "2-datchikdagi  ", merge_format3)
    worksheet.write('A' + str(uzunlik1 + 8), "№", merge_format2)
    worksheet.write('B' + str(uzunlik1 + 8), "Boshlanish ", merge_format2)
    worksheet.write('C' + str(uzunlik1 + 8), " Sarfi", merge_format2)
    worksheet.write('D' + str(uzunlik1 + 8), "Jami ", merge_format2)

    total2 = 0
    for x in range(0, uzunlik2):
        total2 = total2 + massivsensor2[x][1] * writeSensorinDatabase

        worksheet.write('A' + str(x + uzunlik1 + 8), x + 1)  # 28/02/13 12:00
        worksheet.write('B' + str(x + uzunlik1 + 8), massivsensor2[x][2], format5)
        # datetime.strptime('4/22/16 10:00:00',"%m/%d/%y %H:%M:%S") 28/02/13 12:00
        # worksheet.write('C'+str(x), totals)    # 28/02/13 12:00
        worksheet.write('C' + str(x + uzunlik1 + 8), massivsensor2[x][1])  # 28/02/13 12:00
        worksheet.write('D' + str(x + uzunlik1 + 8),
                        massivsensor2[x][1] * writeSensorinDatabase)  # delta time qo'yish kerak

    worksheet.merge_range('A' + str(uzunlik1 + uzunlik2 + 9) + ':' + 'C' + str(uzunlik1 + uzunlik2 + 9),
                          "Umumiy 2-datchikdagi rasxod", merge_format)
    worksheet.write('D' + str(uzunlik1 + uzunlik2 + 9), total2)

    worksheet.write('A' + str(uzunlik1 + uzunlik2 + 10), "3-datchikdagi  ", merge_format3)
    worksheet.write('A' + str(uzunlik1 + uzunlik2 + 11), "№", merge_format2)
    worksheet.write('B' + str(uzunlik1 + uzunlik2 + 11), "Boshlanish ", merge_format2)
    worksheet.write('C' + str(uzunlik1 + uzunlik2 + 11), " Sarfi", merge_format2)
    worksheet.write('D' + str(uzunlik1 + uzunlik2 + 11), "Jami ", merge_format2)

    total3 = 0
    for x in range(0, uzunlik3):
        total3 = total3 + massivsensor3[x][1] * writeSensorinDatabase
#uzunlik bu yerda har bir water_sensordagi sensorlarga tegishli malumotlar soni
        worksheet.write('A' + str(x + uzunlik1 + uzunlik2 + 11), x + 1)  # 28/02/13 12:00
        worksheet.write('B' + str(x + uzunlik1 + uzunlik2 + 11), massivsensor3[x][2], format5)
        worksheet.write('C' + str(x + uzunlik1 + uzunlik2 + 11), massivsensor3[x][1])  # 28/02/13 12:00
        worksheet.write('D' + str(x + uzunlik1 + uzunlik2 + 11),
                        massivsensor3[x][1] * writeSensorinDatabase)  # delta time qo'yish kerak

    worksheet.merge_range(
        'A' + str(uzunlik1 + uzunlik2 + uzunlik3 + 12) + ':' + 'C' + str(uzunlik1 + uzunlik3 + uzunlik2 + 12),
        "Umumiy 3-datchikdagi rasxod", merge_format)
    worksheet.write('D' + str(uzunlik1 + uzunlik2 + uzunlik3 + 12), total2)


    worksheet.merge_range(
        'A' + str(uzunlik1 + uzunlik2 + uzunlik3 + 14) + ':' + 'C' + str(uzunlik1 + uzunlik3 + uzunlik2 + 14),
        "Umumiy  rasxod", merge_format4)
    worksheet.write('D' + str(uzunlik1 + uzunlik2 + uzunlik3 + 14), total2 + total1 + total3)

    workbook.close()


# Add Button and Label
Button(thirdWindow, text="Hisobot",
       command=grad_date, bg='#00ffff', width='12', font=('italic', 14, 'bold')).grid(row=2, column=2, columnspan=2,
                                                                                      padx=320, pady=20)

date = Label(thirdWindow, text="")
date.grid(row=3, column=1, padx=20, pady=20)

date2 = Label(thirdWindow, text="")
date2.grid(row=3, column=2, padx=20, pady=20)
mydb.commit()
motor_sensor()

water_sensor()
ogoh()
window.mainloop()