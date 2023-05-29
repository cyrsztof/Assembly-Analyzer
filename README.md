# Assembly-Analyzer

To use:
1) put the get_assembly.bat file inside the project directory of specific VTune project.
2) inside the script edit"input_directory" to the name of directory containing results of the analsisis you want to get the assembly code for.
3) make sure the vtune command is available in your system's PATH
4) provide the names.csv file conatining names of all the functions found during the analysis. You can do it in number of ways, such as from Intel VTune GUI select top-down view, hide all the columns except for the "function name", then hit ctrl+a to select all rows, right click and export to the csv file. You need to make sure that there are no additional characters in the file, you can achieve that using "Find and replace functionality" of Notepad++.

The script will perform vtune command generating assembly code for a single file at a time and will put the csv file with results in the output directory. After going through all functions in the names.csv file it will merge all the files into a single one containing all assembly code from that analysis.

After creating the csv file with assembly code you can run the python script that will do the analysis of occurance of each assembly instruction present in the code, as well as their execution time based on the types of arguments used.
To do that put the input file into input directory of the project, change filename variable to the name of that file in the main.py file and run the file. The results will be put into results directory. 
