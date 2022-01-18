import bcrypt
import sys

password = sys.argv[1]
hash = sys.argv[2]

password_encoded = password.encode('utf-8')
hash_encoded = hash.encode('utf-8')
print('Password codificado: ',password_encoded)
print('Hash codificado: ',hash_encoded)

if bcrypt.checkpw(password_encoded,hash_encoded):
    print('Password match!!')
else:
    print('Password mismatch')