from flask import Flask
from flask import request
from flask_cors import CORS
import json
import repo
app = Flask(__name__)
CORS(app)


@app.route('/')
def landing():
    return '< h1 > Landing page < /h1 >'


@app.route('/add-student-data', methods=['POST'])
def addStudent():
    return repo.addStudentData(request.json["data"])


@app.route('/add-student-marks/<student_uid>', methods=['POST'])
def addMarks(student_uid):
    return repo.addStudentMarks(request.json["data"], student_uid)


@app.route('/students-data')
def getStudentsData():
    grade = request.args.get('grade', default='class1', type=str)
    section = request.args.get('section', default='A', type=str)
    exam_type = request.args.get('exam-type', default='sem1', type=str)
    return repo.sendStudentData(grade=grade, section=section, exam_type=exam_type)
