#-*- coding: UTF-8 -*-
# !/usr/bin/python3.5

stack = []

def pushit():
    stack.append(input('Enter New String: ').strip())

def popit():
    if len(stack) == 0:
        print('Cannot pop from an empty stack！')
    else:
        print("Remove ['%s']" % (stack.pop()))

def viewstack():
    print(stack)

CMDs = {'u': pushit, 'o': popit, 'v': viewstack}

def showmenu():
    pr = '''
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit
    
    Enter choices: '''

    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except(EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print('\nYour picked: [%s]' % choice)

            if choice not in 'uovq':
                print('Invalid option, try again.')
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()

