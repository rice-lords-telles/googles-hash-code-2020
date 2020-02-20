from tqdm import tqdm
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Possible Data Structure
# {
#     total_books: 6,
#     total_libraries: 2,
#     total_days: 7,
#     book_scores: [1, 2, 3, 6, 5, 4],
#     library_id: [
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


def get_input(file_path):
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
        total_books=-0, total_libraries=0, total_days=0, books=[], libraries=[]
    )
    line_num = (
        # used to track whether we are in the top 2 rows or in the library
        # section
        0
    )
    library_line_one = (
        True  # used to track whether we are on line 1 or line2 of each library
    )

    with open(file_path) as data:
        num_lines = sum(1 for line in open(file_path))

        for num in tqdm(range(num_lines)):
            line = data.readline().strip()
            if not line:
                break
            line = line.strip().split(" ")
            if line_num == 0:
                # First line of file:
                # [num of diff books][num of libraries][days for scanning]
                output["total_books"] = int(line[0])
                output["total_libraries"] = int(line[1])
                output["total_days"] = int(line[2])
            elif line_num == 1:
                # Second line of file = [score of each book]
                output["books"] = [int(i) for i in line]
            else:
                # iterating through libraries
                if library_line_one:
                    # line: book_total, signup, shipping
                    library = dict(
                        total_books=int(line[0]),
                        books=[],
                        signup=int(line[1]),
                        shipping=int(line[2]))
                    output["libraries"].append(library)
                else:
                    # line: [book_value_1, book_value_2]
                    current_library = len(output["libraries"]) - 1
                    output["libraries"][current_library]["books"] = [
                        int(i) for i in line
                    ]

                library_line_one = not library_line_one

            line_num += 1

    lib_0 = output['libraries'][0]
    lib_1 = output['libraries'][1]
    total_days = output['total_days']
    total_libraries = output['total_libraries']

    lib_0_days = lib_0['signup'] + (lib_0['total_books'] - lib_0['shipping'])
    lib_1_days = lib_1['signup'] + (lib_1['total_books'] - lib_1['shipping'])

    # return output
    return (lib_0_days + lib_1_days - total_days) / total_libraries

print(get_input("a_example.txt"))
