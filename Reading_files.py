#-------------------------------------------------------------------------------
# Name:        Reading
# Purpose:
#
# Author:      kenny.coons
#
# Created:     18/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def read_file(): #Function that imports a file for reading
    file = open('Dillbill.txt', 'r')
    all_lines = file.read() #reads all lines in text file
    print(all_lines) #prints all lines it read
    file.close() #closes text file after it prints the lines that it read

def list_file():
    file = open('Dillbill.txt', 'r')
    Dillbill_list = file.readlines()
    print(Dillbill_list)

def read_linebyline():
    file = open('Dillbill.txt', 'r')
    line = file.readline()
    print(line)
    line2 = file.readline
    print(line2)
    line3 = file.readline
    print(line3)

def main():
    read_file()
    list_file()
    read_linebyline()

#Main Code
main()


