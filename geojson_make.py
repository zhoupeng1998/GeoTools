import json
import argparse
import sys

def parse_file(file):
    lines = []
    with open(file, 'r') as f:
        data = f.read()
        lines = data.split('\n')
        f.close()
    return lines

def make_feature(coords):
    feature_type = 'LineString'
    if len(coords) == 1:
        feature_type = 'Point'

    if len(coords) > 1:
        coords = [list(map(float, coord.split(','))) for coord in coords]
    else:
        coords = list(map(float, coords[0].split(',')))

    feature = {
        'type': 'Feature',
        'geometry': {
            'type': feature_type,
            'coordinates': coords
        },
        'properties': {}
    }
    return feature

def main():
    parser = argparse.ArgumentParser(description='Convert a file to geojson')
    parser.add_argument('--input', '-i', help='file to convert')
    parser.add_argument('--output', '-o', help='file to write to')
    args = parser.parse_args()
    input = args.input
    output = args.output
    
    lines = []
    if input is not None:
        lines = parse_file(input)
    else:
        for line in sys.stdin:
            lines.append(line)

    json_data = {
        'type': 'FeatureCollection',
        'features': []
    }
    for line in lines:
        coords = line.split(' ')
        if len(coords) != 0:
            json_data['features'].append(make_feature(coords))
    
    if output is not None:
        with open(output, 'w') as f:
            f.write(json.dumps(json_data))
            f.close()
    else:
        print(json.dumps(json_data))

if __name__ == '__main__':
    main()
