#!/usr/bin/python
import json, sys, hashlib
import fractions

p = 0
q = 0
divisor = 0
def usage():
    print """Usage:
    python find_waldo.py student_id (i.e., qchenxiong3)"""
    sys.exit(1)

#TODO -- n1 and n2 share p or q?
def is_waldo(n1, n2):


    global divisor
    result = False

    divisor = fractions.gcd(n1, n2)

    if divisor != 1:
        result = True


    #your code ends here

    return result

# Euclid's algorithm to get modular inverse
def egcd(a, b):
    # base case
    if a == 0:
        return (b, 0, 1)

    #recursive call
    g, y, x = egcd(b % a, a)

    return (g, x - (b//a) * y, y)

#TODO -- get private key of n1
def get_private_key(n1, n2, e):
    d = 0

    n = (divisor - 1) * (n1/divisor -1)
    g, x, y = egcd(e, n)
    if g != 1:
        raise Exception('No modular inverse')
    return x % n


def main():
    if len(sys.argv) != 2:
        usage()

    all_keys = None
    with open("keys4student.json", 'r') as f:
        all_keys = json.load(f)

    name = hashlib.sha224(sys.argv[1].strip()).hexdigest()
    if name not in all_keys:
        print sys.argv[1], "not in keylist"
        usage()

    pub_key = all_keys[name]
    n1 = int(pub_key['N'], 16)
    e = int(pub_key['e'], 16)
    d = 0
    waldo = "dolores"

    print "your public key: (", hex(n1).rstrip("L"), ",", hex(e).rstrip("L"), ")"

    for classmate in all_keys:
        if classmate == name:
            continue
        n2 = int(all_keys[classmate]['N'], 16)

        if is_waldo(n1, n2):
            waldo = classmate
            d = get_private_key(n1, n2, e)
            break
    
    print "your private key: ", hex(d).rstrip("L")
    print "your waldo: ", waldo


if __name__ == "__main__":
    main()
