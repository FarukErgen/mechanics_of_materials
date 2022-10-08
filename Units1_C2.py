# Mechanics of Materials Sixth Edition Unit 1 problem C2

print("Solution of the 1.C2")

# size of member ABC (mm)

a, b = 10, 50

# size of vertical links (mm)
c, d = 8, 36

length_AB = 250
length_BC = 400

load_A_point = 20000

# Momentb = 0

force_C = (load_A_point*length_AB)/length_BC

force_B = (load_A_point + force_C)

# d = diameter of pin (each of four pins has same diameter)

for i in range(10, 31):
    print("for d=", i, " mm:")
    max_normal_stress_B = (force_B/2)/(c*(d-i))

    average_normal_stress_C = (force_C/2)/(c*d)

    average_shearing_stress_B = (force_B/2)/(3.14*i*i/4)

    average_shearing_stress_C = (force_C/2)/(3.14*i*i/4)

    average_bearing_stress_B = force_B/(a*(i))

    average_bearing_stress_C = force_C/(a*(i))

    print("Max. normal stress B:", round(max_normal_stress_B, 2))
    print("Average normal stress C:", round(average_normal_stress_C, 2))
    print("Average shearing stress B:", round(average_shearing_stress_B, 2))
    print("Average shearing stress C:", round(average_shearing_stress_C, 2))
    print("Average bearing stress B:", round(average_bearing_stress_B, 2))
    print("Average bearing stress C:", round(average_bearing_stress_C, 2))
    print("-------------------------------------")
