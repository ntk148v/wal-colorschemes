import json
from pathlib import Path
from turtle import color

from pytablewriter import MarkdownTableWriter

desc = '''<div align="center">
	<h1>PyWal colorschemes</h1>
	<blockquote align="center">Collection of awesome color schemes for PyWal</blockquote>
	<p>
		<a href="https://github.com/ntk148v/wal-colorschemes/blob/master/LICENSE">
			<img alt="GitHub license" src="https://img.shields.io/github/license/ntk148v/wal-colorschemes?style=for-the-badge">
		</a>
		<a href="https://github.com/ntk148v/wal-colorschemes/stargazers">
			<img alt="GitHub stars" src="https://img.shields.io/github/stars/ntk148v/wal-colorschemes?style=for-the-badge">
		</a>
		<br>
	</p><br>
</div>

## Getting started

- [PyWal](https://github.com/dylanaraps/pywal) is a tool to generate and change color-schemes on the fly.
- PyWal has a set of built-in color schemes. This repository aims to provide some more.
- [Install PyWal](https://github.com/dylanaraps/pywal/wiki/Installation)
- Copy [colorschemes](./colorschemes) to PyWal config directory.

```bash
$ cp -r colorschemes ~/.config/wal
```

- Validate & switch to new colorscheme

```bash
$ wal --theme
User Themes:
 - ayu-dark
 - ayu-light
 - badwolf
 - candid
 - catppuccin
 - darker-monokai
 - github-light
 - horizon
 - iceberg
 - kanagawa
 - ...

$ wal --theme <colorscheme>
```

## Preview

'''


def generate_preview():
    preview = ""
    for path in Path('colorschemes').rglob('*.json'):
        with open(path.absolute(), 'r') as f:
            colorscheme = json.load(f)
            preview += f"### {path.name[:-5].capitalize()}\n\n"
            preview += f"[Reference]({colorscheme['refer']})\n\n"
            colormappings = []
            for k, v in colorscheme['special'].items():
                colormappings.append(
                    [k, f'![{v}](https://via.placeholder.com/60x40/{v}/000000?text={v})'])
            for k, v in colorscheme['colors'].items():
                colormappings.append(
                    [k, f'![{v}](https://via.placeholder.com/60x40/{v}/000000?text={v})'])
            writer = MarkdownTableWriter(
                headers=['Color', 'Preview'],
                value_matrix=colormappings,
                margin=1)
            preview += writer.dumps() + "\n"
    return preview


if __name__ == '__main__':
    with open('README.md', 'w') as f:
        f.write(desc)
        f.write(generate_preview())
