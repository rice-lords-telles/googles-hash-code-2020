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
#             books: [0, 1, 2, 3, 4],
#             signup: 2,
#             # books per day
#             bpd: 2
#         },
#         {
#             books: [0, 2, 3, 5],
#             signup: 3,
#             bpd: 1
#         }
#     ]
# }
TEST_INPUTS = [
    "a_example.txt",
    "b_read_on.txt",
    "c_incunbul.txt",
    "d_tough_choices.txt",
    "d_tough_choices",
    "e_so_many+books.txt",
    "f_libraries_of_the_world.txt",
]


def algorithm_template(file_path):
    """Return: Array"""
    return []


def get_input():
    """
    :returns:
    {
        total_books: 0,
        total_libraries: 0,
        total_days: 0,
        books: [7, 3, 6, 9]
        library_id:[
            {
                books: [2],
                signup: 0,
                shipping: 0
            },
        ]
    }
    """
    line_num = (
        1  # used to track whether we are in the top 2 rows or in the library section
    )
    library_line_one = (
        True  # used to track whether we are on line 1 or line2 of each library
    )
    library_id = 0  # used to track library ID for assignment

    with open("a_example.txt") as data:
        line = data.readline()
        if line_num == 1:
            # First line of file = [num of diff books][num of libraries][days for scanning]
            total_books = line.split(" ", 0)
            total_libraries = line.split(" ", 1)
            total_days = line.split(" ", 2)
        elif line_num == 2:
            # Second line of file = [score of each book]
            books = [int(i) for i in line.split()]
        else:
            # iterating through libraries
            if library_line_one:
                # first line of library
                library_id = {"books": []}
                library_line_one != library_line_one
            else:
                # second line of library
                library_line_one != library_line_one

        line_num += 1
