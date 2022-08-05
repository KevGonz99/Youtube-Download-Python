from ctypes import resize
from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox

print(os.getcwd)

def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def popup():
    MessageBox.showinfo("Sobre mi","Hola :)")

root = Tk()
root.config(bd=15)
root.title("YouTube Download")
root.iconbitmap("Python.ico")
root.config(bg="gray18")
root.geometry('650x203')
root.resizable(0,0)
root.config(relief="groove")


imagen = PhotoImage(file="Youtube.png")
foto = Label(root,image=imagen, bd=0)
foto.grid(row=0,column=0)
foto.place(x=0,y=0)


menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label= 'Para mas informacion',menu=helpmenu)
helpmenu.add_command(label='Informacion del autor',command=popup)
menubar.add_command(label='Salir',command=root.destroy)

instrucciones = Label(root, text = 'Programa creado para descargar videos de YouTube', fg ="white" ,bg= "gray18",font ="20")
instrucciones.grid(row=0,column=1,padx=5,pady=10)
instrucciones.place(x=200,y=0) 
instrucciones.fg= "while"

videos = Entry(root,width=25)
videos.grid(row=1,column=1,padx=0,pady=10)
videos.place(x=280,y=50) 

boton = Button(root,text='Descargar',command = accion)
boton.grid(row=2,column=1)
boton.place(x=350,y=91) 

root.mainloop()

