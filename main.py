import matplotlib.pyplot as plt



startT = int(input("Введите начальную температуру: "))
plavT = int(input("Введите температуру плавления: "))
C = int(input("Введите удельную теплоёмкость(Дж\Кг): "))
lamb = int(input("Введите удельную теплоту плавления(Дж\Кг): "))
mass = int(input("Введите массу(Кг): "))

x = []
y = []

maxT = max([startT, plavT])
minT = min([startT, plavT])


x.append(0)
y.append(startT)

Q2 = C * mass * (maxT - minT)


x.append(Q2)
y.append(plavT)


limdMultiMass = (lamb * mass) + Q2


x.append(limdMultiMass)
y.append(plavT)

plt.plot(x, y)
plt.xlabel("Q Кдж")
plt.ylabel("t°C")
plt.title("Отношение количества теплоты от температуры")
plt.show()
print("\n")