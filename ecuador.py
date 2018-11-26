import tkinter
import csv
from tkinter import *

tk = Tk()

with open('coordenadas-ECU.csv')as File:
    reader=csv.reader(File, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
    coordenadas={}
    for row in reader:
        coordenadas[row[0]]=(float(row[1]),float(row[2]),float(row[3]),float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]),float(row[11]), float(row[12]), float(row[13]), float(row[14]))
        
with open('1997-1998.csv') as File:
    reader=csv.reader(File, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
    red={}            

    nombreanterior='zzz'
    for row in reader:
        nombre=row[0]
        if nombreanterior!=nombre:
            red[nombre]={}
            nombreanterior=nombre
    
        red[row[0]][row[1]]=float(row[2])
        
def funecu():
    canvas=Canvas(tk,width=1000, height=660, bg='white')
    tk.title("ECU")
    canvas.pack(expand=YES, fill=BOTH)
    for i in coordenadas.keys():
        canvas.create_text(coordenadas[i][0],coordenadas[i][1],text=i, font=('Times New Roman',15))
        canvas.create_rectangle(coordenadas[i][2], coordenadas[i][3], coordenadas[i][4], coordenadas[i][5])
    exp=0
    imp=0    
    for i in red.keys():
        if (i!='ECU'):
            for j in red[i].keys():
                if (j=='ECU'):
                    imp+=red[i][j]                    
                    if (i=='ARG' or i=='BOL' or i=='BRA' or i=='CHL' or i=='COL' or i=='VEN' or i=='PER' or i=='PRY' or i=='URY'):
                        if (red[i][j]>0 and red[i][j]<=2000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][6], coordenadas[j][7], arrow=LAST, fill='red', width=2)
                        elif (red[i][j]>2000000 and red[i][j]<=4000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][6], coordenadas[j][7], arrow=LAST, fill='orange', width=2)
                        elif (red[i][j]>4000000 and red[i][j]<=6000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][6], coordenadas[j][7], arrow=LAST, fill='yellow', width=2)
                        elif (red[i][j]>6000000 and red[i][j]<=80000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][6], coordenadas[j][7], arrow=LAST, fill='blue', width=2)
                        elif (red[i][j]>80000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][6], coordenadas[j][7], arrow=LAST, fill='green', width=2)
                    else:
                        if (red[i][j]>0 and red[i][j]<=2000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][10], coordenadas[j][11], arrow=LAST, fill='red', width=2)
                        elif (red[i][j]>2000000 and red[i][j]<=4000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][10], coordenadas[j][11], arrow=LAST, fill='orange', width=2)
                        elif (red[i][j]>4000000 and red[i][j]<=6000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][10], coordenadas[j][11], arrow=LAST, fill='yellow', width=2)
                        elif (red[i][j]>6000000 and red[i][j]<=8000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][10], coordenadas[j][11], arrow=LAST, fill='blue', width=2)
                        elif (red[i][j]>8000000):
                            canvas.create_line(coordenadas[i][6], coordenadas[i][7], coordenadas[j][10], coordenadas[j][11], arrow=LAST, fill='green', width=2)
        else:
            for j in red[i].keys(): 
                exp+=red[i][j]                
                if (j=='ARG' or j=='BOL' or j=='BRA' or j=='CHL' or j=='COL' or j=='VEN' or j=='PER' or j=='PRY' or j=='URY'):
                    if (red[i][j]>0 and red[i][j]<=2000000):
                        canvas.create_line(coordenadas[i][8], coordenadas[i][9], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='red', width=2)
                    elif (red[i][j]>2000000 and red[i][j]<=4000000):
                        canvas.create_line(coordenadas[i][8], coordenadas[i][9], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='orange', width=2)
                    elif (red[i][j]>4000000 and red[i][j]<=6000000):
                        canvas.create_line(coordenadas[i][8], coordenadas[i][9], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='yellow', width=2)
                    elif (red[i][j]>6000000 and red[i][j]<=80000000):
                        canvas.create_line(coordenadas[i][8], coordenadas[i][9], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='blue', width=2)
                    elif (red[i][j]>80000000):
                        canvas.create_line(coordenadas[i][8], coordenadas[i][9], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='green', width=2)
                else:
                    if (red[i][j]>0 and red[i][j]<=2000000):
                        canvas.create_line(coordenadas[i][12], coordenadas[i][13], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='red', width=2)
                    elif (red[i][j]>2000000 and red[i][j]<=4000000):
                        canvas.create_line(coordenadas[i][12], coordenadas[i][13], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='orange', width=2)
                    elif (red[i][j]>4000000 and red[i][j]<=6000000):
                        canvas.create_line(coordenadas[i][12], coordenadas[i][13], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='yellow', width=2)
                    elif (red[i][j]>6000000 and red[i][j]<=8000000):
                        canvas.create_line(coordenadas[i][12], coordenadas[i][13], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='blue', width=2)
                    elif (red[i][j]>8000000):
                        canvas.create_line(coordenadas[i][12], coordenadas[i][13], coordenadas[j][8], coordenadas[j][9], arrow=LAST, fill='green', width=2)
    expn=exp-imp
    canvas.create_text(coordenadas['ECU'][0], 563, text=('Exportacion= ',exp, ' de dolares'), font=('Times New Roman',10))
    canvas.create_text(coordenadas['ECU'][0], 598, text=('Importacion= ',imp,' de dolares'), font=('Times New Roman',10))
    canvas.create_text(coordenadas['ECU'][0], 633, text=('Exportacion neta= ',expn,' de dolares'), font=('Times New Roman',10))
    