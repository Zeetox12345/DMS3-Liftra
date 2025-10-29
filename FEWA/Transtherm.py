### TRANSIENT THERMAL ANALYSIS CODE
### SOLVER, CURRENTLY USING NROPT,FULL


def trans_create(p):
    Weldlength = p["Weldlength"]
    Weldwidth = p["Weldwidth"]
    Weldthick = p["Weldthick"]
    Weldthroat = p["Weldthroat"]
    X1 = p["X1"]
    Y1 = p["Y1"]
    Z1 = p["Z1"]
    Weld_vel = p["Weld_vel"]
    break_weld_pass_1 = p["Break_1"]

    time_weld_pass_1 = Weldlength/Weld_vel
    Analysis_time = time_weld_pass_1 + break_weld_pass_1
    time_inc = 0.5

    DIR_pass1 = 1

    def extract_value(v):
        if isinstance(v,set):
            return list(v)[0]
        return v

    with open("trans_file.txt","w") as file:
        file.write("!----- TRANSIENT THERMAL ANALYSIS ----- \n \n")
        file.write(f"!X1 value: {X1} \n!Y1 value: {Y1} \n!Z1 value: {Z1} \n \n")
        file.write("/SOLU \n") # Intialize Solution Menu
        file.write("ANTYPE,TRANSIENT,NEW \n") # New Transient Thermal
        file.write("KBC,1 \n") # Stepped BC's
        file.write("ALLSEL,ALL \n") # Make sure everything (elemtns, nodes etc.) is selected
        file.write("TUNIF,75 \n \n") # Setting Initial Temperature for all nodes

        # Convection
        file.write("! Apply Convection \n")
        file.write("ALLSEL,ALL \n")
        file.write("SF,ALL,CONV,7.5e-6,22 \n")


        file.write("\n!--- Time step options --- \n") # Time Step Options
        file.write("AUTOTS,OFF \n")
        file.write("DELTIM,0.5 \n") # Time Step of 0.5 sec
        file.write(f"TIME,{Analysis_time:.2f} \n") # Set Analysis time
        file.write("timint,on \n") # Set time integration on
        file.write("!------------------------- \n \n")

        file.write(f"X1 = {extract_value(X1)} \n")
        file.write(f"Y1 = {extract_value(Y1)} \n")
        file.write(f"Z1 = {extract_value(Z1)} \n")
        file.write("DIR_Pass1 = 1 ! + x \n") # Direction of Pass 1
        file.write("CMSEL,ALL \n") # Select all Components
        file.write("*GET,EMAX,ELEM,,NUM,MAX \n") # Select Max Node Number REDUNDANT
        file.write("*GET,EMIN,ELEM,,NUM,MIN \n ") # Select Min Node Number REDUNDANT
        file.write("ALLSEL,ALL\n") # Make sure everything is selected
        file.write("NROPT,FULL \n") # Full Newton Raphson Solver

        # Goldack Parameters
        file.write("!---Source Parameters --- \n")
        file.write("A = 3.0 \n")
        file.write("B = 4.0 \n")
        file.write("C1 = 4.0 \n")
        file.write("C2 = 16.0 \n")
        file.write("TAU = 0 \n")
        file.write("FF = 0.6 \n")
        file.write("FR = 1.4 \n")
        file.write("PI = acos(-1) \n")
        file.write(f"VEL_1 = {Weld_vel} \n \n") # Welding Velocity for Pass 1
        file.write("Q = 2840000 \n")


        # Timing
        file.write("! TIMING (per pass + break) \n")
        file.write(f"time_inc = {time_inc} ! sec \n") # Time incement for CMH
        file.write(f"time_weld_pass_1 = {time_weld_pass_1:.2f} \n") # Weld time for Pass 1
        file.write(f"break_weld_pass_1 = {break_weld_pass_1} ! s \n") # Break for Pass 1

        # Number of Steps
        n1 = time_weld_pass_1 / time_inc
        nb1 = break_weld_pass_1 / time_inc
        file.write("n1 = time_weld_pass_1 / time_inc \n")
        file.write("nb1 = break_weld_pass_1 / time_inc \n")

        # Start/end times for welds
        TBASE1 = 0
        END1 = TBASE1 + time_weld_pass_1 
        
        file.write(f"TBASE1 = {TBASE1} \n")
        file.write(f"END1 = {END1} \n")


        # PASS 1
        file.write("\n!--- PASS_1 --- \n") 
        file.write("*DO,i1,1,n1,1 \n")
        file.write(f"WTIME = TBASE1 + (i1*time_inc) \n")
        file.write("BFEDELE,ALL,HGEN \n")
        file.write("  TIME,WTIME \n \n")
        file.write(f"  Xc = X1 + DIR_pass1*{Weld_vel}*(WTIME-{TBASE1}-TAU)  \n")
        file.write(f"  Yc = Y1 \n")
        file.write(f"  Zc = Z1 \n")

        file.write("  *GET,ECNT,ELEM,,COUNT \n")
        file.write("  *IF,ECNT,GT,0,THEN \n")
        file.write("    *GET,EMINS1,ELEM,,NUM,MIN \n")
        file.write("    *GET,EMAXS1,ELEM,,NUM,MAX \n \n")

        file.write("    *DO,jj1,EMINS1,EMAXS1,1 \n")
        file.write("      X = CENTRX(jj1) \n")
        file.write("      Y = CENTRY(jj1) \n")
        file.write("      Z = CENTRZ(jj1) \n \n")
        file.write("      XREL = X - Xc \n")
        file.write("      YREL = Y - Yc \n")
        file.write("      ZREL = Z - Zc \n \n")

        file.write("      *IF,YREL,GT,0,THEN \n")
        file.write("        C = C1 \n")
        file.write("        F = FF \n")
        file.write("      *ELSE \n")
        file.write("        C = C2 \n")
        file.write("        F = FR \n")
        file.write("      *ENDIF \n")
        file.write("      PART1 = (6*(3**0.5)*Q*F)/(A*B*C*PI*(PI**0.5)) \n")
        file.write("      PART2 = (exp(-3*(XREL/A)**2))*(exp(-3*(YREL/B)**2))*(exp(-3*(ZREL/C)**2)) \n")
        file.write("      QF = PART1*PART2 \n \n")
        file.write("      BFE,jj1,HGEN,,QF \n")
        file.write("    *ENDDO \n")
        file.write("  *ENDIF \n")
        file.write("  ALLSEL,ALL \n")
        file.write("  SOLVE \n")
        file.write("  BFDELE,ALL,HGEN \n ")
        file.write("*ENDDO \n")
        file.write("BFEDELE,ALL,HGEN \n \n")


        # Break After Pass 1
        file.write("!--- BREAK AFTER PASS 1 --- \n")
        file.write("*IF,nb1,GT,0,THEN \n")
        file.write("  *DO,ib1,1,nb1,1 \n")
        file.write("    WTIME = END1 + ib1*time_inc \n")
        file.write("    TIME,WTIME \n")
        file.write("    ALLSEL,ALL \n")
        file.write("    SOLVE \n")
        file.write("  *ENDDO \n")
        file.write("*ENDIF \n")


        # Solve Transient Thermal 
        file.write("SOLVE \n")
        


        file.write("\n!----- FINISH TRANSIENT THERMAL ANALYSIS ----- \n \n")