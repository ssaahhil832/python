Student_details={"sahil": 59,
                 "Alisha":60,
                 "rahul": 54}
student_name= input("Enter the student's name :")
marks=Student_details.get(f"{student_name}") 
if student_name in Student_details :
    print(f"{student_name}'s marks {marks}")
else :
    print(f"studnet not found.")    

 