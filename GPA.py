# Module Vs. Credit Points

CP_MATH = 3
CP_CS = 3
CP_ELEC = 2
CP_MECH = 2
CP_FL_MECH = 2
CP_MAT = 2

TOTAL = 14

# Grade Vs. Grade Points

def GradePoint_Cal(Grade):
    if (Grade == 'A+')or(Grade == 'A'):
        return 4.00
    elif (Grade == 'A-'):
        return 3.70
    elif (Grade == 'B+'):
        return 3.30
    elif (Grade == 'B'):
        return 3.00
    elif (Grade == 'B-'):
        return 2.70
    elif (Grade == 'C+'):
        return 2.30
    elif (Grade == 'C'):
        return 2.00
    elif (Grade == 'C-'):
        return 1.70
    elif (Grade == 'D'):
        return 1.00
    else:
        return 0.00

# Calculation

def GPA(MATH, CS, ELEC, MECH, FL_MECH, MAT):
    Sum = MATH*CP_MATH + CS*CP_CS + ELEC*CP_ELEC + MECH*CP_MECH + FL_MECH*CP_FL_MECH + MAT*CP_MAT
    return float(Sum)/TOTAL

# Input

print("Enter your grades accordingly")
Maths = GradePoint_Cal(input("Maths: "))
Com_Sc = GradePoint_Cal(input("Programming Fundementals: "))
Etric = GradePoint_Cal(input("Electrical Fundementals: "))
Mech = GradePoint_Cal(input("Mechanics: "))
Fluid = GradePoint_Cal(input("Fluid Mechanics: "))
Material = GradePoint_Cal(input("Properties of Materials: "))

# Finalization

Final_GPA = GPA(Maths, Com_Sc, Etric, Mech, Fluid, Material)
print("Your GPA is " + str('%.2f' % Final_GPA))

input("Press Enter to exit")

# 3.7 < First Class
# 3.3 < Second Upper
# 3.0 < Second Lower
# 2.0 < Pass