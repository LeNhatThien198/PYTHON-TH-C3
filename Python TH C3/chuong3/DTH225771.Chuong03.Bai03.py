import math
print("Chương trình giải phương trình bậc 2")
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
if a == 0:
    if b == 0 and c ==0:
        print("Phương trình vô số nghiệm")
    elif b == 0 and c!=0:
        print("Phương trình vô nghiệm")
    else:
        x=-c/b
        print("x= ",x)
else:
    delta=b**2-4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x=-b/(2*a)
        print("Phương trình có nghiệm kép x1=x2= ",x)
    else:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("Phương trình có 2 nghiệm: ")
        print("x1= ", x1)
        print("x2= ", x2)
