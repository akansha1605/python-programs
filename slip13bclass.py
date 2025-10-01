class Demo:
    def __init__(self, size):
        self.q = []
        self.size = size

    def insert(self):
        if len(self.q) == self.size:
            print("Queue is full!")
        else:
            n = int(input("Enter the value of n: "))
            self.q.append(n)
            print(n, "is added to the queue")

    def delete(self):
        if len(self.q) == 0:
            print("Queue is empty!")
        else:
            e = self.q.pop(0) 
            print(e, "is removed")

    def display(self):
        print("Current queue:", self.q)



size = int(input("Enter the size of the queue: "))
d = Demo(size)

while True:
    print("\nSelect the operation:")
    print("1. Insert\n2. Delete\n3. Display\n4. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        d.insert()
    elif choice == 2:
        d.delete()
    elif choice == 3:
        d.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid option!")

