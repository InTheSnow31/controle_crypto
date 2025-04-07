from random import randint
from merkle import *
from lll import *

# sakado is a list of n int, s an int
# returns the encoding of this problem into an euclidean lattice
# represented as 2-dim array; lines form a free family of R^{n+2}
# there are n+1 lines
def sakado2base(sakado: list, s: int):
    # TODO TODO TODO
    # construire la base qui encode le sac a dos
    # suivre l'idee de Lagarias-Odlyzenko
    return base

# sac=[2,6,18,23,98]
# sacb=sakado2base(sac,122)
# print(sacb)

# n is the length of the sakado
# test that a vector of length n+2 is a solution of a sakado problem
def accept(n: int, vec: array):
    ok = True
    for i in range(n+2):
        if not (vec[i] in [0, 1]):
            ok = False
    if (vec[n] != 1 or vec[n+1] != 0):
        ok = False
    return ok


# returns a list of vectors int 0,1
# uses LLL algo
# selects the base-vectors encoding a solution to the sakado problem
def small_vec1(sakado: list, s: int):  # n is length of sakado
    base = sakado2base(sakado, s)
    # Lagarias reduction inserts one more line-vector in the base
    n = len(base)-1
    rbase = LLL(base)
    lcandidates = []
    for vec in rbase:
        if accept(n, vec):
            lcandidates.append(vec)
    return array(lcandidates)


# sakado is a list of n int
# returns a string of n characters 0,1 or the answer "failure"
# sol based on LLL algorithm by Lagarias-Odlyzko method
def lll_solution(sakado: list, s: int):
    tentative = small_vec1(sakado, s)
    if len(tentative) == 0:
        return "failure"
    else:
        return vec2binstring(tentative[0])[:-2]


# auxiliary function for brute-force solution
# treats the subsequence of sakado from debut to fin (both included)
# returns a list of integers in 0,1 or None if no solution
def bf_sol(sakado: list, debut: int, fin: int, s: int):
    #  TODO TODO TODO
    # affecter a lint une liste d'entiers (dans {0,1} )
    # qui est une solution au problem du sac a dos pour l'entier s
    # et la liste des entiers d'indice entre debut et fin
    return lint


# sakado is a list of n int
# returns a string of n characters 0 1 or the answer "failure"
# brute-force solutions
def brutef_solution(sakado: list, s: int):
    n = len(sakado)
    vec = bf_sol(sakado, 0, n-1, s)
    if vec:
        return vec2binstring(vec)
    else:
        return ("failure")


# pk is a list of int
# m is an int
# returns a string of characters which is encrypted into m by key pk
# does NOT use the SECRET key
def llldecrypt(pk: list, m: int):
    binsol = lll_solution(pk, m)
    if binsol == "failure":
        return binsol
    else:
        return bin2string(binsol)
