
# given a filepath, extracts the lines from the file and returns them
def lines_extractor(filepath):
    with open(filepath) as f:
        return f.readlines()


# given a line, splits the line by space, and returns the result
# array
def line_splitter(line):
    return line.split()


# given array of strings, splits each string by space, and returns
# the result array of string arrays
def lines_splitter(lines):
    lines = []
    for line in lines:
        lines.append(line_splitter(line))
    return lines



