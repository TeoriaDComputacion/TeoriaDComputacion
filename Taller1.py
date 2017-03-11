import pylab as pl
import numpy as np
import math as m

f  = -7. /8
f2 =  1./8
OM2 = (m.pi*2)*f2
OM  = (m.pi*2)*f
FI = 0
print f,f2,OM2,OM
def ooo(*a):
    return 0
def sen(t,om,n=1):
    return n*m.sin((om * t) + FI)
def cos(t,om,n=1):
    return n*m.cos((om * t) + FI)


def graf(F,om,i,v, x_0=-10., x_f=11.,n=1.):
    x = np.arange(x_0, x_f, i)
    y = [F(l,om,n) for l in x]

    if x_f > 1: pl.xticks(np.arange(x_f))
    pl.plot(x,y, v)
    pl.xlabel("Hz")
    pl.ylabel("f(x)")
    pl.grid(True)
##primer Punto
graf(ooo,0,1.,"-",0,12)
graf(sen,OM,0.001,"-",0)#sen con frecuencia de -7. /8
graf(sen,OM2,0.1,"-",0) #sen con frecuencia de 1. /8
graf(sen,OM,1.,"o",0) #senalmuestreada a un Hz


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