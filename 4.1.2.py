A=[]
B=[]
C=[]
import random
n=int(input('Nhập số phần tử List A: ' ))
m=int(input('Nhập số phần tử List B: ' ))
while n<=0 or m<=0:
        n=int(input('n phải là số nguyên dương. Hay Nhập lại: '))
        m=int(input('m phải là số nguyên dương. Hay Nhập lại: '))

for i in range(1,n+1):
    giatri=random.randint (-100,100)
    A.append(giatri)
for j in range(1,m+1):
    giatri=random.randint (-100,100)
    B.append(giatri)
print ('\nXUẤT LIST NGẪU NHIÊN')
print ('A = ',A)
print ('\nB = ',B)
print("\nGHÉP LIST A VA LIST B THÀNH LIST C")
print("------------------------------------");
C.extend(A)
C.extend(B)
print('C=',C)
print("\nSẮP XẾP LIST C TĂNG DẦN")
print("-------------------------");
C.sort()
print('C=',C)
x=int(input('Nhập số nguyên x: ' ))
if x in C:
    i=C.index(x)
    print (x,' xuất hiện đầu tiên tại vi tri: C[',i,'], Giá trị: ',C[i])
else:
    print (x,' Không xuất hiện trong C')
print("\nXÓA PHẦN TỬ TRÙNG NHAU TRONG LIST - IN LIST MỚI")
print("-------------------------------------------------");
Cnew = []
for i in C:
    if i not in Cnew:
        Cnew.append(i)
print('C mới=', Cnew)