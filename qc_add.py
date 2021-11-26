import qc_create

boxes = {
	"0": "Generic",
	"1": "Head",
	"2": "Chest",
	"3": "Stomach",
	"4": "Left arm",
	"5": "Right arm",
	"6": "Left leg",
	"7": "Right leg",
	"8": "Neck"
}

def model():
	print("What do you want your model name to be? (EX: shell\\shell.mdl)")
	mdl = input("Model name - ")
	if mdl == mdl:
		nfil = open(qc_create.qc_file + ".qc", "a")
		nfil.write("$modelname" + "		" + '"' + mdl + '"' + "\n")
		print(mdl + " has been added to " + qc_create.qc_file + ".qc!")

def body():
	print("What's the name of your reference mesh? (EX: mymodel.smd)")
	bdy = input("Reference mesh name - ")
	print("What do you want the body name to be? (EX: modelname)")
	bdy_nme = input("Body name - ") 
	if bdy == bdy:
		nfil = open(qc_create.qc_file + ".qc", "a")
		nfil.write("$body" + "		" + bdy_nme + '	' + '"' + bdy + '"' + "\n")
		print(bdy + " has been added to " + qc_create.qc_file + ".qc!")

def mat():
	print("What's the file directory to your model's texture? (models\\modeltexture\\)")
	mat = input("Material directory - ")
	if mat == mat:
		nfil = open(qc_create.qc_file + ".qc", "a")
		nfil.write("$cdmaterials" + "		" + '"' + mat + '"' + "\n")
		print(mat + " has been added to " + qc_create.qc_file + ".qc!")

def stat():
	nfil = open(qc_create.qc_file + ".qc", "a")
	nfil.write("$staticprop" + "\n")
	print("$staticprop has been added to " + qc_create.qc_file + ".qc!")

def seq():
	print("What's the name of the animation file? (EX: idle.smd)")
	seq = input("Animation file - ")
	print("What do you want to name the sequence? (EX: idle)")
	seq_nme = input("Sequence name - ")
	if seq == seq:
		nfil = open(qc_create.qc_file + ".qc", "a")
		nfil.write("$sequence" + "		" + seq_nme + '	' + '"' + seq + '"' + "\n")
		print(seq + " has been added to " + qc_create.qc_file + ".qc!")

def hbox():
	print("What group number do you want to assign to a hitbox?")
	print(boxes)
	box_numb = input("Hitbox number - ")
	print("What bone do you want to assign to your hitbox? (EX: head_bone)")
	box_nme = input("Hitbox name - ")
	print("What're the hitbox's min x, y and z values? (EX: 1 2 3)")
	box_min = input("Min x, y and z values - ")
	print("What're the hitbox's max x, y and z values? (EX: 1 2 3)")
	box_max = input("Max x, y and z values - ")
	nfil = open(qc_create.qc_file + ".qc", "a")
	nfil.write("$hbox" + "	" + box_numb + "  " + box_nme + box_min + " " + box_max + "\n")
	print("$hbox has been added to " + qc_create.qc_file + ".qc!" )

def coll():
	print("What's your collision model name (EX: collision_model.smd)")
	coll_mod = input("Collision model name - ")
	if coll_mod == coll_mod:
		nfil = open(qc_create.qc_file + ".qc", "a")
		nfil.write("$collisionmodel" + "   " + '"' + coll_mod + '"' + ' { $concave }')
		print(coll_mod + " has been added to " + qc_create.qc_file + ".qc!")