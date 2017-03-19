#-*- coding: UTF-8 -*-
# !/usr/bin/python3.5

db ={}

def newuser():
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break

    pwd = input('passwd: ')

    db[name] = pwd

def olduser():
    name = input('login: ')
    pwd = input('passwd: ')
    password = db.get(name)
    if password == pwd:
        print('welcome back %s' % name)
    else:
        print('login incorrect')

def showmenu():
    prompt = '''
    (N)ew User Login
    (E)xisting User Login 
    (Q)uit

    Enter your choice: '''


    done = False

    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'

            print('\nYour picked: [%s]' % choice)

            if choice not in 'neq':
                print('Invalid choice, try again')
            else:
                chosen = True

        if choice == 'q':
            done = True
        elif choice == 'n':
            newuser()
        elif choice == 'e':
            olduser()


if __name__ == '__main__':
    showmenu()

