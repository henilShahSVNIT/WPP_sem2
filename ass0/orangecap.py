t1dhoni = input('Dhoni run in test 1 : ')
t1kohli = input('Kohli run in test 1 : ')
t1sachin = input('Sachin run in test 1 : ')

t2dhoni = input('Dhoni run in test 2 : ')
t2kohli = input('Kohli run in test 2 : ')
t2sachin = input('Sachin run in test 2 : ')

t0dhoni = int(t1dhoni) + int(t2dhoni)
t0kohli = int(t1kohli) + int(t2kohli)
t0sachin = int(t1sachin) + int(t2sachin)

if(t0dhoni > t0kohli and t0dhoni > t0sachin):
    print('Dhoni wins the orange cap')
else:
    if(t0kohli > t0sachin and t0kohli > t0dhoni):
        print('Kohli wins the orange cap')
    else:
        print('Sachin wins the orange cap')
