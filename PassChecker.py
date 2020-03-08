checkpass = input('Enter your Password :')
count = 0

for i in range(0, 8):
    fname = (f'{i}.prik')
    fhandle = open(fname)


    for past in fhandle:
        past=past.strip()
        if past == checkpass:
            print(past, 'isn\'t  hard to brute. ')
            count = count + 1
            break
        else:
            print(past)


if count == 0:
    print('All Good. ')