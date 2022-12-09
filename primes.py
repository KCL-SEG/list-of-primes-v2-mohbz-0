#
#
# Abdurrahmaan Mohabbat
# 09/12/2022
# List Of Primes Generator
#

def primes(num):
    if num < 1:
        raise ValueError('Input Too Low. Input number greater than 0')
    primeList = []
    for c in range(num):
        if len(primeList) == 0:
            i = 1
        else:
            i = primeList[len(primeList)-1]
        run = True
        while run:
            i+=1
            for d in range(i):

                if d == 0:
                    pass
                elif d+1 == i:
                    primeList.append(i)
                    run = False
                    break
                elif (i % (d+1)) == 0:
                    break
    return primeList
