"""
The "brute force" approach in this is just make sure we do _something_.
{
    total_books: 0,
    total_libraries: 0,
    total_days: 0,
    books: [7, 3, 6, 9]
    libraries:[
        {
            total_books: 0,
            books: [2],
            signup: 0, # of days left
            shipping: 0 # number we can scan per day
        },
    ]
}
"""


def as_they_come_algorithm(processor_data):
    """
    output:
    total libraries
    first libarary, number of books
    book1, book2, book3

    second libarary, number of books
    book1, book2, book3
    """
    output = []
    number_of_libraries = 0
    elasped_days = 0

    library_index = 0

    while (
        elasped_days < processor_data["total_days"]
        and number_of_libraries < processor_data["total_libraries"]
    ):
        number_of_libraries += 1
        library = processor_data["libraries"][library_index]
        elasped_days += library["signup"]

        if not elasped_days < processor_data["total_days"]:
            break
        days_left = processor_data["total_days"] - elasped_days
        days_left = 0 if days_left < 0 else days_left
        number_of_books_to_process = None
        books_per_day = int(library["total_books"] / library["shipping"])
        if books_per_day == 0:
            books_per_day = 1
        print("-------------------------")
        print(library["total_books"], library["shipping"])
        if library["total_books"] / books_per_day < days_left:

            number_of_books_to_process = int(library["total_books"] / books_per_day)
        else:
            number_of_books_to_process = library["total_books"]
        output.append([library_index, number_of_books_to_process])
        print("days_left ", days_left)
        print("number to process", number_of_books_to_process)
        output.append(library["books"][:number_of_books_to_process])
        library_index += 1

    output.insert(0, [number_of_libraries])
    print(output)
    return output
