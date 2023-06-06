#básico

for a in range (151):
    print(a)

print("________________________________________________")
#Múltiplos de cinco

for b in range(5,1001):
    if(b%5==0):
        print(b)

print("________________________________________________")
#contar, a la manera del Dojo

for c in range(1, 101):
    if(c % 10 == 0):
        print("Coding Dojo")
    elif(c % 5 == 0):
        print("Coding")
    else:
        print(c)

print("________________________________________________")
#whoa. Es un gran idiota

suma = 0
for d in range(0,500001):
    if(d %2 !=0):
        suma +=d
print(suma)


print("________________________________________________")
#cuenta regresiva de a 4

for e in range (2018, 0, -4):
    print(e)


print("________________________________________________")
#comtador flexible

lowNum=1
highNum=161
mult=6

for f in range(lowNum, highNum):
    if(f %mult ==0):
        print(f)