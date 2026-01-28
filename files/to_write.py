#txt files
"""
def main():

  name = input ( "What's your name?: ")

  with open( "names.txt", "a" ) as file: 
    file.write( name + "\n")


main()
"""

#csv files

def main():

  flag = 1

  with open ( "names.csv", "a" ) as file:
    while flag == 1:
      name = input( "\nName: ")
      home = input( "Home: ")
      pet = input( "pet: ")
      file.write( name + "," + home + "," + pet + "\n" )
      flag = int( input( "\n1. Add person\n0. Stop adding\nAnswer: " ))

main()
