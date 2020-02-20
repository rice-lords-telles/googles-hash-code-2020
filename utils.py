from tqdm import tqdm

TEST_INPUTS = [
    "a_example.txt",
    "b_read_on.txt",
    "c_incunabula.txt",
    "d_tough_choices.txt",
    "d_tough_choices.txt",
    "e_so_many_books.txt",
    "f_libraries_of_the_world.txt",
]


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
                total_books: 0,
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
        0  # used to track whether we are in the top 2 rows or in the library section
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
                # First line of file = [num of diff books][num of libraries][days for scanning]
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
                        shipping=int(line[2]),
                    )
                    output["libraries"].append(library)
                else:
                    # line: [book_value_1, book_value_2]
                    current_library = len(output["libraries"]) - 1
                    output["libraries"][current_library]["books"] = [
                        int(i) for i in line
                    ]

                library_line_one = not library_line_one

            line_num += 1
    return output


def write_output_to_files(output, input_file_name):
    output_path = "{}.out.txt".format(input_file_name)
    with open(output_path, "w") as descriptor:
        for items in output:
            if not items:
                break
            descriptor.write(" ".join(str(x) for x in items))
