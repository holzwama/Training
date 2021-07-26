def abwechselnd(gen1, gen2):
    next1, next2 = True, True
    while next1 or next2:
        try:
            yield next(gen1)
        except StopIteration:
            next1 = False
        
        try:
            yield next(gen2)
        except StopIteration:
            next2 = False
