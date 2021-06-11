from pathlib import Path

file = open("Test_python.txt","rt")

def pathname(path):
    path_name = Path(path).stem
    return path_name


print(file.read())

file.close()