import random
import timeit

NumRan = open("NumRan.txt", "w")
NumRan.write("0,")

for x in range(1000):
    num1=random.random()
    nums=str(num1)
    NumRan.write(f'{num1},')
    #print (num1)
    
NumTime = open("NumTime.txt", "w")
NumTime.write("0,")

for x in range(1000):
    tiempo = timeit.timeit (stmt=nums, number=1)
    NumTime.write(f'\n{tiempo},')
    
    
NumRan.close()
NumRan=open("NumRan.txt","r")
print(NumRan.read())

NumTime.close()
NumTime = open("Numtime.txt","r")
print (NumTime.read())