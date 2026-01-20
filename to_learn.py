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

#





