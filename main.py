import qc_create
import qc_add

print(".QC Maker | A program by: JanColon")
print("Type 'qc-help' for all valid commands")

## Valid command list (gets printed w/ 'qc-help' command)
cond_list = [
"qc-help", "qc-create", "qc-op", 
"qc-add-model", "qc-add-body", 
"qc-add-mat", "qc-static", 
"qc-add-seq", "qc-add-coll-mod", 
"qc-add-hbox", ""]

def main():
	global inp
	inp = input("Command - ")
	com(inp)

def hlp():
	print(cond_list)

## Command & error handling
## TODO: Make an error message that doesn't get shown w/ valid commands
def com(command):
	cond_func = None
	for i in range(0, len(cond_list)):
		if command == cond_list[i]:
			cond_func = ["hlp", "qc_create.create", "qc_create.op", 
			"qc_add.model", "qc_add.body", "qc_add.mat", 
			"qc_add.stat", "qc_add.seq", "qc_add.coll", 
			"qc_add.hbox", ""]
			func = eval(cond_func[i] + "()") ## TODO: fix 'IndexError: List Index Out of Range' error
	else:
		main()

if __name__ == "__main__":
	main()
else:
	pass