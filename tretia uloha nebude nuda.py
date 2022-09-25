c=int(input('Vypíš počet všetkých čísel ktoré sú delitelné 7 a 4 od 1 do ... :'))
a=0
for i in range(1,c):
    if i%4 == 0 and i%7 ==0:
        a=a+1
print(a)
