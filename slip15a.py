class Student:
    def accept(self):
       self.name=input("Enter the name of student:")
       self.marks=int(input("Enter the marks of the students:"))
    
    def display(self):
        self.oldmarks=self.marks
        self.marks=int(input("Enter the new total marks of the student"))
        print("Student name:",self.name)
        print("Students old total marks:",self.oldmarks)
        print("Students new total marks:",self.marks)
       
stud=Student()
stud.accept()
stud.display()