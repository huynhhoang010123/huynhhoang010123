a,b=1,2
tong=0
print(a,end=" ")
while (a <4000000-1):
    if a % 2==0:
        tong +=a
    a,b=b,a+b
    print(a,end=" ")
print( "\n tong cac so chan trong day fobobaci la:",tong)
