# get user input
print("please copy and paste digikey page.\n"
      "To end recording Press Ctrl+d on Linux/Mac on Crtl+z on Windows")
lines = []
try:
	while True:
		user_input = input()
		lines.append(user_input)
except EOFError:
	pass

# clear the screen
import os
os.system('cls')  # For Windows

'''
Manufacturer_Part_Number = ""
Manufacturer = ""
Distributor_Part_Number = ""
Description = ""
Value = ""
Tolerance = ""
Package_Case = ""
Packaging = ""
'''

# extract data from input
for line in lines:
	if line.find("Manufacturer Part Number") == 0:
		Manufacturer_Part_Number = line[24:]
	elif line.find("Manufacturer Standard") == 0:
		pass
	elif line.find("Categories") == 0:
		Type = line[10:]
	elif line.find("Manufacturer") == 0:
		Manufacturer = line[12:]
	elif line.find("Digi-Key Part NumberManufacturer Part Number") == 0:
		pass
	elif line.find("Digi-Key Part Number") == 0:
		Distributor_Part_Number = line[20:]
	elif line.find("Detailed Description") == 0:
		Description = line[20:]
	elif line.find("Resistance") == 0:
		Value = line[10:]
	elif line.find("Capacitance") == 0:
		Value = line[11:]
	elif line.find("Inductance Frequency") == 0:
		pass
	elif line.find("Inductance") == 0:
		Value = line[10:]
	elif line.find("Tolerance") == 0:
		Tolerance = line[9:]
	elif line.find("Package / Case") == 0:
		Package_Case = line[14:]
	elif line.find("Packaging ?") == 0:
		Packaging = line[11:-2]

if Manufacturer_Part_Number == "":
	print("Error extracting part information")
	exit();
	
# copy manufacturer part number to clipboard
import pyperclip
pyperclip.copy(Manufacturer_Part_Number)
spam = pyperclip.paste()


#symbol
print("Select footprint for component:")
print("[1] Standard resistor")
print("[2] Standard capacitor")
print("[3] Standard inductor")
print("[4] Other")

symbol_selection = input()
if symbol_selection == "1":
	part_symbol = "discrete\RESISTOR,SMALL R1,analog\R"
if symbol_selection == "2":
	part_symbol = "discrete\CAPACITOR NON-POL,discrete\CAP NP,SMALL CAP,analog\C"
if symbol_selection == "3":
	part_symbol = "INDUCTOR,INDUCTORa,analog\L"
	

# put the data in database
import pyodbc

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb)};'
    r'DBQ=D:\CIS_DB\my_orcad_cis_db.MDB;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()


# table columns
data = ( \
	["[Part Number]", Distributor_Part_Number], \
	["[Part Type]", Type], \
	["[Distributor]", "Digi-Key"], \
	["[Value]", Value], \
	["[Description]", Description], \
	["[Tolerance]", Tolerance], \
	["[Schematic Part]", part_symbol], \
	["[Allegro PCB Footprint]", "none"], \
	["[Manufacturer Part Number]", Manufacturer_Part_Number], \
	["[Manufacturer]", Manufacturer], \
	["[Distributor Part Number]", Distributor_Part_Number], \
	["[Package / Case]", Package_Case], \
	["[Packaging]", Packaging], \
	)

columns = data[0][0]
values = "'" + data[0][1] + "'"
success_message = data[0][0] + ": "+ data[0][1]

for i in range(1, len(data)):
		columns += ", " + data[i][0]
		values += ", '" + data[i][1] + "'"
		success_message += "\n" + data[i][0] + ": "+ data[i][1]
		
insert_query = "INSERT INTO Components ("+ columns +") VALUES (" + values + ")"
crsr.execute(insert_query)
cnxn.commit()

print ("Part has been succesfully added to CIS database:")
print (success_message)
end = input()