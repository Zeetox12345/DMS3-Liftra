import sys

# Read arguments
Weldlength = float(sys.argv[1])
Weldwidth  = float(sys.argv[2])
Weldthick  = float(sys.argv[3])
Weldthroad = float(sys.argv[4])

with open("Ncreate.txt","w") as file:
    file.write("NODE CREATION \n")
    file.write("N,1,1,1,1 \n")
    file.write("N,2,2,2,2 \n")
    file.write("N,3,3,3,3 \n")
    file.write("FINISH NODE CREATION \n")
