
# given a filepath, extracts the lines from the file and returns them
def lines_extractor(filepath):
    with open(filepath) as f:
        return f.readlines()

