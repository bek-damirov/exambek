from django.db import models
from datetime import timedelta, datetime


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name='Язык програмирования')
    month_to_learn = models.IntegerField(verbose_name='количество месяцев, продолжительность курса')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            a = self.name
            if a.islower():
                self.name.title()
                super().save(*args, **kwargs)


class AbstractPerson(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        unique_together = (["email"])

    def save(self, *args, **kwargs):
        if self.phone_number:
            if self.phone_number[0] == '0':
                number = self.phone_number[1:9]
                self.phone_number = f'"+996"{number}'
                super().save(*args, **kwargs)


OS = (
    ('windows', 'Windows'),
    ('mac', 'MacOs'),
    ('linux', 'Linux')
)


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=50, null=True, blank=True, verbose_name='место учебы/работы')
    has_own_notebook = models.BooleanField(default=True, verbose_name="Есть ли ноутбук")
    preferred_os = models.CharField(max_length=10, choices=OS)

    def __str__(self):
        return self.work_study_place


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=50, null=True, blank=True, verbose_name="основное место работы")
    experience = models.DateField(verbose_name='Опыт работы с:')
    study = models.ManyToManyField(Student, related_name='lessons', through='Course')

    def __str__(self):
        return self.main_work


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование курса')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField(verbose_name='Дата начала курсов')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mentor.name} - {self.student.name}'

    def get_end_date(self):
        if self.mentor and self.student:
            a = self.language.month_to_learn * 30
            now = datetime.now()
            end = timedelta(a)
            the_end = now - end
            print('примерная дата окончания', the_end)
