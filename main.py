import matplotlib.pyplot as plt



startT = int(input("Введите начальную температуру: "))
plavT = int(input("Введите температуру плавления: "))
C = int(input("Введите удельную теплоёмкость: "))
lamb1 = int(input("Введите первую часть удельной теплоты плавления: "))
lamb2 = int(input("Введите степень удельной теплоты плавления: "))
mass = int(input("Введите массу: "))
 
lamb = lamb1 ** lamb2
Qcount = 0
#dumbNumber = 10000000000 ** 100000000000000
x = []
y = []

def Qcal(endQ, endT, lamMultMass, x: list , y: list):
    for q in range(endQ, lamMultMass, C):
        x.append(q)
        y.append(endT)

for temp in range(startT, plavT+1):

    deltaT = temp - startT
    Q = C * mass * deltaT

    if temp >= plavT:
        Qcal(Q, temp, Q * lamb, x , y)
        break
    else:
        x.append(Q)
        y.append(temp)
    

plt.plot(x, y)
plt.xlabel("Q Кдж")
plt.ylabel("t°C")
plt.title("Отношение количества теплоты от температуры")
plt.show()