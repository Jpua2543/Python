for x in range(0, 151, 1):
    print(x)


for x in range(5, 1005,5):
    print(x)


for count in range(1 ,101):
    if count % 10 == 0:
        print("Coding Dojo")
    elif count % 5 == 0:
        print("Coding")
    else:
        print(count)

sum = 0
for i in range(0, 500000):
    if i % 2 == 1:
        sum = sum + i
print(sum)

for x in range(2018,0,-4):
    print(x)

lowNum = 1
highNum = 160
mult = 2
for x in range(lowNum,highNum+1):
    if x % mult == 0:
        print(x)