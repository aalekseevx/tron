compile_cpp() {
    g++ -pedantic -Wall -Wextra -Wcast-align -Wcast-qual -Wctor-dtor-privacy -Wdisabled-optimization -Wformat=2 -Winit-self -Wmissing-declarations -Wmissing-include-dirs -Wold-style-cast -Woverloaded-virtual -Wredundant-decls -Wshadow -Wsign-conversion -Wsign-promo -Wstrict-overflow=5 -Wswitch-default -Wundef -Wzero-as-null-pointer-constant -Werror -std=c++17 -O2 -isystem lib "$1" -o "$2"
}

echo "Changing dir to problemdir..."
script_dir="$(dirname "${BASH_SOURCE[0]}")"
problemdir="$(dirname "$script_dir")"
cd "$problemdir"
echo "Changed."


echo "Generating levels..."
# Optimize using config info
pipenv run python3 src/generator_public.py --test_id 1 --test_file tests/01.json --test_description_file etc/01.txt
pipenv run python3 src/generator_public.py --test_id 2 --test_file tests/02.json --test_description_file etc/02.txt
pipenv run python3 src/generator_public.py --test_id 3 --test_file tests/03.json --test_description_file etc/03.txt
pipenv run python3 src/generator_public.py --test_id 4 --test_file tests/04.json --test_description_file etc/04.txt
pipenv run python3 src/generator_public.py --test_id 5 --test_file tests/05.json --test_description_file etc/05.txt
echo "Public levels generated."

if test -f "src/generator_private.py"; then
    pipenv run python3 src/generator_private.py --test_id 6 --test_file tests/06.json --test_description_file etc/06.txt
	pipenv run python3 src/generator_private.py --test_id 7 --test_file tests/07.json --test_description_file etc/07.txt
	pipenv run python3 src/generator_private.py --test_id 8 --test_file tests/08.json --test_description_file etc/08.txt
	pipenv run python3 src/generator_private.py --test_id 9 --test_file tests/09.json --test_description_file etc/09.txt
	pipenv run python3 src/generator_private.py --test_id 10 --test_file tests/10.json --test_description_file etc/10.txt
    echo "Private level generated."
else
	echo "Warning! Private levels ignored."
fi
echo "Levels generated."

echo "Compiling validator"
# g++ -std=c++17 -O2 -I lib src/validator.cpp -o bin/validator
compile_cpp src/validator.cpp bin/validator
echo "Validator compiled."

echo "Compiling solutions..."
g++ -std=c++17 -O2 solutions/ermolin.cpp -o bin/ermolin
g++ -std=c++17 -O2 solutions/starkov.cpp -o bin/starkov
g++ -std=c++17 -O2 solutions/alekseev.cpp -o bin/alekseev
echo "Solutions compiled."

echo "Compiling statements..."
cd src
latex -shell-escape problem.tex
latex -shell-escape problem.tex
dvipdfm problem.dvi
rm problem.aux
rm problem.log
rm problem.dvi
rm -f missfont.log
cd ..
mv src/problem.pdf statements/russian/problem.pdf
echo "Statements compiled."