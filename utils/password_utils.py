# Handles password from string to hashed

import bcrypt

# The password you want to hash
password = ""

# Generate the salt and hash the password
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# hashed is a bytes object, so decode it to string if you want to store or print it nicely
hashed_str = hashed.decode('utf-8')

print("Hashed password:", hashed_str)

