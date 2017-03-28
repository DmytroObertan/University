from caesar import Caesar
from substitution import Substitution
from vigener import Vigener
from diffi_helmann import DiffiHellmann


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
        6.Vigener encrypt
        7.Vigener decrypt
        8. Diffi-Helmann keys
        9.Exit
        ''')
        if choise == '9':
            b = False
        elif choise == '6':
            word = raw_input('Input word ').strip()
            key = raw_input('Input key ')
            vig = Vigener(word, key)
            print 'ENCRYPTED= ' + vig._encrypt()
        elif choise == '7':
            word = raw_input('Input word ').strip()
            key = raw_input('Input key ')
            vig = Vigener(word, key)
            print 'DECRYPTED= ' + vig._decrypt()
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
            new = subs.frequency_analysis()
            print 'RESULT = ' + new
            while True:
                choise = \
                    raw_input('''What do you want to do?
                        1.Replace symbols
                        2.Exit
                        ''')
                if choise == '1':
                    a = raw_input('What to replace?')
                    b = raw_input('With what to replace?')
                    new = subs.repl(new, a, b)
                    print 'RESULT = ' + new
                elif choise == '2':
                    break
        elif choise == '8':
            a = int(raw_input('Secret value of first '))
            g = int(raw_input('Value of g '))
            p = int(raw_input('Value of p '))
            b = int(raw_input('Secret value of second '))
            diffi = DiffiHellmann(a, g, p, b)
            print 'Checking if keys is the same. It may take some time '
            print  str(diffi._get_keys())
        else:
            print 'Make a right choise'


if __name__ == '__main__':
    run()
