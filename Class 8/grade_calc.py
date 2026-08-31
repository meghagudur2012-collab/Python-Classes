marks = int(input("Enter Marks here: "))
grade = ""

if(marks < 0 or marks > 100):
    print("Invalid marks. Please enter marks between 0 and 100.")
    grade = "ERROR. INVALID MARKS"

elif(marks >= 90):
    grade = "A"

elif(marks >= 80):
    grade = "B"

elif(marks >= 70):
    grade = "C"

elif(marks >= 60):
    grade = "D"

elif(marks < 60):
    grade = "F"


print(f"""
            marks: {marks}
            grade: {grade}


""")
