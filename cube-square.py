def areaCube(a):
    return(a*a*a)
def surfaceCube(a):
    return(6*a*a)
a=5
print("cube is:",areaCube(a))
print("Totalsurface area is:",surfaceCube(a))

pi=22/7
r=5
def areaSphere():
    return (4*pi*r**2)
def volumeSphere():
    return(4/3*(pi*r**3))
print("area is:",areaSphere())
print("volume of sphere is:",volumeSphere())
