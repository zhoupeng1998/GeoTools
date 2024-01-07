import json
import argparse
import sys
from utils import *

def flip_coord(coord):
    xy = coord.strip().split(',')
    flipped = f"{xy[1]},{xy[0]}"
    return flipped

def main():
    parser = argparse.ArgumentParser(description='Convert a file to geojson')
    parser.add_argument('--input', '-i', help='file to convert')
    parser.add_argument('--output', '-o', help='file to write to')
    args = parser.parse_args()
    input = args.input
    output = args.output
    
    lines = []
    out_lines = []
    if input is not None:
        lines = parse_coord_file(input)
    else:
        for line in sys.stdin:
            lines.append(line)

    for line in lines:
        coords = line.split(' ')
        flipped = [flip_coord(coord) for coord in coords]
        out_lines.append(flipped)
    
    if output is not None:
        with open(output, 'w') as f:
            for line in out_lines:
                for coord in line:
                    f.write(coord)
                    f.write(' ')
                f.write('\n')
            f.close()
    else:
        for line in out_lines:
            for coord in line:
                print(coord + ' ', end='')
            print()

if __name__ == '__main__':
    main()
