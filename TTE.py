
import os
import fileinput
import time

os.chdir('C:\\Users\\SH\\Documents\\WC')

with open('SKUtranstemp.html', 'r', encoding="utf8") as rf:
	with open('SKUtranstempWF.html', 'w', encoding="utf8") as wf:
		# with open('SKUtranstempOF.html', 'w', encoding="utf8") as of:
		chunk_size =  6699
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)


with open('SKUtranstempWF.html', 'rb+') as file:
	chunk_size = 6699
	file_chunk = file.read(chunk_size)
	while len(file_chunk) > 0:
		for line in file:
			for word in line:
				if word == 'storeid':
					file.writes(word.replace('storeid', 'CH'))
					print(file.writes())
