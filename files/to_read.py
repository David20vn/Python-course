#txt files
"""
def main():
  with open ( "names.txt", "r") as file:
    for line in sorted( file ):
      print ( line.strip() )

  
main()
"""

#csv

#1 with simple comas
"""
def main():

  students = []

  with open("names.csv") as file:
    for line in file:
      name, house, pet = line.strip().split(",")
      student = { "name": name, "house": house, "pet": pet }
      students.append(student)

    for student in sorted( students, key = lambda student: student['name'] ):
      print( f"{student['name']} live in {student['house']} and have a {student['pet']}")


main()
"""

#2 with comas in quots

import csv

def main():

  students = []

  with open("names.csv") as file:
    data = csv.DictReader(file)
    for row in data:
      students.append( row )

    for student in sorted( students, key= lambda student: student['name']):
      print( f"{student['name']} live in {student['house']} and have a {student['pet']}")

main()