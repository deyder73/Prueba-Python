import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

Nombre = input('¿Cómo te llamas? ')
print('Hola', Nombre)
print('¡Sea bienvenido al programa de ajuste de curvas!')

Título=input('Ingrese el título de la gráfica: ')
Variable_independiente = input('Ingrese el nombre de los datos de las variables independientes: ')
Variable_dependiente = input('Ingrese el nombre de los datos de las variables dependientes: ')
Archivo =input('Ingrese el nombre del archivo de datos (registrados en el bolc de notas), y al final incluya la extensión *.txt: ')

df = pd.read_csv(Archivo, header=None, names=[Variable_independiente, Variable_dependiente])
print(df.head())
print(type(df.head))
x=df.ix[:,0]
print(x)
y=df.ix[:,1]
print(y)
plt.plot(x,y,'ro')
plt.title(Título)
plt.ylabel(Variable_dependiente)
plt.xlabel(Variable_independiente)
plt.grid(axis='both')
print('Tipos de gráfica')
print('1-Lineal')
print('2-Polinómica')
print('3-Potencial')
print('4-Exponencial')
print('5-Logarítmica')

Grado = int(input('Ingrese la opción de la gráfica que desea ajustar; '))
if Grado == 1:
    print('La gráfica tendrá forma lineal')
    Coeficientes=np.polyfit(x,y,1)
    Polinomio=np.poly1d(Coeficientes)
    print('Ecuación: ',(Polinomio))
    ys=Polinomio(x)
    plt.plot(x, y,'ko', label="Datos Originales")
    plt.plot(x,ys, label="Curva Ajustada")
    plt.legend()
    plt.show()
    t=linregress(y,x)
    R1=(t.rvalue)**2
    print ("El coeficiente de correlacion es:")
    print(R1)

elif Grado == 2:
    print('La gráfica tendrá forma cuadrática')

    Coeficientes=np.polyfit(x,y,2)
    Polinomio=np.poly1d(Coeficientes)
    print('Ecuación: ',(Polinomio))
    ys=Polinomio(x)
    plt.plot(x, y,'ko', label="Datos Originales")
    plt.plot(x,ys, label="Curva Ajustada")
    
    plt.legend()
    plt.show()
    t=linregress(ys,x)
    R2 = r2_score(y, Polinomio(x))
    
    print ("El coeficiente de correlacion es:")
    print(R2)

elif Grado == 3:
    print('La gráfica tendrá forma potencial')

    Coeficientes = np.polyfit(np.log(x),np.log(y), 1)
    Polinomio=np.exp(Coeficientes)
    print('Ecuación: f(x) = ',Polinomio[1],'* x ^',Coeficientes[0])
    ys = Polinomio[1]*(x**(Coeficientes[0]))
    plt.plot(x, y,'ko', label="Datos Originales")
    plt.plot(x,ys,color='green',label="Curva Ajustada")
    plt.legend()
    plt.show()
    t=linregress(np.log(y),np.log(x))
    R3=(t.rvalue)**2
    print ("El coeficiente de correlacion es:")
    print(R3)
   
elif Grado == 4:
    print('La gráfica tendrá forma exponencial')

    Coeficientes = np.polyfit(x, np.log(y), 1)
    Polinomio=np.exp(Coeficientes)
    print('Ecuación: f(x) = ',Polinomio[1],'* e ^',np.log(Polinomio[0]),'x')
    ys = np.exp(np.polyval(Coeficientes,x))
    plt.plot(x, y,'ko', label="Datos Originales")
    plt.plot(x,ys,color='red', label="Curva Ajustada")
    plt.legend()
    plt.show()
    t=linregress(np.log(y),x)
    R4=(t.rvalue)**2
    print ("El coeficiente de correlacion es:")
    print(R4)

elif Grado == 5:
    print('La gráfica tendrá forma logarítmica')

    Coeficientes = np.polyfit(np.log(x), y, 1)
    print('Ecuación: f(x) = ',Coeficientes[0],'ln(x) +',Coeficientes[1])
    ys=Coeficientes[0]*np.log(x)+ Coeficientes[1]
    plt.plot(x, y,'ko', label="Datos Originales")
    plt.plot(x,ys,color='blue',label="Curva Ajustada")
    plt.legend()
    plt.show()
    t=linregress(y,np.log(x))
    R5=(t.rvalue)**2
    print ("El coeficiente de correlacion es:")
    print(R5)


plt.show()
