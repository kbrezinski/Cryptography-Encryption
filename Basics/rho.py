
import hashlib

h = 'password'

for i in range(120):
    h = hashlib.new('md5', h.encode('ascii')).hexdigest()[-3:]
    print(h, end=' ')
