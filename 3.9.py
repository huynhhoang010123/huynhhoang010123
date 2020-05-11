import math
def Tinh(R):
    cv=2*R*math.pi
    dt=R*R*math.pi
    print("chu vi hinh tron la: ",cv)
    print("dien tich hinh tron la: ",dt)
def temp_convert(var):
   try:
      return int(var)
   except ValueError :

      R = input("moi nhap ban kinh: ")

R=int(input("moi nhap ban kinh: "))
temp_convert(R)
Tinh(R)