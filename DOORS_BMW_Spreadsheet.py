#Nile Fairfield 

import os, sys, win32com.client

def runMacro(fpath, macro_name):
	for path, subdirs, files in os.walk(fpath):

		for name in files:
			try:
				fullname = fpath + "\\" + name
				xl.Workbooks.Open(Filename=fullname,ReadOnly=1)

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
#fpath_input = "C:\Users\fairfield\Desktop\Upload\eXchangeRound4\MGU_Garmin_Round4_Export"

print "Enter the name of the Excel Macro:"
#Get the input for directory
macro_name_input = raw_input("> ")
#old_str_input = "RE_29_January_2015.zip"

#Run function
runMacro(fpath_input, macro_name_input)