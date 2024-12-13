import os

print("This is still WIP. Type 'proceed' below to proceed.")
choice = input("Type: ")

if choice == "proceed":
    print("Welcome to STE! (Simple Text Editor)")
    print("Read files directly from Python!")

    while True:
        type = input("What would you like to do? (write, read, new, delete, dir): ").lower()
        file = input("What file? (Needs to be in this folder and needs to include the file format, e.g., work.txt): ")
        
        if type == "write":
            writetype = input("Append or Overwrite? : ").lower()
            writeparam = input("File content: ")
            if writetype == "overwrite":
                opf = open(file, "w")
                opf.write(writeparam)
                opf.close()

                opf = open(file, "r")
                print(opf.read())
                opf.close()

            if writetype == "append":
                opf = open(file, "a")
                opf.write(writeparam)
                opf.close()

                opf = open(file, "r")
                print(opf.read())
                opf.close()

        if type == "read":
            opf = open(file, "r")
            print(opf.read())
            opf.close()

        if type == "new":
            print("DISCLAIMER: You can't set the file path yet.")
            opf = open(file, "x")
         
        if type == "delete":
         	if file != main.py:
         		os.remove(file)
         	
         	else:
         		print("You cannot remove BIFE.")
         	