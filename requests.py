def addMarksRequest(all_marks, exam_type, student_uid):
    print("In add marks reuest")
    for marks in all_marks:
        print("student exam type and uid already present")
        if marks["student_uid"] == student_uid and marks["exam_type"] == exam_type:
            return False
    return True


def addStudentRequest(all_students, roll_number, grade, section):
    for student in all_students:
        if student["roll_number"] == roll_number and student["grade"] == grade and student["section"] == section:
            return False
    return True


def isStudentPresent(all_students, student_uid):
    print("In is student present")
    for student in all_students:
        print(student)
        if student["uid"] == student_uid:
            print('student is present')
            return True
    return False
