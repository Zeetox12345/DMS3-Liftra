#############################################################
############## Finite Element Weld Analysis #################
#############################################################

# Main Document
import os
import subprocess
import GeoCreate
import Meshing
import Transtherm

##### NOTES / TO BE INVESTIGATED
# MAKE SURE UNITS ARE CORRECT INCLUDING TEMPERATURE



def main():

    # Read user input
    variables = {} # Allocate array
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

    # Run Material properties script
    subprocess.run(["python","Matprop.py",], check=True)

    # Compute Parameters from GeoCreate.py
    params = GeoCreate.comp_params(
        variables["Weldlength"],
        variables["Weldwidth"],
        variables["Weldthick"],
        variables["Weldthroat"],
    )
    # Add Weld_v to params manually
    for key in ["Weld_vel","Break_1"]:
        params[key] = variables[key]
    
        
    # Run ncreate in GeoCrate txt file to be passed.
    GeoCreate.write_ncreate(params)
    
    # Running the Meshing.py
    Meshing.meshing_create(params)

    ###### CREATE RUNFILE #####
    with open("Runfile.txt", "w") as file:
        file.write("!-------------------------------------- \n")
        file.write("!---------- APDL EXCECUTABLE ---------- \n")
        file.write("!-------------------------------------- \n \n ")
        file.write("!INITIALIZING \n ")
        file.write("/PREP7\n") 
        file.write("/UNITS,MPa\n \n") # [mm,Mg,s,C] - 1e6 Mg to 1 kg  

        
        with open("Matprop.txt", "r") as geo_file:
            for line in geo_file:
                file.write(line)

        # Insert geometry (Ncreate.txt content)
        with open("Ncreate.txt", "r") as geo_file:
            for line in geo_file:
                file.write(line)
        file.write("/PNUM,KP,1\n")
        file.write("/REPLOT\n")

        # Open the meshing file to be passed into the runfile
        with open("meshing_file.txt","r") as mesh_file:
            for line in mesh_file:
                file.write(line)

        # Running Transient Thermal Script
        Transtherm.trans_create(params)

        # Read output txt file from transtherm.py
        with open("trans_file.txt","r") as trans_file:
            for line in trans_file:
                file.write(line)



        # SaveFile
        file.write("!SAVING FILE \n")
        file.write("SAVE, SaveFile2.db\n")
    ##### END RUNFILE #####


    # Settings for Ansys APDL
    ansys_path = r"C:\Program Files\ANSYS Inc\v251\ansys\bin\winx64\ANSYS251.exe"
    input_file = "Runfile.txt"
    workdir = r"C:\Users\atbys\OneDrive - Aalborg Universitet\9. semester\VisualCodeLiftra\DMS3-Liftra\FEWA"
    output_dir = os.path.join(workdir,"Ansout")
    output_file = os.path.join(output_dir,"FEWA_output.txt")

    # Run the whole thaang
    """
    subprocess.run([
        ansys_path,
        "-b",
        "-i", os.path.abspath(input_file),
        "-o", output_file,
        "-dir", output_dir,
        "-j","FEWA",
        "-np", "4"
    
    ])
    """
if __name__ == "__main__":
    main()
