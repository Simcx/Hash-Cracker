# Introduction

A password cracker is used to resolve passwords from hashes or guess them based on the behavior of a webpage's response. They may be used by ethical hackers when performing penetration tests. While many password cracking tools exist such as THC Hydra, hashcat, and John the Ripper, it is important to know how they work should you ever have the need to create one of your own. In this example, we will be creating a cracker that resolves hashes from input to plaintext as output using a wordlist in what is known as a **dictionary attack**.

Note: This is only for educational purposes and any and all malicious activity is highly discouraged. Only use this tool on yourself and/or those who have granted you permission to do so.

## Requirements

- Python 3 installed
- any IDE (You can even use Notepad++)
# How it Will Work

A **wordlist** is just that -- a list of words, each on their own, separate line. Like this:

```txt
cat
dog
bird
tree
house
```

There are widely known ones out there like rockyou.txt, SecLists, dirb wordlists, etc., and which one you use depends on what you are doing as an ethical hacker. Programs that take a wordlist will iterate through it (that means we'll be using a loop in our code) and use that specific word somehow. 

A **hash** is what is used to protect passwords and maintain data integrity. When you first register an account to a website, that website (hopefully) will not store your password in plaintext. If something were to happen such as a data breach, the hash will be a line of defense for your password not to be exposed (that is, unless you use a bad password, in which it will be cracked easily). When you log in and enter your password, the input password you entered will be hashed and compared to the password hash of the username you entered. If there is a match, you will be logged in.

In this case, we will **hash** each word we iterate through and compare them to the target hash (the one we use as input), and if we find a match, we'll output the plaintext password. The final project will look like this:

![Screenshot 2025-04-27 183104](https://github.com/user-attachments/assets/bb7771cc-3140-4c91-ac63-1ec744a509c6)


We will be using Python's `hashlib` library. You don't need to install it with `pip`, it is a standard library in Python.

`hashlib` allows you to work with hashes like MD5, SHA256, etc. We will be working with SHA256 in our project.

# Programming

First we need to import the module `hashlib` and define the function that will crack the password. it will take one argument: the hash that we want to crack.

```python
import hashlib

def crack_password(hashed_pass):
```

Inside that function we have to read our wordlist. Here is the wordlist I am using:

```txt
123456
password
12345678
qwerty
123456789
12345
1234
111111
1234567
dragon
baseball
abc123
football
monkey
letmein
696969
shadow
master
666666
qwertyuiop
123321
mustang
1234567890
michael
654321
superman
1qaz2wsx
7777777
121212
000000
qazwsx
123qwe
killer
trustno1
jordan
jennifer
zxcvbnm
asdfgh
hunter
buster
soccer
harley
batman
andrew
tigger
sunshine
iloveyou
2000
charlie
robert
thomas
hockey
ranger
daniel
starwars
klaster
112233
george
computer
michelle
jessica
pepper
1111
zxcvbn
555555
11111111
131313
freedom
777777
pass
maggie
159753
aaaaaa
ginger
princess
joshua
cheese
amanda
summer
love
6969
nicole
chelsea
biteme
matthew
access
yankees
987654321
dallas
austin
thunder
taylor
matrix
the
password
treetop
mypassword
s3v3nf0rty
aw3s0m3p@$$w0rd
```

We can use the `open()` built-in Python function and make it a variable with the `with` keyword:

```python
with open('wordlist.txt', 'r') as file:
```

Now we can loop through each word with a for loop. Here is what the entire thing should look like now:

```python
import hashlib

def crack_password(hashed_pass):
    with open('wordlist.txt', 'r') as file:
        for word in file:
```

We want to go through each word in the wordlist, hash it, then compare it to our target hash. If they are equal, we will return a match. If not, we keep going. Below, we use `encode()` and `hexdigest()` to get the SHA256 value in what is called a **digest**:

```python
for word in file:
	hashed = word.strip()
	if hashlib.sha256(hashed.encode()).hexdigest() == hashed_pass:
	    return f'\nMatch for hash {hashed_pass} : {hashed}'
```

The `strip()` method is very important in our `hashed` variable assignment because without it, our `hashed` variable will contain `'value\n'`. The `\n` will produce a different hash, which will make all of the values wrong even if there is a word in our list that could be the match.

`'pepper' -> 8cbbcf29d9cef89675c5f5c1dcfe827d0570416a5aaba30dd0de159661ad905b`
`'pepper\n' -> f44eb291149cb8bd1441bdfa5aa57e9807d03074a5245f666ebec1188330983b`

If our wordlist gets exhausted (all iterations do not match), then we return a message saying so:

```python
with open('wordlist.txt', 'r') as file:
        for word in file:
            hashed = word.strip()
            if hashlib.sha256(hashed.encode()).hexdigest() == hashed_pass:
                return f'\nMatch for hash {hashed_pass} : {hashed}' # Match
    return f'\nNo match found in given wordlist for {hashed_pass}' # No match
```
Here is the final product:
```python
# Standard Library Imports
import hashlib

def crack_password(hashed_pass):
    with open('wordlist.txt', 'r') as file:
        for word in file:
            hashed = word.strip()
            if hashlib.sha256(hashed.encode()).hexdigest() == hashed_pass:
                return f'\nMatch for hash {hashed_pass} : {hashed}'
    return f'\nNo match found in given wordlist for {hashed_pass}'
```

You can test this out by giving it arguments that are and are not found in the wordlist. The function needs a hash to properly work, so don't forget to hash it:
```python
print(crack_password(hashlib.sha256('letmein'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('aw3s0m3p@$$w0rd'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('notinwordlist'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('dallas'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('alsonotinwordlist'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('starwars'.encode()).hexdigest()))
print(crack_password(hashlib.sha256('pepper'.encode()).hexdigest()))
```
You can run it by opening the cmd and `cd`ing to the directory in which your python script and wordlist are found.

Again, this is only for ethical, educational purpose. Do not use this under any other circumstances, or it is possible you can face legal consequences.
