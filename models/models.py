from core.database import Base, Sessionlocal
from sqlalchemy import Column, ForeignKey, Integer, VARCHAR
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    username = Column(VARCHAR(25), nullable=False)
    first_name = Column(VARCHAR(25), nullable=False)
    last_name = Column(VARCHAR(25), nullable=False)
    email = Column(VARCHAR(25), nullable=False)
    password = Column(VARCHAR(25), nullable=False)
    phone = Column(VARCHAR(25), nullable=False)

    def __init__(self, id_user, username, first_name, last_name, email, password, phone):
        self.id_user = id_user
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone

    def __repr__(self):
        return 'User ' + str(self.id_user) + ' ' + self.username + ' ' + self.first_name + ' ' + self.last_name + ' ' + self.email + ' ' + self.password + ' ' + self.phone + '\n'


class Major(Base):
    __tablename__ = 'major'
    id_major = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45), nullable=False)

    def __init__(self, id_major, name):
        self.id_major = id_major
        self.name = name

    def __repr__(self):
        return 'Major ' + str(self.id_major) + ' ' + self.name + '\n'


class Student(Base):
    __tablename__ = 'student'
    id_student = Column(Integer, primary_key=True)
    name_student = Column(VARCHAR(45), nullable=False)
    last_name_student = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    rating = Column(VARCHAR(45))
    id_major = Column(Integer, ForeignKey('major.id_major'), nullable=False)

    def __init__(self, id_student, name_student, last_name_student, phone, email, id_major):
        self.id_student = id_student
        self.name_student = name_student
        self.last_name_student = last_name_student
        self.phone = phone
        self.email = email
        self.id_major = id_major

    def __repr__(self):
        return 'Student ' + str(self.id_student) + ' ' + self.name_student + ' ' + self.last_name_student + ' ' + self.email + ' ' + str(self.id_major) + '\n'


class Subject(Base):
    __tablename__ = 'subject'
    id_subject = Column(Integer, primary_key=True)
    name_subject = Column(VARCHAR(100), nullable=False)

    def __init__(self, id_subject, name_subject):
        self.id_subject = id_subject
        self.name_subject = name_subject

    def __repr__(self):
        return 'Subject ' + str(self.id_subject) + ' ' + self.name_subject + '\n'


class Mark(Base):
    __tablename__ = 'mark'

    id_mark = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Integer, nullable=False)
    id_subject = Column(Integer, ForeignKey('subject.id_subject'), nullable=False)
    id_student = Column(Integer, ForeignKey('student.id_student'), nullable=False)

    def __init__(self, grade, id_subject, id_student):
        self.grade = grade
        self.id_subject = id_subject
        self.id_student = id_student

    def __repr__(self):
        return 'Mark ' + str(self.grade) + ' ' + str(self.id_student) + ' ' + str(self.id_subject) + '\n'