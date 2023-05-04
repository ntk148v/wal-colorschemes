#!/usr/bin/env python3
#
# Wrapper for converting a iTerm color scheme to Wal format
#
# Usage:
# python3 convert_itemcolors.py file.itermcolors

from argparse import ArgumentParser
import json
import xml.etree.ElementTree as ET


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def main(src: str, dst: str):
    tree = ET.parse(src)
    root = tree.getroot()

    keys = root.findall("./dict/key")
    dicts = root.findall("./dict/dict")

    wal = {
        "refer": "PLACEHOLDER",
        "special": {},
        "colors": {},
    }

    for i in range(len(keys)):
        for count, child in enumerate(dicts[i]):
            if "Blue" in child.text:
                b = int(float(dicts[i][count+1].text) * 255.0)
            if "Green" in child.text:
                g = int(float(dicts[i][count+1].text) * 255.0)
            if "Red" in child.text:
                r = int(float(dicts[i][count+1].text) * 255.0)
        # convert!
        if "Background" in keys[i].text:
            wal['special']['background'] = rgb_to_hex((r, g, b))
        elif "Foreground" in keys[i].text:
            wal['special']['foreground'] = rgb_to_hex((r, g, b))
        elif "Cursor Color" in keys[i].text:
            wal['special']['cursor'] = rgb_to_hex((r, g, b))
        elif "Ansi" in keys[i].text:
            wal['colors'][f'color{keys[i].text.split()[1].strip()}'] =\
                rgb_to_hex((r, g, b))
    # write to file
    with open(dst, "w") as f:
        f.write(json.dumps(wal, indent=2))


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Convert iTerm color scheme to Wal format')
    parser.add_argument('--src', type=str,
                        help='Path to iTerm color scheme')
    parser.add_argument('--dst', type=str,
                        help='Path to save Wal color scheme')
    args = parser.parse_args()
    main(args.src, args.dst)
