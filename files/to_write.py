#txt files
"""
def main():

  name = input ( "What's your name?: ")

  with open( "names.txt", "a" ) as file: 
    file.write( name + "\n")


main()
"""

#csv files

import sys
import csv

def main():

  name = sys.argv[1]
  house = sys.argv[2]
  pet = sys.argv[3]

  with open( "names.csv", "a", newline="" ) as file:
    writer = csv.writer( file )
    writer.writerow([ name, house, pet ])


main()
