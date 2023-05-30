@echo off
setlocal enabledelayedexpansion

set "input_file=names.csv"
set "output_directory=output"
set "input_directory=r000ue2"

if not exist "%output_directory%" mkdir "%output_directory%"

set index=1

for /f "usebackq delims=" %%a in ("%input_file%") do (
	set "name=%%a"
	
	rem Generate the output file name using a numerical index
    set "output_filename=%output_directory%\output_!index!.csv"
    set /a index+=1
	
    vtune -report hotspots -r !input_directory! -source-object function=!name! -group-by=address -column=Assembly,"Hardware Event Sample Count:INST_RETIRED.ANY:Self","Hardware Event Sample Count:CPU_CLK_UNHALTED.THREAD:Self" -show-as samples -report-output "!output_filename!" -format csv -csv-delimiter ;
	
	rem Remove the header rows from the output file
    more +2 "!output_filename!" > "!output_filename!.tmp" & move /y "!output_filename!.tmp" "!output_filename!" > nul
)

echo Execution completed. Generating merged output CSV file.

cd "%output_directory%"

copy *.csv merged_output.csv

echo Merged output CSV file generated successfully.
