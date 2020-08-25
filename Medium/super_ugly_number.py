def nthSuperUglyNumber(n, primes):
        uglies=[1]
        indexes=[0]*len(primes)
        while len(uglies)<n:
            # for index,prime in enumerate(primes):
            out=[prime*uglies[indexes[index]] for index,prime in enumerate(primes)]
            uglies.append(min(out))
            for index,prime in enumerate(primes):
                if uglies[indexes[index]]*prime==uglies[-1]:
                    indexes[index]+=1
        return uglies[-1]
