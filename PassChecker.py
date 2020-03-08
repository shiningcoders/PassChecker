for i in range(0, 8):
    fname = (f'{i}.prik')
    fhandle = open(fname)

    checkpass = input('Enter your Password (! to exit) :')

    if checkpass == '!':
        exit(0)
    else:
        count = 0


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