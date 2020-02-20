#!/usr/bin/env python3


def main():
    line_num = 1
    library_line_one = True

    with open("a_example.txt") as data:
        line = data.read()
        if line_num == 1:
            # First line of file = [num of diff books][num of libraries][days for scanning]
            pass
        elif line_num == 2:
            # Second line of file = [score of each book]
            pass
        else:
            # iterating through libraries
            if library_line_one:
                #first line of library
                library_line_one != library_line_one
            else:
                #second line of library
                library_line_one != library_line_one
            
            
        line_num += 1

    




if __name__ == '__main__':
    main()