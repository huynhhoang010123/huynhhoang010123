
a=int(input("nhap a: "))
b=int(input("nhap b: "))
c=int(input("nhap c: "))
import math
if a==0:
    x=-c/a
    print("nghiem cua phuong trinh la:",x)
else:
    deta=b*b-4*a*c
    if deta==0:
        x=-b/2*a
        print("phương trình coa nghiệm kép: x= ",x)
    elif deta<0:
        print("phương trình vô nghiệm")
    else:
        x1=(-b+math.sqrt(deta))/2*a
        x2=(-b-math.sqrt(deta))/2*a
        print("phương trình có 2 nghiệm phân biệt: x1=",x1,"x2=",x2)
