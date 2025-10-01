class Mydate:
    try:
       def accept(self):
        self.d=int(input("Enter the date:"))
        self.m=int(input("Enter the month:"))
        self.y=int(input("Enter the year:"))
       def display(self):
        if self.d>31:
            raise ValueError("Date value is greater than 31")
        if self.m>12:
            raise ValueError("Month value is greater than 12")
        print("Date is:",self.d ,"-" ,self.m ,"-", self.y)
    except ValueError as e:
         print(e)


m=Mydate()
m.accept()
m.display()