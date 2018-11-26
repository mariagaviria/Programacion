import tkinter
from tkinter import *
import argentina
import bolivia
import belize
import brasil
import chile
import canada
import colombia
import costarica
import ecuador
import guatemala
import honduras
import jamaica
import mexico
import nicaragua
import panama
import peru
import paraguay
import elsalvador
import uruguay
import estadosunidos
import venezuela
import csv

tk = Tk()

with open('coordenadas.csv')as File:
    reader=csv.reader(File, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
    coordenadas={}
    for row in reader:
        coordenadas[row[0]]=(float(row[1]),float(row[2]),float(row[3]),float(row[4]))
        
        
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
        
def farg():
    argentina.funarg()    
def fbol():
    bolivia.funbol()
def fblz():
    belize.funblz()
def fbra():
    brasil.funbra()
def fchl():
    chile.funchl()
def fcan():
    canada.funcan()
def fcol():
    colombia.funcol()
def fcri():
    costarica.funcri()
def fecu():
    ecuador.funecu()
def fgtm():
    guatemala.fungtm()
def fhnd():
    honduras.funhnd()
def fjam():
    jamaica.funjam()
def fmex():
    mexico.funmex()
def fnic():
    nicaragua.funnic()
def fpan():
    panama.funpan()
def fper():
    peru.funper()
def fpry():
    paraguay.funpry()
def fslv():
    elsalvador.funslv()
def fury():
    uruguay.funury()
def fusa():
    estadosunidos.funusa()
def fven():
    venezuela.funven()


        
def sketch():
    canvas=Canvas(tk,width=1300, height=620, bg='white')
    tk.title("1997-1998")
    canvas.pack(expand=YES, fill=BOTH)
    widget=Button(canvas,text='ARG', bg="white",command=farg)
    canvas.create_window(coordenadas['ARG'][0], coordenadas['ARG'][1], window=widget)
    widget=Button(canvas,text='BOL', bg="white",command=fbol)
    canvas.create_window(coordenadas['BOL'][0], coordenadas['BOL'][1], window=widget)
    widget=Button(canvas,text='BLZ', bg="white",command=fblz)
    canvas.create_window(coordenadas['BLZ'][0], coordenadas['BLZ'][1], window=widget)
    widget=Button(canvas,text='BRA', bg='white',command=fbra)
    canvas.create_window(coordenadas['BRA'][0], coordenadas['BRA'][1], window=widget)
    widget=Button(canvas, text='CHL', bg='white', command=fchl)
    canvas.create_window(coordenadas['CHL'][0], coordenadas['CHL'][1], window=widget)
    widget=Button(canvas, text='CAN', bg='white', command=fcan)
    canvas.create_window(coordenadas['CAN'][0], coordenadas['CAN'][1], window=widget)
    widget=Button(canvas, text='COL', bg='white', command=fcol)
    canvas.create_window(coordenadas['COL'][0], coordenadas['COL'][1], window=widget)
    widget=Button(canvas, text='CRI', bg='white', command=fcri)
    canvas.create_window(coordenadas['CRI'][0], coordenadas['CRI'][1], window=widget)
    widget=Button(canvas, text='ECU', bg='white', command=fecu)
    canvas.create_window(coordenadas['ECU'][0], coordenadas['ECU'][1], window=widget)
    widget=Button(canvas, text='GTM', bg='white', command=fgtm)
    canvas.create_window(coordenadas['GTM'][0], coordenadas['GTM'][1], window=widget)
    widget=Button(canvas, text='HND', bg='white', command=fhnd)
    canvas.create_window(coordenadas['HND'][0], coordenadas['HND'][1], window=widget)
    widget=Button(canvas, text='JAM', bg='white', command=fjam)
    canvas.create_window(coordenadas['JAM'][0], coordenadas['JAM'][1], window=widget)
    widget=Button(canvas,text='MEX', bg="white",command=fmex)
    canvas.create_window(coordenadas['MEX'][0], coordenadas['MEX'][1], window=widget)
    widget=Button(canvas,text='NIC', bg="white",command=fnic)
    canvas.create_window(coordenadas['NIC'][0], coordenadas['NIC'][1], window=widget)
    widget=Button(canvas,text='PAN', bg="white",command=fpan)
    canvas.create_window(coordenadas['PAN'][0], coordenadas['PAN'][1], window=widget)
    widget=Button(canvas,text='PER', bg="white",command=fper)
    canvas.create_window(coordenadas['PER'][0], coordenadas['PER'][1], window=widget)
    widget=Button(canvas,text='PRY', bg="white",command=fpry)
    canvas.create_window(coordenadas['PRY'][0], coordenadas['PRY'][1], window=widget)
    widget=Button(canvas,text='SLV', bg="white",command=fslv)
    canvas.create_window(coordenadas['SLV'][0], coordenadas['SLV'][1], window=widget)
    widget=Button(canvas,text='URY', bg="white",command=fury)
    canvas.create_window(coordenadas['URY'][0], coordenadas['URY'][1], window=widget)
    widget=Button(canvas,text='USA', bg="white",command=fusa)
    canvas.create_window(coordenadas['USA'][0], coordenadas['USA'][1], window=widget)
    widget=Button(canvas,text='VEN', bg="white",command=fven)
    canvas.create_window(coordenadas['VEN'][0], coordenadas['VEN'][1], window=widget)
        
    for i in red.keys():
        for j in red[i].keys():
            if red[i][j]>0:
                canvas.create_line(coordenadas[i][2], coordenadas[i][3], coordenadas[j][2], coordenadas[j][3]) 
c=sketch()
mainloop()