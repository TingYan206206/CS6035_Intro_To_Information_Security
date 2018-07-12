def get_factors(n):
    p = 0
    q = 0

    # your code starts her
    i = int(n ** (.5))
    while i > 0:
        if n % i == 0:
            p = i
            break
        i = i - 1
    q = n / p
    return p, q


def get_key(p, q, e):
    d = 0

    N = (p-1)*(q-1)
    while d <= N:
        if (d * e) % N == 1:
            break
        d = d + 1

    # your code starts here


    # your code ends here
    return d

def main():
    n = 33
    # print 33**(.5)
    (p, q) = get_factors(n)

    print p, q

    d = get_key(p, q, 7)

    print d

if __name__ == "__main__":
    main()