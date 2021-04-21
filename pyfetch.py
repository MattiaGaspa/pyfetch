#!/usr/bin/python3
import os, sys, psutil, distro

username = os.environ['USER']

osname = distro.linux_distribution()[0] + '/Linux ' + distro.linux_distribution()[1]

arch = os.uname()[4]

kernel = os.uname()[2]

uptime = int(float(open('/proc/uptime').read().split(' ')[0]) - (float(open('/proc/uptime').read().split(' ')[0]) % 1))

shell = os.environ['SHELL']

editor = os.environ['EDITOR']

lang = os.environ['LANGUAGE']

encoding = os.device_encoding(0)

pythonv = sys.version[0] + sys.version[1] + sys.version[2] + sys.version[3] + sys.version[4] + sys.version[5]

cpu_number = os.cpu_count()
cpu_current_clock = int(psutil.cpu_freq().current)
cpu_max_clock = psutil.cpu_freq().max

ram = psutil.virtual_memory().total
used_ram = psutil.virtual_memory().used
ram_percent = psutil.virtual_memory().percent

swap = psutil.swap_memory().total
used_swap = psutil.swap_memory().used
swap_percent = psutil.swap_memory().percent

def secs_to_other(time):
    d = int(time / 86400)
    h = int(time / 3600 % 24)
    m = int(time / 60 % 60)

    time = ''
    if d > 1:
        time += str(d) + ' days '
    if h > 1:
        time += str(h) + ' hours '
    if m > 1:
        time += str(m) + ' mins '
    return time

def convert(bytes):
    unitIndex = 0
    units = ['B','KB','MB','GB','TB']
    while 1000 <= bytes:
        bytes /= 1000
        unitIndex += 1
    return f"{round(bytes)}{units[unitIndex]}"

if psutil.sensors_battery().power_plugged:
    batt_stat = 'plugged ({}%)'.format(int(psutil.sensors_battery().percent))
else:
    batt_stat = str(int(psutil.sensors_battery().percent)) + '% (' + secs_to_other(psutil.sensors_battery().secsleft) + 'left)'

