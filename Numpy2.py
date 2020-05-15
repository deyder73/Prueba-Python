#Funciones especiales de Numpy generadora de arreglos
import numpy as np

#arange(): crea un arreglo en donde se especiica el inicio, fin y su intervalo de datos
#sintaxis -> np.arrange(Inicio, Fin, Incremento)
array1d=np.arange(5)                         #Genera un arreglo unidimensional de números desde el 0 hasta el 4 con paso 1
print(array1d)

array1d=np.arange(0, 12, 1)                  #Genera un arreglo unidimensional de números desde el 0 hasta el 11 con paso 1
print(array1d)

array2d=np.arange(0, 12, 2).reshape(2, 3)     #Genera un arreglo bidimensional de números desde el 0 hasta el 10 con paso 2 (ajustando la forma del arreglo con reshape)
print(array2d)

array3d=np.arange(9).reshape(3, 3)            #Genera un arreglo bidimensional de números desde el 0 hasta el 8 (ajustando con reshape)
print(array3d)
print()

#linspace(): crea un arreglo donde se especifica el inicio, fin y el número de elementos
#sintaxis -> np.linspace(Inicio, Fin, # de Elementos)
array1d=np.linspace(1, 12, 2)                #Genera un arreglo unidimensioal de números desde el 1 hasta el 12 don 2 elementos
print(array1d)

array1d=np.linspace(1, 12, 4)                #Genera un arreglo unidimensional de números desde el 1 hasta el 12 con 4 elementos
print(array1d)

array2d=np.linspace(1, 12, 12).reshape(4,3)  #Genetra un arreglo bidimensional de números desde el 1 hasta el 12 con 12 elementos (ajustando la forma con reshape)
print(array2d)
print()

#logspace(): crea un arreglo que devuelve los valores al operar el logarítmo específicado
#sintaxis -> np.logspace(Inicio, Fin, [Booleano Opcional] endpoint=true/false, # de elementos, base del log, dtype)
thearray=np.logspace(5, 10, endpoint=True, num=10, base=10000000.0, dtype=float)
print(thearray)
print()

#zeros(): genera un arreglo de ceros con la dimensión especificada
array1d=np.zeros(3)
print(array1d)

array2d=np.zeros((2, 4))
print(array2d)
print()

#ones(): crea un arreglo de unos con la dimensión especificada
array1d=np.ones(3)
print(array1d)

array2d=np.ones((2, 4))
print(array2d)
print()

#full(): crea un arreglo de un número específico con las dimensiones dadas
#sintaxis -> np.full(dimensión, número específico)
array1d=np.full((3), 2)
print(array1d)

array2d=np.full((2, 4), 3)
print(array2d)

#eye(): crea un arreglo cuadrado donde todos los elementos son 0 excepto a una diagonal k dada donde todos son 1.
#sintaxis -> np.eye(dimensión, dtype)
#         -> np.eye(dimensión, diagonal k)
array1=np.eye(3, dtype=int)
print(array1)

array2=np.eye(5, k=2)
print(array2)
print()

#random number array: genera números aleatorios descritos de la siguiente manera
#np.random.rand(size) -> genera un arreglo específicado de números aleatorios uniformemente distribuidos entre 0 y 1
#np.random.randn(size) -> genera un arreglo especificado de números aleatorios normalmente destribuidos entre 0 y 1
#np.random.randint(número límite, size) -> genera un arreglo especificado de números aleatorios uniformemente destribuidos etre 0 y el número límite
print(np.random.rand(3, 2))              #Uniformemente distribuido
print(np.random.randn(3, 2))             #Normalmente distribuido

print(np.random.randint(2, size=5))
print(np.random.randint(3, size=(2, 2)))
print()

#identity(): genera un arreglo bidimensional identidad
#sintaxis -> np.identity(dimensión)
print(np.identity(3))

#diag(): genera un arreglo bidimensional donde la diagonal principal se construye en base a un conjunto de números
#sintaxis -> np.diag(número)
print(np.diag(np.arange(0, 8, 1)))

#generando una matriz diagonal a partir de otra matriz
print(np.diag(np.diag(np.arange(9).reshape((3,3)))))   #el atributo np.diag() interno extrae los elementos de la diagonal de la matriz y el externo genera la matriz diagonal de esos mismos elementos
