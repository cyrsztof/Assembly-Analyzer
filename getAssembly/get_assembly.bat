@echo off
setlocal enabledelayedexpansion

set "input_file=names.csv"
set "output_directory=output"
set "input_directory=r007ue"

if not exist "%output_directory%" mkdir "%output_directory%"

set "invalid_chars=<>:""/\|?*"

for /f "usebackq delims=" %%a in ("%input_file%") do (
	set "name=%%a"
	
	rem Sanitize the name by replacing invalid characters with an underscore (_)
    set "sanitized_name=!name!"

    for %%b in (!invalid_chars!) do set "sanitized_name=!sanitized_name:%%b=_!"
    
    vtune -report hotspots -r %input_directory% -source-object function=!name! -group-by=address -column=Assembly,Instructions,Clockticks -report-output "%output_directory%\!sanitized_name!_results.csv" -format csv -csv delimiter ;
)

echo Execution completed. Generating merged output CSV file.

cd "%output_directory%"

copy *.csv merged_output.csv
del /Q *.csv

echo Merged output CSV file generated successfully.