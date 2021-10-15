import json
from random import randrange
import lorem
from django.core.management.base import BaseCommand
from SkillDiary.settings import BASE_DIR
from authapp.models import *
from mainapp.models import Profession, Course, Task, Comment


JSON_PATH = 'mainapp/json'


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):

        # adding profession
        with open(f'{BASE_DIR}/mainapp/data/prof.txt', "r") as file:
            professions = file.readlines()
            for profession in professions:
                Profession.objects.get_or_create(name=profession)
            file.close()
        # adding persons and city
        with open(f'{BASE_DIR}/mainapp/data/persons.json', "r", errors='ignore') as infile:
            persons = json.load(infile)
            for person in persons:
                result = City.objects.get_or_create(name=person['city'])
                person['city'] = result[0]
                new_user = Person(**person)
                new_user.save()

        # adding course
        with open(f'{BASE_DIR}/mainapp/data/course.txt', "r") as file:
            courses = file.readlines()
            for course in courses:
                persons = Person.objects.all()
                professions = Profession.objects.all()
                city = City.objects.all()
                Course.objects.get_or_create(name=course, person=persons[randrange(40)],
                                             profession=professions[randrange(40)], rate=randrange(100),
                                             location=city[randrange(40)],
                                             target="win", start_date="2021-10-14", end_date="2021-10-30",
                                             status='WORK')
            file.close()

        # adding tasks
        courses = Course.objects.all()
        for course in courses:
            for i in range(randrange(10)):
                Task.objects.get_or_create(name=f'Task {i}', start_date="2021-10-14", end_date="2021-10-30",
                                           course=course, status="WORK")

        # adding comments
        tasks = Task.objects.all()
        for task in tasks:
            for i in range(randrange(10)):
                Comment.objects.get_or_create(text=lorem.text(), task=task)

    # Create superuser
    print('Create superuser: skilldiary')
    super_user = Person.objects.create_superuser('skilldiary', 'root@localhost.local', input('Enter password for super user: '))
