@echo off                                                                
if "%~1"=="" (                                                          
 echo You need to start this script with a DOORS Module                  
  goto :real_end                                                        
)                                                                        
                                                                         
"C:\Program Files (x86)\IBM\Rational\DOORS\9.3\bin\DOORS.exe" -o READ_ONLY -u fairfield -password Ni1104le -f "%TEMP%" -D "current = read(\"%~1\", true);  -batch "C:\Program Files (x86)\IBM\Rational\DOORS\9.3\lib\dxl\addins\user\commas.dxl"

