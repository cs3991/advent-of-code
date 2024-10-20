#!/bin/bash
D=$date

# if there's an argument, get that day instead of the current day
if [[ "$1" != "" ]]; then
	if !( [[ "$1" =~ ^[0-9]+$ ]] && [ "$1" -ge 1 ] && [ "$1" -le 25 ]); then
		echo "Argument should be a day number between 1 and 25" >&2 && exit 1
	fi
	DAY=$1
else
	DAY=$(date -d "$D" '+%d')
fi

MONTH=$(date -d "$D" '+%m')
YEAR=$(date -d "$D" '+%Y')
while [[ $(basename "$(pwd)") != "advent-of-code" && "$(pwd)" != "/" ]]; do
	cd ..
done
if [[ "$(pwd)" == "/" ]]
then
	echo "Ce script doit être lancé depuis un sous dossier de advent-of-code"
fi

mkdir -p "$YEAR"

day_padded=$(printf "%02d" $DAY)

if [ -f "$YEAR/$day_padded.sh" ]; then
    echo "File $YEAR/$day_padded.sh already exists!" >&2 && exit 1
fi


touch "$YEAR/$day_padded.sh"

