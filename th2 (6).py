import re
value=[]
items=[x for x in input("nhap mat khau: ").split(',')]

for n in items:
    if len(n)<6 or len(n)>12:
        continue
    else:
        pass
    if not re.search("[0-9]",n):
        continue
    elif not re.search("[A-Z]",n):
        continue
    elif not re.search("[a-z]",n):
        continue
    elif not re.search("[$#@]",n):
        continue
    elif re.search("\s",n):
        continue
    else:
        pass
    value.append(n)
print(",".join(value))
    
