import numpy as np
'''
Índices en matrices
'''
#Para ello se señala el arreglo seguido de un par de corchetes y dentro de ella se especifica la posición del arreglo
#En arreglos unidimensiobales
array1d=np.array([1, 2, 3, 4, 5, 6])
print(array1d[0])           #Muestra el primer elemento
print(array1d[-1])          #Muestra el último elemento
print(array1d[3])           #Muestra el cuarto elemento
print(array1d[-4])          #Muestra el cuarto elemento recorrido de derecha a izquierda
print(array1d[[0, -1]])     #Creamos un arreglo a partir de la selección de datos de otro arreglo
print()

#En arreglos bidimensionales
array2d=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array2d[0, 0])        #Muestra el elemento que se encuentra en la primera fila y la primera columna
print(array2d[0, 1])        #Muestra el elemento que se encuentra en la primera fila y la segunda columna
print(array2d[1, 0])        #Muestra el elemento que se encuentra en la primera fila y la primera columna
print(array2d[2, 2])        #Muestra el elemento que se encuentra en la tercera fila y la tercera columna
print()

#En arreglos tridimensionales
array3d=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array3d[0, 0, 0])   
print(array3d[1, 0, 0])
print(array3d[0, 1, 0])
print(array3d[0, 0, 1])
print(array3d[1, 1, 2])
print(array3d[1, 1, 0])
print()

'''
Simple corte unidimensional
'''
print()
