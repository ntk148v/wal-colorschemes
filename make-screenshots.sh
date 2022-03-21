#!/bin/bash
WINID=$(xdotool getmouselocation --shell | sed -n '/^WINDOW/s/.*=//p')

shots=./screenshots
rm -rf $shots
for scheme in colorschemes/**/*.json ; do
  clear
  prefix=$shots
  mkdir -p $prefix
  wal --theme $scheme
  echo $scheme
  clear
  bash ./preview-colors.sh
  sleep 0.2
  filename=$(basename $scheme)
  xwd -id $WINID | convert "xwd:-" "png:$prefix/${filename%.json}.png"
done
