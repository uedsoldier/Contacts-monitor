import bcrypt
import sys
import errno

password = sys.argv[1]
salt_rounds = (int)(sys.argv[2])

if(salt_rounds < 10 and salt_rounds > 20):
    print('Salt rounds deben estar en el rango [10,20]')
    sys.exit(errno.EINVAL)
else:
    print('Salt rounds: ',salt_rounds)
    password_encoded = password.encode('utf-8')
    print('Password codificado: ',password_encoded)
    seed = bcrypt.gensalt(salt_rounds)
    print('Semilla (seed): ',seed)
    hashed = bcrypt.hashpw(password_encoded,seed)
    print('Password codificado y cifrado: ',hashed)
    sys.exit(0)