class GroupLimitError(Exception):
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} років"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f"{self.first_name} {self.last_name}, {self.gender}, "
                f"{self.age} років, record book: {self.record_book}")


class Group:

    def __init__(self, number, limit=10):
        self.number = number
        self.group = set()
        self.limit = limit

    def add_student(self, student):
        if len(self.group) >= self.limit:
            raise GroupLimitError(
                f"Група '{self.number}' вже містить {self.limit} студентів. "
                f"Неможливо додати: {student.first_name} {student.last_name}"
            )
        self.group.add(student)

    def find_student(self, last_name):
        for student_in_group in self.group:
            if student_in_group.last_name == last_name:
                return student_in_group
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print("Після додавання двох студентів:")
print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')

print("\nПісля видалення Taylor:")
print(gr)

gr.delete_student('Taylor')

print("\nДодаємо студентів до заповнення групи:")

try:
    for i in range(1, 12):
        st = Student('Male', 18 + i, f'Name{i}',
                     f'Last{i}', f'RB{i}')
        gr.add_student(st)
        print(f"Додано: {st.first_name} {st.last_name}")
except GroupLimitError as e:
    print('\n: Перехоплено виняток користувача!')
    print(e)

print("\nКінцевий склад групи:")
print(gr)
