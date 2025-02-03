#This script is my solution for Codecademy's gradebook project using Python

#This sets the preassigned values to the last_semester_gradebook variable based on the contents of the Codecademy course
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#This is a list of subjects
subjects = [
  "physics",
  "calculus",
  "poetry",
  "history",
]

#This is a list of grades
grades = [
  "98",
  "97",
  "85",
  "88",
]

#The gradebook variable combines the subjects list and grades list
gradebook= [
    [subjects[0], grades[0]],
    [subjects[1], grades[1]],
    [subjects[2], grades[2]],
    [subjects[3], grades[3]],
]

gradebook.append(["computer science", "100"])
gradebook.append(["visual arts", "93"])

gradebook[-1][1] = "98"

gradebook.remove(["poetry", "85"])
gradebook.append(["poetry", "Pass"])

full_gradebook = last_semester_gradebook + gradebook

print("This is a list of current grades:")
for subject, grade in gradebook:
    print(f"{subject}: {grade}")

print("\nThis is a list of all grades:")
for subject, grade in full_gradebook:
    print(f"{subject}: {grade}")
