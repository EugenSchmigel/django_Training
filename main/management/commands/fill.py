from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'lastname': 'Max', 'firstname': 'Muster'},
            {'lastname': 'Ivo', 'firstname': 'Volk'},
            {'lastname': 'Kevin', 'firstname': 'Kaiser'},
            {'lastname': 'Rita', 'firstname': 'Petry'}
        ]

        students_for_create = []
        for students_item in student_list:
            students_for_create.append(Student(**students_item))

        Student.objects.bulk_create(students_for_create)
