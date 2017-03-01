from caesar import Caesar
from substitution import Substitution


def run():
    b = True
    while b:
        print '##########MENU##########'
        choise = \
            raw_input('''What do you want to do?
        1.Encrypt with caesar
        2.Decrypt with caesar
        3.Encrypt with subsitution
        4.Decrypt with subsitution
        5.Try to hack the substitution method
        6.Exit
        ''')
        if choise == '6':
            b = False
        elif choise == '1':
            word = raw_input('Input word ').strip()
            key = int(raw_input('Input key '))
            caesa = Caesar(word, key)
            print 'ENCRYPTED= ' + caesa._encrypt()
        elif choise == '2':
            word = raw_input('Input word ').strip()
            key = int(raw_input('Input key '))
            caesa = Caesar(word, key)
            print 'DECRYPTED= ' + caesa._decrypt()
        elif choise == '3':
            word = raw_input('Input word ').strip()
            subs = Substitution(word)
            print 'ENCRYPTED= ' + subs._encrypt()
        elif choise == '4':
            word = raw_input('Input word ').strip()
            subs = Substitution(word)
            print 'DECRYPTED= ' + subs._decrypt()
        elif choise == '5':
            word = raw_input('Input word ').strip()
            subs = Substitution(word)
            print subs.frequency_analysis()
        else:
            print 'Make a right choise'


if __name__ == '__main__':
    run()
