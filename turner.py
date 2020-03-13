import os

# https://openpyxl.readthedocs.io/en/stable/
from openpyxl import *

# What is the current shift
# https://stackoverflow.com/a/103081
# https://janakiev.com/blog/python-shell-commands/
 
stream = os.popen('date +%H') # 07 15 23
currentHour = stream.read()

# TODO fix default
def shiftPicker(currentHour):
	return {
		'07': "morning",
		'15': "evening",
		'23': "night"
	}.get(currentHour, "night")
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

# Expert names to be inserted into JSON
# We are filling this array only with those who will be on the shift
experts = []

# TODO switch 300 to purposly defined value
colB = dnXls['B']

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

# Constructing D experts
for cell in colB:
	if cell.value == EXPERT_TAG:

		# converting cell object into cell row number (still string)
		# <Cell u'Schedule'.
		# https://developers.google.com/edu/python/strings
		cell = str(cell)[19:len(str(cell)) - 1]
		if timePickerD(currentShift) in (dnXls['D' + cell].value):

			# https://stackoverflow.com/questions/2464959/whats-the-u-prefix-in-a-python-string
			experts.append(dnXls['A' + cell].value.encode('ascii', 'ignore'))

colB = khXls['B']
# Constructing K experts
for cell in colB:
	if cell.value == EXPERT_TAG:

		# converting cell object into cell row number (still string)
		# <Cell u'Schedule'.
		# https://developers.google.com/edu/python/strings
		cell = str(cell)[19:len(str(cell)) - 1]
		if timePickerK(currentShift) in (khXls['D' + cell].value):

			# https://stackoverflow.com/questions/2464959/whats-the-u-prefix-in-a-python-string
			experts.append(khXls['A' + cell].value.encode('ascii', 'ignore'))

# prints experts on the current shift
print (experts)

# removing them from the memory
del dnXls
del khXls
