def convert(str):
    result=tuple((int(x[0]),int(x[1])) for x in str)
    return result
str=(('333','33'),('1416','55'))
print("original tuple values:")
print(str)
print("New tuple values:")
print(convert(str))