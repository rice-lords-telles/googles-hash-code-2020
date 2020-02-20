# INPUT

# 6 2 7 - 6 books, 2 libraries, 7 days of scanning
# 1 2 3 6 5 4 - scores of the books (in order)
# 5 2 2 - Lib0 has 5 books, signup takes 2 days, can ship 2 books per day
# 0 1 2 3 4 - books in Lib0
# 4 3 1 - Lib1 has 4 books, signup takes 3 days, can ship 1 book per day
# 0 2 3 5 - books in Lib1

# OUTPUT

# 2 - Two libraries signed up for scanning
# 1 3 - First library to signup is Lib1, after signup, send 3 books to scan
# 5 2 3 - Lib1 will send book 5, book 2, book 3 in order
# 0 5 - Second library to sign up is Lib0, after signup, send 5 books
# 0 1 2 3 4 - Lib0 will send book 0, 1, 2, 3, 4 in order

# Get File info
def get_input(file_name):
    capacity = None
    pizza_type = None
    with open(file_name) as descriptor:
        print("reading file")
        line = descriptor.readline().split(" ")
        capacity = int(line[0])
        pizza_types = descriptor.readline().split(" ")
        print("got types")
        pizza_types = [int(item) for item in pizza_types]
        print("converted types")
    return capacity, pizza_types
