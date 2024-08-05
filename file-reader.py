
# given a filepath, extracts the lines from the file and returns them
def lines_extractor(filepath):
    with open(filepath) as f:
        return f.readlines()


# given a line, splits the line by space, and returns the result
# array
def line_splitter(line):
    return line.split()



