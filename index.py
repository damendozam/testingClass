import random

arrayExample = [1,2,3,4,5]

for i in range(5):
    arrayExample[i]=int(random.uniform(100, 200))
    print(arrayExample[i-1])

varInput=int(input('Ingresa un valor:'))
print(varInput)

for i in range(5):
    if arrayExample[i] >= varInput:
        print("El valor del arreglo es mayor")
    else:
        print("El valor del arreglo es menor")
    print(str(arrayExample[i])+'>'+str(varInput))
