import os

# taking todays date in the same format as in XLSX. Sorry, not that good
# at Python yet.
# https://janakiev.com/blog/python-shell-commands/
stream = os.popen('date +%d.%m.%Y')
output = stream.read()
output

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
