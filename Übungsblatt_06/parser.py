
def convert(list):
    tupled = tuple(map(float, list.split(' ')))
    return tupled

def parser(file):
    obj_parse = open(file,"r")
    for line in obj_parse:
        line_ = line[2:]
        parsed_ = convert(line_)
        print(parsed_)
    file.close()


obj_file = "test.obj"
parser(obj_file)
