import bcrypt
hashed = b'$2b$12$bZAolC7AgXoglETZ0b7AZ.JcJ6p.oHXAjIrS1skOHCGaA6y//eghC'  # example from your DB
print(bcrypt.checkpw(b'jhane', hashed))  # should print True if this matches
