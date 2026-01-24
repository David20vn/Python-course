# VARIABLES AND FUNCTIONS

# strings
"""
name = input ("Whay is your name?: ")
name, firstLast, secondLast = name.split(" ")
print ( f"your name is: {name} {firstLast} {secondLast}." )
"""

# int
"""
x = float ( input ( "What's x?: " ))
y = float ( input ( "What's y?: " ))
print ( f"{x/y:.2f}" )
"""

#make a fuction
"""
def main():
  value = int ( input ( "Wat's the value to square?: " ))
  print ( f"The square of the value is { square( value )}")

def square ( x ):
  return pow ( x, 2 )

main()
"""


# CONDITIONALS

#if
"""
def main():
  score = request_score()
  grade = get_grade( score )
  if score != -1:
    print ( f"Your final grade is: {grade}")
  else:
    print ( "Invalid score.")

def request_score():
  n = int( input( "What was your score? ( 0 - 100 ): " ))
  if n < 0 or n > 100:
    return -1
  else:
    return n
  
def get_grade( n ):
  if n == -1:
    return 
  elif n >= 90:
    return "A"
  elif n >= 80:
    return "B"
  elif n >= 70:
    return "C"
  elif n >= 60:
    return "D"
  else:
    return "F"
  
main ()
"""


#Loops 

#simple while and for
"""
def main():
  number = get_number()
  meow( number )

def get_number ():
  while True:
    value = int( input( "How many times do you want to meow?: " ))
    if value < 0:
      continue
    else:
      return value 

def meow( n ):
  for _ in range( n ):
    print( "meow" )

main()
"""

# loops using dictionaries
"""
def main():
  people = [
    { "name": "David", "place": "Pereira", "pet": "cat" },
    { "name": "Juan", "place": "Armenia", "pet": "dog" },
    { "name": "Eve", "place": "Choco", "pet": "rabbit" },
    { "name": "Ana", "place": "Cali", "pet": None }
  ]

  print_people( people )

def print_people( list ):
  for person in list:
    for element in person:
      print ( f"{ element }: { person[ element ]} " )
    print()
  
main()
"""


# Exceptions

#Secure users input
"""
def main():
  number = get_number( "What's the number?: " )
  print( f"The number is {number}" )

def get_number( prompt ):
  while True:
    try:
      return int( input( prompt ))
    except:
      print ( "The response should be an integer" ) # I could use "pass" too

main()
"""


# Libraries and packages
"""
import cowsay
import sys

def main():
  if len( sys.argv ) == 2:
    cowsay.cow ( "hello\n"+sys.argv[1])

main()
"""

#request
"""
import requests
import sys
import json

def main():

  if len( sys.argv ) != 2:
    sys.exit( "Must have 2 arguments." )
  
  response = requests.get( "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1] )

  results = response.json()["results"]

  for result in results:
    print ( result ["trackName"])


main()
"""

#own librarie
"""
import sys
from own_librarie import hello
from own_librarie import bye

def main():
  hello( sys.argv[1] )
  bye( sys.argv[1] )


main()
"""

