
import base64

# 1 char = 6 bits, 4 char = 3 bytes

cipher = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

print(base64.b64encode(bytes.fromhex(cipher)))

