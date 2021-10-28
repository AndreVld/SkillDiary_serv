import json
from random import randrange
import lorem
from django.core.management.base import BaseCommand
from SkillDiary.settings import BASE_DIR
from courseapp.models import Profession, Course
from task_app.models import Task, Comment
from users_app.models import Person


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):

        # adding profession
        with open(f'{BASE_DIR}/courseapp/data/prof.txt', "r") as file:
            professions = file.readlines()
            for profession in professions:
                Profession.objects.get_or_create(name=profession)
            file.close()
        # adding persons and city
        with open(f'{BASE_DIR}/courseapp/data/persons.json', "r", errors='ignore') as infile:
            persons = json.load(infile)
            for person in persons:
                new_user = Person(**person)
                new_user.save()

        # adding course
        with open(f'{BASE_DIR}/courseapp/data/course.txt', "r") as file:
            courses = file.readlines()
            for course in courses:
                persons = Person.objects.all()
                professions = Profession.objects.all()

                perosn = persons[randrange(40)]
                Course.objects.get_or_create(name=course, person=perosn,
                                             profession=professions[randrange(40)], rate=randrange(100),
                                             location=perosn.city,
                                             target="win", start_date="2021-10-14", end_date="2021-10-30",
                                             status='WORK')
            file.close()

        # adding tasks
        courses = Course.objects.all()
        for course in courses:
            for i in range(randrange(10)):
                Task.objects.get_or_create(name=f'Task {i}', start_date="2021-10-14", end_date="2021-10-30",
                                           course=course, status="WORK",user=course.person)

        # adding comments
        tasks = Task.objects.all()
        for task in tasks:
            for i in range(randrange(10)):
                Comment.objects.get_or_create(text=lorem.text(), task=task)

    # Create superuser
    print('Create superuser: skilldiary')
    super_user = Person.objects.create_superuser('skilldiary', 'root@localhost.local', input('Enter password for super user: '),city='Moscow',first_name='Alex',last_name='Ivanov')
