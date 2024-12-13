print("This is still WIP. Type 'bIfE' below to proceed.(case sensivite)")
choice = input("Type: ")
if choice == "bIfE":
	print("Welcome to BIFE! (Built In File Editor)")
	print("Read files directly from Python!")
	type = input("What would you like to do? (write, read, new) : ").lower()
	file = input("What file? (Needs to be in this folder and needs to include the file format. If using 'new' parameter this doesn't apply eg: work.txt: ")
		
	if type == "write":
		writetype = input("Append or Overwrite? : ").lower()
		if writetype == "overwrite":
			opf = open(file, "w")
			writeparam = input("File content : ")
			opf.write(writeparam)
			opf.close()
			
			opf = open(file, "r")
			print(opf.read())
			
		if writetype == "append":
			opf = open(file, "a")
			writeparam = input("File content : ")
			opf.write(writeparam)
			opf.close
			
			opf = open(file, "r")
			print(opf.read())
			
	if type == "read":
		opf = open(file, "r")
		print(opf.read())
		opf.close
	
	if type == "new":
		print("DISCLAIMER: You can't set the file path yet.")
		opf = open(file, "x")