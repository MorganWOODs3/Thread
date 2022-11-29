import os

ip = input('ip :')
os.system(('ping -n 4 {}'.format(ip)))

