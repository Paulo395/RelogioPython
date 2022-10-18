from turtle import *
from datetime import *

def fundo():
    for i in range(60):
        if i % 5 == 0:
            color("red")
            width(6)
        else:
            color("white")
            width(3)
        pu()
        fd(150)
        pd()
        fd(20)
        pu()
        bk(170)
        rt(6)

def desenhar():
    #Apagar
    reset()

    #Desenhar
    fundo()
    
    agora = datetime.now()
    h = agora.hour
    m = agora.minute
    s = agora.second

    ah = (h/12)*360 + (m/60)*30
    am = m/60*360
    seg = (s/60)*360

    pd()
    #Horas
    width(5)
    seth(ah)
    fd(100)
    bk(100)

    #Minutos
    width(3)
    seth(am)
    fd(140)
    bk(140)
    
    #Segundos
    width(1)
    color("red")
    seth(seg)
    fd(130)
    bk(130)
    


    #Atualizar
    ht()
    update()

    #repetir
    ontimer(desenhar,1000)

mode("logo")
tracer(0)
bgcolor("black")
desenhar()