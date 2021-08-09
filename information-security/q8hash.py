import sys, hashlib, os

#obtain the argument
arg = sys.argv[1]

salt = os.urandom(32)

print(hashlib.sha512(arg.encode('utf-8')+salt).hexdigest())


