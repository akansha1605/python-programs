l=[10,20,30,10,50]
duplicate=[]
for n in l:
    if n not in duplicate:
        duplicate.append(n)
        print(duplicate)