color = {
    'normal': '\u001b[00;0m',
    'Arch': '\u001b[36;1m',
    'Debian': '\u001b[31;1m',
    'Gentoo': '\u001b[35;1m',
    'Manjaro': '\u001b[32;1m',
    'Ubuntu': '\u001b[31;1m'
}
logo = {
    'Arch': [
        '                    \u001b[36;1my:\u001b[00;0m\t\t\t\t',
        '                  \u001b[36;1msMN-\u001b[00;0m\t\t\t\t',
        '                 \u001b[36;1m+MMMm`\u001b[00;0m\t\t\t\t',
        '                \u001b[36;1m/MMMMMd`\u001b[00;0m\t\t\t',
        '               \u001b[36;1m:NMMMMMMy\u001b[00;0m\t\t\t',
        '              \u001b[36;1m-NMMMMMMMMs\u001b[00;0m\t\t\t',
        '             \u001b[36;1m.NMMMMMMMMMM+\u001b[00;0m\t\t\t',
        '            \u001b[36;1m.mMMMMMMMMMMMM+\u001b[00;0m\t\t\t',
        '            \u001b[36;1moNMMMMMMMMMMMMM+\u001b[00;0m\t\t\t',
        '          \u001b[36;1m`+:-+NMMMMMMMMMMMM+\u001b[00;0m\t\t\t',
        '          \u001b[36;1m.sNMNhNMMMMMMMMMMMM/\u001b[00;0m\t\t\t',
        '        \u001b[36;1m`hho/sNMMMMMMMMMMMMMMM/\u001b[00;0m\t\t\t',
        '       \u001b[36;1m`.`omMMmMMMMMMMMMMMMMMMM+\u001b[00;0m\t\t',
        '      \u001b[36;1m.mMNdshMMMMd+::oNMMMMMMMMMo\u001b[00;0m\t\t',
        '     \u001b[36;1m.mMMMMMMMMM+\u001b[00;0m     \u001b[36;1m`yMMMMMMMMMs\u001b[00;0m\t\t',
        '    \u001b[36;1m.NMMMMMMMMM/\u001b[00;0m        \u001b[36;1myMMMMMMMMMy\u001b[00;0m\t\t',
        '   \u001b[36;1m-NMMMMMMMMMh\u001b[00;0m         \u001b[36;1m`mNMMMMMMMMd`\u001b[00;0m\t\t',
        '  \u001b[36;1m/NMMMNds+:.`\u001b[00;0m             \u001b[36;1m`-/oymMMMm.\u001b[00;0m\t\t',
        ' \u001b[36;1m+Mmy/.\u001b[00;0m                          \u001b[36;1m`:smN:\u001b[00;0m\t\t',
        '\u001b[36;1m/+.\u001b[00;0m                                  \u001b[36;1m-o.\u001b[00;0m\t'],
    'Debian': [
        '       \u001b[00;1m_,met$$$$$gg.\t\t',
        '    \u001b[00;1m,g$$$$$$$$$$$$$$$P.\t\t',
        '  \u001b[00;1m,g$$P"     """Y$$.".\t\t',
        ' \u001b[00;1m,$$P\'              `$$$.\t',
        '\u001b[00;1m,$$P       ,ggs.     `$$b:\t',
        '\u001b[00;1m`d$$\'     ,$P"\'   \u001b[31;1m.\u001b[00;1m    $$$\t',
        ' \u001b[00;1m$$P      d$\'     \u001b[31;1m,\u001b[00;1m    $$P\t',
        ' \u001b[00;1m$$:      $$.   \u001b[31;1m-\u001b[00;1m    ,d$$\'\t',
        ' \u001b[00;1m$$;      Y$b._   _,d$P\'\t',
        ' \u001b[00;1mY$$.    \u001b[31;1m`.\u001b[00;1m`"Y$$$$P"\'\t\t',
        ' \u001b[00;1m`$$b      \u001b[31;1m"-.__\u001b[00;1m\t\t',
        '  \u001b[00;1m`Y$$\t\t\t\t',
        '   \u001b[00;1m`Y$$.\t\t\t',
        '     \u001b[00;1m`$$b.\t\t\t',
        '       \u001b[00;1m`Y$$b.\t\t\t',
        '          \u001b[00;1m`"Y$b._\t\t',
        '              \u001b[00;1m`"""\t\t'
    ],
    'Gentoo': [
        '         \u001b[35;1m-/oyddmdhs+:.\u001b[00;1m\t\t\t',
        '     \u001b[35;1m-o\u001b[00;1mdNMMMMMMMMNNmhy+\u001b[35;1m-`\u001b[00;0m\t\t',
        '   \u001b[35;1m-y\u001b[00;1mNMMMMMMMMMMMNNNmmdhy\u001b[35;1m+-\u001b[00;0m\t\t',
        ' \u001b[35;1m`o\u001b[00;1mmMMMMMMMMMMMMNmdmmmmddhhy\u001b[35;1m/`\u001b[00;0m\t\t',
        ' \u001b[35;1mom\u001b[00;1mMMMMMMMMMMMN\u001b[35;1mhhyyyo\u001b[00;1mhmdddhhhd\u001b[35;1mo`\u001b[00;0m\t',
        '\u001b[35;1m.y\u001b[00;1mdMMMMMMMMMMd\u001b[35;1mhs++so/s\u001b[00;1mmdddhhhhdm\u001b[35;1m+`\u001b[00;0m\t',
        ' \u001b[35;1moy\u001b[00;1mhdmNMMMMMMMN\u001b[35;1mdyooy\u001b[00;1mdmddddhhhhyhN\u001b[35;1md.\u001b[00;0m\t',
        '  \u001b[35;1m:o\u001b[00;1myhhdNNMMMMMMMNNNmmdddhhhhhyym\u001b[35;1mMh\u001b[00;0m\t',
        '    \u001b[35;1m.:\u001b[00;1m+sydNMMMMMNNNmmmdddhhhhhhmM\u001b[35;1mmy\u001b[00;0m\t',
        '       \u001b[35;1m/m\u001b[00;1mMMMMMMNNNmmmdddhhhhhmMNh\u001b[35;1ms:\u001b[00;0m\t',
        '    \u001b[35;1m`o\u001b[00;1mNMMMMMMMNNNmmmddddhhdmMNhs\u001b[35;1m+`\u001b[00;0m\t',
        '  \u001b[35;1m`s\u001b[00;1mNMMMMMMMMNNNmmmdddddmNMmhs\u001b[35;1m/.\u001b[00;0m\t',
        ' \u001b[35;1m/N\u001b[00;1mMMMMMMMMNNNNmmmdddmNMNdso\u001b[35;1m:`\u001b[00;0m\t\t',
        '\u001b[35;1m+M\u001b[00;1mMMMMMMNNNNNmmmmdmNMNdso\u001b[35;1m/-\u001b[00;0m\t\t',
        '\u001b[35;1myM\u001b[00;1mMNNNNNNNmmmmmNNMmhs+/\u001b[35;1m-`\u001b[00;0m\t\t',
        '\u001b[35;1m/h\u001b[00;1mMMNNNNNNNNMNdhs++/\u001b[35;1m-`\u001b[00;0m\t\t\t',
        '\u001b[35;1m`/\u001b[00;1mohdmmddhys+++/:\u001b[35;1m.`\u001b[00;0m\t\t\t',
        '  \u001b[35;1m`-//////:--.\u001b[00;1m\t\t\t\t'],
    'Manjaro': [
        '\u001b[32;1m██████████████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m██████████████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m██████████████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m██████████████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m            \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t'],
    'Ubuntu': [
        '            \u001b[31;1m.-/+oossssoo+/-.\u001b[00;1m\t\t\t',
        '        \u001b[31;1m`:+ssssssssssssssssss+:`\u001b[00;1m\t\t',
        '      \u001b[31;1m-+ssssssssssssssssssyyssss+-\u001b[00;1m\t\t',
        '    \u001b[31;1m.ossssssssssssssssss\u001b[00;1mdMMMNy\u001b[31;1msssso.\u001b[00;1m\t\t',
        '   \u001b[31;1m/sssssssssss\u001b[00;1mhdmmNNmmyNMMMMh\u001b[31;1mssssss/\u001b[00;1m\t\t',
        '  \u001b[31;1m+sssssssss\u001b[00;1mhm\u001b[31;1myd\u001b[00;1mMMMMMMMNddddy\u001b[31;1mssssssss+\u001b[00;1m\t\t',
        ' \u001b[31;1m/ssssssss\u001b[00;1mhNMMM\u001b[31;1myh\u001b[00;1mhyyyyhmNMMMNh\u001b[31;1mssssssss/\u001b[00;1m\t\t',
        '\u001b[31;1m.ssssssss\u001b[00;1mdMMMNh\u001b[31;1mssssssssss\u001b[00;1mhNMMMd\u001b[31;1mssssssss.\u001b[00;1m\t',
        '\u001b[31;1m+ssss\u001b[00;1mhhhyNMMNy\u001b[31;1mssssssssssss\u001b[00;1myNMMMy\u001b[31;1msssssss+\u001b[00;1m\t',
        '\u001b[31;1moss\u001b[00;1myNMMMNyMMh\u001b[31;1mssssssssssssss\u001b[00;1mhmmmh\u001b[31;1mssssssso\u001b[00;1m\t',
        '\u001b[31;1moss\u001b[00;1myNMMMNyMMh\u001b[31;1msssssssssssssshmmmh\u001b[31;1mssssssso\u001b[00;1m\t',
        '\u001b[31;1m+ssss\u001b[00;1mhhhyNMMNy\u001b[31;1mssssssssssss\u001b[00;1myNMMMy\u001b[31;1msssssss+\u001b[00;1m\t',
        '\u001b[31;1m.ssssssss\u001b[00;1mdMMMNh\u001b[31;1mssssssssss\u001b[00;1mhNMMMd\u001b[31;1mssssssss.\u001b[00;1m\t',
        ' \u001b[31;1m/ssssssss\u001b[00;1mhNMMM\u001b[31;1myh\u001b[00;1mhyyyyhdNMMMNh\u001b[31;1mssssssss/\u001b[00;1m\t\t',
        '  \u001b[31;1m+sssssssss\u001b[00;1mdm\u001b[31;1myd\u001b[00;1mMMMMMMMMddddy\u001b[31;1mssssssss+\u001b[00;1m\t\t',
        '   \u001b[31;1m/sssssssssss\u001b[00;1mhdmNNNNmyNMMMMh\u001b[31;1mssssss/\u001b[00;1m\t\t',
        '    \u001b[31;1m.ossssssssssssssssss\u001b[00;1mdMMMNy\u001b[31;1msssso.\u001b[00;1m\t\t',
        '      \u001b[31;1m-+sssssssssssssssss\u001b[00;1myyy\u001b[31;1mssss+-\u001b[00;1m\t\t',
        '        \u001b[31;1m`:+ssssssssssssssssss+:`\u001b[00;1m\t\t',
        '            \u001b[31;1m.-/+oossssoo+/-.\u001b[00;1m\t\t\t']
}

