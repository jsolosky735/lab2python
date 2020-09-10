#Author: Jamys Solosky jjs7331@psu.edu
#Collaborator: Balade Shafa bks5681@psu.edu
#Collaborator: Patrick Podobinski pbp5221@psu.edu
#Collaborator: Clare Robson cir5887@psu.edu
#Section: 6
#Breakout:13
def getLetterGrade (grade):
  if grade >= 93.0:
    gradel = "A"
  elif grade >= 90.0:
    gradel = "A-"
  elif grade >= 87.0:
    gradel = "B+"
  elif grade >= 83.0:
    gradel = "B"
  elif grade >= 80.0:
    gradel = "B-"
  elif grade >= 77.0:
    gradel = "C+"
  elif grade >= 70.0:
    gradel = "C"
  elif grade >= 60.0:
    gradel = "D"
  else:
    gradel = "F"
  return gradel

def run():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = float(grade)
  print(getLetterGrade(grade))
  print(f"Your letter grade for CMPSC 131 is {lettergrade}.")

if __name__ == "__main__":
  run() 



  