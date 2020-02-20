from utils import get_input, TEST_INPUTS, write_output_to_files
from collections import OrderedDict
from brute_force import as_they_come_algorithm

# can you see this?

# can you edit this

# This is Roy

# hello hello

# Possible Data Structure
# {
# total_books: 0,
# total_libraries: 0,
# total_days: 0,
# books: [7, 3, 6, 9]
#     libraries:[
#         {
#             total_books: 0
#             books: [],
#             signup: 0,
#             shipping: 0
#         }],
#        ...
# }

# Example
# {
#     total_books: 6,
#     total_libraries: 2,
#     total_days: 7,
#     book_scores: [1, 2, 3, 6, 5, 4],
#     libraries:[
#         {
#             total_books: 5
#             books: [0, 1, 2, 3, 4],
#             signup: 2,
#             # books per day
#             bpd: 2
#         },
#         {
#             total_books: 5
#             books: [0, 2, 3, 5],
#             signup: 3,
#             bpd: 1
#         }
#     ]
# }


def set_lib_priority(all_data):
    """Return array with priority for each library
        priority = (signup day cost/total days available) / (num of books/books per day)
        This will give us a value and the largest value is what we want to start with.
        Protected against divide by 0 errors because input is guaranteed to be at least 1
    """
    lib_priority = {}
    # lib_priority_arr = [all_data['total_libraries']]
    lib_index = 0

    for lib in all_data["libraries"]:
        signup = lib["signup"]
        total_days = all_data["total_days"]
        book_in_lib = lib["total_books"]
        books_per_day = lib["bpd"]

        priority = (signup / total_days) / (books_in_lib / books_per_day)

        lib_priority[lib_index] = priority

        lib_index += 1

        sorted_lib_priority = OrderedDict(sorted(lib_priority.items()))

    return sorted_lib_priority


def book_score(all_data):
    book_priority = {}
    lib_index = 0

    for lib in all_data["libraries"]:
        for book in lib[books]:
            book_priority[lib_index]

    return sorted_book_priority


def lib_picker(lib_dict):
    num_libraries = 0
    lib_id = None
    num_books_to_send = 0
    books_sent = None


def algorithm_template(file_path):
    """Return: Array"""
    return []


def main():
    os.mkdir
    # all_data = get_input()
    for input_file in TEST_INPUTS:
        data = get_input(input_file)
        output = as_they_come_algorithm(data)
        write_output_to_files(
            output, "output/" + input_file + as_they_come_algorithm.__name__
        )
    # lib_priority_dict = set_lib_priority(all_data)
    # book_priority_dict = book_score(all_data)
    # lib_picker(lib_priority_dict)


if __name__ == "__main__":
    main()
