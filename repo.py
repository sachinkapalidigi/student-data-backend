import csv
import time
import requests
students_data = []
students_marks = []


def write_csv(csv_file_name):
    with open(csv_file_name, 'w') as csvfile:
        fieldnames = ['uid', 'roll_number', 'name', 'grade', 'section',
                      'exam_type', 'english', 'kannada', 'maths', 'science', 'social']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


try:
    f1 = open('./data/students_data.csv')
    f2 = open('./data/students_marks.csv')
except:
    write_csv('./data/students_data.csv')
    write_csv('./data/students_marks.csv')
    f1 = open('./data/students_data.csv')
    f2 = open('./data/students_marks.csv')
finally:
    f1.close()
    f2.close()


def getStudentsData():
    with open('data/students_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        global students_data
        students_data = []
        for row in reader:
            students_data.append(dict(row))
    with open('data/students_marks.csv') as csvfile2:
        reader2 = csv.DictReader(csvfile2)
        global students_marks
        students_marks = []
        for row2 in reader2:
            students_marks.append(dict(row2))
    return [students_data, students_marks]


def writeStudentsData():
    with open('data/students_data.csv', 'w') as csvfile:
        fieldnames = ['uid', 'roll_number', 'name', 'grade', 'section']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in students_data:
            writer.writerow(data)
        return True
    return False


def writeStudentsMarks():
    with open('data/students_marks.csv', 'w') as csvfile:
        fieldnames = ['uid', 'student_uid', 'exam_type',
                      'english', 'kannada', 'maths', 'science', 'social']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in students_marks:
            writer.writerow(data)
        return True
    return False


def addStudentData(data):
    getStudentsData()
    # validation here
    isValid = requests.addStudentRequest(
        students_data, data["roll_number"], data["grade"], data["section"])
    if isValid:
        uid = str(time.time()).replace('.', '')
        students_data.append({
            "uid": uid,
            "roll_number": data["roll_number"],
            "name": data["name"],
            "grade": data["grade"],
            "section": data["section"]
        })
        writeStudentsData()
        return {
            "error": False,
            "message": "Student data successfully added"
        }
    else:
        return {
            "error": True,
            "message": "Student data could not be added"
        }


def addStudentMarks(data, student_uid):
    getStudentsData()
    # validate here
    print(students_data, type(student_uid), student_uid)
    isValid = requests.isStudentPresent(students_data, student_uid) and requests.addMarksRequest(
        students_marks, data["exam_type"], student_uid)
    if isValid:
        marks_to_append = {
            "uid": len(students_marks)+1,
            "student_uid": student_uid,
            "exam_type": data["exam_type"],
            "kannada": data["kannada"],
            "english": data["english"],
            "maths": data["maths"],
            "science": data["science"],
            "social": data["social"]
        }
        students_marks.append(marks_to_append)
        writeStudentsMarks()
        return {
            "error": False,
            "message": "Student data successfully added"
        }
    else:
        return {
            "error": True,
            "message": "Student marks could not be added"
        }


def sendStudentData(grade='class1', section='A', exam_type='sem1'):
    [info, marks] = getStudentsData()
    # print(marks, info)
    data_to_send = []
    for student in info:
        if student["grade"] == grade and student["section"]:
            data = student
            for student_marks in marks:
                # print(student["uid"], student_marks["student_uid"],
                #       student_marks["exam_type"], exam_type)
                if (student_marks["student_uid"] == student["uid"]) and (student_marks["exam_type"] == exam_type):
                    print('true')
                    data["marks"] = {
                        "exam_type": exam_type,
                        "english": student_marks["english"],
                        "kannada": student_marks["kannada"],
                        "maths": student_marks["maths"],
                        "science": student_marks["science"],
                        "social": student_marks["social"]
                    }
            data_to_send.append(data)
    return {
        "data": data_to_send
    }
