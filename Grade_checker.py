try:
    score = int(input("enter test score 0-100: "))
    if score >= 90:
          print("Grade: A - Very Impressive!")
    elif score >= 80:
          print("Grade: B - Very Good!")
    elif score >= 70:
          print("Grade: C - Very Nice")
    elif score >= 60:
          print("Grade: D - Good")
    else:
          print("Grade: F - Halaka ni mama mo") 
except ValueError:
   print("INVALID INPUT!! Please Input A Number Again (0-100)")  
   
    
