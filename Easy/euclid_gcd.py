def gcd(m, n):
    if m < n:
        m, n = n, m
    while True:
        r = m % n
        if r == 0:
            return n
        m, n = n, r 