echo "Changing dir to problemdir..."
script_dir="$(dirname "${BASH_SOURCE[0]}")"
problemdir="$(dirname "$script_dir")"
cd "$problemdir" >/dev/null 2>&1
echo "Changed."

echo "Deleting tests..."
rm tests/*
rm etc/*
echo "Tests deleted."

echo "Deleting binary files"
rm bin/*
echo "Binary files deleted."

echo "Deleting pycache"
rm -rf src/__pycache__
rm -rf solutions/__pycache__
rm -rf lib/__pycache__
rm -rf config/__pycache__
echo "pycache deleted"

echo "Deleting compiled statements."
rm statements/russian/*
rm statements/english/*
echo "Compiles statements deleted."
