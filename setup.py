import os, sys

def help():
    print('Available options:')
    print('\tinstall\tInstall pyfetch')
    print('\tuninstall\tUninstall pyfetch')

try:
    if sys.argv[1] == 'install':
        print('Installing pyfetch...')
        os.system('cp pyfetch.py /usr/bin/pyfetch')
        print('Changing permission for /usr/bin/pyfetch...')
        os.system('chmod +x /usr/bin/pyfetch')
        print('Copying pyfetch.conf in /etc/pyfetch/pyfetch.conf')
        os.system('mkdir /etc/pyfetch')
        os.system('cp pyfetch.conf /etc/pyfetch')
    elif sys.argv[1] == 'uninstall':
        print('Uninstalling pyfetch...')
        os.system('rm -f /usr/bin/pyfetch')
        print('Removing /etc/pyfetch directory')
        os.system('rm -rf /etc/pyfetch')
    else:
        print('Unknown options:', sys.argv[1])
        help()
except:
    print('Error:', sys.exc_info())
    help()
