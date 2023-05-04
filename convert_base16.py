#!/usr/bin/env python3
#
# Wrapper for converting a base16 color scheme to Wal format
#
# Usage:
# python3 convert_base16.py file.yaml

from argparse import ArgumentParser
import json
import yaml


def main(src: str, dst: str):
    wal = {}
    # Read base16.yml file
    with open(src, 'r') as f:
        base16 = yaml.safe_load(f)
        wal = {
            "refer": "PLACEHOLDER",
            "special": {
                "background": "#"+base16["base00"],
                "foreground": "#"+base16["base05"],
                "cursor": "#"+base16["base05"]
            },
            "colors": {
                "color0": "#"+base16["base00"],
                "color1": "#"+base16["base08"],
                "color2": "#"+base16["base0B"],
                "color3": "#"+base16["base0A"],
                "color4": "#"+base16["base0D"],
                "color5": "#"+base16["base0E"],
                "color6": "#"+base16["base0C"],
                "color7": "#"+base16["base05"],
                "color8": "#"+base16["base03"],
                "color9": "#"+base16["base09"],
                "color10": "#"+base16["base01"],
                "color11": "#"+base16["base02"],
                "color12": "#"+base16["base04"],
                "color13": "#"+base16["base06"],
                "color14": "#"+base16["base0F"],
                "color15": "#"+base16["base07"],
            },
        }

    # write to file
    with open(dst, "w") as f:
        f.write(json.dumps(wal, indent=2))


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Convert base16 color scheme to Wal format')
    parser.add_argument('--src', type=str,
                        help='Path to iTerm color scheme')
    parser.add_argument('--dst', type=str,
                        help='Path to save Wal color scheme')
    args = parser.parse_args()
    main(args.src, args.dst)
