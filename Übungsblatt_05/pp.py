def nat(n):
    yield n
    yield from nat(n+1)

def prim(n=None):
    if n == None:
        n=nat(2)
    p = next(n)
    yield p
    yield from prim(i for i in n if i%p != 0)

def pprim():
    p_gen = prim()
    p_old, p_new = next(p_gen), next(p_gen)
    while True:
        if p_old + 2 == p_new:
            yield (p_old, p_new)
        p_old, p_new = p_new, next(p_gen)