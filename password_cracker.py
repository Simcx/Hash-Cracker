# Standard Library Imports
import hashlib

def crack_password(hashed_pass):
    with open('wordlist.txt', 'r') as file:
        for word in file:
            hashed = word.strip() # use strip() method or \n will be included in the variable and hash. Not good
            if hashlib.sha256(hashed.encode()).hexdigest() == hashed_pass:
                return f'\nMatch for hash {hashed_pass} : {hashed}'
    return f'\nNo match found in given wordlist for {hashed_pass}'

# Test cases

print(crack_password(hashlib.sha256('letmein'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('aw3s0m3p@$$w0rd'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('notinwordlist'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('dallas'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('alsonotinwordlist'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('starwars'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('pepper'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('pepper\n'.encode()).hexdigest()))