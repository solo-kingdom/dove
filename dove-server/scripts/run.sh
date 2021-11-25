#!/bin/sh
# check config
if [ -z "$DOVE_CONFIG" ]; then
  exit 1
fi

# base config & source tools
fp="$(
  cd "$(dirname "$0")" || exit
  pwd -P
)"
cd "$fp/.." || exit
base="$(pwd)"
echo "$base"

python3 manage.py runserver 0.0.0.0:8000
