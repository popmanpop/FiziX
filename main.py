import matplotlib.pyplot as plt



startT = int(input("Введите начальную температуру: "))
plavT = int(input("Введите температуру плавления: "))
C = int(input("Введите удельную теплоёмкость(Дж\Кг): "))
lamb = int(input("Введите удельную теплоту плавления(Дж\Кг): "))
mass = int(input("Введите массу(Кг): "))


x = []
y = []

def Qcal(endQ, endT, lamMultMass, x: list , y: list):
    for q in range(endQ, lamMultMass):
        if q + 1 == lamMultMass:
            x.append(q)
            y.append(endT)
        if q == endQ:
            x.append(q)
            y.append(endT)

for temp in range(startT, plavT+1):

    deltaT = temp - startT
    Q = C * mass * deltaT
    
    if temp == startT:
        x.append(Q)
        y.append(temp)
    if temp + 1 == plavT + 1:
        x.append(Q)
        y.append(temp)
    if temp >= plavT:
        Qcal(Q, temp, mass * lamb, x , y)
        break
    
    

plt.plot(x, y)
plt.xlabel("Q Кдж")
plt.ylabel("t°C")
plt.title("Отношение количества теплоты от температуры")
plt.show()