import os, sys

osname = os.uname()[0] + ' ' + os.uname()[1]
kernel = os.uname()[2]
arch = os.uname()[4]
encoding = os.device_encoding(0)
pythonv = sys.version[0] + sys.version[1] + sys.version[2] + sys.version[3] + sys.version[4] + sys.version[5]
cpu_number = os.cpu_count()

print('OS:', osname)
print('Architecture:', arch)
print('Kernel:', kernel)
print('Encoding:', encoding)
print('Python version:', pythonv)
print('CPU number:', cpu_number)
