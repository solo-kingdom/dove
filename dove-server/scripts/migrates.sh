#!/bin/sh
# base config & source tools
fp="$(
  cd "$(dirname "$1")" || exit
  pwd -P
)/$(basename "$1")"
cd "$fp/.." || exit
base="$(pwd)"
echo "$base"

python3 manage.py makemigrations
python3 manage.py migrate
