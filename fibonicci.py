n=int(input("Enter the number of terms"))
def fibonacci(n):
   n1 , n2 = 0 , 1
   for _ in range(n):
       print(n1,end='')
       n3=n1+n2
       n1=n2
       n2=n3


fibonacci(n) 


