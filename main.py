print("Today we are going to be calculating the area of a rectangle")
width = int(input("Enter the width of the rectangle (cm): "))
length = int(input("Enter the length of the rectangle (cm): "))
area = (length * width)
User_Area=int(input("Enter your answer for the area (cm^2)"))
if area ==User_Area:
  print("You are correct the correct answer was (cm)",+ area)
else:
  print("You are wrong the correct answer was (cm^2)",+area)