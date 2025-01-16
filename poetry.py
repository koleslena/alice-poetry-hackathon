
def read_file():
    with open('texts/pushkin-k_kern.txt', 'r') as file:
        lines = [line.rstrip() for line in file]
        return ' '.join(lines[:2])
            