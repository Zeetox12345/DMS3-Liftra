import sys
import math

# Read arguments
Weldlength = float(sys.argv[1])
Weldwidth  = float(sys.argv[2])
Weldthick  = float(sys.argv[3])
Weldthroat = float(sys.argv[4])

# Weld Katete Length
Wkat = Weldthroat / 2 / math.cos(math.radians(45))


with open("Ncreate.txt","w") as file:
    ##### Coordinate is [N,ID,x,y,z]
    file.write("!    KEYPOINT CREATION \n")
    file.write("!Reinforcement Plate \n")
    file.write("K,1,0,0,0 \n")
    file.write(f"K,2,{Weldlength},0,0 \n")
    file.write(f"K,3,{Weldlength},{Weldwidth},0 \n")
    file.write(f"K,4,0,{Weldwidth},0 \n")
    file.write(f"K,5,0,0,{Weldthick} \n")
    file.write(f"K,6,{Weldlength},0,{Weldthick} \n")
    file.write(f"K,7,{Weldlength},{Weldwidth},{Weldthick} \n")
    file.write(f"K,8,0,{Weldwidth},{Weldthick} \n \n")


    file.write("!WeldToe 1 \n")
    file.write(f"K,9,0,-0.5,{Weldthick} \n")
    file.write(f"K,10,0,-0.5,{Weldthick + Wkat} \n")
    file.write(f"K,11,0,{-0.5 + Wkat},{Weldthick} \n")
    file.write(f"K,12,0,{-0.5+  Wkat/2},{Weldthick+Wkat/2}\n")

    file.write(f"K,13,{Weldlength},-0.5,{Weldthick} \n")
    file.write(f"K,14,{Weldlength},-0.5,{Weldthick +Wkat} \n")
    file.write(f"K,15,{Weldlength},{-0.5+Wkat},{Weldthick} \n")
    file.write(f"K,16,{Weldlength},{-0.5+  Wkat/2},{Weldthick+Wkat/2} \n")

    file.write("!    FINISH KEYPOINT CREATION \n")

    file.write("!   LINE CREATION\n ")
    file.write("!Reinforcement Plate \n")
    file.write("L,1,2\n")
    file.write("L,2,3\n")
    file.write("L,3,4\n")
    file.write("L,4,1\n")
    file.write("L,5,6\n")
    file.write("L,6,7\n")
    file.write("L,7,8\n")
    file.write("L,8,5\n")
    file.write("L,1,5\n")
    file.write("L,2,6\n")
    file.write("L,3,7\n")
    file.write("L,4,8\n")

    file.write("!Weld Toe 1 \n")
    file.write("L,9,11\n")
    file.write("L,9,10\n")
    file.write("L,10,12\n")
    file.write("L,12,11\n")

    file.write("L,13,15\n")
    file.write("L,13,14\n")
    file.write("L,14,16\n")
    file.write("L,16,15\n")

    file.write("L,9,13\n")
    file.write("L,10,14\n")
    file.write("L,11,15\n")
    file.write("L,12,16\n")


    file.write("!    FINISH LINE CREATION \n")
    
    # Create Volumes
    file.write("v,1,2,3,4,5,6,7,8 \n")
    file.write("v,9,10,11,13,14,15 \n")

    
