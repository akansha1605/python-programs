def Demo():
 str=input("Enter the String:")
 n=len(str)
 newStr=""
 for i in range(0,n):
  if(i%2==0):
   newStr=newStr+str[i]
   print("New string without odd index characters:",newStr)

Demo()