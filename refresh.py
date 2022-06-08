from tkinter import *
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='water')
mycursor = mydb.cursor()
def refresh():
    sql="Select * from s_motor "
    mycursor.execute(sql)
    refresh2=mycursor.fetchall()
    employee = []
    content = {}
    for result in refresh2:
        content = {'max': result[4], 'min': result[3],}
        employee.append(content)
    print(employee)
    payload = {'key1': '1', 'key2': '4848'}
    r = requests.get('http://product/frontend/web/site/refresh',json=employee)
    print(r.content)
    print(r)
    print(r.request.body)

    # employee ni serverga junatish




window=Tk()
window.geometry("400x200")
window.configure(bg="yellow")
refresh=Button(window,text="refresh",command=refresh,bg="white",width='12',font=('italic', 14, 'bold'))
refresh.grid(row=1,column=1,pady=50,padx=100)
window.mainloop()
