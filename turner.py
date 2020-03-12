import os

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
print(currentShift)

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


