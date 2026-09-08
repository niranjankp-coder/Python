'''
Take the input from the user and find the average
'''
import re

student_count = int(input("ENTER THE STUDENT COUNTS: "))
max_marks = 100
students = {}
for i in range(1, student_count+1):
  student = input(f"ENTER THE STUDENT NAME OF SERIAL NUMBER {i} : ").strip()
  marks = int(input(f"ENTER THE STUDENT MARKS OF SERIAL NUMBER {i}: "))
  try:
    pattern = r"^\d{0,3}$"
    if not re.match(pattern, str(marks)):
      raise ValueError(f"Marks range should be 0-{max_marks}")
    marks = int(marks)

    if marks > max_marks:
      raise ValueError(f"Marks cannot be greaterthan {max_marks}")
  except ValueError as e:
    print(f"Invalid marks {marks}: {e}")
    continue
  students[student] = marks
print(students)

# Finding the average marks
value = 0
for avg_value in students.values():
  value += avg_value
average = value/student_count
print(f"AVERAGE IS: {average}")

'''
output:
ENTER THE STUDENT COUNTS: 3
ENTER THE STUDENT NAME OF SERIAL NUMBER 1 : ravi
ENTER THE STUDENT MARKS OF SERIAL NUMBER 1: 89
ENTER THE STUDENT NAME OF SERIAL NUMBER 2 : raju
ENTER THE STUDENT MARKS OF SERIAL NUMBER 2: 90
ENTER THE STUDENT NAME OF SERIAL NUMBER 3 : kiran
ENTER THE STUDENT MARKS OF SERIAL NUMBER 3: 67
{'ravi': 89, 'raju': 90, 'kiran': 67}
AVERAGE IS: 82.0
'''

  
      
