#Nile Fairfield 

import os, sys

def replace(fpath, old_str, new_str):
	for path, subdirs, files in os.walk(fpath):

		for name in files:
			try:
				lhs, rhs = name.split(old_str, 1)
				new_file = lhs + new_str
				old_fullname = fpath + "\\" + name
				new_fullname = fpath + "\\" + new_file
			
				os.rename(old_fullname, new_fullname)
				print "\n\nSuccessfully renamed " + name + "\n     with " + new_file
				#break
			except ValueError:
				print "\n\nSkipped file " + name
							
#			print "Replace " + name + "with " + new_file + "? Enter 'y'"
#			confirm = raw_input("> ")
#			if confirm == "y":
#				os.rename(old_fullname, new_fullname)
#				print "Successfully renamed " + name + "with " + new_file
#			else:
#				print "cancelled\n"

print "Enter the name of the directory:"
#Get the input for directory
fpath_input = raw_input("> ")

print "Enter the part of the filename you want to replace:"
#Get the input for directory
old_str_input = raw_input("> ")

print "Enter the new string to append to the end of each filename:"
#Get the input for directory
new_str_input = raw_input("> ")

#Run function
replace(fpath_input, old_str_input, new_str_input)