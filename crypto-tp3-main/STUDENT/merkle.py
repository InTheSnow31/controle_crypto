from random import randint
from numpy import *

# global parameters
maxcharacters = 10  # 200 (length of messages overs ASCII code)
maxbinarylength = maxcharacters*8  # each character translates into a 8 bits word

# extended gcd
# returns (gcd(a,b),u,v) such that
# gcd(a,b)=au+bv
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# assume a, m are co-prime
# returns the inverse of a modulo m
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return (x % m)

# w is a string of characters
# returns its translation into a string of 0,1 of length maxbinarylength
# returns "0"^maxbinarylength if w is too long.
def word2bin(w: str):
    binarym = ""
    if len(binarym) > maxbinarylength:
        binarym = "0"
        print("votre message est trop long")
    for letter in w:
        # erase the leading "0b"
        # normalize to 8 bits
        binarym += (bin(ord(letter)).lstrip("0b")).zfill(8)
    # completes up to max length by zeros on the left
    binarym = binarym.zfill(maxbinarylength)
    return binarym

# print("a",word2bin("a"))
# print("abc", word2bin("abc"))

# bw is a string of characters 0,1
# returns its translation into a string of characters
def bin2string(bw: str):
    string = ""
    for i in range(0, len(bw), 8):
        letter = bw[i:i+8]
        valletter = int(letter, 2)
        if valletter != 0:
            string += chr(valletter)
    return string

# translates an array of integers in 0,1 into a string of characters in 0,1
def vec2binstring(vec: array):
    word = ""
    for num in vec:
        if num == 0:
            word += "0"
        if num == 1:
            word += "1"
    return word

# w is a string of characters 0,1
# sakado is a list of int
def bin2int_via_sac(w: str, sakado: list):
    assert (len(w) == len(sakado))
    sum = 0
    for i in range(0, len(w)):
        sum += sakado[i]*int(w[i], 2)
    return sum

# returns a decomposition of s over the list of integers sakado
# the decomposition is a string of characters 0 1 of same length as sakado
# or none if no decomposition exists
# sakado is a super-increasing sequence of int
def greedy_solution(sakado: list, s: int):
    # TODO TODO TODO
    # l'algoritme glouton vu en TD
    # produit une chaine de caracteres
    return sol


class MerkleHellman:

    def __init__(self):
        self.sk = []  # Private (= secret) Key= list of integers
        self.M = 0  # greater than all private key elements
        self.q = 0  # the multiplier; co-prime with M
        self.pk = []  # Public Key
        self.generate_keys()
        print("Public key: ", self.pk)
        print("Private key: ", self.sk)

    def generate_keys(self):
        maxnumberofbits = 8  # 50
        sum = 0
        # TODO TODO TODO
        # affecter a self.sk une liste d'entiers super-sroissante
        self.M = sum + randint(1, 2**maxnumberofbits)
        self.q = self.M-1
        # compute the public key from the private key
        for i in range(maxbinarylength):
            self.pk.append((self.sk[i]*self.q) % self.M)

    # message is a string of characters
    # returns an integer
    def encrypt(self, message):
        # binarymessage= string of 0,1
        binarymessage = word2bin(message)
        print("Binary message: ", binarymessage)
        # TODO TODO TODO
        # affecter a cipher l'entier qui encode le message chiffre
        return cipher

    # cipher is an integer
    # returns a string of characters
    def decrypt(self, cipher):
        binarystring = ""
        cipherint = cipher
        modularinverse = modinv(self.q, self.M)
        # the integer to be decomposed over the secret key
        inversecipher = (cipherint*modularinverse) % self.M
        # decompose the integer
        # TODO TODO TODO
        # affecter a binarystring la decomposition de inversecipher
        # sur le sac a dos
        print("Binary message: ", binarystring)
        # convert into characters
        return bin2string(binarystring)


if __name__ == "__main__":
    protocol = MerkleHellman()
    message = input("Enter plain text to be encrypted:\n > ")
    encrypted = protocol.encrypt(message)
    print("Encrypted message: ", encrypted)
    decrypted = protocol.decrypt(encrypted)
    print("Decrypted message: ", decrypted)
