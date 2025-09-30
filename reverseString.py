class demo:
    def accept(self):
        print("string reverse:")
        self.str1=input("Enter the string")
        self.str2=""
        i=len(self.str1)-1
        while (i>=0):
          self.str2+=self.str1[i]
          i-=1
        print("Reversed string:",self.str2)


d=demo()
d.accept()

