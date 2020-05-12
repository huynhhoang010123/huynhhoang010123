import math
pos=[0,0]
while True:
    s=input()
    if not a:
        break
    movement = s.split("")
    direction=movement[0]
    steps=int(movement[1])
    if direction =="DOWN":
        pos[0]=steps
    elif dirction=="LEFT":
        pos[0]-=steps
    elif direction =="RIGHT":
        pos[1]+=steps
    else:
        pass
print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))