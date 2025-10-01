num=int(input("Enter the number:"))
try:
    if num>=0:
        raise ValueError("Positive Number:Input is correct")
    else:
        raise ValueError("Negative Number:Input is incorrect")
except ValueError as e:
    print(e)