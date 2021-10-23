from core.database import Sessionlocal

import objects.major_objects as major_obj
import objects.student_objects as student_obj
import objects.subject_objects as subject_obj
import objects.mark_objects as mark_obj
import objects.user_objects as user_obj

from models.models import Major
from models.models import Student
from models.models import Subject
from models.models import Mark
from models.models import User


def add_sessions():
    with Sessionlocal() as session:
        session.add(major_obj.major_51)
        session.add(major_obj.major_53)
        session.add(major_obj.major_81)
        session.add(major_obj.major_122)
        session.add(student_obj.student_1)
        session.add(student_obj.student_2)
        session.add(student_obj.student_3)
        session.add(student_obj.student_4)
        session.add(student_obj.student_5)
        session.add(student_obj.student_6)
        session.add(student_obj.student_7)
        session.add(student_obj.student_8)
        session.add(student_obj.student_9)
        session.add(student_obj.student_10)
        session.add(subject_obj.subject_1)
        session.add(subject_obj.subject_2)
        session.add(subject_obj.subject_3)
        session.add(subject_obj.subject_4)
        session.add(subject_obj.subject_5)
        session.commit()


def get_all_objects():
    with Sessionlocal() as session:
        print(session.query(Major).all())
        print('\n')
        print(session.query(Student).all())
        print('\n')
        print(session.query(Subject).all())
        print('\n')
        print(session.query(Mark).all())
        print('\n')
        session.commit()


#add_sessions()
get_all_objects()

