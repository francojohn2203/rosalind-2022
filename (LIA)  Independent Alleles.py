def binomial(k, n):
    if k > n - k:
        k = n - k

    total = 1
    for i in range(1, k + 1):
        total *= (n - (k - i))
        total /= i

    return total


def prob(k, n):
    return binomial(n, 2**k) * 0.25**n * 0.75**(2**k - n)


def getProb(k, n):
    
    return 1 - sum(prob(k, i) for i in range(n))


def main():
   
    with open('rosalind_lia.txt', 'r') as infile:
        k, n = map(int, infile.read().strip().split(' '))

    print('%.3f' % getProb(k, n))


if __name__ == '__main__':
    main()