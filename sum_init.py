  # Initialise the sum
total = 0
while True:
 num = input(" ")

 # Exit if the input is blank
 if num == " ":
  break
 
 try:
  num = int(num)
  # Exit the loop if user enters 0
  if num == 0:
   break
  
  # Add to total sum
  total = total + num
  print(total)

 except ValueError:
  print("invalid")
  print(total)