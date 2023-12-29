from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):

    firstname = models.CharField(max_length=100, verbose_name='Vorname')
    lastname = models.CharField(max_length=100, verbose_name='Nachname')
    avatar = models.ImageField(upload_to='students/', verbose_name='Avatar', **NULLABLE)

    email = models.CharField(max_length=150, verbose_name='email', unique=True, **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='studying')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Studenten'
        ordering = ('lastname',)


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='name')
    description = models.TextField(verbose_name='description')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='student')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
