"""Classify"""
def student_classfier():
    """Classify the student by their ID"""
    students = []
    while True:
        student_id = input()
        if student_id == "END":
            break
        students.append(student_id)
    students.sort()
    year = students[0][:2]
    faculty = int(students[0][2:4])
    amount = 1
    for student in students[1:]:
        if student[:2] != year:
            print(year, faculty, amount)
            year = student[:2]
            faculty = int(student[2:4])
            amount = 1
        else: #checking faculty
            if faculty == int(student[2:4]): #same faculty
                amount += 1
            else:
                print("--", faculty, amount)
                year = student[:2]
                faculty = int(student[2:4])
                amount = 1

student_classfier()
