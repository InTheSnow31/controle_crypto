from attacks import *

# generates randomly, a sakado of length n (it is a list of int)
# with density <= 1/D
def generate_sac(n, D):
    sac = []
    maxnumberofbits = floor(n*D)
    for i in range(n):
        sac += [randint(1, 2**maxnumberofbits)]
    return sac

# generates randomly, a string of characters 0,1 of length n,
def generate_bin(n):
    bst = ""
    for i in range(n):
        coin = randint(0, 1)
        if coin == 0:
            bst += "0"
        else:
            bst += "1"
    return bst


if __name__ == "__main__":
    print("debut")
    w = generate_bin(20)
    sac = generate_sac(20, 3/2)
    sum = bin2int_via_sac(w, sac)
    ww = lll_solution(sac, sum)
    bfw = brutef_solution(sac, sum)
    print("the sac", sac)
    print("the sum", sum)
    print("the initial bin word", w)
    print("the lll computed bin word", ww)
    print("the bruteforce solution", bfw)
    print("fin")

# experimenter les attaques par LLL sur des problemes de sac a dos

# experimenter les attaques par LLL sur l'implementation du protocole de Merkle-Hellman

# experimenter les attaques par brute-force
