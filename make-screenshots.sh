#!/bin/bash

usage() {
    cat << HEREDOC
    Usage:
    $(basename $0) [-f] -i <filename>
    -f: Force overwrite screenshots.
    By default, <filename> is `colorschemes/**/*.json`, which means every files in colorschemes folder.

HEREDOC
    exit 0
}

FORCE=false
FILES="colorschemes/**/*.json"

for i in "$@"; do
    case $i in
        -f)
            FORCE=true
            shift
            ;;
        -h|--help)
            usage
            ;;
        *)
            FILES=$i
            shift
            ;;
    esac
done

WINID=$(xdotool getmouselocation --shell | sed -n '/^WINDOW/s/.*=//p')

shots=./screenshots
if [[ $FORCE = true ]]; then
    rm -rf $shots
fi

for scheme in $FILES ; do
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
