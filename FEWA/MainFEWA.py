#############################################################
############## Finite Element Weld Analysis #################
#############################################################

# Main Document
import os
import subprocess

# Read user input
variables = {}

with open("UsrInput.txt","r") as file:
    for line in file:
        line = line.strip()
        # Skip comments and empty lines
        if not line or line.startswith("#"):
            continue
        # Split variables name and value
        if "=" in line:
            name,value = line.split("=")
            variables[name.strip()] = float(value.strip())

# Create geometry


# Create Runfile
with open("Runfile.txt", "w") as file:
    file.write("\PREP7\n")



# Run ANSYS APDL in batch mode
ansys_path = r"C:\Program Files\ANSYS Inc\v251\ansys\bin\winx64\ANSYS251.exe"
input_file = "Runfile.txt"
output_file = "output.txt"

subprocess.run([ansys_path, "-b", "-i", input_file, "-o", output_file, "-np", "6"])
