# Evan Cropper
# m02lab.py
# app will receive user input to determine if a student has made the dean's list and/or honor roll
studentName = "bobb"
while studentName != "ZZZ":
    studentName = input("Enter student's last name: ")
    if studentName != "ZZZ":
        print("ok")
        studentGPA = float(input("Enter student's GPA: "))
        if studentGPA >= 3.25:
            print("Student has made the Honor Roll")
        if studentGPA >= 3.5:
            print("Student has made the Dean's List")
        else:
            print("Student is not skilled")