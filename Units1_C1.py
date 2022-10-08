# Mechanics of Materials Sixth Edition Unit 1 problem C1

from math import pi
print("Solution of the 1.C1")
try:
    n = int(input("Enter number of loads:"))
except:
    print("Please enter a digit.")
    quit()

loads_list = []
diameters_list = []
average_stress_list = []
for i in range(1, n+1):
    print(i, ".cylindrical element:")
    p = int(input("Enter load for cylindrical element (N): "))
    d = float(input("Enter diameter for cylindrical element (mm):"))
    loads_list.append(p)
    diameters_list.append(d)

for k in range(0, n):
    area = (pi*pow(diameters_list[k], 2))/4
    load = 0
    for m in loads_list[k:]:
        load += m
    stress = load/area
    average_stress_list.append(round(stress, 3))

for c,j in enumerate(average_stress_list):
    print("Average stress of ", c+1, " cylindrical element =", j," Mpa")
    print("------------------------------")
