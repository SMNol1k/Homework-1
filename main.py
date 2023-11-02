def avg_rating(grades):
    grades_count = 0
    grades_sum = 0
    for grade in grades:
            grades_count += len(grades[grade])
            grades_sum += sum(grades[grade])
    return grades_sum / grades_count

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturs(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {avg_rating(self.grades)}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
    
    def grades_average(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.grades_average() > other.grades_average()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.grades_average() < other.grades_average()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.grades_average() == other.grades_average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}


    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_rating(self.grades)}\n')
    
    def grades_average_(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0
        
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.grades_average_() > other.grades_average_()
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.grades_average_() < other.grades_average_()
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.grades_average_() == other.grades_average_()       

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')    


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Sam', 'Winchester', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

lectur_1 = Lecturer('John', 'Smith')
lectur_1.courses_attached += ['Python']

lectur_2 = Lecturer('James', 'Smith')
lectur_2.courses_attached += ['Git']

mentor_1 = Reviewer('Some', 'Buddy')
mentor_1.courses_attached += ['Python']

mentor_2 = Reviewer('Second', 'Buddy')
mentor_2.courses_attached += ['Git']


mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_1, 'Python', 9)
mentor_1.rate_hw(student_1, 'Python', 8)
mentor_1.rate_hw(student_1, 'Git', 8)
mentor_1.rate_hw(student_1, 'Git', 9)
mentor_1.rate_hw(student_1, 'Git', 8)

mentor_2.rate_hw(student_2, 'Git', 8)
mentor_2.rate_hw(student_2, 'Git', 9)
mentor_2.rate_hw(student_2, 'Git', 8)
mentor_2.rate_hw(student_2, 'Python', 9)
mentor_2.rate_hw(student_2, 'Python', 9)
mentor_2.rate_hw(student_2, 'Python', 8)
 
student_1.rate_lecturs(lectur_1, 'Python', 9)
student_1.rate_lecturs(lectur_1, 'Python', 8)
student_1.rate_lecturs(lectur_1, 'Python', 7)

student_2.rate_lecturs(lectur_2, 'Git', 9)
student_2.rate_lecturs(lectur_2, 'Git', 8)
student_2.rate_lecturs(lectur_2, 'Git', 8)

if avg_rating(student_1.grades) > avg_rating(student_2.grades):
    print(f'У студента {student_1.name} {student_1.surname} оценки лучше\n')
else:
    print(f'У студента {student_2.name} {student_2.surname} оценки лучше\n')

if avg_rating(lectur_1.grades) > avg_rating(lectur_2.grades):
    print(f'У лектора {lectur_1.name} {lectur_1.surname} средняя оценка за лекции выше\n')
else:
    print(f'У лектора {lectur_2.name} {lectur_2.surname} средняя оценка за лекции выше\n')

print(student_1.__str__())
print(lectur_1.__str__())
print(mentor_1.__str__())
print(student_1.grades)
print(lectur_1.grades)

print(student_2.__str__())
print(lectur_2.__str__())
print(mentor_2.__str__())
print(student_2.grades)
print(lectur_2.grades)

def average_grade_students(students, course):
    grades_count = 0
    grades_sum = 0
    for student in students:
        if course in student.grades:
            grades_count += len(student.grades[course])
            grades_sum += sum(student.grades[course])
    return grades_sum / grades_count

def average_grade_lecturers(lecturers, course):
    grades_sum = 0
    grades_count = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            grades_sum += sum(lecturer.grades[course])
            grades_count += len(lecturer.grades[course])
    return grades_sum / grades_count

course = 'Python'
print(f"Средняя оценка за лекции по курсу {course}: {average_grade_lecturers([lectur_1, lectur_2], course)}")

course = 'Git'
print(f"Средняя оценка за лекции по курсу {course}: {average_grade_lecturers([lectur_1, lectur_2], course)}")

course = 'Python'
print(f"Средняя оценка за домашние задания по курсу {course}: {average_grade_students([student_1, student_2], course)}")

course = 'Git'
print(f"Средняя оценка за домашние задания по курсу {course}: {average_grade_students([student_1, student_2], course)}")

if student_1 > student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} больше, чем средняя оценка {student_2.name} {student_2.surname}')
elif student_1 < student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} меньше, чем средняя оценка {student_2.name} {student_2.surname}')
else:
    print(f'Средняя оценка {student_1.name} {student_1.surname}  равна средней оценке {student_2.name} {student_2.surname}')

if lectur_1 > lectur_2:
    print(f'Средняя оценка {lectur_1.name} {lectur_1.surname} больше, чем средняя оценка {lectur_2.name} {lectur_2.surname}')
elif lectur_1 < lectur_2:
    print(f'Средняя оценка {lectur_1.name} {lectur_1.surname} меньше, чем средняя оценка {lectur_2.name} {lectur_2.surname}')
else:
    print(f'Средняя оценка {lectur_1.name} {lectur_1.surname}  равна средней оценке {lectur_2.name} {lectur_2.surname}')
