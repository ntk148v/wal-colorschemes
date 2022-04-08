<div align="center">
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


- [Getting started](#getting-started)
- [Contributing](#contributing)
- [Preview](#preview)
	- [Nightfly](#nightfly)
	- [Spaceduck](#spaceduck)
	- [Catppuccin](#catppuccin)
	- [Candid](#candid)
	- [Horizon](#horizon)
	- [Spacecamp](#spacecamp)
	- [Github dark high contrast](#github-dark-high-contrast)
	- [Github dark](#github-dark)
	- [Nord](#nord)
	- [Github dark dimmed](#github-dark-dimmed)
	- [Iceberg](#iceberg)
	- [Urban](#urban)
	- [Ayu dark](#ayu-dark)
	- [Tokyonight storm](#tokyonight-storm)
	- [Tokyonight night](#tokyonight-night)
	- [Github dark default](#github-dark-default)
	- [Snazzy](#snazzy)
	- [Kanagawa](#kanagawa)
	- [Darker monokai](#darker-monokai)
	- [One half dark](#one-half-dark)
	- [Badwolf](#badwolf)
	- [Sonokai](#sonokai)
	- [Srcery](#srcery)
	- [One half light](#one-half-light)
	- [Github light 2](#github-light-2)
	- [Ayu light](#ayu-light)
	- [Tokyonight day](#tokyonight-day)
	- [Github light default](#github-light-default)
	- [Github light](#github-light)


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

### Nightfly

[Reference](https://github.com/bluz71/vim-nightfly-guicolors)

![](./screenshots/nightfly.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#011627|![#011627](https://via.placeholder.com/50x30/011627/000000?text=+)|
|foreground|#acb4c2|![#acb4c2](https://via.placeholder.com/50x30/acb4c2/000000?text=+)|
|cursor    |#acb4c2|![#acb4c2](https://via.placeholder.com/50x30/acb4c2/000000?text=+)|
|color0    |#1d3b53|![#1d3b53](https://via.placeholder.com/50x30/1d3b53/000000?text=+)|
|color1    |#fc514e|![#fc514e](https://via.placeholder.com/50x30/fc514e/000000?text=+)|
|color2    |#a1cd5e|![#a1cd5e](https://via.placeholder.com/50x30/a1cd5e/000000?text=+)|
|color3    |#e3d18a|![#e3d18a](https://via.placeholder.com/50x30/e3d18a/000000?text=+)|
|color4    |#82aaff|![#82aaff](https://via.placeholder.com/50x30/82aaff/000000?text=+)|
|color5    |#c792ea|![#c792ea](https://via.placeholder.com/50x30/c792ea/000000?text=+)|
|color6    |#7fdbca|![#7fdbca](https://via.placeholder.com/50x30/7fdbca/000000?text=+)|
|color7    |#a1aab8|![#a1aab8](https://via.placeholder.com/50x30/a1aab8/000000?text=+)|
|color8    |#7c8f8f|![#7c8f8f](https://via.placeholder.com/50x30/7c8f8f/000000?text=+)|
|color9    |#ff5874|![#ff5874](https://via.placeholder.com/50x30/ff5874/000000?text=+)|
|color10   |#21c7a8|![#21c7a8](https://via.placeholder.com/50x30/21c7a8/000000?text=+)|
|color11   |#ecc48d|![#ecc48d](https://via.placeholder.com/50x30/ecc48d/000000?text=+)|
|color12   |#82aaff|![#82aaff](https://via.placeholder.com/50x30/82aaff/000000?text=+)|
|color13   |#ae81ff|![#ae81ff](https://via.placeholder.com/50x30/ae81ff/000000?text=+)|
|color14   |#7fdbca|![#7fdbca](https://via.placeholder.com/50x30/7fdbca/000000?text=+)|
|color15   |#d6deeb|![#d6deeb](https://via.placeholder.com/50x30/d6deeb/000000?text=+)|

### Spaceduck

[Reference](https://github.com/pineapplegiant/spaceduck)

![](./screenshots/spaceduck.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#0f111b|![#0f111b](https://via.placeholder.com/50x30/0f111b/000000?text=+)|
|foreground|#ecf0c1|![#ecf0c1](https://via.placeholder.com/50x30/ecf0c1/000000?text=+)|
|cursor    |#ecf0c1|![#ecf0c1](https://via.placeholder.com/50x30/ecf0c1/000000?text=+)|
|color0    |#000000|![#000000](https://via.placeholder.com/50x30/000000/000000?text=+)|
|color1    |#e33400|![#e33400](https://via.placeholder.com/50x30/e33400/000000?text=+)|
|color2    |#5ccc96|![#5ccc96](https://via.placeholder.com/50x30/5ccc96/000000?text=+)|
|color3    |#b3a1e6|![#b3a1e6](https://via.placeholder.com/50x30/b3a1e6/000000?text=+)|
|color4    |#00a3cc|![#00a3cc](https://via.placeholder.com/50x30/00a3cc/000000?text=+)|
|color5    |#f2ce00|![#f2ce00](https://via.placeholder.com/50x30/f2ce00/000000?text=+)|
|color6    |#7a5ccc|![#7a5ccc](https://via.placeholder.com/50x30/7a5ccc/000000?text=+)|
|color7    |#686f9a|![#686f9a](https://via.placeholder.com/50x30/686f9a/000000?text=+)|
|color8    |#686f9a|![#686f9a](https://via.placeholder.com/50x30/686f9a/000000?text=+)|
|color9    |#e33400|![#e33400](https://via.placeholder.com/50x30/e33400/000000?text=+)|
|color10   |#5ccc96|![#5ccc96](https://via.placeholder.com/50x30/5ccc96/000000?text=+)|
|color11   |#b3a1e6|![#b3a1e6](https://via.placeholder.com/50x30/b3a1e6/000000?text=+)|
|color12   |#00a3cc|![#00a3cc](https://via.placeholder.com/50x30/00a3cc/000000?text=+)|
|color13   |#f2ce00|![#f2ce00](https://via.placeholder.com/50x30/f2ce00/000000?text=+)|
|color14   |#7a5ccc|![#7a5ccc](https://via.placeholder.com/50x30/7a5ccc/000000?text=+)|
|color15   |#f0f1ce|![#f0f1ce](https://via.placeholder.com/50x30/f0f1ce/000000?text=+)|

### Catppuccin

[Reference](https://github.com/catppuccin/catppuccin)

![](./screenshots/catppuccin.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#1e1e29|![#1e1e29](https://via.placeholder.com/50x30/1e1e29/000000?text=+)|
|foreground|#f2cdcd|![#f2cdcd](https://via.placeholder.com/50x30/f2cdcd/000000?text=+)|
|cursor    |#f2cdcd|![#f2cdcd](https://via.placeholder.com/50x30/f2cdcd/000000?text=+)|
|color0    |#6e6c7c|![#6e6c7c](https://via.placeholder.com/50x30/6e6c7c/000000?text=+)|
|color1    |#f28fad|![#f28fad](https://via.placeholder.com/50x30/f28fad/000000?text=+)|
|color2    |#abe9b3|![#abe9b3](https://via.placeholder.com/50x30/abe9b3/000000?text=+)|
|color3    |#fae3b0|![#fae3b0](https://via.placeholder.com/50x30/fae3b0/000000?text=+)|
|color4    |#96cdfb|![#96cdfb](https://via.placeholder.com/50x30/96cdfb/000000?text=+)|
|color5    |#f5c2e7|![#f5c2e7](https://via.placeholder.com/50x30/f5c2e7/000000?text=+)|
|color6    |#89dceb|![#89dceb](https://via.placeholder.com/50x30/89dceb/000000?text=+)|
|color7    |#c3bac6|![#c3bac6](https://via.placeholder.com/50x30/c3bac6/000000?text=+)|
|color8    |#988ba2|![#988ba2](https://via.placeholder.com/50x30/988ba2/000000?text=+)|
|color9    |#f28fad|![#f28fad](https://via.placeholder.com/50x30/f28fad/000000?text=+)|
|color10   |#abe9b3|![#abe9b3](https://via.placeholder.com/50x30/abe9b3/000000?text=+)|
|color11   |#fae3b0|![#fae3b0](https://via.placeholder.com/50x30/fae3b0/000000?text=+)|
|color12   |#96cdfb|![#96cdfb](https://via.placeholder.com/50x30/96cdfb/000000?text=+)|
|color13   |#f5c2e7|![#f5c2e7](https://via.placeholder.com/50x30/f5c2e7/000000?text=+)|
|color14   |#89dceb|![#89dceb](https://via.placeholder.com/50x30/89dceb/000000?text=+)|
|color15   |#d9e0ee|![#d9e0ee](https://via.placeholder.com/50x30/d9e0ee/000000?text=+)|

### Candid

[Reference](https://github.com/flrnd/candid.vim)

![](./screenshots/candid.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#2f343f|![#2f343f](https://via.placeholder.com/50x30/2f343f/000000?text=+)|
|foreground|#efeeea|![#efeeea](https://via.placeholder.com/50x30/efeeea/000000?text=+)|
|cursor    |#fb7da7|![#fb7da7](https://via.placeholder.com/50x30/fb7da7/000000?text=+)|
|color0    |#818e8e|![#818e8e](https://via.placeholder.com/50x30/818e8e/000000?text=+)|
|color1    |#fb7da7|![#fb7da7](https://via.placeholder.com/50x30/fb7da7/000000?text=+)|
|color2    |#2cda9d|![#2cda9d](https://via.placeholder.com/50x30/2cda9d/000000?text=+)|
|color3    |#ffce5b|![#ffce5b](https://via.placeholder.com/50x30/ffce5b/000000?text=+)|
|color4    |#50c6d8|![#50c6d8](https://via.placeholder.com/50x30/50c6d8/000000?text=+)|
|color5    |#a18bd3|![#a18bd3](https://via.placeholder.com/50x30/a18bd3/000000?text=+)|
|color6    |#4c8273|![#4c8273](https://via.placeholder.com/50x30/4c8273/000000?text=+)|
|color7    |#2f343f|![#2f343f](https://via.placeholder.com/50x30/2f343f/000000?text=+)|
|color8    |#818e8e|![#818e8e](https://via.placeholder.com/50x30/818e8e/000000?text=+)|
|color9    |#fb7da7|![#fb7da7](https://via.placeholder.com/50x30/fb7da7/000000?text=+)|
|color10   |#2cda9d|![#2cda9d](https://via.placeholder.com/50x30/2cda9d/000000?text=+)|
|color11   |#ffce5b|![#ffce5b](https://via.placeholder.com/50x30/ffce5b/000000?text=+)|
|color12   |#50c6d8|![#50c6d8](https://via.placeholder.com/50x30/50c6d8/000000?text=+)|
|color13   |#a18bd3|![#a18bd3](https://via.placeholder.com/50x30/a18bd3/000000?text=+)|
|color14   |#4c8273|![#4c8273](https://via.placeholder.com/50x30/4c8273/000000?text=+)|
|color15   |#2f343f|![#2f343f](https://via.placeholder.com/50x30/2f343f/000000?text=+)|

### Horizon

[Reference](https://github.com/ntk148v/vim-horizon)

![](./screenshots/horizon.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#1c1e26|![#1c1e26](https://via.placeholder.com/50x30/1c1e26/000000?text=+)|
|foreground|#d5d8da|![#d5d8da](https://via.placeholder.com/50x30/d5d8da/000000?text=+)|
|cursor    |#3d425b|![#3d425b](https://via.placeholder.com/50x30/3d425b/000000?text=+)|
|color0    |#1c1e26|![#1c1e26](https://via.placeholder.com/50x30/1c1e26/000000?text=+)|
|color1    |#e95378|![#e95378](https://via.placeholder.com/50x30/e95378/000000?text=+)|
|color2    |#27d797|![#27d797](https://via.placeholder.com/50x30/27d797/000000?text=+)|
|color3    |#f09483|![#f09483](https://via.placeholder.com/50x30/f09483/000000?text=+)|
|color4    |#25b0bc|![#25b0bc](https://via.placeholder.com/50x30/25b0bc/000000?text=+)|
|color5    |#6c6f93|![#6c6f93](https://via.placeholder.com/50x30/6c6f93/000000?text=+)|
|color6    |#b877db|![#b877db](https://via.placeholder.com/50x30/b877db/000000?text=+)|
|color7    |#1c1e26|![#1c1e26](https://via.placeholder.com/50x30/1c1e26/000000?text=+)|
|color8    |#6c6f93|![#6c6f93](https://via.placeholder.com/50x30/6c6f93/000000?text=+)|
|color9    |#ec6a88|![#ec6a88](https://via.placeholder.com/50x30/ec6a88/000000?text=+)|
|color10   |#6bdfe6|![#6bdfe6](https://via.placeholder.com/50x30/6bdfe6/000000?text=+)|
|color11   |#fab38e|![#fab38e](https://via.placeholder.com/50x30/fab38e/000000?text=+)|
|color12   |#21bfc2|![#21bfc2](https://via.placeholder.com/50x30/21bfc2/000000?text=+)|
|color13   |#b877db|![#b877db](https://via.placeholder.com/50x30/b877db/000000?text=+)|
|color14   |#95c4ce|![#95c4ce](https://via.placeholder.com/50x30/95c4ce/000000?text=+)|
|color15   |#d2d4de|![#d2d4de](https://via.placeholder.com/50x30/d2d4de/000000?text=+)|

### Spacecamp

[Reference](https://github.com/jaredgorski/SpaceCamp)

![](./screenshots/spacecamp.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#121212|![#121212](https://via.placeholder.com/50x30/121212/000000?text=+)|
|foreground|#d0d0d0|![#d0d0d0](https://via.placeholder.com/50x30/d0d0d0/000000?text=+)|
|cursor    |#d0d0d0|![#d0d0d0](https://via.placeholder.com/50x30/d0d0d0/000000?text=+)|
|color0    |#282828|![#282828](https://via.placeholder.com/50x30/282828/000000?text=+)|
|color1    |#d71a1a|![#d71a1a](https://via.placeholder.com/50x30/d71a1a/000000?text=+)|
|color2    |#57ba37|![#57ba37](https://via.placeholder.com/50x30/57ba37/000000?text=+)|
|color3    |#f0d50c|![#f0d50c](https://via.placeholder.com/50x30/f0d50c/000000?text=+)|
|color4    |#91aadf|![#91aadf](https://via.placeholder.com/50x30/91aadf/000000?text=+)|
|color5    |#cf73e6|![#cf73e6](https://via.placeholder.com/50x30/cf73e6/000000?text=+)|
|color6    |#b7cbf4|![#b7cbf4](https://via.placeholder.com/50x30/b7cbf4/000000?text=+)|
|color7    |#dedede|![#dedede](https://via.placeholder.com/50x30/dedede/000000?text=+)|
|color8    |#666666|![#666666](https://via.placeholder.com/50x30/666666/000000?text=+)|
|color9    |#ff0000|![#ff0000](https://via.placeholder.com/50x30/ff0000/000000?text=+)|
|color10   |#d8fa3b|![#d8fa3b](https://via.placeholder.com/50x30/d8fa3b/000000?text=+)|
|color11   |#e7c547|![#e7c547](https://via.placeholder.com/50x30/e7c547/000000?text=+)|
|color12   |#b7cbf4|![#b7cbf4](https://via.placeholder.com/50x30/b7cbf4/000000?text=+)|
|color13   |#b77ee0|![#b77ee0](https://via.placeholder.com/50x30/b77ee0/000000?text=+)|
|color14   |#a9c1de|![#a9c1de](https://via.placeholder.com/50x30/a9c1de/000000?text=+)|
|color15   |#eeeeee|![#eeeeee](https://via.placeholder.com/50x30/eeeeee/000000?text=+)|

### Github dark high contrast

[Reference](https://github.com/cdalvaro/github-vscode-theme-iterm)

![](./screenshots/github-dark-high-contrast.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#010409|![#010409](https://via.placeholder.com/50x30/010409/000000?text=+)|
|cursor    |#f0f3f6|![#f0f3f6](https://via.placeholder.com/50x30/f0f3f6/000000?text=+)|
|foreground|#f0f3f6|![#f0f3f6](https://via.placeholder.com/50x30/f0f3f6/000000?text=+)|
|color0    |#7a828e|![#7a828e](https://via.placeholder.com/50x30/7a828e/000000?text=+)|
|color1    |#ff9492|![#ff9492](https://via.placeholder.com/50x30/ff9492/000000?text=+)|
|color10   |#4ae168|![#4ae168](https://via.placeholder.com/50x30/4ae168/000000?text=+)|
|color11   |#f7c843|![#f7c843](https://via.placeholder.com/50x30/f7c843/000000?text=+)|
|color12   |#91cbff|![#91cbff](https://via.placeholder.com/50x30/91cbff/000000?text=+)|
|color13   |#dbb7ff|![#dbb7ff](https://via.placeholder.com/50x30/dbb7ff/000000?text=+)|
|color14   |#56d4dd|![#56d4dd](https://via.placeholder.com/50x30/56d4dd/000000?text=+)|
|color15   |#ffffff|![#ffffff](https://via.placeholder.com/50x30/ffffff/000000?text=+)|
|color2    |#26cd4d|![#26cd4d](https://via.placeholder.com/50x30/26cd4d/000000?text=+)|
|color3    |#f0b72f|![#f0b72f](https://via.placeholder.com/50x30/f0b72f/000000?text=+)|
|color4    |#71b7ff|![#71b7ff](https://via.placeholder.com/50x30/71b7ff/000000?text=+)|
|color5    |#cb9eff|![#cb9eff](https://via.placeholder.com/50x30/cb9eff/000000?text=+)|
|color6    |#39c5cf|![#39c5cf](https://via.placeholder.com/50x30/39c5cf/000000?text=+)|
|color7    |#d9dee3|![#d9dee3](https://via.placeholder.com/50x30/d9dee3/000000?text=+)|
|color8    |#9ea7b3|![#9ea7b3](https://via.placeholder.com/50x30/9ea7b3/000000?text=+)|
|color9    |#ffb1af|![#ffb1af](https://via.placeholder.com/50x30/ffb1af/000000?text=+)|

### Github dark

[Reference](https://github.com/cdalvaro/github-vscode-theme-iterm)

![](./screenshots/github-dark.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#1e2429|![#1e2429](https://via.placeholder.com/50x30/1e2429/000000?text=+)|
|cursor    |#c5e1ff|![#c5e1ff](https://via.placeholder.com/50x30/c5e1ff/000000?text=+)|
|foreground|#d1d5da|![#d1d5da](https://via.placeholder.com/50x30/d1d5da/000000?text=+)|
|color0    |#000000|![#000000](https://via.placeholder.com/50x30/000000/000000?text=+)|
|color1    |#d81029|![#d81029](https://via.placeholder.com/50x30/d81029/000000?text=+)|
|color10   |#00d684|![#00d684](https://via.placeholder.com/50x30/00d684/000000?text=+)|
|color11   |#f2f800|![#f2f800](https://via.placeholder.com/50x30/f2f800/000000?text=+)|
|color12   |#2e8df1|![#2e8df1](https://via.placeholder.com/50x30/2e8df1/000000?text=+)|
|color13   |#e163dc|![#e163dc](https://via.placeholder.com/50x30/e163dc/000000?text=+)|
|color14   |#00badf|![#00badf](https://via.placeholder.com/50x30/00badf/000000?text=+)|
|color15   |#e5e5e5|![#e5e5e5](https://via.placeholder.com/50x30/e5e5e5/000000?text=+)|
|color2    |#00c172|![#00c172](https://via.placeholder.com/50x30/00c172/000000?text=+)|
|color3    |#e2e800|![#e2e800](https://via.placeholder.com/50x30/e2e800/000000?text=+)|
|color4    |#1571ce|![#1571ce](https://via.placeholder.com/50x30/1571ce/000000?text=+)|
|color5    |#c824c2|![#c824c2](https://via.placeholder.com/50x30/c824c2/000000?text=+)|
|color6    |#00aad1|![#00aad1](https://via.placeholder.com/50x30/00aad1/000000?text=+)|
|color7    |#e5e5e5|![#e5e5e5](https://via.placeholder.com/50x30/e5e5e5/000000?text=+)|
|color8    |#666666|![#666666](https://via.placeholder.com/50x30/666666/000000?text=+)|
|color9    |#fe3646|![#fe3646](https://via.placeholder.com/50x30/fe3646/000000?text=+)|

### Nord

[Reference](https://github.com/arcticicestudio/nord)

![](./screenshots/nord.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#2e3440|![#2e3440](https://via.placeholder.com/50x30/2e3440/000000?text=+)|
|foreground|#d8dee9|![#d8dee9](https://via.placeholder.com/50x30/d8dee9/000000?text=+)|
|cursor    |#d8dee9|![#d8dee9](https://via.placeholder.com/50x30/d8dee9/000000?text=+)|
|color0    |#2e3440|![#2e3440](https://via.placeholder.com/50x30/2e3440/000000?text=+)|
|color1    |#bf616a|![#bf616a](https://via.placeholder.com/50x30/bf616a/000000?text=+)|
|color2    |#a3be8c|![#a3be8c](https://via.placeholder.com/50x30/a3be8c/000000?text=+)|
|color3    |#ebcb8b|![#ebcb8b](https://via.placeholder.com/50x30/ebcb8b/000000?text=+)|
|color4    |#81a1c1|![#81a1c1](https://via.placeholder.com/50x30/81a1c1/000000?text=+)|
|color5    |#b48ead|![#b48ead](https://via.placeholder.com/50x30/b48ead/000000?text=+)|
|color6    |#88c0d0|![#88c0d0](https://via.placeholder.com/50x30/88c0d0/000000?text=+)|
|color7    |#e5e9f0|![#e5e9f0](https://via.placeholder.com/50x30/e5e9f0/000000?text=+)|
|color8    |#4c566a|![#4c566a](https://via.placeholder.com/50x30/4c566a/000000?text=+)|
|color9    |#bf616a|![#bf616a](https://via.placeholder.com/50x30/bf616a/000000?text=+)|
|color10   |#a3be8c|![#a3be8c](https://via.placeholder.com/50x30/a3be8c/000000?text=+)|
|color11   |#ebcb8b|![#ebcb8b](https://via.placeholder.com/50x30/ebcb8b/000000?text=+)|
|color12   |#81a1c1|![#81a1c1](https://via.placeholder.com/50x30/81a1c1/000000?text=+)|
|color13   |#b48ead|![#b48ead](https://via.placeholder.com/50x30/b48ead/000000?text=+)|
|color14   |#8fbcbb|![#8fbcbb](https://via.placeholder.com/50x30/8fbcbb/000000?text=+)|
|color15   |#eceff4|![#eceff4](https://via.placeholder.com/50x30/eceff4/000000?text=+)|

### Github dark dimmed

[Reference](https://github.com/cdalvaro/github-vscode-theme-iterm)

![](./screenshots/github-dark-dimmed.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#1c2128|![#1c2128](https://via.placeholder.com/50x30/1c2128/000000?text=+)|
|cursor    |#768390|![#768390](https://via.placeholder.com/50x30/768390/000000?text=+)|
|foreground|#768390|![#768390](https://via.placeholder.com/50x30/768390/000000?text=+)|
|color0    |#545d68|![#545d68](https://via.placeholder.com/50x30/545d68/000000?text=+)|
|color1    |#f47067|![#f47067](https://via.placeholder.com/50x30/f47067/000000?text=+)|
|color10   |#6bc46d|![#6bc46d](https://via.placeholder.com/50x30/6bc46d/000000?text=+)|
|color11   |#daaa3f|![#daaa3f](https://via.placeholder.com/50x30/daaa3f/000000?text=+)|
|color12   |#6cb6ff|![#6cb6ff](https://via.placeholder.com/50x30/6cb6ff/000000?text=+)|
|color13   |#dcbdfb|![#dcbdfb](https://via.placeholder.com/50x30/dcbdfb/000000?text=+)|
|color14   |#56d4dd|![#56d4dd](https://via.placeholder.com/50x30/56d4dd/000000?text=+)|
|color15   |#cdd9e5|![#cdd9e5](https://via.placeholder.com/50x30/cdd9e5/000000?text=+)|
|color2    |#57ab5a|![#57ab5a](https://via.placeholder.com/50x30/57ab5a/000000?text=+)|
|color3    |#c69026|![#c69026](https://via.placeholder.com/50x30/c69026/000000?text=+)|
|color4    |#539bf5|![#539bf5](https://via.placeholder.com/50x30/539bf5/000000?text=+)|
|color5    |#b083f0|![#b083f0](https://via.placeholder.com/50x30/b083f0/000000?text=+)|
|color6    |#39c5cf|![#39c5cf](https://via.placeholder.com/50x30/39c5cf/000000?text=+)|
|color7    |#909dab|![#909dab](https://via.placeholder.com/50x30/909dab/000000?text=+)|
|color8    |#636e7b|![#636e7b](https://via.placeholder.com/50x30/636e7b/000000?text=+)|
|color9    |#ff938a|![#ff938a](https://via.placeholder.com/50x30/ff938a/000000?text=+)|

### Iceberg

[Reference](https://github.com/cocopon/iceberg.vim)

![](./screenshots/iceberg.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#161821|![#161821](https://via.placeholder.com/50x30/161821/000000?text=+)|
|foreground|#c6c8d1|![#c6c8d1](https://via.placeholder.com/50x30/c6c8d1/000000?text=+)|
|cursor    |#c6c8d1|![#c6c8d1](https://via.placeholder.com/50x30/c6c8d1/000000?text=+)|
|color0    |#1e2132|![#1e2132](https://via.placeholder.com/50x30/1e2132/000000?text=+)|
|color1    |#e27878|![#e27878](https://via.placeholder.com/50x30/e27878/000000?text=+)|
|color2    |#b4be82|![#b4be82](https://via.placeholder.com/50x30/b4be82/000000?text=+)|
|color3    |#e2a478|![#e2a478](https://via.placeholder.com/50x30/e2a478/000000?text=+)|
|color4    |#84a0c6|![#84a0c6](https://via.placeholder.com/50x30/84a0c6/000000?text=+)|
|color5    |#a093c7|![#a093c7](https://via.placeholder.com/50x30/a093c7/000000?text=+)|
|color6    |#89b8c2|![#89b8c2](https://via.placeholder.com/50x30/89b8c2/000000?text=+)|
|color7    |#c6c8d1|![#c6c8d1](https://via.placeholder.com/50x30/c6c8d1/000000?text=+)|
|color8    |#6b7089|![#6b7089](https://via.placeholder.com/50x30/6b7089/000000?text=+)|
|color9    |#e98989|![#e98989](https://via.placeholder.com/50x30/e98989/000000?text=+)|
|color10   |#c0ca8e|![#c0ca8e](https://via.placeholder.com/50x30/c0ca8e/000000?text=+)|
|color11   |#e9b189|![#e9b189](https://via.placeholder.com/50x30/e9b189/000000?text=+)|
|color12   |#91acd1|![#91acd1](https://via.placeholder.com/50x30/91acd1/000000?text=+)|
|color13   |#ada0d3|![#ada0d3](https://via.placeholder.com/50x30/ada0d3/000000?text=+)|
|color14   |#95c4ce|![#95c4ce](https://via.placeholder.com/50x30/95c4ce/000000?text=+)|
|color15   |#d2d4de|![#d2d4de](https://via.placeholder.com/50x30/d2d4de/000000?text=+)|

### Urban

[Reference](https://github.com/divadretlaw/urban)

![](./screenshots/urban.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#292a2f|![#292a2f](https://via.placeholder.com/50x30/292a2f/000000?text=+)|
|cursor    |#e7e8eb|![#e7e8eb](https://via.placeholder.com/50x30/e7e8eb/000000?text=+)|
|foreground|#e7e8eb|![#e7e8eb](https://via.placeholder.com/50x30/e7e8eb/000000?text=+)|
|color0    |#36373d|![#36373d](https://via.placeholder.com/50x30/36373d/000000?text=+)|
|color1    |#ff2600|![#ff2600](https://via.placeholder.com/50x30/ff2600/000000?text=+)|
|color10   |#51c34f|![#51c34f](https://via.placeholder.com/50x30/51c34f/000000?text=+)|
|color11   |#fef743|![#fef743](https://via.placeholder.com/50x30/fef743/000000?text=+)|
|color12   |#0088ff|![#0088ff](https://via.placeholder.com/50x30/0088ff/000000?text=+)|
|color13   |#e12ca0|![#e12ca0](https://via.placeholder.com/50x30/e12ca0/000000?text=+)|
|color14   |#16b5b1|![#16b5b1](https://via.placeholder.com/50x30/16b5b1/000000?text=+)|
|color15   |#feffff|![#feffff](https://via.placeholder.com/50x30/feffff/000000?text=+)|
|color2    |#badb93|![#badb93](https://via.placeholder.com/50x30/badb93/000000?text=+)|
|color3    |#fef996|![#fef996](https://via.placeholder.com/50x30/fef996/000000?text=+)|
|color4    |#85c4f8|![#85c4f8](https://via.placeholder.com/50x30/85c4f8/000000?text=+)|
|color5    |#f498be|![#f498be](https://via.placeholder.com/50x30/f498be/000000?text=+)|
|color6    |#a7ebdd|![#a7ebdd](https://via.placeholder.com/50x30/a7ebdd/000000?text=+)|
|color7    |#ebecef|![#ebecef](https://via.placeholder.com/50x30/ebecef/000000?text=+)|
|color8    |#454957|![#454957](https://via.placeholder.com/50x30/454957/000000?text=+)|
|color9    |#dd393b|![#dd393b](https://via.placeholder.com/50x30/dd393b/000000?text=+)|

### Ayu dark

[Reference](https://github.com/ayu-theme/ayu-colors)

![](./screenshots/ayu-dark.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#0a0e14|![#0A0E14](https://via.placeholder.com/50x30/0A0E14/000000?text=+)|
|foreground|#b3b1ad|![#B3B1AD](https://via.placeholder.com/50x30/B3B1AD/000000?text=+)|
|cursor    |#4d5566|![#4D5566](https://via.placeholder.com/50x30/4D5566/000000?text=+)|
|color0    |#0a0e14|![#0A0E14](https://via.placeholder.com/50x30/0A0E14/000000?text=+)|
|color1    |#ffb454|![#FFB454](https://via.placeholder.com/50x30/FFB454/000000?text=+)|
|color2    |#59c2ff|![#59C2FF](https://via.placeholder.com/50x30/59C2FF/000000?text=+)|
|color3    |#c2d94c|![#C2D94C](https://via.placeholder.com/50x30/C2D94C/000000?text=+)|
|color4    |#95e6cb|![#95E6CB](https://via.placeholder.com/50x30/95E6CB/000000?text=+)|
|color5    |#f07178|![#F07178](https://via.placeholder.com/50x30/F07178/000000?text=+)|
|color6    |#ff8f40|![#FF8F40](https://via.placeholder.com/50x30/FF8F40/000000?text=+)|
|color7    |#e6b673|![#E6B673](https://via.placeholder.com/50x30/E6B673/000000?text=+)|
|color8    |#39bae6|![#39BAE6](https://via.placeholder.com/50x30/39BAE6/000000?text=+)|
|color9    |#ffee99|![#FFEE99](https://via.placeholder.com/50x30/FFEE99/000000?text=+)|
|color10   |#f29668|![#F29668](https://via.placeholder.com/50x30/F29668/000000?text=+)|
|color11   |#ff3333|![#FF3333](https://via.placeholder.com/50x30/FF3333/000000?text=+)|
|color12   |#91b362|![#91B362](https://via.placeholder.com/50x30/91B362/000000?text=+)|
|color13   |#6994bf|![#6994BF](https://via.placeholder.com/50x30/6994BF/000000?text=+)|
|color14   |#d96c75|![#D96C75](https://via.placeholder.com/50x30/D96C75/000000?text=+)|
|color15   |#0a0e14|![#0A0E14](https://via.placeholder.com/50x30/0A0E14/000000?text=+)|

### Tokyonight storm

[Reference](https://github.com/folke/tokyonight.nvim)

![](./screenshots/tokyonight_storm.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#24283b|![#24283b](https://via.placeholder.com/50x30/24283b/000000?text=+)|
|foreground|#c0caf5|![#c0caf5](https://via.placeholder.com/50x30/c0caf5/000000?text=+)|
|cursor    |#c0caf5|![#c0caf5](https://via.placeholder.com/50x30/c0caf5/000000?text=+)|
|color0    |#1d202f|![#1D202F](https://via.placeholder.com/50x30/1D202F/000000?text=+)|
|color1    |#f7768e|![#f7768e](https://via.placeholder.com/50x30/f7768e/000000?text=+)|
|color2    |#9ece6a|![#9ece6a](https://via.placeholder.com/50x30/9ece6a/000000?text=+)|
|color3    |#e0af68|![#e0af68](https://via.placeholder.com/50x30/e0af68/000000?text=+)|
|color4    |#7aa2f7|![#7aa2f7](https://via.placeholder.com/50x30/7aa2f7/000000?text=+)|
|color5    |#bb9af7|![#bb9af7](https://via.placeholder.com/50x30/bb9af7/000000?text=+)|
|color6    |#7dcfff|![#7dcfff](https://via.placeholder.com/50x30/7dcfff/000000?text=+)|
|color7    |#a9b1d6|![#a9b1d6](https://via.placeholder.com/50x30/a9b1d6/000000?text=+)|
|color8    |#414868|![#414868](https://via.placeholder.com/50x30/414868/000000?text=+)|
|color9    |#f7768e|![#f7768e](https://via.placeholder.com/50x30/f7768e/000000?text=+)|
|color10   |#9ece6a|![#9ece6a](https://via.placeholder.com/50x30/9ece6a/000000?text=+)|
|color11   |#e0af68|![#e0af68](https://via.placeholder.com/50x30/e0af68/000000?text=+)|
|color12   |#7aa2f7|![#7aa2f7](https://via.placeholder.com/50x30/7aa2f7/000000?text=+)|
|color13   |#bb9af7|![#bb9af7](https://via.placeholder.com/50x30/bb9af7/000000?text=+)|
|color14   |#7dcfff|![#7dcfff](https://via.placeholder.com/50x30/7dcfff/000000?text=+)|
|color15   |#c0caf5|![#c0caf5](https://via.placeholder.com/50x30/c0caf5/000000?text=+)|

### Tokyonight night

[Reference](https://github.com/folke/tokyonight.nvim)

![](./screenshots/tokyonight_night.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#1a1b26|![#1a1b26](https://via.placeholder.com/50x30/1a1b26/000000?text=+)|
|foreground|#c0caf5|![#c0caf5](https://via.placeholder.com/50x30/c0caf5/000000?text=+)|
|cursor    |#c0caf5|![#c0caf5](https://via.placeholder.com/50x30/c0caf5/000000?text=+)|
|color0    |#15161e|![#15161E](https://via.placeholder.com/50x30/15161E/000000?text=+)|
|color1    |#f7768e|![#f7768e](https://via.placeholder.com/50x30/f7768e/000000?text=+)|
|color2    |#9ece6a|![#9ece6a](https://via.placeholder.com/50x30/9ece6a/000000?text=+)|
|color3    |#e0af68|![#e0af68](https://via.placeholder.com/50x30/e0af68/000000?text=+)|
|color4    |#7aa2f7|![#7aa2f7](https://via.placeholder.com/50x30/7aa2f7/000000?text=+)|
|color5    |#bb9af7|![#bb9af7](https://via.placeholder.com/50x30/bb9af7/000000?text=+)|
|color6    |#7dcfff|![#7dcfff](https://via.placeholder.com/50x30/7dcfff/000000?text=+)|
|color7    |#a9b1d6|![#a9b1d6](https://via.placeholder.com/50x30/a9b1d6/000000?text=+)|
|color8    |#414868|![#414868](https://via.placeholder.com/50x30/414868/000000?text=+)|
|color9    |#f7768e|![#f7768e](https://via.placeholder.com/50x30/f7768e/000000?text=+)|
|color10   |#9ece6a|![#9ece6a](https://via.placeholder.com/50x30/9ece6a/000000?text=+)|
|color11   |#e0af68|![#e0af68](https://via.placeholder.com/50x30/e0af68/000000?text=+)|
|color12   |#7aa2f7|![#7aa2f7](https://via.placeholder.com/50x30/7aa2f7/000000?text=+)|
|color13   |#bb9af7|![#bb9af7](https://via.placeholder.com/50x30/bb9af7/000000?text=+)|
|color14   |#7dcfff|![#7dcfff](https://via.placeholder.com/50x30/7dcfff/000000?text=+)|
|color15   |#c0caf5|![#c0caf5](https://via.placeholder.com/50x30/c0caf5/000000?text=+)|

### Github dark default

[Reference](https://github.com/cdalvaro/github-vscode-theme-iterm)

![](./screenshots/github-dark-default.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#010409|![#010409](https://via.placeholder.com/50x30/010409/000000?text=+)|
|cursor    |#8b949e|![#8b949e](https://via.placeholder.com/50x30/8b949e/000000?text=+)|
|foreground|#8b949e|![#8b949e](https://via.placeholder.com/50x30/8b949e/000000?text=+)|
|color0    |#484f58|![#484f58](https://via.placeholder.com/50x30/484f58/000000?text=+)|
|color1    |#ff7b72|![#ff7b72](https://via.placeholder.com/50x30/ff7b72/000000?text=+)|
|color10   |#56d364|![#56d364](https://via.placeholder.com/50x30/56d364/000000?text=+)|
|color11   |#e3b341|![#e3b341](https://via.placeholder.com/50x30/e3b341/000000?text=+)|
|color12   |#79c0ff|![#79c0ff](https://via.placeholder.com/50x30/79c0ff/000000?text=+)|
|color13   |#d2a8ff|![#d2a8ff](https://via.placeholder.com/50x30/d2a8ff/000000?text=+)|
|color14   |#56d4dd|![#56d4dd](https://via.placeholder.com/50x30/56d4dd/000000?text=+)|
|color15   |#f0f6fc|![#f0f6fc](https://via.placeholder.com/50x30/f0f6fc/000000?text=+)|
|color2    |#3fb950|![#3fb950](https://via.placeholder.com/50x30/3fb950/000000?text=+)|
|color3    |#d29922|![#d29922](https://via.placeholder.com/50x30/d29922/000000?text=+)|
|color4    |#58a6ff|![#58a6ff](https://via.placeholder.com/50x30/58a6ff/000000?text=+)|
|color5    |#bc8cff|![#bc8cff](https://via.placeholder.com/50x30/bc8cff/000000?text=+)|
|color6    |#39c5cf|![#39c5cf](https://via.placeholder.com/50x30/39c5cf/000000?text=+)|
|color7    |#b1bac4|![#b1bac4](https://via.placeholder.com/50x30/b1bac4/000000?text=+)|
|color8    |#6e7681|![#6e7681](https://via.placeholder.com/50x30/6e7681/000000?text=+)|
|color9    |#ffa198|![#ffa198](https://via.placeholder.com/50x30/ffa198/000000?text=+)|

### Snazzy

[Reference](https://github.com/connorholyday/vim-snazzy)

![](./screenshots/snazzy.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#272935|![#272935](https://via.placeholder.com/50x30/272935/000000?text=+)|
|foreground|#eff0ea|![#EFF0EA](https://via.placeholder.com/50x30/EFF0EA/000000?text=+)|
|cursor    |#f7f7f7|![#F7F7F7](https://via.placeholder.com/50x30/F7F7F7/000000?text=+)|
|color0    |#000000|![#000000](https://via.placeholder.com/50x30/000000/000000?text=+)|
|color1    |#ff5b56|![#FF5B56](https://via.placeholder.com/50x30/FF5B56/000000?text=+)|
|color2    |#5af78d|![#5AF78D](https://via.placeholder.com/50x30/5AF78D/000000?text=+)|
|color3    |#f3f99c|![#F3F99C](https://via.placeholder.com/50x30/F3F99C/000000?text=+)|
|color4    |#57c7fe|![#57C7FE](https://via.placeholder.com/50x30/57C7FE/000000?text=+)|
|color5    |#ff69c0|![#FF69C0](https://via.placeholder.com/50x30/FF69C0/000000?text=+)|
|color6    |#9aecfe|![#9AECFE](https://via.placeholder.com/50x30/9AECFE/000000?text=+)|
|color7    |#f1f1f0|![#F1F1F0](https://via.placeholder.com/50x30/F1F1F0/000000?text=+)|
|color8    |#686767|![#686767](https://via.placeholder.com/50x30/686767/000000?text=+)|
|color9    |#ff5b56|![#FF5B56](https://via.placeholder.com/50x30/FF5B56/000000?text=+)|
|color10   |#5af78d|![#5AF78D](https://via.placeholder.com/50x30/5AF78D/000000?text=+)|
|color11   |#f3f99c|![#F3F99C](https://via.placeholder.com/50x30/F3F99C/000000?text=+)|
|color12   |#57c7fe|![#57C7FE](https://via.placeholder.com/50x30/57C7FE/000000?text=+)|
|color13   |#ff69c0|![#FF69C0](https://via.placeholder.com/50x30/FF69C0/000000?text=+)|
|color14   |#9aecfe|![#9AECFE](https://via.placeholder.com/50x30/9AECFE/000000?text=+)|
|color15   |#f1f1f0|![#F1F1F0](https://via.placeholder.com/50x30/F1F1F0/000000?text=+)|

### Kanagawa

[Reference](https://github.com/rebelot/kanagawa.nvim)

![](./screenshots/kanagawa.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|foreground|#dcd7ba|![#DCD7BA](https://via.placeholder.com/50x30/DCD7BA/000000?text=+)|
|background|#1f1f28|![#1F1F28](https://via.placeholder.com/50x30/1F1F28/000000?text=+)|
|cursor    |#c8c093|![#C8C093](https://via.placeholder.com/50x30/C8C093/000000?text=+)|
|color0    |#090618|![#090618](https://via.placeholder.com/50x30/090618/000000?text=+)|
|color1    |#c34043|![#C34043](https://via.placeholder.com/50x30/C34043/000000?text=+)|
|color2    |#76946a|![#76946A](https://via.placeholder.com/50x30/76946A/000000?text=+)|
|color3    |#c0a36e|![#C0A36E](https://via.placeholder.com/50x30/C0A36E/000000?text=+)|
|color4    |#7e9cd8|![#7E9CD8](https://via.placeholder.com/50x30/7E9CD8/000000?text=+)|
|color5    |#957fb8|![#957FB8](https://via.placeholder.com/50x30/957FB8/000000?text=+)|
|color6    |#6a9589|![#6A9589](https://via.placeholder.com/50x30/6A9589/000000?text=+)|
|color7    |#c8c093|![#C8C093](https://via.placeholder.com/50x30/C8C093/000000?text=+)|
|color8    |#727169|![#727169](https://via.placeholder.com/50x30/727169/000000?text=+)|
|color9    |#e82424|![#E82424](https://via.placeholder.com/50x30/E82424/000000?text=+)|
|color10   |#98bb6c|![#98BB6C](https://via.placeholder.com/50x30/98BB6C/000000?text=+)|
|color11   |#e6c384|![#E6C384](https://via.placeholder.com/50x30/E6C384/000000?text=+)|
|color12   |#7fb4ca|![#7FB4CA](https://via.placeholder.com/50x30/7FB4CA/000000?text=+)|
|color13   |#938aa9|![#938AA9](https://via.placeholder.com/50x30/938AA9/000000?text=+)|
|color14   |#7aa89f|![#7AA89F](https://via.placeholder.com/50x30/7AA89F/000000?text=+)|
|color15   |#dcd7ba|![#DCD7BA](https://via.placeholder.com/50x30/DCD7BA/000000?text=+)|
|color16   |#ffa066|![#FFA066](https://via.placeholder.com/50x30/FFA066/000000?text=+)|
|color17   |#ff5d62|![#FF5D62](https://via.placeholder.com/50x30/FF5D62/000000?text=+)|

### Darker monokai

[Reference](https://github.com/ntk148v/vscode-darker-monokai)

![](./screenshots/darker-monokai.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#161821|![#161821](https://via.placeholder.com/50x30/161821/000000?text=+)|
|foreground|#f8f8f2|![#f8f8f2](https://via.placeholder.com/50x30/f8f8f2/000000?text=+)|
|cursor    |#f8f8f2|![#f8f8f2](https://via.placeholder.com/50x30/f8f8f2/000000?text=+)|
|color0    |#161821|![#161821](https://via.placeholder.com/50x30/161821/000000?text=+)|
|color1    |#f92672|![#f92672](https://via.placeholder.com/50x30/f92672/000000?text=+)|
|color2    |#a6e22e|![#a6e22e](https://via.placeholder.com/50x30/a6e22e/000000?text=+)|
|color3    |#f4bf75|![#f4bf75](https://via.placeholder.com/50x30/f4bf75/000000?text=+)|
|color4    |#66d9ef|![#66d9ef](https://via.placeholder.com/50x30/66d9ef/000000?text=+)|
|color5    |#ae81ff|![#ae81ff](https://via.placeholder.com/50x30/ae81ff/000000?text=+)|
|color6    |#a1efe4|![#a1efe4](https://via.placeholder.com/50x30/a1efe4/000000?text=+)|
|color7    |#f8f8f2|![#f8f8f2](https://via.placeholder.com/50x30/f8f8f2/000000?text=+)|
|color8    |#66d9ef|![#66d9ef](https://via.placeholder.com/50x30/66d9ef/000000?text=+)|
|color9    |#f92672|![#f92672](https://via.placeholder.com/50x30/f92672/000000?text=+)|
|color10   |#a6e22e|![#a6e22e](https://via.placeholder.com/50x30/a6e22e/000000?text=+)|
|color11   |#f4bf75|![#f4bf75](https://via.placeholder.com/50x30/f4bf75/000000?text=+)|
|color12   |#66d9ef|![#66d9ef](https://via.placeholder.com/50x30/66d9ef/000000?text=+)|
|color13   |#ae81ff|![#ae81ff](https://via.placeholder.com/50x30/ae81ff/000000?text=+)|
|color14   |#a1efe4|![#a1efe4](https://via.placeholder.com/50x30/a1efe4/000000?text=+)|
|color15   |#f9f8f5|![#f9f8f5](https://via.placeholder.com/50x30/f9f8f5/000000?text=+)|

### One half dark

[Reference](https://github.com/sonph/onehalf)

![](./screenshots/one-half-dark.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#282c34|![#282c34](https://via.placeholder.com/50x30/282c34/000000?text=+)|
|foreground|#dcdfe4|![#dcdfe4](https://via.placeholder.com/50x30/dcdfe4/000000?text=+)|
|cursor    |#dcdfe4|![#dcdfe4](https://via.placeholder.com/50x30/dcdfe4/000000?text=+)|
|color0    |#282c34|![#282c34](https://via.placeholder.com/50x30/282c34/000000?text=+)|
|color1    |#e06c75|![#e06c75](https://via.placeholder.com/50x30/e06c75/000000?text=+)|
|color2    |#98c379|![#98c379](https://via.placeholder.com/50x30/98c379/000000?text=+)|
|color3    |#e5c07b|![#e5c07b](https://via.placeholder.com/50x30/e5c07b/000000?text=+)|
|color4    |#61afef|![#61afef](https://via.placeholder.com/50x30/61afef/000000?text=+)|
|color5    |#c678dd|![#c678dd](https://via.placeholder.com/50x30/c678dd/000000?text=+)|
|color6    |#56b6c2|![#56b6c2](https://via.placeholder.com/50x30/56b6c2/000000?text=+)|
|color7    |#dcdfe4|![#dcdfe4](https://via.placeholder.com/50x30/dcdfe4/000000?text=+)|
|color8    |#61afef|![#61afef](https://via.placeholder.com/50x30/61afef/000000?text=+)|
|color9    |#e06c75|![#e06c75](https://via.placeholder.com/50x30/e06c75/000000?text=+)|
|color10   |#98c379|![#98c379](https://via.placeholder.com/50x30/98c379/000000?text=+)|
|color11   |#e5c07b|![#e5c07b](https://via.placeholder.com/50x30/e5c07b/000000?text=+)|
|color12   |#61afef|![#61afef](https://via.placeholder.com/50x30/61afef/000000?text=+)|
|color13   |#c678dd|![#c678dd](https://via.placeholder.com/50x30/c678dd/000000?text=+)|
|color14   |#56b6c2|![#56b6c2](https://via.placeholder.com/50x30/56b6c2/000000?text=+)|
|color15   |#dcdfe4|![#dcdfe4](https://via.placeholder.com/50x30/dcdfe4/000000?text=+)|

### Badwolf

[Reference](https://github.com/sjl/badwolf)

![](./screenshots/badwolf.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#1c1b1a|![#1c1b1a](https://via.placeholder.com/50x30/1c1b1a/000000?text=+)|
|foreground|#f8f6f2|![#f8f6f2](https://via.placeholder.com/50x30/f8f6f2/000000?text=+)|
|cursor    |#f8f6f2|![#f8f6f2](https://via.placeholder.com/50x30/f8f6f2/000000?text=+)|
|color0    |#1c1b1a|![#1c1b1a](https://via.placeholder.com/50x30/1c1b1a/000000?text=+)|
|color1    |#ff2c4b|![#ff2c4b](https://via.placeholder.com/50x30/ff2c4b/000000?text=+)|
|color2    |#8cffba|![#8cffba](https://via.placeholder.com/50x30/8cffba/000000?text=+)|
|color3    |#f4cf86|![#f4cf86](https://via.placeholder.com/50x30/f4cf86/000000?text=+)|
|color4    |#0a9dff|![#0a9dff](https://via.placeholder.com/50x30/0a9dff/000000?text=+)|
|color5    |#ff9eb8|![#ff9eb8](https://via.placeholder.com/50x30/ff9eb8/000000?text=+)|
|color6    |#ffa724|![#ffa724](https://via.placeholder.com/50x30/ffa724/000000?text=+)|
|color7    |#e5e9f0|![#e5e9f0](https://via.placeholder.com/50x30/e5e9f0/000000?text=+)|
|color8    |#4c566a|![#4c566a](https://via.placeholder.com/50x30/4c566a/000000?text=+)|
|color9    |#ff2c4b|![#ff2c4b](https://via.placeholder.com/50x30/ff2c4b/000000?text=+)|
|color10   |#8cffba|![#8cffba](https://via.placeholder.com/50x30/8cffba/000000?text=+)|
|color11   |#f4cf86|![#f4cf86](https://via.placeholder.com/50x30/f4cf86/000000?text=+)|
|color12   |#0a9dff|![#0a9dff](https://via.placeholder.com/50x30/0a9dff/000000?text=+)|
|color13   |#ff9eb8|![#ff9eb8](https://via.placeholder.com/50x30/ff9eb8/000000?text=+)|
|color14   |#fade3e|![#fade3e](https://via.placeholder.com/50x30/fade3e/000000?text=+)|
|color15   |#ffffff|![#ffffff](https://via.placeholder.com/50x30/ffffff/000000?text=+)|

### Sonokai

[Reference](https://github.com/sainnhe/sonokai)

![](./screenshots/sonokai.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#2c2e34|![#2c2e34](https://via.placeholder.com/50x30/2c2e34/000000?text=+)|
|foreground|#e2e2e3|![#e2e2e3](https://via.placeholder.com/50x30/e2e2e3/000000?text=+)|
|cursor    |#e2e2e3|![#e2e2e3](https://via.placeholder.com/50x30/e2e2e3/000000?text=+)|
|color0    |#181819|![#181819](https://via.placeholder.com/50x30/181819/000000?text=+)|
|color1    |#ff6077|![#ff6077](https://via.placeholder.com/50x30/ff6077/000000?text=+)|
|color2    |#9ed072|![#9ed072](https://via.placeholder.com/50x30/9ed072/000000?text=+)|
|color3    |#e7c664|![#e7c664](https://via.placeholder.com/50x30/e7c664/000000?text=+)|
|color4    |#76cce0|![#76cce0](https://via.placeholder.com/50x30/76cce0/000000?text=+)|
|color5    |#b39df3|![#b39df3](https://via.placeholder.com/50x30/b39df3/000000?text=+)|
|color6    |#f39660|![#f39660](https://via.placeholder.com/50x30/f39660/000000?text=+)|
|color7    |#e2e2e3|![#e2e2e3](https://via.placeholder.com/50x30/e2e2e3/000000?text=+)|
|color8    |#595f6f|![#595f6f](https://via.placeholder.com/50x30/595f6f/000000?text=+)|
|color9    |#ff6077|![#ff6077](https://via.placeholder.com/50x30/ff6077/000000?text=+)|
|color10   |#a7df78|![#a7df78](https://via.placeholder.com/50x30/a7df78/000000?text=+)|
|color11   |#e7c664|![#e7c664](https://via.placeholder.com/50x30/e7c664/000000?text=+)|
|color12   |#85d3f2|![#85d3f2](https://via.placeholder.com/50x30/85d3f2/000000?text=+)|
|color13   |#b39df3|![#b39df3](https://via.placeholder.com/50x30/b39df3/000000?text=+)|
|color14   |#f39660|![#f39660](https://via.placeholder.com/50x30/f39660/000000?text=+)|
|color15   |#e2e2e3|![#e2e2e3](https://via.placeholder.com/50x30/e2e2e3/000000?text=+)|

### Srcery

[Reference](https://github.com/srcery-colors/srcery-vim)

![](./screenshots/srcery.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#1c1b19|![#1C1B19](https://via.placeholder.com/50x30/1C1B19/000000?text=+)|
|foreground|#fce8c3|![#FCE8C3](https://via.placeholder.com/50x30/FCE8C3/000000?text=+)|
|cursor    |#fbb829|![#FBB829](https://via.placeholder.com/50x30/FBB829/000000?text=+)|
|color0    |#1c1b19|![#1C1B19](https://via.placeholder.com/50x30/1C1B19/000000?text=+)|
|color1    |#ef2f27|![#EF2F27](https://via.placeholder.com/50x30/EF2F27/000000?text=+)|
|color2    |#519f50|![#519F50](https://via.placeholder.com/50x30/519F50/000000?text=+)|
|color3    |#fbb829|![#FBB829](https://via.placeholder.com/50x30/FBB829/000000?text=+)|
|color4    |#2c78bf|![#2C78BF](https://via.placeholder.com/50x30/2C78BF/000000?text=+)|
|color5    |#e02c6d|![#E02C6D](https://via.placeholder.com/50x30/E02C6D/000000?text=+)|
|color6    |#0aaeb3|![#0AAEB3](https://via.placeholder.com/50x30/0AAEB3/000000?text=+)|
|color7    |#baa67f|![#BAA67F](https://via.placeholder.com/50x30/BAA67F/000000?text=+)|
|color8    |#918175|![#918175](https://via.placeholder.com/50x30/918175/000000?text=+)|
|color9    |#f75341|![#F75341](https://via.placeholder.com/50x30/F75341/000000?text=+)|
|color10   |#98bc37|![#98BC37](https://via.placeholder.com/50x30/98BC37/000000?text=+)|
|color11   |#fed06e|![#FED06E](https://via.placeholder.com/50x30/FED06E/000000?text=+)|
|color12   |#68a8e4|![#68A8E4](https://via.placeholder.com/50x30/68A8E4/000000?text=+)|
|color13   |#ff5c8f|![#FF5C8F](https://via.placeholder.com/50x30/FF5C8F/000000?text=+)|
|color14   |#2be4d0|![#2BE4D0](https://via.placeholder.com/50x30/2BE4D0/000000?text=+)|
|color15   |#fce8c3|![#FCE8C3](https://via.placeholder.com/50x30/FCE8C3/000000?text=+)|

### One half light

[Reference](https://github.com/sonph/onehalf)

![](./screenshots/one-half-light.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#fafafa|![#fafafa](https://via.placeholder.com/50x30/fafafa/000000?text=+)|
|foreground|#383a42|![#383a42](https://via.placeholder.com/50x30/383a42/000000?text=+)|
|cursor    |#f0f0f0|![#f0f0f0](https://via.placeholder.com/50x30/f0f0f0/000000?text=+)|
|color0    |#383a42|![#383a42](https://via.placeholder.com/50x30/383a42/000000?text=+)|
|color1    |#e45649|![#e45649](https://via.placeholder.com/50x30/e45649/000000?text=+)|
|color2    |#50a14f|![#50a14f](https://via.placeholder.com/50x30/50a14f/000000?text=+)|
|color3    |#c18401|![#c18401](https://via.placeholder.com/50x30/c18401/000000?text=+)|
|color4    |#0184bc|![#0184bc](https://via.placeholder.com/50x30/0184bc/000000?text=+)|
|color5    |#a626a4|![#a626a4](https://via.placeholder.com/50x30/a626a4/000000?text=+)|
|color6    |#0997b3|![#0997b3](https://via.placeholder.com/50x30/0997b3/000000?text=+)|
|color7    |#fafafa|![#fafafa](https://via.placeholder.com/50x30/fafafa/000000?text=+)|
|color8    |#383a42|![#383a42](https://via.placeholder.com/50x30/383a42/000000?text=+)|
|color9    |#e45649|![#e45649](https://via.placeholder.com/50x30/e45649/000000?text=+)|
|color10   |#50a14f|![#50a14f](https://via.placeholder.com/50x30/50a14f/000000?text=+)|
|color11   |#c18401|![#c18401](https://via.placeholder.com/50x30/c18401/000000?text=+)|
|color12   |#0184bc|![#0184bc](https://via.placeholder.com/50x30/0184bc/000000?text=+)|
|color13   |#a626a4|![#a626a4](https://via.placeholder.com/50x30/a626a4/000000?text=+)|
|color14   |#0997b3|![#0997b3](https://via.placeholder.com/50x30/0997b3/000000?text=+)|
|color15   |#fafafa|![#fafafa](https://via.placeholder.com/50x30/fafafa/000000?text=+)|

### Github light 2

[Reference](https://github.com/cdalvaro/github-vscode-theme-iterm)

![](./screenshots/github-light-2.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#f6f8fa|![#f6f8fa](https://via.placeholder.com/50x30/f6f8fa/000000?text=+)|
|cursor    |#00408e|![#00408e](https://via.placeholder.com/50x30/00408e/000000?text=+)|
|foreground|#57606a|![#57606a](https://via.placeholder.com/50x30/57606a/000000?text=+)|
|color0    |#000000|![#000000](https://via.placeholder.com/50x30/000000/000000?text=+)|
|color1    |#d81029|![#d81029](https://via.placeholder.com/50x30/d81029/000000?text=+)|
|color10   |#00d400|![#00d400](https://via.placeholder.com/50x30/00d400/000000?text=+)|
|color11   |#b2bd00|![#b2bd00](https://via.placeholder.com/50x30/b2bd00/000000?text=+)|
|color12   |#004fab|![#004fab](https://via.placeholder.com/50x30/004fab/000000?text=+)|
|color13   |#c900c2|![#c900c2](https://via.placeholder.com/50x30/c900c2/000000?text=+)|
|color14   |#009ac0|![#009ac0](https://via.placeholder.com/50x30/009ac0/000000?text=+)|
|color15   |#a5a5a5|![#a5a5a5](https://via.placeholder.com/50x30/a5a5a5/000000?text=+)|
|color2    |#00c200|![#00c200](https://via.placeholder.com/50x30/00c200/000000?text=+)|
|color3    |#929a00|![#929a00](https://via.placeholder.com/50x30/929a00/000000?text=+)|
|color4    |#004fab|![#004fab](https://via.placeholder.com/50x30/004fab/000000?text=+)|
|color5    |#c900c2|![#c900c2](https://via.placeholder.com/50x30/c900c2/000000?text=+)|
|color6    |#009ac0|![#009ac0](https://via.placeholder.com/50x30/009ac0/000000?text=+)|
|color7    |#555555|![#555555](https://via.placeholder.com/50x30/555555/000000?text=+)|
|color8    |#666666|![#666666](https://via.placeholder.com/50x30/666666/000000?text=+)|
|color9    |#d81029|![#d81029](https://via.placeholder.com/50x30/d81029/000000?text=+)|

### Ayu light

[Reference](https://github.com/ayu-theme/ayu-colors)

![](./screenshots/ayu-light.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#fafafa|![#FAFAFA](https://via.placeholder.com/50x30/FAFAFA/000000?text=+)|
|foreground|#575f66|![#575F66](https://via.placeholder.com/50x30/575F66/000000?text=+)|
|cursor    |#8a9199|![#8A9199](https://via.placeholder.com/50x30/8A9199/000000?text=+)|
|color0    |#55b4d4|![#55B4D4](https://via.placeholder.com/50x30/55B4D4/000000?text=+)|
|color1    |#f2ae49|![#F2AE49](https://via.placeholder.com/50x30/F2AE49/000000?text=+)|
|color2    |#399ee6|![#399EE6](https://via.placeholder.com/50x30/399EE6/000000?text=+)|
|color3    |#86b300|![#86B300](https://via.placeholder.com/50x30/86B300/000000?text=+)|
|color4    |#4cbf99|![#4CBF99](https://via.placeholder.com/50x30/4CBF99/000000?text=+)|
|color5    |#f07171|![#F07171](https://via.placeholder.com/50x30/F07171/000000?text=+)|
|color6    |#fa8d3e|![#FA8D3E](https://via.placeholder.com/50x30/FA8D3E/000000?text=+)|
|color7    |#e6ba7e|![#E6BA7E](https://via.placeholder.com/50x30/E6BA7E/000000?text=+)|
|color8    |#abb0b6|![#ABB0B6](https://via.placeholder.com/50x30/ABB0B6/000000?text=+)|
|color9    |#a37acc|![#A37ACC](https://via.placeholder.com/50x30/A37ACC/000000?text=+)|
|color10   |#ed9366|![#ED9366](https://via.placeholder.com/50x30/ED9366/000000?text=+)|
|color11   |#f51818|![#F51818](https://via.placeholder.com/50x30/F51818/000000?text=+)|
|color12   |#99bf4d|![#99BF4D](https://via.placeholder.com/50x30/99BF4D/000000?text=+)|
|color13   |#709ecc|![#709ECC](https://via.placeholder.com/50x30/709ECC/000000?text=+)|
|color14   |#f27983|![#F27983](https://via.placeholder.com/50x30/F27983/000000?text=+)|
|color15   |#f8f9fa|![#F8F9FA](https://via.placeholder.com/50x30/F8F9FA/000000?text=+)|

### Tokyonight day

[Reference](https://github.com/folke/tokyonight.nvim)

![](./screenshots/tokyonight_day.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#e1e2e7|![#e1e2e7](https://via.placeholder.com/50x30/e1e2e7/000000?text=+)|
|foreground|#3760bf|![#3760bf](https://via.placeholder.com/50x30/3760bf/000000?text=+)|
|cursor    |#3760bf|![#3760bf](https://via.placeholder.com/50x30/3760bf/000000?text=+)|
|color0    |#e9e9ed|![#e9e9ed](https://via.placeholder.com/50x30/e9e9ed/000000?text=+)|
|color1    |#f52a65|![#f52a65](https://via.placeholder.com/50x30/f52a65/000000?text=+)|
|color2    |#587539|![#587539](https://via.placeholder.com/50x30/587539/000000?text=+)|
|color3    |#8c6c3e|![#8c6c3e](https://via.placeholder.com/50x30/8c6c3e/000000?text=+)|
|color4    |#2e7de9|![#2e7de9](https://via.placeholder.com/50x30/2e7de9/000000?text=+)|
|color5    |#9854f1|![#9854f1](https://via.placeholder.com/50x30/9854f1/000000?text=+)|
|color6    |#007197|![#007197](https://via.placeholder.com/50x30/007197/000000?text=+)|
|color7    |#6172b0|![#6172b0](https://via.placeholder.com/50x30/6172b0/000000?text=+)|
|color8    |#a1a6c5|![#a1a6c5](https://via.placeholder.com/50x30/a1a6c5/000000?text=+)|
|color9    |#f52a65|![#f52a65](https://via.placeholder.com/50x30/f52a65/000000?text=+)|
|color10   |#587539|![#587539](https://via.placeholder.com/50x30/587539/000000?text=+)|
|color11   |#8c6c3e|![#8c6c3e](https://via.placeholder.com/50x30/8c6c3e/000000?text=+)|
|color12   |#2e7de9|![#2e7de9](https://via.placeholder.com/50x30/2e7de9/000000?text=+)|
|color13   |#9854f1|![#9854f1](https://via.placeholder.com/50x30/9854f1/000000?text=+)|
|color14   |#007197|![#007197](https://via.placeholder.com/50x30/007197/000000?text=+)|
|color15   |#3760bf|![#3760bf](https://via.placeholder.com/50x30/3760bf/000000?text=+)|

### Github light default

[Reference](https://github.com/cdalvaro/github-vscode-theme-iterm)

![](./screenshots/github-light-default.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#f6f8fa|![#f6f8fa](https://via.placeholder.com/50x30/f6f8fa/000000?text=+)|
|cursor    |#576069|![#576069](https://via.placeholder.com/50x30/576069/000000?text=+)|
|foreground|#57606a|![#57606a](https://via.placeholder.com/50x30/57606a/000000?text=+)|
|color0    |#24292f|![#24292f](https://via.placeholder.com/50x30/24292f/000000?text=+)|
|color1    |#cf222e|![#cf222e](https://via.placeholder.com/50x30/cf222e/000000?text=+)|
|color10   |#1a7f37|![#1a7f37](https://via.placeholder.com/50x30/1a7f37/000000?text=+)|
|color11   |#633c01|![#633c01](https://via.placeholder.com/50x30/633c01/000000?text=+)|
|color12   |#218bff|![#218bff](https://via.placeholder.com/50x30/218bff/000000?text=+)|
|color13   |#a475f9|![#a475f9](https://via.placeholder.com/50x30/a475f9/000000?text=+)|
|color14   |#3192aa|![#3192aa](https://via.placeholder.com/50x30/3192aa/000000?text=+)|
|color15   |#8c959f|![#8c959f](https://via.placeholder.com/50x30/8c959f/000000?text=+)|
|color2    |#116329|![#116329](https://via.placeholder.com/50x30/116329/000000?text=+)|
|color3    |#4d2d00|![#4d2d00](https://via.placeholder.com/50x30/4d2d00/000000?text=+)|
|color4    |#0969da|![#0969da](https://via.placeholder.com/50x30/0969da/000000?text=+)|
|color5    |#8250df|![#8250df](https://via.placeholder.com/50x30/8250df/000000?text=+)|
|color6    |#1b7c83|![#1b7c83](https://via.placeholder.com/50x30/1b7c83/000000?text=+)|
|color7    |#6e7781|![#6e7781](https://via.placeholder.com/50x30/6e7781/000000?text=+)|
|color8    |#57606a|![#57606a](https://via.placeholder.com/50x30/57606a/000000?text=+)|
|color9    |#a40e26|![#a40e26](https://via.placeholder.com/50x30/a40e26/000000?text=+)|

### Github light

[Reference](https://github.com/cormacrelf/vim-colors-github)

![](./screenshots/github-light.png)

|  Color   |  Hex  |                             Preview                              |
|----------|:-----:|:----------------------------------------------------------------:|
|background|#ffffff|![#ffffff](https://via.placeholder.com/50x30/ffffff/000000?text=+)|
|foreground|#24292e|![#24292e](https://via.placeholder.com/50x30/24292e/000000?text=+)|
|cursor    |#2b3137|![#2b3137](https://via.placeholder.com/50x30/2b3137/000000?text=+)|
|color0    |#ffffff|![#ffffff](https://via.placeholder.com/50x30/ffffff/000000?text=+)|
|color1    |#e36209|![#e36209](https://via.placeholder.com/50x30/e36209/000000?text=+)|
|color2    |#005cc5|![#005cc5](https://via.placeholder.com/50x30/005cc5/000000?text=+)|
|color3    |#6f42c1|![#6f42c1](https://via.placeholder.com/50x30/6f42c1/000000?text=+)|
|color4    |#22863a|![#22863a](https://via.placeholder.com/50x30/22863a/000000?text=+)|
|color5    |#d73a49|![#d73a49](https://via.placeholder.com/50x30/d73a49/000000?text=+)|
|color6    |#669cc2|![#669cc2](https://via.placeholder.com/50x30/669cc2/000000?text=+)|
|color7    |#2b3137|![#2b3137](https://via.placeholder.com/50x30/2b3137/000000?text=+)|
|color8    |#c8d1db|![#c8d1db](https://via.placeholder.com/50x30/c8d1db/000000?text=+)|
|color9    |#f18338|![#f18338](https://via.placeholder.com/50x30/f18338/000000?text=+)|
|color10   |#032f62|![#032f62](https://via.placeholder.com/50x30/032f62/000000?text=+)|
|color11   |#45267d|![#45267d](https://via.placeholder.com/50x30/45267d/000000?text=+)|
|color12   |#3ebc5c|![#3ebc5c](https://via.placeholder.com/50x30/3ebc5c/000000?text=+)|
|color13   |#b31d28|![#b31d28](https://via.placeholder.com/50x30/b31d28/000000?text=+)|
|color14   |#f16636|![#f16636](https://via.placeholder.com/50x30/f16636/000000?text=+)|
|color15   |#2d343a|![#2d343a](https://via.placeholder.com/50x30/2d343a/000000?text=+)|

