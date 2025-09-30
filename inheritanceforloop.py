class Student:
    def accept(self):
        self.rno=int(input("Enter the roll number of student:"))
        self.name=input("Enter the name of student:")
        self.age=int(input("Enter the age of the student:"))
        self.gender=input("Enter the gender of the student:")

    def display(self):
        print("Roll number of student:",self.rno)
        print("Name of the student:",self.name)
        print("Age of the student:",self.age)
        print("Gender of the student:",self.gender)

class Test(Student):
    def gmarks(self):
        self.marathi=int(input("Enter marks of marathi:"))
        self.hindi=int(input("Enter marks of hindi:"))
        self.english=int(input("Enter marks of english:"))

    def dmarks(self):
        print("Enter marks of marathi:",self.marathi)
        print("enter the marks of hindi:",self.hindi)
        print("Enter the  marks of english:",self.english)
        print("Total marks:",self.marathi+self.hindi+self.english)

n=int(input("Enter the number of students you want to take for the record:"))

for i in range(n):
     s = Test()
     s.accept()
     s.gmarks()
     s.dmarks()
