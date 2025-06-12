#!/usr/bin/env bash

# Function to convert hex to rgb
hex_to_rgb() {
    hex=$1
    r=$((16#${hex:0:2}))
    g=$((16#${hex:2:2}))
    b=$((16#${hex:4:2}))
    echo "$r;$g;$b"
}

# Display a simple color preview that shows blocks of colors
print_color() {
    local color=$1
    local rgb=$(hex_to_rgb $color)
    echo -en "\e[48;2;${rgb}m   \e[0m"
}

# Get colors from pywal cache
colors=($(cat ~/.cache/wal/colors | sed 's/#//g'))

echo "  "  # Add padding at top
echo -n "  "  # Add left padding
# Print first row (colors 0-7)
for i in {0..7}; do
    print_color "${colors[$i]}"
done
echo
echo -n "  "  # Add left padding
# Print second row (colors 8-15)
for i in {8..15}; do
    print_color "${colors[$i]}"
done
echo
echo "  "  # Add padding at bottom
