a=input('while, for, both? ')

if a=='while':
    print('countdown!')
    x=10
    while x>0:
        print(x)
        x=x-1

    while True:
        y=(input('say something: '))
        if y=='hello':
            print ('almost there')
            continue

        if y=='hey':
            break
        else:
            print('try again')

    print('\ngood job, you guessed')

elif a=='for':
    b, c, d, e = input('enter four numbers, split them by ",": ').split(',')
    for i in [b,c,d,e]:
        i=int(i)
        i=(i-1/2)**5
        print(i)
    print('\ndone')

elif a=='both':
    ab, ac, ad, ae = input('enter four numbers, split them by ","').split(',')
    for ai in [ab,ac,ad,ae]:
        ai=int(ai)
        while ai>0:
            print(ai)
            ai=ai-1