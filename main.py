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


def get_input(file_path=TEST_INPUTS[0]):
    """
    :returns:
    {
        total_books: 0,
        total_libraries: 0,
        total_days: 0,
        books: [7, 3, 6, 9]
        libraries:[
            {
                books: [2],
                signup: 0,
                shipping: 0
            },
        ]
    }
    """
    output = dict(
        total_books=-1, total_libraries=-1, total_days=-1, books=[], libraries=[]
    )
    line_num = (
        0  # used to track whether we are in the top 2 rows or in the library section
    )
    library_line_one = (
        True  # used to track whether we are on line 1 or line2 of each library
    )
    # library_id = 0  # used to track library ID for assignment

    with open(file_path) as data:
        while 1:
            line = data.readline()
            if not line:
                break
            line = line.split(" ")
            print(line)
            if line_num == 0:
                # First line of file = [num of diff books][num of libraries][days for scanning]
                output["total_books"] = int(line[0])
                output["total_libraries"] = int(line[1])
                output["total_days"] = int(line[2])
            elif line_num == 1:
                print(line)
                # Second line of file = [score of each book]
                output["books"] = [int(i) for i in line]
            else:
                # iterating through libraries
                if library_line_one:
                    # line: book_total, signup, shipping
                    library = dict(books=[], signup=int(line[1]), shipping=int(line[2]))
                    output["libraries"].append(library)
                else:
                    # line: [book_value_1, book_value_2]
                    current_library = len(output["libraries"]) - 1
                    output["libraries"][current_library]["books"] = [
                        int(i) for i in line
                    ]

                library_line_one != library_line_one

            line_num += 1
    return output
