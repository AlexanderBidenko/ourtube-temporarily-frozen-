import copy
import math
from matplotlib import pyplot as plt


dict_of_param = dop = {"CO2": [-393.51, 213.6, 37.13],
                    "CaCO3": [-1206, 92.9, 81.85],
                    "CaO": [-635.1, 39.7, 42.8]}

tusk = "CaCO3=CaO+CO2"
left = (tusk.split("=")[0]).split("+")
right = (tusk.split("=")[1]).split("+")

"""
print(left)
print(right)
print(len(left) + len(right))
"""

d_H_0_298 = 0
d_S_0_298 = 0
d_Cp_0_298 = 0

for i in range(len(right)):
    if dop.get(right[i]):
        d_H_0_298 += (dop.get(right[i])[0])
        d_S_0_298 += (dop.get(right[i])[1])
        d_Cp_0_298 += (dop.get(right[i])[2])
    else:
        if right[i][0].isdigit() and int(right[i][0]) != 0:
            d_H_0_298 += (dop.get(right[i][1:])[0]) * int(right[i][0])
            d_S_0_298 += (dop.get(right[i][1:])[1]) * int(right[i][0])
            d_Cp_0_298 += (dop.get(right[i][1:])[2]) * int(right[i][0])
        elif bool(right[i][3].isdigit()) == False:
            d_H_0_298 += ((dop.get(right[i][3:])[0]) * float(right[i][0:3]))
            d_S_0_298 += ((dop.get(right[i][3:])[1]) * float(right[i][0:3]))
            d_Cp_0_298 += ((dop.get(right[i][3:])[2]) * float(right[i][0:3]))
        elif bool(right[i][4].isdigit()) == True:
            d_H_0_298 += ((dop.get(right[i][3:])[0]) * float(right[i][0:4]))
            d_S_0_298 += ((dop.get(right[i][3:])[1]) * float(right[i][0:4]))
            d_Cp_0_298 += ((dop.get(right[i][3:])[2]) * float(right[i][0:4]))

        

for i in range(len(left)):
    if dop.get(left[i]):
        d_H_0_298 -= (dop.get(left[i])[0])
        d_S_0_298 -= (dop.get(left[i])[1])
        d_Cp_0_298 -= (dop.get(left[i])[2])
    else:
        if left[i][0].isdigit() and int(left[i][0]) != 0:
            d_H_0_298 -= (dop.get(left[i][1:])[0]) * int(left[i][0])
            d_S_0_298 -= (dop.get(left[i][1:])[1]) * int(left[i][0])
            d_Cp_0_298 -= (dop.get(left[i][1:])[2]) * int(left[i][0])
        elif bool(left[i][3].isdigit()) == False:
            d_H_0_298 -= ((dop.get(left[i][3:])[0]) * float(left[i][0:3]))
            d_S_0_298 -= ((dop.get(left[i][3:])[1]) * float(left[i][0:3]))
            d_Cp_0_298 -= ((dop.get(left[i][3:])[2]) * float(left[i][0:3]))
        elif bool(left[i][4].isdigit()) == True:
            d_H_0_298 -= ((dop.get(left[i][3:])[0]) * float(left[i][0:4]))
            d_S_0_298 -= ((dop.get(left[i][3:])[1]) * float(left[i][0:4]))
            d_Cp_0_298 -= ((dop.get(left[i][3:])[2]) * float(left[i][0:4]))


print(d_H_0_298)
print(d_S_0_298)
print(d_Cp_0_298)


d_G_0_298 = (d_H_0_298 * 1000) - (298 * d_S_0_298)
print(d_G_0_298)
d_G_n = copy.deepcopy(d_G_0_298)
list_of_dG = []
list_of_dT = []
list_of_dG.append(d_G_n)
temperature = 300
t = temperature
list_of_dT.append(t)
if d_G_0_298 > 0:
    while d_G_n > 0:
        t += 200
        d_G_n = (d_H_0_298 * 1000) - (t*d_S_0_298) - (d_Cp_0_298*(t - 298.16)) + (d_Cp_0_298*t*math.log(t/298.16))
        list_of_dG.append(d_G_n)
        list_of_dT.append(t)
    t += 200
    d_G_n = (d_H_0_298 * 1000) - (t * d_S_0_298) - (d_Cp_0_298 * (t - 298.16)) + (d_Cp_0_298 * t * math.log(t / 298.16))
    list_of_dG.append(d_G_n)
    list_of_dT.append(t)
"""    a = [[1, 2, -3],
              [2, 1, 2],
              [3, -2, -1]]
    b = [4, 3, 9]
    x = LA.solve(a, b) """
print(list_of_dG)

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
plt.figure(figsize=(12, 7))
plt.plot(list_of_dT, list_of_dG, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)

plt.legend()

plt.grid(True)

plt.show()
