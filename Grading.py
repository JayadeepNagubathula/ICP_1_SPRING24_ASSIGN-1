def Grade():
  s_name=str(input("Enter the student name:")) #taking the name of the student  from user 
  totalmarks=float(input("enter the total marks:"))# Asking the user to enter the marks
  percentage= float((totalmarks/100)*100) #calculating the percentage of the student by using total marks
  print(percentage) #printing the percentage of the student
  
  if(percentage>=90):#check condition for the grades displaying
  
   print ( s_name +" got A grade")
   
  elif(percentage>=80 and percentage<90):
    
    print(s_name + " got B grade")
    
  elif(percentage>=70 and percentage<80):
   
    print(s_name + " got C grade")
    
  elif(percentage>=60 and percentage<70):
  
     print ( s_name + " got D grade")
     
  elif(percentage>=0 and percentage<60):

      
       print(s_name + " have failed")

  else:

        print("INVALID INPUT")
       
 
Grade() #calling the Grade function to execute our program.
