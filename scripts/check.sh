script_dir="$(dirname "${BASH_SOURCE[0]}")"
problemdir="$(dirname "$script_dir")"

pipenv run python3 "$problemdir/src/check.py" "$@"