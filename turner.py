import os

# taking todays date in the same format as in XLSX. Sorry, not that good
# at Python yet.
# https://janakiev.com/blog/python-shell-commands/
stream = os.popen('date +%d.%m.%Y')
output = stream.read()
output
