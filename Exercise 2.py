# Студент
class Student:
    # Инициализация параметров
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = {}
        self.avg = {}

    # Функция расчета средней оценки студента по курсам
    def av_mark_st(self):
        for course_name, grade in self.grades.items():
            self.average_grade[course_name] = sum(grade)/len(grade)

    # Функция оценки лектора студентом
    def rate_lec(self, lecturer, course, grade):
        if course in lecturer.courses_attached and course in self.courses_in_progress and isinstance(lecturer, Lecturers):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('ошибка добавления оценки Student - > lecturer')

    # Функция вывода информации о студенте
    def __str__(self):
        return f'Студенты \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка по курсам: {self.average_grade}  \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    # Сравнение студентов между собой по средней оценке за курс
    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        for course_name, grade in self.average_grade.items():
            for course_name_2, grade_2 in other.average_grade.items():
                if course_name == course_name_2:
                    if grade > grade_2:
                        self.avg[course_name] = True
                    else:
                        self.avg[course_name] = False
        return print ('Средняя оценка больше:', self.avg)

# Преподаватель
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # Функция оценки студента преподавателем
    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and isinstance(cool_mentor, Reviewer):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('ошибка добавления оценки Reviewer -> Student')

class Lecturers(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.average_grade = {}
        self.avg = {}

     # Функция расчета средней оценки лектора по курсам
    def av_mark_lec(self):
        for course_name, grade in self.grades.items():
            self.average_grade[course_name] = sum(grade) / len(grade)

    # Функция вывода информации о лекторе
    def __str__(self):
        return f'Лекторы \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка по курсам: {self.average_grade}  \nЧитаемые лекции: {", ".join(self.courses_attached)} '

    # Сравнение лекторов между собой по средней оценке за курс
    def __gt__(self, other):
        if not isinstance(other, Lecturers):
            print('Not a Lecturers!')
            return
        for course_name, grade in self.average_grade.items():
            for course_name_2, grade_2 in other.average_grade.items():
                if course_name == course_name_2:
                    if grade > grade_2:
                        self.avg[course_name] = True
                    else:
                        self.avg[course_name] = False
        return print ('Средняя оценка больше:', self.avg)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'Ревьюеры \nИмя: {self.name} \nФамилия: {self.surname}'

# ввод экземпляров в классы

best_student = Student('stud name', 'stud surname', 'gender')
best_student.courses_in_progress += ['Python', 'Git']

best_student2 = Student('stud name 2', 'stud surname 2', 'gender')
best_student2.courses_in_progress += ['Python', 'Git']

cool_mentor = Reviewer('ment_name', 'ment_surname')
cool_mentor.courses_attached += ['Python', 'Git']
cool_lector = Lecturers('lect_name', 'lect_surname')
cool_lector.courses_attached += ['Python', 'Git']
cool_lector2 = Lecturers('lect_name2', 'lect_surname2')
cool_lector2.courses_attached += ['Python', 'Git']

# Выставление оценок студентам

cool_mentor.rate_st(best_student, 'Python', 1)
cool_mentor.rate_st(best_student, 'Git', 7)
cool_mentor.rate_st(best_student, 'Python', 3)
cool_mentor.rate_st(best_student, 'Git', 9)
cool_mentor.rate_st(best_student2, 'Python', 5)
cool_mentor.rate_st(best_student2, 'Git', 2)
cool_mentor.rate_st(best_student2, 'Python', 6)
cool_mentor.rate_st(best_student2, 'Git', 3)

# Выставление оценок лекторам

best_student.rate_lec(cool_lector, 'Git', 3)
best_student.rate_lec(cool_lector, 'Git', 5)
best_student.rate_lec(cool_lector, 'Python', 10)
best_student.rate_lec(cool_lector, 'Python', 8)
best_student.rate_lec(cool_lector2, 'Git', 1)
best_student.rate_lec(cool_lector2, 'Git', 3)
best_student.rate_lec(cool_lector2, 'Python', 0)
best_student.rate_lec(cool_lector2, 'Python', 3)

print(cool_lector.grades)
print(best_student.grades)

