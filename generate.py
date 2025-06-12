import json
from pathlib import Path
from turtle import color

from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style

# Description
desc = '''<div align="center">
	<h1>PyWal colorschemes</h1>
	<blockquote align="center">Collection of awesome color schemes for PyWal</blockquote>
	<p>
		<a href="https://github.com/ntk148v/wal-colorschemes/blob/master/LICENSE">
			<img alt="GitHub license" src="https://img.shields.io/github/license/ntk148v/wal-colorschemes?style=for-the-badge">
		</a>
		<a href="https://github.com/ntk148v/wal-colorschemes/stargazers"> <img alt="GitHub stars" src="https://img.shields.io/github/stars/ntk148v/wal-colorschemes?style=for-the-badge"> </a>
		<br>
	</p><br>
</div>

'''

# Getting started
gs = '''

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

## Contributing

Pull requests are the best way to propose changes to the codebase (we use
[Github Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests:

- Fork the repo and create your branch from master.
- Make changes.
- Issue that pull request!

You may want to check out some scripts:
- [generate.py](./generate.py): Generate this README page.
- [convert_itermcolor.py](./convert_itermcolor.py): Convert .itermcolor to wal colorscheme file.
- [make-screenshots.sh](./make-screenshots.sh): Auto apply colors and capture screenshots.
- [preview-colors.sh](./preview-colors.sh): Preview colors in style.

## Preview

'''

# Table of content
toc = '''
- [Getting started](#getting-started)
- [Contributing](#contributing)
- [Preview](#preview)
'''

preview = ""


def generate_preview():
    global preview, toc
    for path in Path('colorschemes').rglob('*.json'):
        with open(path.absolute(), 'r') as f:
            colorscheme = json.load(f)
            name = path.name[:-5].replace('_', ' ').\
                replace('-', ' ').\
                capitalize()
            toc += f"	- [{name}](#{path.name[:-5].replace('_', '-')})\n"
            preview += f"### {name}\n\n"
            preview += f"[Reference]({colorscheme.get('refer', '#')})\n\n"
            colormappings = []
            for k, v in colorscheme['special'].items():
                colormappings.append(
                    [k, v.lower(), f'![{v}](https://via.placeholder.com/50x30/{v.strip("#")}/000000.png?text=+)'])
            for k, v in colorscheme['colors'].items():
                colormappings.append(
                    [k, v.lower(), f'![{v}](https://via.placeholder.com/50x30/{v.strip("#")}/000000.png?text=+)'])
            writer = MarkdownTableWriter(
                headers=['Color', 'Hex', 'Preview'],
                value_matrix=colormappings,
                column_styles=[
                    Style(),
                    Style(align="center"),
                    Style(align="center")
                ])

            preview += f"""<details>
    <summary>Colors, click me</summary>

{writer.dumps()}

</details>

"""


if __name__ == '__main__':
    generate_preview()
    with open('README.md', 'w') as f:
        f.write(desc)
        f.write(toc)
        f.write(gs)
        f.write(preview)
