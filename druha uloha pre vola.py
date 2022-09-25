c=int(input('Vypíš sučet párnych čísel od 1 do ... :'))
a=0
for i in range(1,c):
    if i%2 == 0:
        a=a+i
print(a)
