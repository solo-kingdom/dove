#!/bin/sh
# base config & source tools
fp="$(
  cd "$(dirname "$0")" || exit
  pwd -P
)"
cd "$fp/.." || exit
base="$(pwd)"

. "$base/scripts/common/tools.sh"

python3 manage.py makemigrations
python3 manage.py migrate
