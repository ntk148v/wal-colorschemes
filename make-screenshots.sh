#!/bin/bash

usage() {
    cat <<HEREDOC
    Usage:
    $(basename $0) [-f] -i <filename>
    -f: Force overwrite screenshots.
    By default, <filename> is $(colorschemes/**/*.json), which means every files in colorschemes folder.

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
    -h | --help)
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

capture_preview() {
    local scheme=$1
    local prefix=$2
    local active_window=$(xdotool getactivewindow)

    # Set up terminal size for consistent capture
    echo -en "\e[8;6;40t"  # Set terminal to 6 lines by 40 columns
    clear

    # Apply theme and show preview
    wal --theme "$scheme" >/dev/null 2>&1
    bash ./preview-colors.sh

    # Wait for display to update
    sleep 0.1

    # Capture and process
    filename=$(basename "$scheme")
    output_file="$prefix/${filename%.json}.png"

    xwd -id $active_window -silent | \
        convert xwd:- -crop '100%x25%+0+100' -trim +repage "$output_file"

    # Reset terminal size
    echo -en "\e[8;24;80t"
    clear
}

# Main execution
for scheme in $FILES; do
    clear
    prefix=$shots
    mkdir -p $prefix

    # Capture preview for the current scheme
    capture_preview "$scheme" "$prefix"

    # Give visual feedback
    echo "Generated preview for: $scheme"
done
