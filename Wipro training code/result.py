# Function to check pass or fail
def check_result(student,subject, marks):
    if marks >= 50:
        print("Name:", student)
        print("Subject:", subject)
        print("Marks:", marks)
        print("Result: PASS")
    else:
        print("Name:", student)
        print("Subject:", subject)
        print("Marks:", marks)
        print("Result: FAIL")


# Main program
student_name = input("Enter student name: ")
subject_name = input("Enter subject name: ")
marks_obtained = int(input("Enter marks: "))

check_result(student_name,subject_name, marks_obtained)
