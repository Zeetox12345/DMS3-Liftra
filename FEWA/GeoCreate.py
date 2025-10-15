import sys

# Read arguments
Weldlength = float(sys.argv[1])
Weldwidth  = float(sys.argv[2])
Weldthick  = float(sys.argv[3])
Weldthroat = float(sys.argv[4])

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
    file.write(f"K,8,0,{Weldwidth},{Weldthick} \n")

    file.write("!    FINISH KEYPOINT CREATION \n")

    file.write(" !   LINE CREATION\n ")
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
    file.write("!    FINISH LINE CREATION \n")
    
    
    file.write("v,1,2,3,4,5,6,7,8 \n")

    
