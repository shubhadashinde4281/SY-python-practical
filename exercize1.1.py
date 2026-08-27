
name = input("Enter student name: ")

marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\n========== STUDENT SCORECARD ==========")
print("Student Name :", name)
print("Subject 1    :", marks1)
print("Subject 2    :", marks2)
print("Subject 3    :", marks3)
print("---------------------------------------")
print("Total Marks  :", total)
print("Average      :", round(average, 2))
print("=======================================")