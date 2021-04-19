import os, sys

print('OS:', os.uname()[0], os.uname()[1])
print('Encoding:', os.device_encoding(0))
print('CPU number:', os.cpu_count())
