import pylab as pl   
import numpy as np
import math as m

f1  = -7./8
f2 =  1./8


fang1 = (m.pi*2)*f1  
fang2 = (m.pi*2)*f2  #Frecuencia angular

FI = 0

print "frecuencia -7/8: ", f1 
print "frecuencia 1/8: ", f2 

print "f.angular 1: ", fang1
print "f.angular 2: ", fang2 

#para que es esto? 
def ooo(*a):
    return 0

def sen(t, fang , Amp=1):
    return Amp* m.sin((fang * t) + FI)

def cos(t,fang ,Amp=1):
    return Amp* m.cos((fang * t) + FI)


 #funcion, frecuencia angular, pasos de 0,001, color, inicio, fin
def graf(f, fang, i, color, x_0=-10, x_f=11, A=1):

    x = np.arange(x_0, x_f, i)
    y = [f( l, fang, A) for l in x]

    if x_f > 1: pl.xticks(np.arange(x_f))

    pl.plot(x, y, color)
    pl.xlabel("Hz")
    pl.ylabel("f(x)")
    pl.grid(True)

##primer Punto

 	#funcion, w, pasos de 0,001, color, inicio, fin
graf(sen, fang1, 0.001, '-g', 0, 12)#sen con frecuencia de -7. /8,
graf(sen, fang2, 0.001, '-b', 0, 12) #sen con frecuencia de 1. /8
graf(sen, fang1, 1, '-r', 0, 12) #senalmuestreada a un Hz







pl.show()

##Mmuestreos a 40 hz
i= .0001;V="-";o_=0; f=.3
graf(ooo,0,i,V,o_,f)
graf(cos,20,i,V,o_,f)#X1 cos(20t)
graf(cos,20*40,i,V,o_,f)#X1 cos(20t)40hz
pl.show()

i= .0001;V="-";o_=0; f=.05
graf(ooo,0,i,V,o_,f)
graf(cos,100,i,V,o_,f) #X2 cos(100t)
graf(cos,100*40,i,V,o_,f) #X2 cos(100t)40hz
pl.show()

i= .0001;V="-";o_=0; f=.05
graf(ooo,0,i,V,o_,f)
graf(cos,100,i,V,o_,f,n=3)   #X  3cos(100t)
graf(cos,100*40,i,V,o_,f,n=3)   #X  3cos(100t)40hz
pl.show()


###Segundo Punto
#la frecuencia de muestreo para evitar el aliasing
#   Si fx = 200 Hz cual seria x(n)

i= .0001;V="-";o_=0; f=.05
graf(ooo,0,i,V,o_,f)
graf(sen,200,i,V,o_,f,n=3)   #X sen(2.PI.200hzt)
i= .0025;V="o"
graf(sen,200,i,V,o_,f,n=3)   #X  Muestreo a 400hz
pl.show()


#   Si f1 = 75 Hz cual seria x(n)
i= .0001;V="-";o_=0; f=.2
graf(ooo,0,i,V,o_,f)
graf(sen,75,i,V,o_,f,n=3)   #X sen(2.PI.75hzt)
i=  1./150 ;V="o"
graf(sen,75,i,V,o_,f,n=3)   #X  Muestreo a 400hz
pl.show()






