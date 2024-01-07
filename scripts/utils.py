def parse_coord_file(file):
    lines = []
    with open(file, 'r') as f:
        data = f.read()
        lines = data.split('\n')
        f.close()
    return lines