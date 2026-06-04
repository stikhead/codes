a = 0
b = -1

if a<10:
    print(f'{a} is less than 10')
else:
    print(f'{b} is less than {a}')


if a>5 and b>=7:
    print(True)
elif a==5 or b>=0:
    print(f'{a} and {b}')
else: 
    if a==0:
        print(a)


score = 85
# if score>=80 and score<=100:
#     print(f'great score!')

if 80<= score <=100: #pythonic style - math like chaining 
    print('valid score!')