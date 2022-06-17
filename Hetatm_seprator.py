import sys

try:
    if len(sys.argv) < 2: raise SystemError
    pdbname = sys.argv[-1]
    print(f"PDBNAME: {pdbname} Processing...")
except Exception as E:
    print("Failed: ", E)
    print("Please try : \n$ python3.9 Hetatm_seprator.py <Protein.pdb>")
    raise SystemExit


Protein = []
Ligand = {}
with open(pdbname) as pp:
    for lines in pp:
        if lines.startswith("ATOM"):
            Protein.append(lines)
        if lines.startswith("HETATM"):
            #HETATM 8095 Br   LIG     1     -35.425  63.160  18.271  0.00  0.00      x_11Br
            name = "_".join(lines[17:26].split())
            if name not in Ligand: Ligand[name] = []
            Ligand[name].append(lines)
           
with open("Protein.pdb", "w") as pp:
    for lines in Protein:
        pp.write(lines)
    pp.write("TER\nEND")
    print(f"Finished! writing: Protein.pdb")


for each_ligand in Ligand:
    with open(f"{each_ligand}.pdb", "w") as ll:
        for lines in Ligand[each_ligand]:
            ll.write(lines)
        ll.write("TER\nEND")
        print(f"Finished! writing: {each_ligand}")
