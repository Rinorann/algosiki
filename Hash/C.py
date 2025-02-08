def h(g, x = 91, p = 100):
    res = 0
    for symbol in g:
        res *= x
        res += ord(symbol)
        res %= p
    return res

def search(table, key):
    kh = h(key)
    number = kh % 10
    if table[number]:
        for i in range(len(table[number])):
            if table[number][i][1] == key:
                return table[number][i][2]
        return 'KeyError'
    else:
        return 'KeyError'
