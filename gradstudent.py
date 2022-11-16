from student import  Student

class GradStudent(Student):
    def __init__(self, name, studentID, undergrad_degree):
        super().__init__(name, studentID)
        self.undergrad = undergrad_degree

    def take_masters_class(self):
        print(f"{self.name} is taking a grad class now")
