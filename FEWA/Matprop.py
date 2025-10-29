# Material Properties

# Temperature Dependent Thermal Conductivity
temp_C = [0, 800, 1459, 1500, 2500]
k_W_mK = [53.334, 27.3, 27.3, 259.3, 259.3]

# Temperature Dependent Heat Capacity
temp_HC = [31.81, 599.92, 723.87, 803.23, 1394.04, 1488.06, 1506.69]
HC =      [494.22, 1042.38, 2558.42, 961.87, 1215.78, 5371.89, 987.12]

Temp_Mech = [20,100,200,300,400,500,600,700,800,900,1000,1100,1200,1500]
EmodMPA = [200,200,180,160,140,120,62,26,18,13.5,9,4.5,3,3]
EmodGPA = [e*1000 for e in EmodMPA]

nu = [0.30,0.31,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.39,0.40,0.41,0.42,0.46]
sigy = [690,690,621,552,483,414,213.9,89.7,62.1,46.575,31.05,15.525,5,5]
tan = [585,585,472.095,358.605,245.7,210.6,105.3,43.875,29.25,21.9375,14.625,7.3125,0.1,0.1]

Temp_CTE = [0,100,200,300,400,600,800,1200,1500]
CTE = [1.2e-5,1.22e-5,1.24e-5,1.26e-5,1.28e-6,1.32e-5,1.36e-5,1.44e-5,1.5e-5]

with open("Matprop.txt", "w") as file:
    file.write("!----- MATERIAL PROPERTIES ----- \n \n ")
    file.write("MP, DENS, 1, 7.85E-9      ! Density [Mg/mm^3] \n")

    # Thermal Conductivity
    file.write("!TD Thermal Conductivity [W/mmC] \n")
    file.write("MPTEMP,1," + ",".join(str(t) for t in temp_C) + "\n")
    file.write("MPDATA,KXX,1,1," + ",".join(f"{k/1000.0:.6g}" for k in k_W_mK) + "\n")

    # Heat Capacity
    file.write("MPTEMP,\n \n")
    file.write("!TD Heat Capacity [Nmm/MgC] \n")
    file.write("MPTEMP,")
    file.write("MPTEMP,1," + ", ".join(str(t) for t in temp_HC) + " \n")
    file.write("MPTEMP, , 1506.69 \n")
    file.write("MPDATA,C,1,1," + ",".join(f"{cp:.6g}" for cp in HC) + "\n")
    file.write("MPDATA, C, 1, 7, 987.12 \n")
    file.write("MPTEMP,\n")

    # E Modulus
    file.write("! Youngs Modulus [GPA] \n")
    file.write("MPTEMP,1," + ",".join(str(t) for t in Temp_Mech[0:6])  + "\n")
    file.write("MPTEMP, ," + ",".join(str(t) for t in Temp_Mech[6:12]) + "\n")
    file.write("MPTEMP, ," + ",".join(str(t) for t in Temp_Mech[12:14]) + "\n")
    file.write("MPDATA,EX,1,1,"  + ",".join(f"{v:.6g}" for v in EmodGPA[0:6])   + "\n")
    file.write("MPDATA,EX,1,7,"  + ",".join(f"{v:.6g}" for v in EmodGPA[6:12])  + "\n")
    file.write("MPDATA,EX,1,13," + ",".join(f"{v:.6g}" for v in EmodGPA[12:14]) + "\n")
    file.write("MPTEMP,\n")

    # Coefficient of Thermal Expansion [1/C]
    file.write("! Temperature-Dependent Coefficient of Thermal Expansion\n")
    file.write("MPTEMP,1," + ",".join(str(t) for t in Temp_CTE[0:6]) + "\n")
    file.write("MPTEMP, ," + ",".join(str(t) for t in Temp_CTE[6:]) + "\n")
    file.write("MPDATA,ALPX,1,1," + ",".join(f"{v:.6g}" for v in CTE[0:6]) + "\n")
    file.write("MPDATA,ALPX,1,7," + ",".join(f"{v:.6g}" for v in CTE[6:]) + "\n")
    file.write("MPTEMP,\n")

    # Poisson Ratio - Use the same MPTEMP
    file.write("MPTEMP,1," + ",".join(str(t) for t in Temp_Mech[0:6])  + "\n")
    file.write("MPTEMP, ," + ",".join(str(t) for t in Temp_Mech[6:12]) + "\n")
    file.write("MPTEMP, ," + ",".join(str(t) for t in Temp_Mech[12:14]) + "\n")    
    file.write("MPDATA,PRXY,1,1,"+",".join(str(t) for t in nu[0:6]) + " \n")
    file.write("MPDATA,PRXY,1,7,"+",".join(str(t) for t in nu[6:12]) + " \n")
    file.write("MPDATA,PRXY,1,,"+",".join(str(t) for t in nu[12:14]) + " \n")

    # BISO TD Model [MPa Units]
    file.write("TB, PLAS, 1, 2,,BISO \n")
    for i in range(len(Temp_Mech)):
        file.write(f"TBTEMP,{Temp_Mech[i]} \n")
        file.write(f"TBDATA,1,{sigy[i]},{tan[i]} \n")



    file.write("!----- FINISH MATERIAL PROPERTIES -----\n \n")