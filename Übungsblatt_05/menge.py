class Set(object):
    """
    docstring
    """
    def __init__(self, lis):
        if isinstance(lis, list):
            self.set = lis
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.set)

    def add(self, ele):
        if ele not in self.set:
            self.set.append(ele)