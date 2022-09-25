b=int(input('Vypíš počet čísel od ... :'))
c=int(input('Vypíš počet čísel do ... :'))
a=0
for i in range(b,c+1):
    if i%8 == 0:
        a=a+1
print(a)
