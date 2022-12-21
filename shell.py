import datetime
from user.models import Student, Mentor, Language, Course

python = Language.objects.create(name='Python', months_to_learn=6)
java_script = Language.objects.create(name='Java Script', months_to_learn=6)
ux_ui = Language.objects.create(name='UX-UI', months_to_learn=2)

Amanov_Aman = Student.objects.create(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898',
                                     work_study_place='School №13', has_own_notebook=True, preferred_os='windows')
Apina_Alena = Student.objects.create(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888',
                                     work_study_place='TV', has_own_notebook=True, preferred_os='mac')
Phil_Spencer = Student.objects.create(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312',
                                      work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='linux')


Ilona_Maskova = Mentor.objects.create(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454',
                                      main_work= None, experience='2021-10-23')
Halil_Nurmuhametov = Mentor.objects.create(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876',
                                           main_work='University of Fort Collins', experience='2010-9-18')


Course.objects.create(name='Python-21', language=python, date_started='2022-08-01', mentor=Halil_Nurmuhametov, student=Amanov_Aman)

