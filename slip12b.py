str="hiihellohere"
print(str)
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for j in dict:
    print(j,"-",dict[j])
