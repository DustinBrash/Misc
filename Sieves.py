def Ero(ceiling):
    table = [True for x in xrange(ceiling + 1)]
    end = int(ceiling ** .5) + 1
    for i in xrange(end):
        if not table[i] or i < 2:
            continue
        table[i * 2::i] = [False for x in range(len(table[i * 2::i]))]
    out = [n for n, i in enumerate(table) if i]
    return out
        

def At(ceiling):
    a, b, c = [1, 13, 17, 29, 37, 41, 49, 53], [7, 19, 31, 43], [11, 23, 47, 59]
    sieve, results = [False for n in xrange(1, ceiling +1)], [2, 3, 5]
    for n in xrange(1, ceiling + 1):
        for x in xrange(1, int(n ** .5) + 1):
            for y in xrange(1, int( n ** .5) + 1):
                if n % 60 in a:                
                    if (4 * (x ** 2) + (y ** 2)) == n:                    
                        sieve[n] = not sieve[n]
                elif n % 60 in b:
                    if (3 * (x ** 2) + (y ** 2)) == n:
                        sieve[n] = not sieve[n]
                elif n % 60 in c:
                    if (3 * (x ** 2) - (y ** 2)) == n:
                        sieve[n] = not sieve[n]
    for n in xrange(1, ceiling):
        if sieve[n]:            
            results.append(n)
            sieve[n ** 2:: n ** 2] = [False for i in xrange(len(sieve[n ** 2:: n ** 2]))]
    return results
