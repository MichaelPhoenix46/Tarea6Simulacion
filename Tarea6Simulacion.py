from numpy import *
import matplotlib.pyplot as plt

#valores para x1
#x1 = linspace(-20,20,100)
#d = ((x1**3)-3)

#y1 = sign(d) * (abs(d)) ** (1/3)

d = input("Declarar incognita")
try:
    if d == "y":
        x = linspace(-20, 20, 100)
        y = eval(input("Declarar ecuacion"))
    elif d == "x":
        y = linspace(-20, 20, 100)
        x = eval(input("Declarar ecuacion"))
    elif d == "y2":
        x = linspace(-20, 20, 100)
        y1 = eval(input("declarar ecuacion"))
        y = sign(y1) * (abs(y1)) ** (1/2)
    elif d == "x2":
        y = linspace(-20,20, 100)
        x1 = eval(input("declarar ecuacion"))
        x = sign(x1) * (abs(x1)) ** (1/2)
    elif d == "y3":
        x = linspace(-20, 20, 100)
        y1 = eval(input("declarar ecuacion"))
        y = sign(y1) * (abs(y1)) ** (1/3)
    elif d == "x3":
        y = linspace(-20,20, 100)
        x1 = eval(input("declarar ecuacion"))
        x = sign(x1) * (abs(x1)) ** (1/3)




    #valores para x2
    #x2 = linspace(-10,10,100)
    #y2 = eval(input('formula de sistema 2'))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')


    plt.plot(x, y)
    #plt.plot(x2, y2)
    plt.show()

except:
    print("algo fue digitado mal")



