with open("to_clean") as filenames:
	lines = filenames.readlines()
	lines = [lines[i].strip() for i in range(len(lines)) if i % 6 != 0]
	with open("cleaned","w") as outfile:
		outfile.write("\n".join(lines))