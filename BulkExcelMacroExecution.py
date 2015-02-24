#Nile Fairfield 
#Run an Excel macro on all files in a folder

import os, win32com.client
def runMacro(fpath, macro_name):
    exp_path = fpath + "\\Processed"
    for path, subdirs, files in os.walk(fpath):
        xl=win32com.client.Dispatch("Excel.Application")
        xl.Visible = True
                 
        for name in files:
            try:
                fullname = path + "\\" + name
                print fullname
                 
                book = xl.Workbooks.Open(fullname)
                xl.Application.Run(macro_name)
                book.Close(SaveChanges=0)
            except ValueError:
                print "error"
                 
print "Enter the name of the directory:"
#Get the input for directory
fpath_input = raw_input("> ")
 
print "Enter the name of the Excel Macro:"
macro_name_input = raw_input("> ")
# Example: macro_name_input = "PERSONAL.XLSB!macro_name"
 
#Run function
runMacro(fpath_input, macro_name_input)