#This scrips is my solution for Codecademy's gradebook project using Python
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = [
  "physics",
  "calculus",
  "poetry",
  "history",
]

grades = [
  "98",
  "97",
  "85",
  "88",
]

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
print(f"\n{gradebook}")

print("\nThis is a list of all grades:")
print(f"\n{full_gradebook}")
