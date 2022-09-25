c=int(input('Vypíš sučet čísel od 1 do ... :'))
a=0
for i in range(1,c):
    if i%i == 0:
        a=a+i
print(a)
