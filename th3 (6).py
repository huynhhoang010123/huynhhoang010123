def get_sum(*num):
    tmp= 0
    #duyet cac ham so
    for i in num:
        tmp+=i
    return tmp
tong= get_sum(1,2,3,4,5)
print(tong)