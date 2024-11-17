def grade_point_to_letter(grade_point):
  """Convert grade points to letter grades.
  Args:
  grade_point (float): Numeric grade point to convert.

  Returns:
  str: Corresponding letter grade.
  """
  if grade_point < 40:
    return "F"
  elif 40 <= grade_point and grade_point < 50:
    return "D"
  elif 50 <= grade_point and grade_point < 60:
    return "C"
    
  elif 60 <= grade_point and grade_point < 70:
    return "B"
    
  elif 70 <= grade_point and grade_point < 80:
    return "A"
    
  elif grade_point > 80:
    return "A+"
  else:
    raise ValueError # Raise error for invalid grade points

def letter_point_to_grade_point(letter_grade):
  """"Convert letter grades to grade point ranges.
    
  Args:
    letter_grade (str): Letter grade to convert.

  Returns:
    str: Corresponding grade point range.
  """
  #Convert string to uppercase
  letter_grade = letter_grade.upper()

  if letter_grade == "F":
   return "0-40"
    
  elif letter_grade == "D":
   return "40-50"

  elif letter_grade == "C":
   return "50-60"

  elif letter_grade == "B":
   return "60-70" 

  elif letter_grade == "A":
   return "70-80"

  elif letter_grade == "A+":
   return "80+"

  else:
   raise ValueError
    
while True:
    user_input = input()
    
    # Exit condition for the loop
    if user_input.lower() == "end" or user_input == " ":
      break 

    try:
      # Try converting numeric grade point to letter grade
      grade_point = float(user_input)
      letter_grade = grade_point_to_letter(grade_point)
      print(letter_grade)
    
    except ValueError:
      try:
        # Try converting letter grade to grade point range
        letter_grade = user_input
        grade_point = letter_point_to_grade_point(letter_grade)
        print(grade_point)
      except ValueError:
          break