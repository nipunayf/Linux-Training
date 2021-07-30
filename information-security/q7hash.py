import sys, hashlib, os

#obtain the argument
arg = sys.argv[1]

salt = os.urandom(32)

print(hashlib.pbkdf2_hmac(
    'sha512', #digest algorithm
    arg.encode('utf-8'), #tobe converted
    salt, #salt
    200000 # iterations
))



