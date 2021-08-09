import sys, hashlib

#obtain the argument
arg = sys.argv[1]

salt = b"Km5d5ivMy8iexuHcZrsD"

print(hashlib.pbkdf2_hmac(
    'sha512', #digest algorithm
    arg.encode('utf-8'), #tobe converted
    salt, #salt
    200000 # iterations
).hex())



