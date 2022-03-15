#!/bin/bash

# Use eg: `xwininfo -int` to get the id of a wezterm
# and pass it to this script
WINID=$1

shots=./screenshots
rm -rf ./screenshots
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
