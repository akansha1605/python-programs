dict={"a":1,"b":2,"c":4,"d":7}
print(dict)
check_key=input("Enter key to check:")
check_value=input("Enter the value:")
if check_key in dict:
    print(check_key,"is present")
    dict.pop(check_key)
    dict[check_key]=check_value
else:
    print(check_key,"is not present")
    dict[check_key]=check_value
print("updated dictionary:",dict)
