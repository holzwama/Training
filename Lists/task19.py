

print_list = ["Hello", "Worlddsadadad", "in", "a", "frame"]

def printing(list_):
    length_ = len(list_)
    size = max(list_, key = len)
    border_ = len(size)
    counter = 0
    if counter == 0:
         print('*' * (border_ + 2))
    while counter <= (length_ - 1):
        print("*" + list_[counter] + "*")
        
        counter += 1
    if counter == length_:
        print('*' * (border_ + 2))

printing(print_list)