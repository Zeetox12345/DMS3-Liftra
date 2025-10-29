###################################################
#################### MESHING ###################### 
# This document creates the Meshing_file.txt which is passed into Runfile.txt


# Meshing
def meshing_create(p):
    Wkat = p["Wkat"]
    Weldlength = p["Weldlength"]
    Weldwidth = p["Weldwidth"]
    Weldthick = p["Weldthick"]
    Weldthoat = p["Weldthroat"]

    with open("meshing_file.txt","w") as file:
        file.write("\n!----- MESHING ----- \n")
        file.write("ET,1,SOLID279 ! Element Type \n")

        file.write("!Selecting Lines \n")
        # Weld SHORT Edge Selection
        wsE = Weldthoat
        file.write("LSEL,S,LINE,, 14 \n")
        file.write("LSEL,A,LINE,, 25 \n")
        file.write("LSEL,A,LINE,, 29 \n")
        file.write("LSEL,A,LINE,, 27 \n")

        file.write("LSEL,A,LINE,, 30 \n")
        file.write("LSEL,A,LINE,, 28 \n")
        file.write("LSEL,A,LINE,, 18 \n")
        file.write("LSEL,A,LINE,, 26 \n")

        file.write(f"LESIZE, ALL, {wsE/4} \n")

        # Weld LONG Edge Selection
        file.write("LSEL,S,LINE,, 21 \n")
        file.write("LSEL,A,LINE,, 5 \n")
        file.write("LSEL,A,LINE,, 22 \n")
        file.write("LSEL,A,LINE,, 24 \n")
        file.write("LSEL,A,LINE,, 23 \n")
        file.write(f"LESIZE, ALL, {wsE/2} \n")

        # RP HORIZONTAL Edge Selection
        file.write("LSEL,S,LINE,, 4 \n")
        file.write("LSEL,A,LINE,, 32 \n")
        file.write("LSEL,A,LINE,, 3 \n")
        file.write("LSEL,A,LINE,, 7 \n")
        file.write("LSEL,A,LINE,, 2 \n")
        file.write("LSEL,A,LINE,, 31 \n")
        file.write("LSEL,A,LINE,, 1 \n")
        file.write(f"LESIZE, ALL, {wsE/2} \n")

        # RP VERTICAL Line Selection
        file.write("LSEL,S,LINE,, 10 \n")
        file.write("LSEL,A,LINE,, 11 \n")
        file.write("LSEL,A,LINE,, 12 \n")
        file.write("LSEL,A,LINE,, 9 \n")
        file.write(f"LESIZE, ALL, {Weldthick/2} \n")

        file.write("LSEL,ALL \n")
        file.write("/PNUM,LINE,1 \n")
        file.write("LPLOT \n")

        # Create Mesh
        file.write("!Setting Mesh Parameters \n ")
        file.write("MSHKEY, 1 \n")
        file.write("VSWEEP, ALL ! Creating Mesh \n")
        file.write("SHPP,SUMMARY\n")
        file.write("!----- MESH FINISH ----- \n \n")

if __name__ == "__main__":
    import sys