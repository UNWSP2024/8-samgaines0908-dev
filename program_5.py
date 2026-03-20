# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

#Author: Sam Gaines 
#Date: 3/19/2026
#Tile: Course Info

#List of course IDs
course_ids=[
    "MAT2121", "MAT1126","MAT2055",
    "COM2008","COM1075","COM4105",
    "COS2005","COS3271","COS4855",
]
#list of course names
course_names=[
    "Calculus and Analytic Geometry I","Pre-Calculus", "Statistics",
    "Film Appreciation","Public Speaking","Mass Media and Society",
    " Python Programming","Programming I - Java", "Project Capstone",
]
# asks the user to enter the course of there choice
subject=input(" Please enter your subject( Mat, COM, COS): ")
print("\nCourse with subject ",subject + ":")
# Ensures that the ID matches the course name.
for i in range(len(course_ids)):
    if course_ids[i].startswith(subject):
        print(course_ids[i]+"-"+ course_names[i])

