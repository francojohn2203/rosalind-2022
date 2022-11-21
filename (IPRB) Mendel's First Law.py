def iprb(k, m, n):
    i = m * m + 4 * n * n + 4 * m * n - 4 * n - m
    j = 4 * (k + m + n) * (k + m + n - 1)
    rst = 1 - float(i) / j
    return rst

if __name__ == "__main__":
    with open("rosalind_iprb.txt", 'r') as f:
        k, m, n = map(int, f.readline().strip().split(" "))
        print(iprb(k, m, n))