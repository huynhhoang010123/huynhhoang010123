x=int(input("nhap so tu nhien cho truoc: "))
def giaithua(x):
    if x==0:
        return 1
    return x* giaithua(x-1)
print(giaithua(x))
