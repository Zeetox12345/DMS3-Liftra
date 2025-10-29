### TRANSIENT THERMAL ANALYSIS CODE


def trans_create(p):
    Weldlength = p["Weldlength"]
    Weldwidth = p["Weldwidth"]
    Weldthick = p["Weldthick"]
    Weldthroat = p["Weldthroat"]
    X1 = p["X1"]
    Y1 = p["Y1"]
    Z1 = p["Z1"]

    with open("trans_file.txt","w") as file:
        file.write("!----- TRANSIENT THERMAL ANALYSIS ----- \n \n")
        file.write(f"X1 value: {X1} \nY1 value: {Y1} \nZ1 value: {Z1} \n \n")
        file.write("/SOLU \n") # Intialize Solution Menu
        file.write("ANTYPE,TRANSIENT,NEW \n") # New Transient Thermal
        file.write("ALLSEL,ALL") # Make sure everything (elemtns, nodes etc.) is selected
        file.write("TUNIF,75") # Setting Initial Temperature for all nodes