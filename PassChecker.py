# Enter password to check
checkpass = input('Enter your Password :')
count = 0

# Loop to change password lists (It deployes one after another)
for i in range(0, 8):
    fname = (f'{i}.prik')
    fhandle = open(fname)

    #Check if password present in list
    for past in fhandle:
        past=past.strip()
        if past == checkpass:
            print(past, 'isn\'t  hard to brute. ')
            count = count + 1
            exit(0)
        else:
            print(past)

# If password not present in lists
if count == 0:
    print('All Good. ')