#link of the challenge
#https://www.codewars.com/kata/5b4e779c578c6a898e0005c5

num = 3
cont = 0
espaços = 1
a = ''

for c in range(1,num + 1):
    if num > 1:
        if c == 1:
            a += 'I\n '
        if c > 1 and c < num:
            a += 'I\n '
            a += ' ' * espaços
            espaços += 1
        if c == num:
            a += 'I'
    else:
        a += 'I'


print(a)
