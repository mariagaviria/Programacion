import tkinter
from tkinter import *
import csv

tk = Tk()

with open('1995-1996.csv') as File:
    reader=csv.reader(File, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
    exportacion={}            

    nombreanterior='zzz'
    for row in reader:
        nombre=row[0]
        if nombreanterior!=nombre:
            exportacion[nombre]={}
            nombreanterior=nombre
    
        exportacion[row[0]][row[1]]=float(row[2])
    #print(y)        

with open('coordenadas.csv')as File:
    reader=csv.reader(File, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
    coordenadas={}
    for row in reader:
        coordenadas[row[0]]=(float(row[1]),float(row[2]),float(row[3]),float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]))
        
def sketch(coordenadas,exportacion):
    canvas=Canvas(tk,width=1000, height=660, bg='white')
    tk.title("1995-1996")
    canvas.pack(expand=YES, fill=BOTH)
    for i in coordenadas.keys():
        canvas.create_text(coordenadas[i][0],coordenadas[i][1],text=i, font=('Times New Roman',15))
        
    for i in exportacion.keys():
        if (i!='VEN'):
            for j in exportacion[i].keys():
    #           if (exportacion[i][j]>0 and exportacion[i][j]<99999):
    #                    canvas.create_line(coordenadas[i][2],coordenadas[i][3],coordenadas[j][2], coordenadas[j][3], arrow=LAST, width=1)
    #                    
    #                elif (exportacion[i][j]>99999 and exportacion[i][j]<1000000):
    #                    canvas.create_line(coordenadas[i][2],coordenadas[i][3],coordenadas[j][2], coordenadas[j][3], arrow=LAST, width=2)
    #                        
    #                elif (exportacion[i][j]>1000000 and exportacion[i][j]<100000000):
    #                    canvas.create_line(coordenadas[i][2],coordenadas[i][3],coordenadas[j][2], coordenadas[j][3], arrow=LAST, width=3)
    #                        
    #                elif (exportacion[i][j]>1000000 and exportacion[i][j]<100000000):
    #                    canvas.create_line(coordenadas[i][2],coordenadas[i][3],coordenadas[j][2], coordenadas[j][3], arrow=LAST, width=5)

    return canvas

def plataexportada(exportacion):
    plata={}
    for i in exportacion.keys():
        plata[exportacion[i]]={}
        for j in exportacion[i].keys():
            if exportacion[i][j]>0:
                plata[exportacion[i]]=exportacion[i][j]
    return plata

print(coordenadas)
#print(exportacion['COL']['BRA'])
#print(y)
print(exportacion)
#print(plataexportada(exportacion))
c=sketch(coordenadas,exportacion)
mainloop()


