import random
answer = int(random.uniform(1,10))
number = int(input('猜猜数字：'))
if number == answer:
    print('厉害，第一次就对了')
while number != answer:
    if number>answer:
        print("bigger")
        number = int(input('再猜一次：'))
    if number<answer:
        print("smaller")
        number = int(input('再猜一次'))
    if number == answer:
        print('bingo')
        break
