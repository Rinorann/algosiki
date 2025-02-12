def h(txt):
    res = 0
    for symbol in txt:
        res = (res * x + ord(symbol)) % p
    return res

def rabin_karp(s, g):
    n = len(g)
    m = len(s)
    if m > n:
        return -1  

    ref = h(s)  
    current_hash = h(g[:m])  

    

    flag = False
    for i in range(n - m + 1):
        if current_hash == ref:
            if g[i:i+m] == s:
                print(i, end=' ')
                flag = True

        if i < n - m:
            current_hash = (current_hash - ord(g[i]) * pow(x, m - 1)) % p 
            current_hash = (current_hash * x + ord(g[i + m])) % p 

    if not flag:
        print(-1)
    else:
        print()  
x = 69
p = 1000
s = input()
g = input()

rabin_karp(s, g)
