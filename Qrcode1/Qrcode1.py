
import qrcode
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter
from PIL import Image
from PIL import ImageDraw
from qrcode.main import QRCode
from PIL import ImageFont



ws = Tk()
ws.title('QrCode generator')
ws.geometry('800x600')
ws.config(bg='#4a6a8c')


def generate():
    qr = qrcode.QRCode(box_size=180)
    img = qrcode.make(msg.get()+'\t'+msg1.get()+'\t'+msg2.get()+'\t'+msg3.get()+'\t'+msg4.get()+'\t'+msg5.get()+'\t'+msg6.get()+'\t'+variable1.get() +'\t'+variable.get()+'\t'+msg9.get())
    draw = ImageDraw.Draw(img)

    draw.text((55, 15), msg1.get())
    draw.text((55, 25), msg2.get())
    type(img) 
    img.save(f'{save_name.get()}.png')
    Label(ws, text='File Saved!', fg='green').pack()

frame = Frame(ws, bg='#4a7a8c')
frame.pack(expand=True)
Label(
    frame,
    text='Data',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=0, column=0, sticky='w')

msg = Entry(frame)
msg.grid(row=0, column=1)
Label(
    frame,
    text='Linia',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=1, column=0, sticky='w')

msg1 = Entry(frame)
msg1.grid(row=1, column=1)
Label(
    frame,
    text='PO number:',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=2, column=0, sticky='w')

msg2 = Entry(frame)
msg2.grid(row=2, column=1)
Label(
    frame,
    text='Material number:',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=3, column=0, sticky='w')

msg3 = Entry(frame)
msg3.grid(row=3, column=1)
Label(
    frame,
    text='Cantitate:',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=4, column=0, sticky='w')

msg4 = Entry(frame)
msg4.grid(row=4, column=1)
Label(
    frame,
    text='Material description:',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=5, column=0, sticky='w')

msg5 = Entry(frame)
msg5.grid(row=5, column=1)
Label(
    frame,
    text='Problem description:',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=6, column=0, sticky='w')

msg6 = Entry(frame)
msg6.grid(row=6, column=1)
Label(
    frame,
    text='Description failure mode:',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=7, column=0, sticky='w')

step_list1 = ['Defect de calitate', 'Test hidraulic NOK/ Test pneumatic NOK', 'Deteriorat la asamblare', 'Galvanizare neconforma/Vopsire neconforma', 'Coriziune', 'Componentul nu se poate asambla', 'Componentul nu se poate dezasambla', 'Reglaj masina', 'Inscriptionare NOK']
# setting variable for Integers
variable1 = StringVar()
variable1.set(step_list1[1])
dropdown = OptionMenu(
    ws,
    variable1,
    *step_list1,
)
dropdown.place(relx=0.54, rely=0.55, anchor='nw')
Label(
    frame,
    text='Step1:',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=8, column=0, sticky='w')
# color choices available.
step_list = ['961', 'Blocat Q-Point']
# setting variable for Integers
variable = StringVar()
variable.set(step_list[1])
dropdown = OptionMenu(
    ws,
    variable,
    *step_list,
)
dropdown.place(relx=0.31, rely=0.59, anchor='nw')
Label(
    frame,
    text='Nume:',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=9, column=0, sticky='w')

msg9 = Entry(frame)
msg9.grid(row=9, column=1)
Label(
    frame,
    text='Save as',
    font = ('Times', 18),
    bg='#4a7a8c',
).grid(row=10, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=10, column=1)

btn = Button(
    ws, 
    text='Generate QR code',
    command=generate
    )
btn.pack()

ws.mainloop()