class demo:
    def accept(self):
        self.str1=input("Enter the value of first string:")
        self.str2=input("Enter the value of second string:")

        str3 =self.str1+self.str2
        print("Concatenation of two strings:",str3)


d=demo()
d.accept()