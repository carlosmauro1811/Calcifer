#Esto es para hacer una interfas grafica de usuario (Guide)

 #Importar la librería
import tkinter as tk 
import math
import numpy as np
#from PIL import ImageTk #Libreria pillow que me sirve para trabajar con imagenes
from tkinter import ttk #Para agregar etiquetas debemos importar ttk
from matplotlib import pyplot as plt #Esta es la librería para hacer graficas

def resultado():
    vol1=int(entrada1.get())
    vol2=int(entrada2.get())
    resultado=vol1/vol2
    return var1.set(resultado) 

def resultado2():
    vol1=int(entrada1.get())
    vol2=int(entrada2.get())
    resultado2=(vol1/vol2)*(1/math.sqrt(3))
    return var1.set(resultado2)  

def resultado3():
    vol1=int(entrada1.get())
    vol2=int(entrada2.get())
    resultado3=(vol1/vol2)*(math.sqrt(3))
    return var1.set(resultado3)

"---------------------OPEN-------------------------------------------------------------------------------"
"Activacion de segunda ventana por medio de boton CONTINUAR"
    


def grafica():
    
    #Procedo a generar los datos para la grafica
    "Señal 1"
    x=np.array(range(400))*0.1
    y=np.zeros(len(x))
    for i in range(len(x)):
        y[i]=math.sin(x[i])#+100)
    
    "Señal 2" 
    x2=np.array(range(400))*0.1
    y2=np.zeros(len(x))
    for i in range(len(x2)):
        y2[i]=math.sin(x2[i]+90) 
        
    "Señal 3"   
    x3=np.array(range(400))*0.1
    y3=np.zeros(len(x))
    for i in range(len(x3)):
        y3[i]=math.sin(x3[i]+180)    
        
    #Ahora generamos la grafica
    plt.plot(x,y,x2,y2,x3,y3)
    plt.ion()
    #plt.show()#Para mostrar el grafico por si no sale
    plt.xlabel("Tiempo")#Ponerle un titulo al eje x
    plt.ylabel("Amplitud")#Titulo al eje Y
    plt.title("DESFASE DE CADA SEÑAL DEL TRANSFORMADOR")#Ponerle un titulo general a la grafica
    plt.grid()#Activar la malla
    n=[0,5,-2,2]  #Rango
    plt.axis(n)#Con este modulo establecemos los limites de la grafica en Eje x y eje y   
    plt.legend(['Fase1','Fase2',"Fase3"])#Para colocar una legenda
    
    
    
def abrirventana():#Inicializo la ventana 2 Grafica de voltajes trifásicos
    ventana.withdraw()#Esta linea de codigo es para cerrar la ventana principal, al abrirse la segunda ventana
    ventana2=tk.Tk()
    ventana2.title("Grafica de voltajes trifásicos")
    ventana2.resizable(0,0)#Para que no se pueda modificar tamaño ventana
    ventana2.geometry("500x150") #Esto es para definir la geometría de la ventana
    ventana2.configure(background="dark slate blue") #para colocarle color a la ventana
    etiqueta4=tk.Label(ventana2,text="Visualizar graficas de las 3 fases",background="lavender").place(x=155,y=10)
    #etiqueta4.pack(side=tk.TOP)
    #botonout=tk.Button(ventana2,text="OK",command=ventana2.destroy)place.(x=210,y=320)
    botonsalir=tk.Button(ventana2,text="Salir",fg="Blue",command=ventana2.destroy).place(x=210,y=100)
    botongrafica=tk.Button(ventana2,text="grafica",fg="Blue",command=grafica).place(x=210,y=50)#Este es el boton para mostrar la grafica
    #botonout.pack(side=tk.TOP)



#Funcion para cerrar la ventana 2     
#def cerrarventana():
#   ventana2.destroy()
"---------------------------CLOSE-----------------------------------------------------------------------"







#Inicializar ventana
ventana=tk.Tk()
ventana.title("Calculadora de devanados del transformador")
ventana.resizable(0,0)#Para que no se pueda modificar tamaño ventana
ventana.geometry("500x340") #Esto es para definir la geometría de la ventana
ventana.configure(background="dark slate blue") #para colocarle color a la ventana



var1=tk.StringVar()#Esta es la variable en la que se guarda el resultado mostrado en el recuadro de respuesta



"Etiquetas y configuracion de color y texto"
#Para agregar etiquetas Label (Se requiere importar ttk)
etiqueta=ttk.Label(ventana, text="Voltaje devanado primario",background="lavender")#Aquí estoy añadiendo la etiqueta y modificando su color
etiqueta.pack(padx=5,pady=4,ipadx=5,ipady=5)
entrada1=tk.Entry(ventana)#Este es el recuadro en el cual se ingresara el voltaje del primario
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)#Aquí estoy cuadrando la localización del recuadro
#Para la segunda etiqueta
etiqueta2=ttk.Label(ventana, text="Voltaje devanado secundario",background="lavender")#Aquí estoy añadiendo la etiqueta y modificando su color
etiqueta2.pack(padx=5,pady=4,ipadx=5,ipady=5)
entrada2=tk.Entry(ventana)#Este es el recuadro en el cual se ingresara el voltaje del primario
entrada2.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)



"Botones de control para general la respuesta"
#Pimer boton 
botondevanados=tk.Button(ventana,text="Y-Y",background="royal blue",command=resultado).place(x=70, y=152)
#Segundo boton
botondevanados2=tk.Button(ventana,text="Y-D",background="royal blue",command=resultado2).place(x=110,y=152)
#Tercer boton
botondevanados3=tk.Button(ventana,text="D-Y",background="royal blue",command=resultado3).place(x=360,y=152)
#Cuarto boton
botondevanados4=tk.Button(ventana,text="D-D",background="royal blue",command=resultado).place(x=400,y=152)
#Recuadro de respuesta
res=tk.Label(ventana,background="lavender",textvariable=var1,padx=5,pady=5,width=20)
res.pack()
#Etiqueta 
etiqueta3=ttk.Label(ventana, text="Seleccione el tipo de conexión",background="lavender").place(x=169,y=184)
"Boton que abre la segunda ventana"
boton=tk.Button(ventana,text="Continuar",fg="Blue",command=abrirventana).place(x=210,y=300)#Boton (continuar) para abrir la nueva ventana


"---------------------OPEN -------------------------------------------------------------------------------"
#etiqueta5=tk.Label(ventana,text="Ingrese el resultado obtenido",bg="lavender",fg="black").place(x=160,y=310)#Etiqueta de la parte inferior que nos pide ingresar el resultado

#entrada3=tk.Entry(ventana).place(x=180,y=280)#Para la entrada del resultado

  


  










#Activar ventana osea que se muestre en pantalla
ventana.mainloop()
#ventana2.mainloop()
#win.mainloop()