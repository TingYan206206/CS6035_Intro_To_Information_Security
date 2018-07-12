
from decimal import *
p = 0
q = 0
divisor = 0;

def get_factors(n):
    global p,q
    i = int(n**(.5))
    while i >= 2:
        if n % i == 0:
            p = i
            break
        i = i - 1
    q = n/p
    # return (p,q)

def gcd(a, b):

    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)


#TODO -- n1 and n2 share p or q?
def is_waldo(n1, n2):

    global divisor
    result = False

    divisor = gcd(n1, n2)

    if divisor != 1:
        result = True


    #your code ends here

    return result


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

#TODO -- get private key of n1
def get_private_key(n1, n2, e):
    d = 0
    # divisor = gcd(n1, n2)
    n = (divisor - 1) * (n1/divisor -1)
    g, x, y = egcd(e, n)
    if g != 1:
        raise Exception('No modular inverse')
    return x % n
    #your code starts here

    #your code ends here

    # return d







def main():

    n1 = 33
    n2 = 44

    print is_waldo(n1, n2)
    print get_private_key(33, 44, 3)

    print 1.0/3

if __name__ == "__main__":
    main()