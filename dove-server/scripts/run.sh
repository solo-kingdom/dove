#!/bin/sh
# base config & source tools
fp="$(
  cd "$(dirname "$0")" || exit
  pwd -P
)"
cd "$fp/.." || exit
base="$(pwd)"

. "$base/scripts/common/tools.sh"

# check config
if [ -z "$DOVE_CONFIG" ]; then
  quit "environment variable DOVE_CONFIG not set" 0
fi

python3 manage.py runserver 0.0.0.0:8000
