#!/usr/bin/python
import json, sys, hashlib
from decimal import *

def usage():
    print """Usage:
    python recover.py student_id (i.e., qchenxiong3)"""
    sys.exit(1)


#TODO
def recover_msg(N1, N2, N3, C1, C2, C3):

    # m = 42
    # your code starts here: to calculate the original message - m
    # Note 'm' should be an integer
    
    # convert the int to message string
    getcontext().prec = 1000
    getcontext().rounding = ROUND_UP

    m = long(pow(C1, Decimal(1) / Decimal(3)))
    msg = hex(m).rstrip('L')[2:].decode('hex')
    return msg

def main():
    if len(sys.argv) != 2:
        usage()

    all_keys = None
    with open('keys4student.json', 'r') as f:
        all_keys = json.load(f)

    name = hashlib.sha224(sys.argv[1].strip()).hexdigest()
    if name not in all_keys:
        print sys.argv[1], "not in keylist"
        usage()

    data = all_keys[name]
    N1 = int(data['N0'], 16)
    N2 = int(data['N1'], 16)
    N3 = int(data['N2'], 16)
    C1 = int(data['C0'], 16)
    C2 = int(data['C1'], 16)
    C3 = int(data['C2'], 16)
    
    msg = recover_msg(N1, N2, N3, C1, C2, C3)
    print msg
    
if __name__ == "__main__":
    main()
