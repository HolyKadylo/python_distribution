import os
import json

# https://openpyxl.readthedocs.io/en/stable/
from openpyxl import *

# What is the current shift
# https://stackoverflow.com/a/103081
# https://janakiev.com/blog/python-shell-commands/
 
stream = os.popen('date +%H') # 07 15 23
currentHour = stream.read()

# TODO fix default
def shiftPicker(currentHour):
        currentHour = int(currentHour)
        shiftPicker={
                0: "night",
        	    1: "night",
        	    2: "night",
        	    3: "night",
        	    4: "night",
        	    5: "night",
        	    6: "morning",
        	    7: "morning",
        	    8: "morning",
        	    9: "morning",
        	    10: "morning",
        	    11: "morning",
        	    12: "morning",
        	    13: "morning",
                14: "evening",
        	    15: "evening",
        	    16: "evening",
        	    17: "evening",
        	    18: "evening",
        	    19: "evening",
        	    20: "evening",
        	    21: "evening",
        	    22: "night",
        	    23: "night"
            }
        return shiftPicker.get(currentHour,"Invalid time")
currentShift = shiftPicker (currentHour)
#print(currentShift)

# reading the stings into variables
STRINGS = open("STRINGS", "r")
DPT1_TAG = STRINGS.readline()
DPT2_TAG = STRINGS.readline()
EXPERT_TAG = STRINGS.readline()
K_NIGHT = STRINGS.readline()
K_MORNING = STRINGS.readline()
K_EVENING = STRINGS.readline()
D_NIGHT = STRINGS.readline()
D_MORNING = STRINGS.readline()
D_EVENING = STRINGS.readline()
STRINGS.close()

# slicing out the last symbol
DPT1_TAG = DPT1_TAG[0:len(DPT1_TAG) - 1]
DPT2_TAG = DPT2_TAG[0:len(DPT2_TAG) - 1]
EXPERT_TAG = EXPERT_TAG[0:len(EXPERT_TAG) - 1]
K_NIGHT = K_NIGHT[0:len(K_NIGHT) - 1]
K_MORNING = K_MORNING[0:len(K_MORNING) - 1]
K_EVENING = K_EVENING[0:len(K_EVENING) - 1]
D_NIGHT = D_NIGHT[0:len(D_NIGHT) - 1]
D_MORNING = D_MORNING[0:len(D_MORNING) - 1]
D_EVENING = D_EVENING[0:len(D_EVENING) - 1]


# loading worksheets from workbooks
dnXls = load_workbook('dn.xlsx').active
khXls = load_workbook('kh.xlsx').active

# Expert and specialists names to be inserted into JSON
# We are filling this array only with those who will be on the shift
experts = []
specialists = [] # main dpt
specialists2 = [] # sub dpt

# TODO switch 300 to purposly defined value
#colB = dnXls['B']

# returns correct string of the time depending on the shift type
def timePickerD(currentShift):
	return {
		'morning': D_MORNING,
		'evening': D_EVENING,
		'night': D_NIGHT
	}.get(currentShift, "night")
def timePickerK(currentShift):
	return {
		'morning': K_MORNING,
		'evening': K_EVENING,
		'night': K_NIGHT
	}.get(currentShift, "night")

# https://stackoverflow.com/questions/706721/how-do-i-pass-a-method-as-a-parameter-in-python
def constructK (TAG):
	arr = []
	colB = khXls['B']
	for cell in colB:
		if cell.value == TAG:

			# converting cell object into cell row number (still string)
			# <Cell u'Schedule'.
			# https://developers.google.com/edu/python/strings
			cell = str(cell)[19:len(str(cell)) - 1]
			try:
				if timePickerK(currentShift) in khXls['D' + cell].value:

					# https://stackoverflow.com/questions/2464959/whats-the-u-prefix-in-a-python-string
					arr.append(khXls['A' + cell].value.encode('ascii', 'ignore'))
			except TypeError:
				pass
	return arr


def constructD (TAG):
	arr = []
	colB = dnXls['B']
	for cell in colB:
		if cell.value == TAG:

			# converting cell object into cell row number (still string)
			# <Cell u'Schedule'.
			# https://developers.google.com/edu/python/strings
			cell = str(cell)[19:len(str(cell)) - 1]
			try:
				if timePickerD(currentShift) in dnXls['D' + cell].value:

					# https://stackoverflow.com/questions/2464959/whats-the-u-prefix-in-a-python-string
					arr.append(dnXls['A' + cell].value.encode('ascii', 'ignore'))
			except TypeError:
				pass
	return arr

experts = constructD (EXPERT_TAG)
specialists = constructD (DPT1_TAG)
specialists2 = constructD (DPT2_TAG)
experts.extend(constructK (EXPERT_TAG))
specialists.extend(constructK (DPT1_TAG))
specialists2.extend(constructK (DPT2_TAG))

class Distro:
	ShiftType = 'Morning'
	ShiftLeader = 'Unknown'
	SMEs = []
	CSs = []
class SME:
	name = "None"
class CS:
	name = "None"

distro = Distro()

for exp in experts:
	sme = SME()
	sme.name = exp
	distro.SMEs.append(sme)
	
for sp in specialists:
	cs = CS()
	cs.name = sp
	distro.CSs.append(cs)
	
print (distro.CSs)
distro.ShiftType = currentShift
#distro.SMEs = experts
jsonStr = json.dumps(distro.__dict__)
print("++++++++++++")
print(jsonStr)
print("++++++++++++")

# writing to the file
with open('test.json', 'w') as json_file:
	json.dump(jsonStr, json_file)
	json_file.close()

# prints people on the current shift
print ("=experts=")
print (experts)
print ("=specialists=")
print (specialists)
print ("=sub-spec=")
print (specialists2)

# removing them from the memory
del dnXls
del khXls
