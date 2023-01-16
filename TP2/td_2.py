"""Module td_2 printing python version.""" # Adding module
import sys #importing sys library
from os import path #importing path library



ADN_LIST=("A","C","G","T") #creating a list of possible nucleotides

def adn_read(fastafile): #defining function name and its parameters
    """Function printing python version.""" #Adding a docstring
    if fastafile.endswith((".faa",".fa")): #if given file ends with ".faa" or ".fa"
        #print that the file is fasta file
        print(str(fastafile) + " is fasta file")
        #open the file in reading mode using utf-8 encoding
        with open(fastafile,"r", encoding="utf-8") as file:
            lines = file.readlines() # in "lines" store all lines of the file
            line_counter = 0 #creating variable "line_counter" equal to zero
            header = "" #creating an apmpty variable "header" to store sequence name later
            for line in lines: #for each line in variable "lines"
                line_counter += 1 #add 1 to variable "line_counter"

                if line[0] == ">": #if the first element of the line is ">"
                    #store the line in "header" and remove last character which is "\n" 
                    header = line.strip()
                else: #otherwise
                    line = line.strip() #remove the last character of the line
                    line = line.upper() #transform all the characters to uppercase letters
                    column_counter = 0 # creating variable "column_counter" equal to 0
                    for char in line: #for each character in the line
                        column_counter += 1 #add 1 to vqriable "column_counter"
                        if char not in ADN_LIST: #if character is not in list of nucleotides
                            #stock the character followed by "is not a nucl in line" and line number
                            error_output = ( str(char) +
                            " Is not a nucl in line " + str(line_counter)+
                            # followed by "and column" and column number
                            # followed by "for sequence" and sequence name
                            " and column " + str(column_counter)+ " for sequence "+header[1:] +
                            " in file " + str(fastafile) + "\n")
                            #followed by "in file" and file name in "error_output"
                            with open("error_output.txt","a", encoding="utf-8") as error_file:
                            #create a file called "error_output.txt"
                                error_file.write(error_output) # put the information stocked in
                                #"error_output" into created file
    else: # if doesn't end fith ".faa" or ".fa"
        print("This is not a fasta file") #print "This is not a fasta file"
for arg in sys.argv[1:]: #for each argument indicated by user starting
    #from the second argument (first in pyhon)
    #if the path to a file doesn't exist
    if path.exists(arg) is False:
        #print file name followed by "doesn't exist..."
        print("File " + str(arg)+ " doesn't exist, passing on the next argument")
    else: #Otherwise
        adn_read(arg) #execute the adn_read function with the given argument as a parameter
        print("Analysis for  "+str(arg)+ " is done") # print that analysis is finished
