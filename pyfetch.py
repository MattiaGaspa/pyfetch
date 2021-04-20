#!/usr/bin/python3
import os, sys, psutil

username = os.environ['USER']
osname = os.uname()[0] + ' ' + os.uname()[1]
arch = os.uname()[4]
kernel = os.uname()[2]
def uptime():
    time = int(float(open('/proc/uptime').read().split(' ')[0]) - (float(open('/proc/uptime').read().split(' ')[0]) % 1))
    d = int(time / 86400)
    h = int(time / 3600 % 24)
    m = int(time / 60 % 60)

    uptime = ''
    if d > 1:
        uptime += str(d) + ' days '
    if h > 1:
        uptime += str(h) + ' hours '
    if m > 1:
        uptime += str(m) + ' mins '
    return uptime
shell = os.environ['SHELL']
editor = os.environ['EDITOR']
lang = os.environ['LANGUAGE']
encoding = os.device_encoding(0)
pythonv = sys.version[0] + sys.version[1] + sys.version[2] + sys.version[3] + sys.version[4] + sys.version[5]
cpu_number = os.cpu_count()
ram = psutil.virtual_memory().total
used_ram = psutil.virtual_memory().used
swap = psutil.swap_memory().total
used_swap = psutil.swap_memory().used
def convert(bytes):
    unitIndex = 0
    units = ['B','KB','MB','GB','TB']
    while 1000 <= bytes:
        bytes /= 1000
        unitIndex += 1
    return f"{round(bytes)}{units[unitIndex]}"

color = {
    'normal': '\u001b[00;0m',
    'gentoo': '\u001b[35;1m'
}
logo = {
    'gentoo': [
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
        '  \u001b[35;1m`-//////:--.\u001b[00;1m\t\t\t\t'
    ]
}

print(logo[os.uname()[1]][0] + color[os.uname()[1]] + username + color["normal"] + '@' + color[os.uname()[1]] + os.uname()[1] + color["normal"])
print(logo[os.uname()[1]][1] + ('-' * len(username + '@' + os.uname()[1])))
print(logo[os.uname()[1]][2] + color[os.uname()[1]] + 'OS' + color["normal"] + ':', osname, arch)
print(logo[os.uname()[1]][3] + color[os.uname()[1]] + 'Kernel' + color["normal"] + ':', kernel)
print(logo[os.uname()[1]][4] + color[os.uname()[1]] + 'Uptime' + color["normal"] + ': %s' % uptime())
print(logo[os.uname()[1]][5] + color[os.uname()[1]] + 'Shell' + color["normal"] + ':', shell)
print(logo[os.uname()[1]][6] + color[os.uname()[1]] + 'Editor' + color["normal"] + ':', editor)
print(logo[os.uname()[1]][7] + color[os.uname()[1]] + 'Language' + color["normal"] + ':', lang)
print(logo[os.uname()[1]][8] + color[os.uname()[1]] + 'Encoding' + color["normal"] + ':', encoding)
print(logo[os.uname()[1]][9] + color[os.uname()[1]] + 'Python version' + color["normal"] + ':', pythonv)
print(logo[os.uname()[1]][10] + color[os.uname()[1]] + 'CPU number' + color["normal"] + ':', cpu_number)
print(logo[os.uname()[1]][11] + color[os.uname()[1]] + 'Memory' + color["normal"] + ':', convert(used_ram) + '/' + convert(ram))
print(logo[os.uname()[1]][12] + color[os.uname()[1]] + 'Swap' + color["normal"] + ':', convert(used_swap) + '/' + convert(swap))
for i in range(13, len(logo[os.uname()[1]])):
    print(logo[os.uname()[1]][i])
