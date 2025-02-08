def h(g, x = 91, p = 100):
    res = 0
    for symbol in g:
        res *= x
        res += ord(symbol)
        res %= p
    return res
def insert(table, key, value):
    kh = h(key)
    number = kh % 10
    if table[number]:
        for j in range(len(table[number])):
            if table[number][j][1] == key:
                table[number][j][2] = value
                break
        else:
            table[number].append([kh, key, value])
    else:
        table[number].append([kh, key, value])



n = int(input())
hash_table = [[] for _ in range(10)]
for i in range(n):
    init = input().split()
    insert(hash_table, init[0], init[1])
for i in range(10):
    if hash_table[i]:
        print(i)
        for k in range(len(hash_table[i])):
            print(*hash_table[i][k])