print(logo[distro.linux_distribution()[0]][0] + color[distro.linux_distribution()[0]] + username + color["normal"] + '@' + color[distro.linux_distribution()[0]] + os.uname()[1] + color["normal"])
print(logo[distro.linux_distribution()[0]][1] + ('-' * len(username + '@' + os.uname()[1])))
print(logo[distro.linux_distribution()[0]][2] + color[distro.linux_distribution()[0]] + 'OS' + color["normal"] + ':', osname, arch)
print(logo[distro.linux_distribution()[0]][3] + color[distro.linux_distribution()[0]] + 'Kernel' + color["normal"] + ':', kernel)
print(logo[distro.linux_distribution()[0]][4] + color[distro.linux_distribution()[0]] + 'Uptime' + color["normal"] + ': %s' % secs_to_other(uptime))
print(logo[distro.linux_distribution()[0]][5] + color[distro.linux_distribution()[0]] + 'Shell' + color["normal"] + ':', shell)
print(logo[distro.linux_distribution()[0]][6] + color[distro.linux_distribution()[0]] + 'Editor' + color["normal"] + ':', editor)
print(logo[distro.linux_distribution()[0]][7] + color[distro.linux_distribution()[0]] + 'Language' + color["normal"] + ':', lang)
print(logo[distro.linux_distribution()[0]][8] + color[distro.linux_distribution()[0]] + 'Encoding' + color["normal"] + ':', encoding)
print(logo[distro.linux_distribution()[0]][9] + color[distro.linux_distribution()[0]] + 'Python version' + color["normal"] + ':', pythonv)
print(logo[distro.linux_distribution()[0]][10] + color[distro.linux_distribution()[0]] + 'CPU' + color["normal"] + ':', '(' + str(cpu_number) + ')', '@', str(cpu_current_clock) + 'GHz', '/', str(cpu_max_clock) + 'GHz')
print(logo[distro.linux_distribution()[0]][11] + color[distro.linux_distribution()[0]] + 'Memory' + color["normal"] + ':', convert(used_ram), '/', convert(ram), str(ram_percent) + '%')
print(logo[distro.linux_distribution()[0]][12] + color[distro.linux_distribution()[0]] + 'Swap' + color["normal"] + ':', convert(used_swap), '/', convert(swap), str(swap_percent) + '%')
print(logo[distro.linux_distribution()[0]][13] + color[distro.linux_distribution()[0]] + 'Battery' + color["normal"] + ':', batt_stat)
for i in range(14, len(logo[distro.linux_distribution()[0]])):
    print(logo[distro.linux_distribution()[0]][i])
