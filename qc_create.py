def create():
	print("What do you want the file name to be?")
	global qc_file
	qc_file = input("Name your .qc file - ")
	if qc_file == qc_file:
		file_make(qc_file)

def file_make(name):
	file = open(name + ".qc", "x")
	print(name + ".qc created!")

def op():
	print("What's the name of your existing .qc file? (No extension)")
	fn = input("Your existing .qc file - ")
	if fn == fn:
		global qc_file
		qc_file = fn
		open(qc_file + ".qc", "r")
		print(qc_file + " can now be edited!")