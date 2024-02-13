#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#input()
print(my_lista) #Imprimir lista
"""
print(type(my_lista)) #Imprimir tipo de la lista
print(my_lista[2]) #Imprimir el elemento (x+1) de la lista

print("my_lista size: ", len(my_lista)) #Imprime la cantidad de objetos guardados en la lista 
print(my_lista[0:2]) #Imprime los objetos que se encuentran en el rando asignado (x:y) de la lista
print(my_lista[:4]) #Imprime los objetos de la lista en orden hasta el rango asginado

my_lista.append('Blanco') #Agrega elemento al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro') #Agrega un elemento en la posicion (x+1) de la lista 
print(my_lista)

my_lista.extend(['Marron', 'Gris']) #Concatena a otra lista
print(my_lista)

print(my_lista.index('Azul')) #Devuelve la posición del objeto asignado.

my_lista.remove('Marron') #Remueve de la lista el objeto asignado
print(my_lista)

my_lista.insert(8, 'Marron') #Agrega EL elemento en la posicion (8+1) de la lista 
print(my_lista)

print(my_lista.pop()) #Elimina e imprime el ultimo elemento de la lista 
print(my_lista)
size = len(my_lista) #Guarda en la variable size el tamaño de la lista
print("size = ", size) #Imprime el valor de size

my_lista_3 = my_lista*3 #Guarda en la lista (my_lista_3) los elementos triplicados en orden de (my_lista)
print("my_lista_3: ", my_lista_3) #Imprime los elementos de my_lista_3
""" 
print(my_lista)
my_lista.sort()
print(my_lista)
